import tkinter as tk
from tkinter import ttk
import requests
import threading
import time
import csv
from io import StringIO
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from collections import deque

# Konfigurasi InfluxDB
INFLUX_QUERY_URL = "http://localhost:8086/api/v2/query"
ORG = "ITS"
BUCKET = "ISImonitor"
TOKEN = "mTjO4KT4rlVLw3IISNiewi_JWxiErLd67bxRbx_oSrHmVz8-eTjcqT_IxBEoTSJRud40uBsz9uaPC7aYMOrwZQ=="

# Riwayat data
history_length = 50
temp_history = deque(maxlen=history_length)
rh_history = deque(maxlen=history_length)
time_history = deque(maxlen=history_length)

def get_latest_data():
    flux_query = f'''
    from(bucket: "{BUCKET}")
      |> range(start: -1m)
      |> filter(fn: (r) => r._measurement == "monitoring")
      |> filter(fn: (r) => r._field == "temperature" or r._field == "humidity")
      |> last()
    '''

    headers = {
        "Authorization": f"Token {TOKEN}",
        "Content-Type": "application/vnd.flux",
        "Accept": "application/csv"
    }

    try:
        response = requests.post(
            INFLUX_QUERY_URL,
            params={"org": ORG},
            headers=headers,
            data=flux_query
        )

        reader = csv.DictReader(StringIO(response.text))
        data = {}
        for row in reader:
            try:
                field = row["_field"]
                value = float(row["_value"])
                data[field] = value
            except:
                continue

        if "temperature" in data and "humidity" in data:
            return data["temperature"], data["humidity"]
        return None
    except Exception as e:
        print("❌ Exception query Influx:", e)
        return None

def get_data_range(start_time, end_time):
    flux_query = f'''
    from(bucket: "{BUCKET}")
      |> range(start: {start_time}, stop: {end_time})
      |> filter(fn: (r) => r._measurement == "monitoring")
      |> filter(fn: (r) => r._field == "temperature" or r._field == "humidity")
    '''

    headers = {
        "Authorization": f"Token {TOKEN}",
        "Content-Type": "application/vnd.flux",
        "Accept": "application/csv"
    }

    try:
        response = requests.post(
            INFLUX_QUERY_URL,
            params={"org": ORG},
            headers=headers,
            data=flux_query
        )

        reader = csv.DictReader(StringIO(response.text))
        rows = []
        for row in reader:
            try:
                time_str = row["_time"]
                field = row["_field"]
                value = float(row["_value"])
                rows.append((time_str, field, value))
            except:
                continue

        return rows
    except Exception as e:
        print("❌ Exception query Influx:", e)
        return []

def update_data():
    while True:
        result = get_latest_data()
        current_time = time.strftime('%H:%M:%S')

        if result:
            temp, rh = result
            label_temp.config(text=f"Suhu: {temp:.1f} °C")
            label_rh.config(text=f"Kelembaban: {rh:.1f} %")
            status_label.config(text="✅ Data dari Influx")

            temp_history.append(temp)
            rh_history.append(rh)
            time_history.append(current_time)

            plot_graph()
        else:
            label_temp.config(text="Suhu: ---")
            label_rh.config(text="Kelembaban: ---")
            status_label.config(text="❌ Gagal ambil data")

        time.sleep(2)

def plot_graph():
    ax1.clear()
    ax2.clear()

    fig.patch.set_facecolor('black')
    ax1.set_facecolor('black')
    ax2.set_facecolor('black')

    x = list(range(len(time_history)))
    times = list(time_history)

    ax1.plot(x, list(temp_history), label='Suhu (°C)', color='red', marker='o', linestyle='-')
    ax2.plot(x, list(rh_history), label='Kelembaban (%)', color='cyan', marker='x', linestyle='-')

    ax1.set_title("Grafik Suhu", color='white')
    ax2.set_title("Grafik Kelembaban", color='white')
    ax1.set_ylabel("°C", color='white')
    ax2.set_ylabel("%", color='white')

    interval = 5
    tick_positions = x[::interval]
    tick_labels = times[::interval]

    ax1.set_xticks(tick_positions)
    ax2.set_xticks(tick_positions)
    ax1.set_xticklabels(tick_labels, rotation=45, ha="right", color='white')
    ax2.set_xticklabels(tick_labels, rotation=45, ha="right", color='white')

    for ax in [ax1, ax2]:
        ax.tick_params(axis='y', colors='white')
        ax.tick_params(axis='x', colors='white')
        ax.grid(True, linestyle='--', alpha=0.3, color='gray')
        for spine in ax.spines.values():
            spine.set_color('white')

    fig.tight_layout()
    canvas.draw()

def auto_refresh_table():
    rows = get_data_range("-5m", "now()")
    for i in table.get_children():
        table.delete(i)
    
    if rows:
        grouped = {}
        for t, f, v in rows:
            if t not in grouped:
                grouped[t] = {}
            grouped[t][f] = v

        for t in sorted(grouped.keys())[-20:]:
            row = grouped[t]
            temp = row.get("temperature", "--")
            rh = row.get("humidity", "--")
            table.insert("", "end", values=(t[11:19], f"{temp:.1f}", f"{rh:.1f}"))
    root.after(5000, auto_refresh_table)

# GUI Setup
root = tk.Tk()
root.title("Monitor SHT20 dari InfluxDB")
root.geometry("900x700")

notebook = ttk.Notebook(root)
tab_realtime = ttk.Frame(notebook)
tab_table = ttk.Frame(notebook)
notebook.add(tab_realtime, text="📡 Realtime")
notebook.add(tab_table, text="📋 Tabel Historis")
notebook.pack(fill="both", expand=True)

# Tab Realtime
label_temp = tk.Label(tab_realtime, text="Suhu: -- °C", font=("Helvetica", 16))
label_temp.pack(pady=5)
label_rh = tk.Label(tab_realtime, text="Kelembaban: -- %", font=("Helvetica", 16))
label_rh.pack(pady=5)
status_label = tk.Label(tab_realtime, text="Status: ---", fg="blue")
status_label.pack(pady=5)

fig = Figure(figsize=(7, 4.5), dpi=100)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
canvas = FigureCanvasTkAgg(fig, master=tab_realtime)
canvas.get_tk_widget().pack(pady=10)

# Tab Tabel Historis
cols = ("Waktu", "Suhu (°C)", "Kelembaban (%)")
table = ttk.Treeview(tab_table, columns=cols, show="headings", height=20)
for col in cols:
    table.heading(col, text=col)
    table.column(col, width=150, anchor="center")
table.pack(padx=10, pady=10, fill="both", expand=True)

# Start background threads
threading.Thread(target=update_data, daemon=True).start()
auto_refresh_table()
root.mainloop()
