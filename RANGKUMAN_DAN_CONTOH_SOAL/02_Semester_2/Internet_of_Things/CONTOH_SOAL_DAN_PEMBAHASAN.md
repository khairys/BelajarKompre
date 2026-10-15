# Bank Contoh Soal & Pembahasan: Internet of Things

> Sumber rujukan: Bank soal UTS & UAS Internet of Things Departemen Informatika Universitas Diponegoro (Koleksi HMIF & Tim Dosen IoT, 2021–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (ARSITEKTUR IOT, SENSOR & PROTOKOL MQTT)

### Soal UTS 1: Hubungan IoT, Big Data, dan Artificial Intelligence (Soal Asli UTS Undip)
**Deskripsi Soal:**
1. Jelaskan bagaimana hubungan simbiotik antara **Internet of Things (IoT)** dan **Big Data**! Pihak mana yang memproduksi data dan pihak mana yang mengolahnya?
2. Berikan sebuah contoh arsitektur nyata penerapan **Artificial Intelligence of Things (AIoT)** pada bidang *Smart Agriculture* (Pertanian Cerdas). Jelaskan alur data dari sensor, proses komputasi di *edge/cloud*, hingga aksi aktuator!

**Kunci Pembahasan & Solusi:**
1. **Hubungan Simbiotik IoT dan Big Data:**
   * **IoT sebagai Produsen Data (*Data Producer*):** Miliaran perangkat fisik dan sensor yang terpasang di lapangan menghasilkan aliran data berkelanjutan (*continuous data streams*) berukuran sangat masif dengan karakteristik **Volume** (jumlah titik data sangat besar per detik), **Velocity** (kecepatan transmisi waktu-nyata), dan **Variety** (format data bervariasi: numerik, gambar, teks).
   * **Big Data sebagai Infrastruktur Analisis (*Data Consumer & Processor*):** Basis data relasional tradisional tidak mampu menampung lonjakan data telemetri tersebut. Teknologi Big Data (seperti Apache Spark, Kafka, InfluxDB) menyediakan infrastruktur terdistribusi untuk menyimpan, memfilter, dan mengekstraksi nilai (*value*) serta wawasan prediktif dari data IoT tersebut.
2. **Arsitektur Sistem AIoT pada Smart Agriculture:**
   * **Tahap 1: Pengumpulan Data (Sensing Layer):** Node sensor ESP32 yang ditanam di lahan pertanian mengukur parameter lingkungan secara berkala (Sensor kelembaban tanah kapasitif, sensor pH tanah, dan sensor suhu/kelembaban udara BME280).
   * **Tahap 2: Transmisi Jaringan (Network Layer):** Data sensor dikirimkan melalui transmisi nirkabel berdaya rendah jarak jauh (**LoRaWAN** atau Wi-Fi) ke sebuah Gateway IoT lokal, lalu diteruskan via protokol **MQTT** ke server pusat.
   * **Tahap 3: Pemrosesan & Inferensi Cerdas (Cloud/Edge Layer):** Model *Machine Learning* (misal: regresi atau Random Forest) menganalisis pola historis cuaca dan tingkat kelembaban tanah. Model memprediksi secara akurat berapa mililiter air dan nutrisi pupuk yang dibutuhkan tanaman dalam 6 jam ke depan.
   * **Tahap 4: Aksi Balik Aktuator (Actuation Layer):** Server mengirimkan perintah balik melalui MQTT ke kontroler katup solenoid (*relay*). Pompa irigasi tetes (*drip irrigation*) menyala secara otomatis selama durasi tertentu tanpa campur tangan manual petani.

---

### Soal UTS 2: Analisis Pemilihan Tingkat Layanan QoS pada Protokol MQTT
**Deskripsi Soal:**
Protokol MQTT memiliki tiga tingkatan *Quality of Service* (QoS 0, QoS 1, dan QoS 2). Tentukan level QoS yang paling tepat dan efisien untuk tiga skenario sistem IoT berikut disertai alasan teknisnya!

1. Sistem monitoring suhu dan kelembaban udara di ruang terbuka yang mengirimkan data setiap 5 detik.
2. Sistem deteksi dini gempa bumi dan alarm kebakaran pada gedung bertingkat.
3. Sistem pembayaran tol nirsentuh berbasis RFID dan dompet digital (*Electronic Toll Collection*).

**Kunci Pembahasan & Solusi:**
1. **Skenario 1 (Monitoring Suhu Lingkungan): $\rightarrow$ Gunakan **QoS 0** (*At most once*)**
   * *Alasan Teknis:* Frekuensi pengiriman sangat tinggi (setiap 5 detik) dan perubahan suhu berlangsung lambat. Kehilangan satu paket data di jalan tidak berdampak kritis bagi sistem karena paket data 5 detik berikutnya akan segera menimpa (*overwrite*) data lama. QoS 0 memberikan konsumsi daya baterai dan penggunaan bandwidth yang paling hemat.
2. **Skenario 2 (Deteksi Dini Kebakaran / Alarm Darurat): $\rightarrow$ Gunakan **QoS 1** (*At least once*)**
   * *Alasan Teknis:* Pesan peringatan bahaya **wajib sampai** ke penerima agar sirine darurat berbunyi. Pengirim akan terus mengirim ulang (*retry*) hingga menerima paket konfirmasi `PUBACK` dari broker. Adanya duplikasi pesan (misal alarm menerima sinyal trigger dua kali) tidak membahayakan sistem, yang terpenting adalah pesan tidak boleh hilang.
3. **Skenario 3 (Transaksi Pembayaran Tol Digital): $\rightarrow$ Gunakan **QoS 2** (*Exactly once*)**
   * *Alasan Teknis:* Transaksi keuangan mutlak membutuhkan konsistensi data yang ketat. Jika menggunakan QoS 0, pemotongan saldo bisa gagal dan gerbang tol tidak membuka. Jika menggunakan QoS 1, saldo pengguna berisiko terpotong ganda (*double charge*) akibat pengiriman ulang pesan. QoS 2 menjamin pesan transaksi diproses **tepat satu kali saja**.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (PEMROGRAMAN ESP32 & KEAMANAN IOT)

### Soal UAS 1: Implementasi Kode C++ Arduino ESP32 untuk MQTT Client
**Deskripsi Soal:**
Tuliskan potongan kode program C++ (*Arduino Framework*) pada mikrokontroler ESP32 menggunakan library `PubSubClient.h` yang membaca sensor potensiometer/analog pada pin `ADC_PIN` (GPIO 34), mengemas nilainya ke dalam format JSON, dan mempublikasikannya ke MQTT broker pada topik `"undip/if/telemetri"` setiap 2 detik!

**Kunci Pembahasan & Solusi (Kode C++):**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

// Konfigurasi Kredensial Jaringan Wi-Fi dan MQTT Broker
const char* ssid = "Hotspot_Kampus";
const char* password = "passwordRahasia";
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;
const char* mqtt_topic = "undip/if/telemetri";

#define POT_PIN 34 // Pin ADC1 pada ESP32 (Toleransi 0-3.3V)

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;

void setup_wifi() {
    delay(10);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
    }
}

