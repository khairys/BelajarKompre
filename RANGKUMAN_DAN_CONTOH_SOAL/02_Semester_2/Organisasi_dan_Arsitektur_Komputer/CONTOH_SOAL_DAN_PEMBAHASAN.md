# Bank Contoh Soal & Pembahasan: Organisasi dan Arsitektur Komputer

> Sumber rujukan: Bank soal UTS & UAS Organisasi dan Arsitektur Komputer Departemen Informatika Universitas Diponegoro (Koleksi Dosen Pengampu: Sutikno, S.T., M.Cs. & Tim Dosen Orkom Undip, 2019–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (KINERJA CPU, HUKUM AMDAHL & CACHE MAPPING)

### Soal UTS 1: Perhitungan Pembagian Bit Alamat pada Cache Memory
**Deskripsi Soal:**
Sebuah komputer memiliki ruang alamat memori utama 32-bit ($2^{32}$ Byte / 4 GB) dengan pengalamatan berbasis *byte* (*Byte-addressable*). Sistem dilengkapi dengan memori cache berkapasitas **64 KB** dengan ukuran setiap blok/baris sebesar **16 Byte**.
1. Jika sistem menggunakan pemetaan langsung (**Direct Mapping**), tentukan pembagian bit alamat untuk bidang **Tag**, **Line / Slot Index**, dan **Word Offset**!
2. Jika sistem diubah menggunakan pemetaan asosiatif set 4-jalur (**4-Way Set-Associative Mapping**), tentukan kembali pembagian bit alamat untuk bidang **Tag**, **Set Index**, dan **Word Offset**!

**Kunci Pembahasan & Solusi:**
1. **Analisis untuk Pemetaan Langsung (Direct Mapping):**
   * Total bit alamat = $32$ bit.
   * **Ukuran Blok:** $16\text{ Byte} = 2^4\text{ Byte} \implies \mathbf{\text{Word Offset} = 4\text{ bit}}$.
   * **Jumlah Line di Cache:**
     $$\text{Jumlah Line} = \frac{\text{Kapasitas Cache}}{\text{Ukuran Blok}} = \frac{64\text{ KB}}{16\text{ Byte}} = \frac{64 \times 1024}{16} = 4096\text{ baris} = 2^{12}$$
     Maka, $\mathbf{\text{Line Index} = 12\text{ bit}}$.
   * **Jumlah Bit Tag:**
     $$\text{Tag} = \text{Total Bit} - \text{Line Index} - \text{Offset} = 32 - 12 - 4 = \mathbf{16\text{ bit}}$$
   * **Format Alamat Direct Mapping:**
     `[ Tag: 16 bit | Line Index: 12 bit | Word Offset: 4 bit ]`
2. **Analisis untuk 4-Way Set-Associative Mapping:**
   * **Word Offset:** Tetap sama karena ukuran blok tidak berubah $= \mathbf{4\text{ bit}}$.
   * **Jumlah Set di Cache:**
     $$\text{Jumlah Set} = \frac{\text{Total Line}}{k} = \frac{4096}{4} = 1024\text{ set} = 2^{10}$$
     Maka, $\mathbf{\text{Set Index} = 10\text{ bit}}$.
   * **Jumlah Bit Tag:**
     $$\text{Tag} = \text{Total Bit} - \text{Set Index} - \text{Offset} = 32 - 10 - 4 = \mathbf{18\text{ bit}}$$
   * **Format Alamat 4-Way Set-Associative:**
     `[ Tag: 18 bit | Set Index: 10 bit | Word Offset: 4 bit ]`

---

### Soal UTS 2: Analisis Kinerja CPU & Hukum Amdahl
**Deskripsi Soal:**
Sebuah program ilmiah membutuhkan waktu eksekusi total 100 detik pada prosesor *single-core*. Dari profil eksekusi program, diketahui bahwa $80\%$ dari total waktu eksekusi tersebut terdiri atas operasi matriks yang dapat diparalelkan secara sempurna ke multi-core, sedangkan sisanya $20\%$ merupakan kode sekuensial murni yang tidak dapat dibagi.
1. Berdasarkan **Hukum Amdahl**, berapakah peningkatan kecepatan (*Speedup*) dan waktu eksekusi total jika program dijalankan pada sistem prosesor dengan **8 core**?
2. Berapakah batas teoritis peningkatan kecepatan maksimum (*Maximum Theoretical Speedup*) yang mungkin dicapai jika jumlah core prosesor ditambah tanpa batas ($N \to \infty$)?

**Kunci Pembahasan & Solusi:**
1. **Peningkatan Kecepatan pada 8 Core:**
   * Fraksi yang dapat diparalelkan: $f = 80\% = 0.8$.
   * Fraksi sekuensial: $1 - f = 20\% = 0.2$.
   * Faktor peningkatan paralel ($k$): $8$ core.
   * **Rumus Hukum Amdahl:**
     $$S = \frac{1}{(1 - f) + \frac{f}{k}} = \frac{1}{0.2 + \frac{0.8}{8}} = \frac{1}{0.2 + 0.1} = \frac{1}{0.3} \approx \mathbf{3.33\times}$$
   * **Waktu Eksekusi Baru:**
     $$\text{Waktu Baru} = \frac{\text{Waktu Awal}}{S} = \frac{100\text{ detik}}{3.333} = \mathbf{30\text{ detik}}$$
     *(Atau: $T_{\text{baru}} = T_{\text{sekuensial}} + \frac{T_{\text{paralel}}}{8} = 20\text{ s} + \frac{80\text{ s}}{8} = 20 + 10 = 30\text{ detik}$).*
2. **Batas Teoretis Maksimum ($k \to \infty$):**
   $$S_{\max} = \lim_{k \to \infty} \frac{1}{(1 - f) + \frac{f}{k}} = \frac{1}{1 - f} = \frac{1}{0.2} = \mathbf{5\times}$$
   Berapa pun banyaknya core yang ditambahkan (bahkan jika dipasang 1.000 core sekalipun), program tidak akan pernah berjalan lebih cepat dari $5\times$ lipat (waktu eksekusi tidak akan pernah bisa lebih singkat dari 20 detik karena dibatasi oleh bagian sekuensial).

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (PIPELINE HAZARDS, RISC/CISC & DMA)

### Soal UAS 1: Analisis Data Hazard pada MIPS 5-Stage Pipeline
**Deskripsi Soal:**
Diberikan urutan instruksi bahasa rakitan (*assembly*) berikut pada prosesor MIPS 5-stage pipeline standar (IF, ID, EX, MEM, WB):
```assembly
I1: ADD R1, R2, R3    ; R1 = R2 + R3
I2: SUB R4, R1, R5    ; R4 = R1 - R5
I3: AND R6, R1, R7    ; R6 = R1 AND R7
```
1. Identifikasikan bahaya data (*Data Hazard*) tipe Read-After-Write (RAW) yang terjadi antar-instruksi di atas!
2. Jika prosesor **TIDAK memiliki** perangkat keras *Forwarding* (hanya mengandalkan *Stalling/Bubble*), berapa siklus clock yang terbuang dan pada siklus ke berapa instruksi `I2` dan `I3` dapat menyelesaikan tahap WB? *(Asumsikan register dapat dibaca dan ditulis pada siklus yang sama: Write pada paruh pertama siklus, Read pada paruh kedua).*
3. Bagaimana mekanisme **Data Forwarding (Bypassing)** dapat menyelesaikan permasalahan tersebut tanpa menunda (*stall*) pipeline?

**Kunci Pembahasan & Solusi:**
1. **Identifikasi Ketergantungan Data RAW:**
   * Instruksi `I1` menghasilkan nilai baru pada register `R1`. Nilai `R1` ini baru dituliskan kembali ke Register File pada tahap **WB (Write Back)** (siklus ke-5).
   * Instruksi `I2` dan `I3` keduanya membutuhkan nilai `R1` sebagai operand masukan pada tahap **ID (Instruction Decode / Register Read)**. Terjadi dependensi data RAW.
2. **Eksekusi Tanpa Forwarding (Dengan Pipeline Stall):**
   * Siklus 1: `I1` masuk tahap IF.
   * Siklus 2: `I1` di ID; `I2` di IF.
   * Siklus 3: `I1` di EX; `I2` tertahan di ID (Stall 1 karena `R1` belum ada).
   * Siklus 4: `I1` di MEM; `I2` masih tertahan di ID (Stall 2).
   * Siklus 5: `I1` di WB (menulis `R1` pada paruh pertama siklus); `I2` akhirnya dapat membaca `R1` di ID pada paruh kedua siklus!
   * *Kesimpulan:* Terjadi pemborosan **2 siklus clock (*bubble*)**.
3. **Penyelesaian dengan Data Forwarding (Bypassing):**
   * Nilai hasil penjumlahan $R2 + R3$ sebenarnya sudah tersedia secara fisik di output ALU pada akhir tahap **EX** instruksi `I1` (siklus ke-3).
   * Sirkuit pendeteksi hazard (*Forwarding Unit*) dapat langsung mengalirkan (*bypass*) kabel jalur data dari register perantara `EX/MEM` langsung ke input ALU tahap `EX` untuk instruksi `I2` pada siklus ke-4.
   * Dengan *Forwarding*, instruksi `I2` dan `I3` dapat berjalan **tanpa penundaan (0 stall cycle)**.

---

### Soal UAS 2: Perbandingan Direct Memory Access (DMA) vs Interrupt-Driven I/O
**Deskripsi Soal:**
Sebuah kartu antarmuka jaringan (*Network Interface Card - NIC*) menerima paket data masuk berukuran 10 Megabyte dari jaringan internet berkecepatan tinggi. Bandingkan efisiensi beban kerja prosesor antara metode **Interrupt-Driven I/O** dan metode **Direct Memory Access (DMA)** dalam menangani transfer data tersebut!

**Kunci Pembahasan & Solusi:**
1. **Analisis Metode Interrupt-Driven I/O:**
   * Pada interrupt-driven I/O standar, transfer data dilakukan per kata (*word-by-word* atau per byte).
   * Setiap kali 1 kata data (misal 4 byte) tiba di buffer antarmuka, kontroler I/O mengirimkan sinyal interupsi ke CPU.
   * CPU harus menghentikan program yang sedang berjalan, menyimpan status konteks register (*context switching*), mengeksekusi rutin layanan interupsi (ISR) untuk membaca data dari port I/O dan menulisnya ke RAM, lalu memulihkan konteks.
   * Untuk data berukuran 10 MB, CPU akan diinterupsi sebanyak:
     $$\text{Jumlah Interupsi} = \frac{10 \times 10^6\text{ Byte}}{4\text{ Byte}} = 2.500.000\text{ kali!}$$
   * *Dampak:* CPU akan mengalami *thrashing* (seluruh kapasitas siklus clock habis terkuras hanya untuk melayani jutaan interupsi), melumpuhkan sistem komputer.
2. **Analisis Metode Direct Memory Access (DMA):**
   * CPU hanya menginisialisasi modul pengontrol DMA di awal dengan mengirimkan: alamat awal buffer RAM, arah transfer, dan jumlah byte (10 MB).
   * Setelah diinisialisasi, pengontrol DMA mengambil alih kendali bus data (*bus mastering* via *cycle stealing*) dan mentransfer seluruh aliran data 10 MB **langsung dari kartu antarmuka ke RAM utama secara otonom**.
   * CPU bebas menjalankan program komputasi lain selama transfer berlangsung.
   * Setelah seluruh blok 10 MB selesai ditransfer ke RAM, modul DMA hanya mengirimkan **tepat 1 kali sinyal interupsi** ke CPU untuk mengabarkan bahwa transfer telah usai.
   * *Kesimpulan:* DMA jauh lebih efisien, mereduksi overhead beban CPU dari jutaan interupsi menjadi hanya 1 kali interupsi saja.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa arsitektur prosesor modern memisahkan Cache Level 1 menjadi Instruction Cache (I-Cache) dan Data Cache (D-Cache), padahal arsitektur Von Neumann menyatakan instruksi dan data disimpan di tempat yang sama?"
**Jawaban Komprehensif:**
Pemisahan tersebut (dikenal sebagai **Modified Harvard Architecture** pada level Cache L1) dirancang secara spesifik untuk mengeliminasi **Structural Hazard** pada pipeline instruksi:
Dalam prosesor dengan pipeline 5 tahap, pada sembarang siklus clock, tahap **IF (Instruction Fetch)** perlu membaca instruksi baru dari memori, sementara pada saat yang bersamaan tahap **MEM (Memory Access)** dari instruksi yang lebih lama (seperti `LW` atau `SW`) perlu membaca/menulis data ke memori.
Jika L1 Cache hanya berupa satu memori tunggal dengan satu port akses, kedua tahapan ini akan berebut bus memori (*structural conflict*), memaksa salah satu tahapan ditunda (*stall*). Dengan memisahkan I-Cache dan D-Cache, pembacaan instruksi dan akses data dapat dieksekusi secara simultan pada siklus clock yang sama tanpa konflik perangkat keras.

### Q2: "Jelaskan perbedaan antara kebijakan penulisan cache Write-Through dan Write-Back serta fungsi dari Dirty Bit!"
**Jawaban Komprehensif:**
* **Write-Through:** Setiap kali operasi penulisan data dilakukan ke blok cache, data baru tersebut **segera dituliskan juga ke memori utama (RAM)** pada saat yang sama. Kelebihan: memori utama selalu mutakhir dan konsisten dengan cache. Kelemahan: memicu kepadatan lalu lintas bus memori dan lambat.
* **Write-Back:** Data baru **hanya dituliskan ke baris cache**, sementara penulisan ke memori utama ditunda hingga blok tersebut harus digusur (*evicted*) karena digantikan oleh blok memori lain.
* **Fungsi Dirty Bit (Modified Bit):** Dalam kebijakan Write-Back, setiap baris cache dilengkapi dengan 1-bit status *Dirty Bit*. Jika bit ini bernilai `1`, artinya data di cache telah dimodifikasi oleh CPU dan berbeda dari data di RAM utama; sehingga saat blok tersebut akan digusur, pengontrol cache tahu bahwa blok tersebut **wajib disalin balik (*written back*) ke RAM**. Jika dirty bit bernilai `0` (bersih), blok dapat langsung ditimpa tanpa perlu disalin ke RAM, menghemat separuh waktu siklus bus.
