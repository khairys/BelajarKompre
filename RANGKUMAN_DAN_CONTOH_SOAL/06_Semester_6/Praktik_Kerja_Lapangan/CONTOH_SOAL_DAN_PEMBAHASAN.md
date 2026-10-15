# Bank Contoh Soal & Pembahasan: Praktik Kerja Lapangan (Seminar PKL)

> **Sumber Rujukan:** Standar Operasional Prosedur Ujian Seminar PKL & Rubrik Evaluasi Sidang Praktik Kerja Lapangan Departemen Informatika Universitas Diponegoro (Kompilasi Pertanyaan Dosen Penguji & Pembimbing PKL Undip).

---

## 🎯 BAGIAN 1: SIMULASI PERTANYAAN SIDANG SEMINAR PKL (ARSITEKTUR & KONTRIBUSI TEKNIS)

### Q1: "Jelaskan secara spesifik apa kontribusi teknis individual yang Anda kerjakan sendiri selama magang di perusahaan, dan apa bedanya dengan pekerjaan yang diselesaikan oleh tim engineer internal perusahaan?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Memastikan bahwa mahasiswa tidak sekadar menumpang nama pada proyek besar perusahaan atau hanya melakukan pekerjaan administratif non-teknis, melainkan benar-benar menghasilkan modul rekayasa perangkat lunak mandiri.
* **Strategi Menjawab yang Benar:**
  1. *Jelaskan Batasan Modul (*System Boundary*):* *"Proyek utama perusahaan adalah 'Super-App Logistik Pelabuhan'. Kontribusi individual saya selama 3 bulan magang difokuskan secara spesifik pada **Sub-Sistem Manajemen Antrean Truk Kontainer (Truck Queue Management Module)**."*
  2. *Uraikan Deliverable Nyata:*
     * *"Saya secara mandiri merancang skema relasi database untuk 4 tabel baru (`antrean`, `jadwal_kedatangan`, `gerbang_dermaga`, `log_audit`)."*
     * *"Saya membangun 6 RESTful API endpoints backend menggunakan Node.js dan Express, lengkap dengan autentikasi JWT token."*
     * *"Saya menulis unit test otomatis menggunakan framework Jest dengan code coverage mencapai $84\%$."*
  3. *Tegaskan Peran dalam Integrasi Tim:* *"Modul yang saya bangun kemudian diintegrasikan ke dalam repositori utama tim engineer senior melalui mekanisme Pull Request (PR) setelah melalui code review berkala."*

---

### Q2: "Mengapa Anda dan tim perusahaan memilih arsitektur Microservices / Monolithic pada proyek magang ini? Apa kelebihan dan tantangan teknis yang Anda hadapi dengan arsitektur tersebut?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Menguji pemahaman mahasiswa terhadap *trade-off* keputusan desain arsitektur perangkat lunak dalam konteks industri nyata.
* **Strategi Menjawab yang Benar:**
  * *"Tim memilih arsitektur **Modular Monolithic** (bukan microservices penuh) karena skala tim pengembang internal masih berukuran 5 orang insinyur dan beban komputasi transaksi perusahaan masih dapat ditangani oleh satu cluster server database vertikal."*
  * *"Keputusan ini menguntungkan proyek magang saya karena: kami tidak perlu menghadapi kompleksitas terdistribusi tingkat tinggi seperti *Distributed Tracing*, *Network Latency overhead*, dan konsistensi transaksi data multi-database (*Two-Phase Commit / Saga Pattern*). Kecepatan pengembangan fitur baru (*time-to-market*) menjadi jauh lebih cepat."*
  * *"Namun tantangannya, kedisiplinan pembagian boundary modul wajib ditegakkan dengan ketat agar kode tidak menjadi 'Big Ball of Mud'. Kami menerapkan *Clean Architecture* dengan memisahkan lapisan Controller, Service/Use Case, dan Data Repository."*

---

### Q3: "Bagaimana alur kerja kolaborasi Git (Gitflow) yang diterapkan di perusahaan tempat Anda magang? Ceritakan pengalaman Anda saat terjadi konflik kode (Merge Conflict) atau kegagalan pipeline CI/CD!"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Menilai kesiapan profesional mahasiswa dalam mengikuti standar kolaborasi rekayasa modern industri.
* **Strategi Menjawab yang Benar:**
  * *"Perusahaan menerapkan standar **Gitflow** dengan aturan proteksi cabang (*branch protection rules*) ketat: cabang `main` hanya untuk produksi dan cabang `develop` untuk integrasi staging. Mahasiswa magang dilarang keras melakukan push langsung ke `develop`."*
  * *"Setiap tugas fitur dikerjakan pada branch terpisah `feature/NIM-nama-fitur`. Sebelum mengajukan Pull Request (PR), saya diwajibkan melakukan `git pull --rebase origin develop` di lokal untuk memastikan kode saya sinkron dengan update rekan lain."*
  * *"Pengalaman saat menghadapi konflik: Pernah terjadi merge conflict pada file migrasi database dan rute API saat rekan tim lain mengubah file yang sama. Saya menyelesaikan konflik tersebut dengan membuka sesi diskusi singkat bersama engineer bersangkutan, membedah perbedaan logika kode baris per baris di editor, memilih kode gabungan yang benar, menjalankan seluruh test unit lokal untuk memastikan tidak ada fitur yang rusak, baru kemudian menyelesaikan merge dan mendorong commit yang bersih."*

---

## 🎯 BAGIAN 2: SIMULASI PENGUJIAN LOGIKA SISTEM, DATABASE & KEAMANAN

