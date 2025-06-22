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

## Langkah Pengkomunikasian Seluruh Sistem
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
```bash
sudo dmesg | grep ttyUSB*
``` berguna untuk mengidentifikasi koneksi dari USB konverter dari modbus sensor SHT20
kemudian command
```bash
sudo chmod a+rw /dev/ttyUSB0``` (sesuaikan dengan deteksi yang ditampilkan), untuk mendapatkan permission untuk membaca data dari sensor
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

### 5. Klik kanan pada folder kemudian klik ‘Open in Terminal’
kemudian masukkan command cd Server kemudian enter, lalu masukkan command
```bash
cargo run```
lalu enter, untuk menjalankan Rust TCP Server dan mengirimkan data dari bacaan sensor yang dikirim ke TCP Server juga dikirimkan ke InfluxDB. Tampilan terminal akan seperti berikut:

 






