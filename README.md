#🍞 “Sistem Monitoring Temperatur dan kelembapan pada Penyimpanan Bahan Mentah Pabrik Roti Rumahan” 🍞
![WhatsApp Image 2025-06-19 at 02 06 13_ed644b8e](https://github.com/user-attachments/assets/71c2dc38-d43d-430f-a74f-165ad48adb8d)
![WhatsApp Image 2025-06-19 at 02 06 13_e7cefb18](https://github.com/user-attachments/assets/dc646fad-02b0-46cd-8ae9-2ad23ee06435)


Kualitas bahan mentah seperti tepung dan ragi sangat mempengaruhi hasil akhir roti, sehingga kestabilan suhu dan kelembapan dalam ruang penyimpanan menjadi faktor krusial. Pada industri roti skala rumahan yang masih mengandalkan proses manual, pemantauan kondisi lingkungan secara konvensional tidak efisien dan rawan kesalahan. Untuk menjawab tantangan ini, dikembangkan sistem pemantauan suhu dan kelembapan berbasis komunikasi serial Modbus RTU dari sensor ke perangkat pengendali, yang datanya dikirim melalui Rust-based TCP server ke backend. Data kemudian disimpan dalam InfluxDB sebagai time-series database, dianalisis dan divisualisasikan secara real-time melalui Grafana serta GUI berbasis PyQt5. Integrasi sistem blockchain dan Web3 digunakan untuk menjamin keamanan dan keotentikan data pemantauan, serta memungkinkan transparansi dalam pencatatan histori penyimpanan. Sistem ini menjamin kontrol lingkungan yang akurat dan terpercaya tanpa bergantung pada platform IoT konvensional.

 ## Authors
1. Yudhistira Ananda Kuswantoro (2042231015)
2. Lusty Hanna Isyajidah        (2042231045)
3. M. Daffi Aryatama            (2042231075)
4. Ahmad Radhy                  (Supervisor)

## Features
1. **Penyimpanan Database dari hasil bacaan sensor di InfluxDB**
2. **Tampilan GUI dengan Grafana dan PyQT5**
3. **Terintegrasi dengan sistem Blockchain**
4. **Menggunakan Web3 untuk Visualisasi Interaktif**

## Requirements
### Software
1. Rust Programming Language 1.86.0
2. Industrial SHT20 Temperature and Humidity Sensor
3. InfluxDB2 Client
4. Grafana
5. Ganache V 7.9.2

### Extension
1. Metamask

### Library for PyQT5

# Langkah Pengkomunikasian Seluruh Sistem
## Diharapkan untuk mengunduh zip atau melakukan clone semua isi repository ini dengan memasukkan
```
https://github.com/Yuhira213/InterconnectionSystemForStorageMonitoring.git
```
## Terlebih dahulu

### 1. Klik kanan pada folder kemudian klik ‘Open in Terminal’
kemudian masukkan command cd sensor kemudian enter, lalu masukkan command 
```
cargo run
```
lalu enter, untuk membaca kemudian mengirimkan data dari bacaan sensor ke Rust TCP Server. Maka tampilannya akan seperti berikut:
![WhatsApp Image 2025-06-19 at 01 49 57_04ee2861](https://github.com/user-attachments/assets/1a3b32ee-89fe-4a1e-be3f-ec3af137b3ac)
terlihat pada tampilan awal tertera “Gagal baca sensor: Permission denied.

### 2. Lalu buat tab baru untuk terminal, 
kemudian masukkan command berikut
```
sudo dmesg | grep ttyUSB*
```
berguna untuk mengidentifikasi koneksi dari USB konverter dari modbus sensor SHT20
kemudian command
```
sudo chmod a+rw /dev/ttyUSB0
(sesuaikan dengan deteksi yang ditampilkan)
```
untuk mendapatkan permission untuk membaca data dari sensor

![image](https://github.com/user-attachments/assets/05124d78-52aa-4365-b2fd-a28afc1d9c35)

Maka setelah itu tampilan dari Terminal dari sensor akan berubah menjadi berikut:

![image](https://github.com/user-attachments/assets/9f869be4-cba3-4ebb-8f3a-35911d182e3e)

### 3. Lalu buat tab baru untuk terminal,
kemudian masukkan command ```ganache``` , kemudian akan muncul tampilan seperti gambar berikut:

![image](https://github.com/user-attachments/assets/d581a9a3-fae3-463e-9ee6-c331ff982113)

setelah itu salin salah satu Private Keys yang diberikan dari tampilan tersebut

![image](https://github.com/user-attachments/assets/3ec94ad9-442f-49e2-924b-0cbe87a82cb5)

### 4. Kemudian buka file main.rs yang terdapat di /Server/src. Kemudian ganti local wallet yang ada di bawah “let wallet: LocalWallet =” kemudian save progressnyaa.
![image](https://github.com/user-attachments/assets/c4c5fcad-a912-423a-8d28-87b78a290144)

### 5. Ganti Influx Token yanga ada pada File main.rs di Sensor/Src/
kemudian sesuaikan bagian yang disorot dengan Influx Token yang dimiliki

![image](https://github.com/user-attachments/assets/6a907846-3908-4048-8daa-d1a0e7f801bd)

Kemudian sesuaikan dengan mengganti org dan bucket yang ada pada "/write?org=ITS&bucket=ISImonitor&precision=s" dengan yang dimiliki dan dipakai saat ini

### 6. Klik untuk tambahkan tab baru dari Terminal
kemudian masukkan command cd Server kemudian enter, lalu masukkan command
```bash
cargo run
```
lalu enter, untuk menjalankan Rust TCP Server dan mengirimkan data dari bacaan sensor yang dikirim ke TCP Server juga dikirimkan ke InfluxDB. Tampilan terminal akan seperti berikut:

![image](https://github.com/user-attachments/assets/dfb52371-1eed-4b9b-a284-0ffb6e22edb4)

Setelah itu salin Smart contract yang tertera pada hasil tampilan terminal

### 7. Kemudian buka script.js yang ada di /Web3 with features
ganti contract Adress yang ada di dalamnya(yang sudah disorot) dengan Smart contract yang sudah disalin tadi lalu save progressnya.

![image](https://github.com/user-attachments/assets/0336bea5-74c3-43cb-9a5e-482e32fb0a20)

### 8. Kemudian klik kanan pada Folder ‘Web3 with feature’ lalu klik open in terminal, 
kemudian jalankan command 
```
python3 -m http.server 8005
```
kemudian enter, untuk menjalankan halaman Web3 dari program sistem.

![image](https://github.com/user-attachments/assets/6c8e2733-7e30-4a2a-b926-1ed9952ab6f3)

setelah itu klik kanan pada (http://0.0.0.0:8005/) kemudian open link

### 9. Kemudian akan diarahkan ke pada Web3 tampilan berikut.
![image](https://github.com/user-attachments/assets/55d6cff6-f092-4884-9f49-73fdc27d05c0)

### 10. Kemudian klik pada extension di dalam firefox lalu klik pada Metamask untuk menghubungkan blockchain.
![image](https://github.com/user-attachments/assets/a6790be1-3915-41dd-8612-9491e4dc6831)

- Setelah itu klik pada tampilan kiri,
  
  ![image](https://github.com/user-attachments/assets/9d57de3e-00f2-4e0f-8c09-efacb16652d0)
  
- Lalu klik ‘add a custom network’
  
  ![image](https://github.com/user-attachments/assets/b3b51564-827e-4f1b-809c-e18b07553858)
  
- Lalu sesuaikan dengan yang ada digambar berikut:
  
  ![image](https://github.com/user-attachments/assets/4e920acf-051e-4ec4-8e30-5c36edfd10b0)
  
  kemudian klik save.
  
- kemudian klik panah ke bawah di sebelah account, lalu klik ‘add account or hardware wallet, lalu klik private keys, Kemudian isikan Private Keys yang didapatkan dari ganache, kemudian klik import.
  
  ![image](https://github.com/user-attachments/assets/8781ffcd-6e33-4f0e-8572-05757b45d4cc)

### 11. Kemudian klik ‘muat data sensor’ pada halaman Web3
kemudian akan muncul tampilan dari extension metamask. Kemudian klik connect maka tampilan dari Web3 akan menampilkan tabel dari data yang telah dikirimkan ke TCP Server

![image](https://github.com/user-attachments/assets/837e5c2f-75ef-4f23-b0f5-3a9c9f24d23c)
![image](https://github.com/user-attachments/assets/672e3ef9-96e1-4329-929d-2bb4532ccb5b)

### 12. Untuk membuka Database dari hasil bacaan sensor
- Buka http://localhost:8086 untuk menuju tampilan web InfluxDB

### 13. Untuk menghubungkan ke Grafana.
- Pastikan Grafana service sudah berjalan, dengan memasukkan command berikut
  ```
  sudo systemctl status grafana-server
  ```
- Lalu buka http://localhost:3000, dan tampilan web Grafana akan ditampilkan.

## Tampilan Dashboard dan Hasil Data
### 1. Tampilan Dashboard dan Grafik pada InfluxDB
![image](https://github.com/user-attachments/assets/a69937d0-7dc7-4b39-b16f-fdc3923bc08c)
![image](https://github.com/user-attachments/assets/93fd7c13-d5fb-4e90-ace6-14e0e39da929)

Dapat dilihat pada Gambar pertama merupakan hasil tampilan grafik pembacaan sensor berdasarkan timestamp pada InfluxDB, dan pada Gambar kedua merupakan tabel data hasil pembacaan sensor berdasarkan timestamp pada InfluxDB. Dalam influxDB berguna untuk menyimpan data pembacaan sensor atau sebagai database yang dikirim dari mikrokontroler dan sensor melalui protokol TCP, lalu akan disimpan dalam struktur data berbasis waktu. Dalam sistem monitoring ini, influxDB yang bertanggung jawab merekam dan menyimpan data, setiap perubahan lingkungan sekecil apapun akan tercatat.

### 2. Hasil Tampilan Grafana
![image](https://github.com/user-attachments/assets/6610149e-95d9-4e0e-a40f-bbe815bd96d6)

Dapat dilihat pada Gambar merupakan hasil tampilan grafik pada grafana yang berperan sebagai interface visual untuk menampilkan data temperatur dan kelembaban secara real-time yang dikirim dari sensor SHT20 dari data yang ada dalam influxDB. Dashboard yang dibuat memberikan grafik time-series chart sehingga pengguna dapat melihat perubahan temperatur dan kelembapan selama proses penyimpanan berlangsung.

### 3. Blockchain dan Web3
![image](https://github.com/user-attachments/assets/fa2468fd-c8f3-46b4-b7ee-f36035859d14)

Pada Gambar pertama diatas merupakan hasil pembacaan tampilan data secara realtime dari sensor SHT20 yang diintegrasikan ke dalam sistem blockchain. Setiap data yang ditampilkan akan dicatat sebagai transaksi dalam jaringan blockchain. Integrasi blockchain pada sistem ini memberikan jaminan keaslian dan integritas data. 

![image](https://github.com/user-attachments/assets/0e370606-b83c-411d-b5d2-4839c948cad0)

Pada Gambar kedua diatas menunjukkan hasil visualisasi grafik temperatur dan kelembapan yang merupakan bagian dari sistem blockchain yang diintegrasikan ke Web3. Terdapat dua grafik yang tertera dalam satu tampilan, gari merah menunjukkan grafik temperatur dalam derajat celcius (°C), dan garis biru menunjukkan grafik kelembapan dalam  persentase (%). 

![image](https://github.com/user-attachments/assets/f90a71f7-1eb8-4d7a-8d5b-f894f19c706f)

Pada Gambar ketiga diatas menunjukkan fitur dari Web3 yang digunakan sebagai pengonfirmasian bahan baku yang sedang melakukan loading in ke gudang bahan baku, yang kemudian ketika dikonfirmasikan maka akan menampilkan status dari data sensor dari waktu tersebut.

### 4. Hasil Interface pada Qt
![image](https://github.com/user-attachments/assets/e343074a-cf9a-4a1d-aa11-ef80fff8ea7d)

Dalam Gambar pertama diatas merupakan tampilan hasil grafik tampilan pada software Qt, disini menampilkan data temperatur dan kelembapan yang dikirimkan dari influxDB secara lokal. Pada Qt ini, bertujuan untuk menampilkan dalam bentuk grafik sederhana yang mudah dipahami pengguna untuk melihat data historis dalam bentuk dua grafik terpisah, grafik merah merupakan grafik untuk tampilan data Suhu dan grafik biru merupakan grafik untuk tampilan data kelembaban. Penggunaan warna yang berbeda untuk tampilan grafik ini bertujuan untuk membantu membedakan dua parameter yang berbeda tersebut. Integrasi langsung dengan influxDB memastikan bahwa data selalu ter-update secara real-time.

![image](https://github.com/user-attachments/assets/5d0cea67-00d0-4691-8f23-45c86bb42b89)

Dalam Gambar kedua diatas menunjukkan tampilan Tabel Historis dari Qt yang berguna untuk menampilkan daya sensor suhu dan kelembaban. Dalam setiap tabel mencatat timestamp secara realtime, Suhu dalam °C dan kelembaban dalam %.
 