### Q1: "Coba buka diagram ERD dan skema database pada Laporan PKL Anda di Bab 3. Mengapa atribut foreign key ini diletakkan di tabel ini? Dan bagaimana Anda menjamin integritas referensial data jika data induk dihapus?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Menguji fondasi teori basis data relasional (MBD) mahasiswa yang diterapkan pada kasus nyata.
* **Strategi Menjawab yang Benar:**
  * *"Relasi antara tabel `Dermaga` dan tabel `AntreanTruk` adalah kardinalitas $1:N$ (Satu dermaga dapat melayani banyak antrean truk). Sesuai aturan normalisasi relasional, atribut Foreign Key `id_dermaga` wajib diletakkan pada entitas sisi banyak ($N$), yaitu pada tabel `AntreanTruk`."*
  * *"Untuk menjamin integritas referensial (*referential integrity*), kami menyetel aturan kekangan (*constraint rule*): `ON DELETE RESTRICT` (atau `ON DELETE NO ACTION`). Sistem tidak akan mengizinkan penghapusan data master dermaga jika masih terdapat record antrean truk aktif yang merujuk padanya, guna mencegah terjadinya record yatim (*orphan records*). Untuk data historis riwayat yang dibatalkan, kami menerapkan teknik **Soft Delete** menggunakan kolom penanda `deleted_at TIMESTAMP` alih-alih menghapus baris fisik dari hard disk."*

---

### Q2: "Bagaimana Anda memastikan bahwa API backend atau form aplikasi yang Anda bangun selama magang aman dari serangan siber umum seperti SQL Injection dan Cross-Site Scripting (XSS)?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Memastikan mahasiswa memahami aspek keamanan perangkat lunak standar OWASP Top 10 pada aplikasi produksi.
* **Strategi Menjawab yang Benar:**
  * *"Untuk menangkal **SQL Injection**: Seluruh interaksi kueri database pada modul saya wajib menggunakan **Object-Relational Mapping (ORM / Query Builder)** yang mengimplementasikan *Prepared Statements* dan *Parametric Binding* secara native. Tidak ada satupun kueri yang menggunakan konkatenasi string SQL mentah dari variabel masukan pengguna."*
  * *"Untuk menangkal **Cross-Site Scripting (XSS)**: Seluruh input teks dari pengguna divalidasi dan disanitasi menggunakan pustaka pembersih (seperti `DOMPurify` / *HTML Entity Encoding*) sebelum ditampilkan kembali ke layar browser, serta menyetel header HTTP `Content-Security-Policy (CSP)`."*
  * *"Untuk proteksi autentikasi: Kami menyetel cookie sesi dengan atribut bendera `HttpOnly` (mencegah pencurian token via skrip JavaScript jahat), `Secure` (hanya dikirim melalui enkripsi HTTPS), dan `SameSite=Strict` untuk memitigasi serangan CSRF."*

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF MATA KULIAH PKL

### Q1: "Apa korelasi antara permasalahan industri yang Anda temukan selama PKL dengan ide topik penelitian Tugas Akhir / Skripsi yang akan Anda ajukan?"
**Jawaban Komprehensif:**
* *"Salah satu manfaat terbesar dari pelaksanaan PKL adalah penemuan celah masalah nyata (*real industry gaps*) yang layak diangkat menjadi topik penelitian skripsi yang bernilai guna tinggi, bukan sekadar topik artifisial."*
* *"Selama PKL di industri logistik, saya menemukan bahwa sistem penjadwalan antrean truk saat ini masih menggunakan aturan heuristik manual sederhana berbasis waktu kedatangan (*First-Come First-Served / FCFS*), yang sering menyebabkan kemacetan parah saat terjadi keterlambatan kapal kontainer."*
* *"Oleh karena itu, untuk penelitian Tugas Akhir/Skripsi, saya merencanakan untuk mengusulkan judul penelitian: **'Optimasi Penjadwalan Dinamis Antrean Truk Kontainer Menggunakan Algoritma Genetika (Genetic Algorithm) / Deep Reinforcement Learning'**. Data riil dan parameter operasional yang telah saya pelajari selama PKL menjadi modal dasar empiris yang sangat kuat untuk memvalidasi model komputasi skripsi saya kelak."*

### Q2: "Sebutkan pelajaran non-teknis (Soft Skills) paling berharga yang Anda peroleh selama magang yang tidak diajarkan secara langsung di bangku perkuliahan kelas!"
**Jawaban Komprehensif:**
* *"Tiga soft skills paling berharga yang saya pelajari:"*
  1. *Komunikasi Lintas Disiplin (*Cross-Functional Communication*):* Kemampuan menjelaskan konsep teknis komputasi yang rumit (seperti struktur API atau latensi database) kepada pemangku kepentingan non-teknis (manajer operasional dan klien bisnis) menggunakan bahasa bisnis yang mudah dipahami.
  2. *Manajemen Ekspektasi & Komitmen Tenggat Waktu:* Belajar bersikap realistis dalam mengestimasi beban kerja fitur dan berani menyampaikan secara transparan (*early escalation*) jika ada kendala, daripada berjanji palsu dan terlambat di akhir.
  3. *Empati Pengguna (*User Empathy*):* Menyadari bahwa keindahan arsitektur kode atau algoritma canggih tidak ada artinya jika antarmuka aplikasi membingungkan pengguna operasional di lapangan. Desain sistem harus selalu berorientasi mempermudah pekerjaan manusia.
