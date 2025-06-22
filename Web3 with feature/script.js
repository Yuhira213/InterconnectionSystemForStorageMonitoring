const contractAddress = "0xf7d269cd81b82775a4646d8a2532c25028e9c38a"; // Ganti dengan alamat kontrak dari Ganache
const abiPath = "abi/SensorStorage.abi";

let chart;

async function loadSensorData() {
  const abiRes = await fetch(abiPath);
  const abi = await abiRes.json();

  const provider = new ethers.BrowserProvider(window.ethereum || "http://localhost:8545");
  await provider.send("eth_requestAccounts", []);
  const signer = await provider.getSigner();
  const contract = new ethers.Contract(contractAddress, abi, signer);

  const filter = contract.filters.DataStored();
  const events = await contract.queryFilter(filter, 0, "latest");

  const tableBody = document.querySelector("#sensorTable tbody");
  tableBody.innerHTML = "";

  const labels = [];
  const temps = [];
  const hums = [];

  events.forEach((e) => {
    const data = e.args;
    const timeStr = new Date(Number(data.timestamp) * 1000).toLocaleString();
    const temp = Number(data.temperature) / 100;
    const hum = Number(data.humidity) / 100;

    tableBody.innerHTML += `
      <tr>
        <td>${timeStr}</td>
        <td>${data.sensorId}</td>
        <td>${data.location}</td>
        <td>${data.stage}</td>
        <td>${temp.toFixed(2)}</td>
        <td>${hum.toFixed(2)}</td>
      </tr>
    `;

    labels.push(timeStr);
    temps.push(temp);
    hums.push(hum);
  });

  renderChart(labels, temps, hums);
}

function renderChart(labels, temps, hums) {
  const ctx = document.getElementById('chart').getContext('2d');

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [
        {
          label: "Temperature (°C)",
          data: temps,
          borderColor: 'rgba(255, 99, 132, 1)',
          fill: false
        },
        {
          label: "Humidity (%)",
          data: hums,
          borderColor: 'rgba(54, 162, 235, 1)',
          fill: false
        }
      ]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}

function showTab(tabId) {
  document.getElementById("historyTab").style.display = "none";
  document.getElementById("inputTab").style.display = "none";
  document.getElementById(tabId).style.display = "block";
}

async function confirmLoading() {
  const input = document.getElementById("datetimeInput").value.trim();
  if (!input) return alert("Harap masukkan tanggal dan waktu.");

  const targetTimestamp = Math.floor(new Date(input).getTime() / 1000);
  if (isNaN(targetTimestamp)) return alert("Format waktu tidak valid.");

  // Gunakan BrowserProvider seperti sebelumnya
  const abiRes = await fetch(abiPath);
  const abi = await abiRes.json();

  const provider = new ethers.BrowserProvider(window.ethereum || "http://localhost:8545");
  await provider.send("eth_requestAccounts", []);
  const signer = await provider.getSigner();
  const contract = new ethers.Contract(contractAddress, abi, signer);

  const filter = contract.filters.DataStored();
  const events = await contract.queryFilter(filter, 0, "latest");

  // Cari event dengan timestamp terdekat
  let closestEvent = null;
  let closestDiff = Infinity;

  for (const e of events) {
    const ts = Number(e.args.timestamp);
    const diff = Math.abs(ts - targetTimestamp);
    if (diff < closestDiff) {
      closestDiff = diff;
      closestEvent = e;
    }
  }

  if (!closestEvent) {
    document.getElementById("resultData").textContent = "Data tidak ditemukan.";
    return;
  }

  const data = closestEvent.args;
  const timeStr = new Date(Number(data.timestamp) * 1000).toLocaleString();
  const temp = Number(data.temperature) / 100;
  const hum = Number(data.humidity) / 100;

  const message = `
    <div style="text-align: center; font-size: 18px;">
    Status Loading In telah Dilakukan:<br/><br/>
    <strong>Waktu:</strong> ${timeStr}<br/>
    <strong>Suhu:</strong> ${temp.toFixed(2)} °C<br/>
    <strong>Kelembapan:</strong> ${hum.toFixed(2)} %<br/>
  `;

  // Tampilkan hasil
  document.getElementById("resultData").innerHTML = message;

  // Tampilkan gambar QR code statis
  const qrCodeContainer = document.getElementById("qrcode");
  qrCodeContainer.innerHTML = `
    <div style="text-align: center; font-size: 18px;">
    <p><strong>Silahkan Konfirmasikan Loading In Barang pada Kontak berikut:</strong></p>
    <img src="img/qrcode.png" alt="QR Code Kontak Konfirmasi" width="450" />
  `;
}