void reconnect() {
    while (!client.connected()) {
        String clientId = "ESP32Client-" + String(random(0xffff), HEX);
        if (client.connect(clientId.c_str())) {
            // Berhasil terhubung ke broker
        } else {
            delay(5000); // Tunggu 5 detik sebelum coba lagi
        }
    }
}

void setup() {
    Serial.begin(115200);
    setup_wifi();
    client.setServer(mqtt_server, mqtt_port);
}

void loop() {
    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    unsigned long now = millis();
    // Non-blocking timer: Kirim data setiap 2000 ms (2 detik)
    if (now - lastMsg > 2000) {
        lastMsg = now;
        
        // Membaca nilai ADC (resolusi 12-bit: 0 - 4095)
        int raw_value = analogRead(POT_PIN);
        float voltage = (raw_value / 4095.0) * 3.3;

        // Membentuk payload string format JSON
        char payload[100];
        snprintf(payload, sizeof(payload), 
                 "{\"adc\": %d, \"voltage\": %.2f}", raw_value, voltage);

        // Publikasikan ke broker dengan QoS 0
        client.publish(mqtt_topic, payload);
        Serial.print("Data terkirim: ");
        Serial.println(payload);
    }
}
```

---

### Soal UAS 2: Analisis Ancaman Keamanan IoT & Kasus Serangan Mirai Botnet
**Deskripsi Soal:**
Pada tahun 2016, serangan siber berskala masif bernama **Mirai Botnet** melumpuhkan sebagian besar infrastruktur internet Amerika Serikat melalui serangan Distributed Denial of Service (DDoS).
1. Jelaskan bagaimana Mirai Botnet dapat menyebar dan menginfeksi ratusan ribu perangkat IoT (seperti IP Camera dan Router rumahan)!
2. Sebutkan 3 langkah mitigasi mendasar yang wajib diterapkan oleh seorang arsitek sistem IoT untuk mencegah perangkatnya dijadikan *zombie botnet*!

**Kunci Pembahasan & Solusi:**
1. **Mekanisme Penyebaran Mirai Botnet:**
   * **Pemindaian Otomatis Port Telnet:** Mirai terus-menerus memindai alamat IP publik di internet untuk mencari perangkat yang membuka port manajemen `Telnet (port 23)` atau `SSH (port 22)`.
   * **Serangan Dictionary Default Credentials:** Mirai membawa tabel daftar pustaka yang berisi sekitar 60 pasangan *username* dan *password* bawaan pabrik (*default credentials*) yang umum digunakan oleh produsen perangkat murah (seperti `admin/admin`, `root/123456`, `default/pass`).
   * Karena mayoritas pengguna tidak pernah mengganti kata sandi bawaan tersebut, Mirai berhasil masuk, menghapus malware pesaing di memori, dan menginstal skrip botnet yang menunggu instruksi *Command and Control* (C2) untuk membanjiri target korban dengan paket data palsu (DDoS).
2. **Tiga Langkah Mitigasi Wajib:**
   * **Wajibkan Pergantian Kredensial Saat Inisialisasi Pertama (*Enforce Password Change*):** Firmware perangkat harus menolak beroperasi dan memaksa pengguna memasukkan kata sandi baru yang kuat saat proses instalasi awal.
   * **Tutup Port Layanan yang Tidak Diperlukan:** Matikan layanan manajemen jarak jauh yang tidak aman seperti Telnet (port 23) dan HTTP biasa. Gunakan antarmuka terenkripsi (SSH port 22, HTTPS).
   * **Pembaruan Firmware Berkala dengan Tanda Tangan Digital (*Secure Signed OTA Updates*):** Memastikan sistem memiliki mekanisme perbaikan celah keamanan secara berkala, dan mikrokontroler hanya menerima pembaruan firmware yang memiliki sertifikat kriptografi resmi dari vendor (*cryptographic signature verification*).

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa protokol MQTT menggunakan arsitektur Publish/Subscribe dengan sebuah Broker perantara, bukan komunikasi langsung Point-to-Point (Client-to-Client)?"
**Jawaban Komprehensif:**
Arsitektur Publish/Subscribe via Broker memberikan keuntungan krusial yang disebut **Decoupling (Pemisahan Ketergantungan)**:
1. **Space Decoupling:** Pengirim (sensor) dan penerima (aplikasi dasbor) tidak perlu saling mengetahui alamat IP masing-masing. Keduanya hanya perlu mengetahui alamat IP satu entitas pusat, yaitu **Broker**.
2. **Time Decoupling:** Pengirim dan penerima tidak harus aktif (*online*) pada waktu yang bersamaan. Broker dapat menyimpan pesan sementara (*retained message / persistent session*) hingga klien subscriber terhubung kembali.
3. **Synchronization Decoupling:** Operasi pengiriman bersifat asinkron; mikrokontroler sensor dapat segera kembali ke mode tidur hemat energi (*deep sleep*) setelah mempublikasikan data ke broker tanpa perlu menunggu aplikasi klien selesai memproses data tersebut.

### Q2: "Apa risiko teknis jika kita menghubungkan sensor bertegangan keluaran 5 Volt secara langsung ke pin input GPIO ESP32, dan bagaimana solusinya?"
**Jawaban Komprehensif:**
* **Risiko Teknis:** ESP32 adalah mikrokontroler dengan toleransi tegangan logika maksimal **3.3 Volt**. Menyuntikkan tegangan 5 Volt secara langsung ke pin GPIO akan merusak dioda proteksi internal dan membakar gerbang silikon transistor SoC secara permanen (*overvoltage breakdown*).
* **Solusi Perangkat Keras:**
  1. Menggunakan modul **Bidirectional Logic Level Converter** berbasis MOSFET.
  2. Menggunakan rangkaian **Pembagi Tegangan (*Voltage Divider*)** sederhana menggunakan dua buah resistor:
     $$V_{\text{out}} = V_{\text{in}} \times \frac{R_2}{R_1 + R_2}$$
     *(Misal menggunakan $R_1 = 1.8\text{ k}\Omega$ dan $R_2 = 3.3\text{ k}\Omega$, tegangan 5V akan diturunkan menjadi tepat $3.23\text{ Volt}$ yang aman bagi ESP32).*
