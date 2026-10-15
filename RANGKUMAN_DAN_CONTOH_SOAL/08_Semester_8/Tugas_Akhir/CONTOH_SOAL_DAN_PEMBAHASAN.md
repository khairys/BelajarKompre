# Bank Contoh Soal & Pembahasan: Ujian Sidang Skripsi & Ujian Lisan Komprehensif (Oral Defense S1 Informatika Undip)

> **Sumber Rujukan:** Kompilasi Bank Pertanyaan Majelis Penguji Sidang Tugas Akhir Departemen Informatika FSM Universitas Diponegoro (Kategori: Pertanyaan Kritis Naskah Skripsi Bab I–V, Pengujian Sistem/Kode Live Demo, dan Pertanyaan Ujian Komprehensif Lisan Lintas Kurikulum).

---

## 🎯 BAGIAN 1: SIMULASI PERTANYAAN KRITIS SIDANG SKRIPSI (SUBSTANSI BAB I S.D. BAB V)

### Q1: "Coba jelaskan dalam waktu 2 menit secara lugas: apa novelty (kebaruan) atau kontribusi pembeda penelitian Anda dibandingkan dengan 3 penelitian rujukan utama pada matriks pustaka Bab 2?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Memastikan mahasiswa memahami posisi kontribusi ilmiah penelitiannya (*scientific positioning*) dan tidak sekadar menjiplak (*copy-paste*) kode atau ide dari paper orang lain.
* **Strategi Menjawab yang Benar:**
  * *"Terima kasih atas pertanyaannya, Bapak/Ibu Penguji. Letak kontribusi dan kebaruan penelitian saya berfokus pada 3 aspek pembeda utama:"*
  1. *Perbandingan dengan Paper A (Santoso et al., 2022):* *"Penelitian terdahulu menggunakan algoritma klasifikasi Support Vector Machine (SVM) standar dengan akurasi $81\%$ namun sangat lambat pada dataset teks berskala besar. Pada penelitian ini, saya menerapkan arsitektur hybrid DistilBERT yang dioptimasi dengan teknik pruning bobot, sehingga waktu inferensi terpangkas $40\%$ dengan akurasi meningkat menjadi $89.5\%$."*
  2. *Perbandingan dengan Paper B (Widodo, 2023):* *"Penelitian terdahulu hanya menguji pada dataset benchmark berbahasa Inggris yang bersih. Kebaruan penelitian saya adalah pengembangan korpus data baru berupa data bahasa daerah/Indonesia informal (slang) dari media sosial lokal yang dilengkapi tahapan pra-pemrosesan normalisasi berbasis leksikon khusus."*
  3. *Perbandingan dengan Paper C (Kurniawan, 2024):* *"Penelitian terdahulu hanya berhenti pada evaluasi metrik teoritis di Jupyter Notebook. Pada skripsi ini, saya mengintegrasikan model ke dalam sistem antarmuka web microservices yang siap pakai dan diuji secara riil oleh pengguna akhir menggunakan kuesioner System Usability Scale (SUS) dengan skor 82.5 (Kategori Grade A)."*

---

### Q2: "Mengapa Anda memilih algoritma X dan bukan algoritma Y atau Z yang lebih populer atau lebih baru? Apa landasan ilmiah dan trade-off komputasinya?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Menguji apakah mahasiswa memilih algoritma berdasarkan justifikasi ilmiah empiris atau hanya sekadar ikut tren tanpa pemahaman mendalam.
* **Strategi Menjawab yang Benar:**
  * *"Pemilihan algoritma didasarkan pada karakteristik data dan batasan lingkungan komputasi penelitian:"*
  * *"Alasan memilih Random Forest dibandingkan Deep Learning (seperti Multi-Layer Perceptron atau CNN):"*
    1. *Skala Dataset:* Dataset yang tersedia dalam studi kasus ini berjumlah $1.500$ baris data tabular. Model Deep Learning cenderung mengalami *overfitting* ekstrem pada data tabular berukuran kecil-menengah tanpa jutaan sampel.
    2. *Kebutuhan Eksplanasi (*Model Explainability*):* Keputusan prediksi sistem ini ditujukan untuk rekomendasi medis/keuangan yang wajib dapat dijelaskan (*explainable AI*). Random Forest memungkinkan ekstraksi *Feature Importance* (Gini Impurity reduction) sehingga praktisi dapat melihat fitur apa yang paling berpengaruh terhadap keputusan sistem, berbeda dengan Deep Learning yang berkarakteristik *Black Box*.
    3. *Efisiensi Komputasi:* Waktu pelatihan Random Forest hanya membutuhkan waktu 4.2 detik pada CPU biasa tanpa memerlukan GPU kelas server.

---

### Q3: "Bagaimana proses pembagian data training dan testing Anda? Apakah ada potensi kebocoran data (Data Leakage)? Dan bagaimana Anda menangani masalah ketidakseimbangan kelas (Imbalanced Class)?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Memeriksa integritas metodologis eksperimen data science / machine learning.
* **Strategi Menjawab yang Benar:**
  * *"Untuk mencegah **Data Leakage**: Proses normalisasi data (seperti Min-Max Scaling atau Standard Scaler) dan imputasi nilai kosong (missing value) hanya dihitung (fit) berdasarkan data latih (*training set*), kemudian parameter statistik tersebut diaplikasikan (transform) ke data uji (*testing set*). Kami tidak pernah melakukan normalisasi pada seluruh dataset sebelum proses split dilakukan."*
  * *"Skema Pembagian Data:* Kami menggunakan **Stratified 5-Fold Cross Validation** untuk memastikan bahwa proporsi distribusi kelas target pada setiap fold identik dengan distribusi populasi aslinya."*
  * *"Penanganan Imbalanced Class:* Karena perbandingan kelas mayoritas dan minoritas adalah $90:10$, kami tidak menggunakan metrik Akurasi standar (karena akurasi semu bisa mencapai $90\%$ meski model hanya menebak kelas mayoritas). Kami menerapkan teknik **SMOTE (Synthetic Minority Over-sampling Technique)** pada data latih, dan mengevaluasi kinerja model menggunakan metrik **F1-Score Makro**, **Precision-Recall AUC**, dan **Confusion Matrix**."*

---

### Q4: "Di Bab 4, Anda menyatakan bahwa akurasi sistem mencapai 92%. Pertanyaan saya: mengapa sistem Anda gagal pada 8% data sisanya? Pola data seperti apa yang gagal diprediksi?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Menguji kedalaman analisis dan kejujuran ilmiah mahasiswa (penguji ingin melihat apakah mahasiswa melakukan *Error Analysis* atau hanya bangga dengan angka tinggi).
* **Strategi Menjawab yang Benar:**
  * *"Terima kasih atas pertanyaannya. Pada subbab 4.3 Pembahasan Kritis, saya telah melakukan analisis kesalahan (*Error Analysis*) secara mendalam pada 8% sampel yang salah diprediksi (*false positive* dan *false negative*):"*
  1. *Faktor Noise & Ambiguitas Konteks:* Sebagian besar kesalahan prediksi klasifikasi teks terjadi pada kalimat yang mengandung sarkasme atau negasi ganda (misal: 'Bagus sekali layanannya, sampai barang saya rusak'). Vektor representasi kata belum mampu menangkap intonasi sarkasme tanpa konteks audio.
  2. *Resolusi Gambar Rendah / Oklusi:* Pada sistem computer vision, model gagal mendeteksi objek saat tingkat pencahayaan di bawah 15 lux atau objek terhalang (*occlusion*) lebih dari $50\%$.
  3. *Solusi Saran di Bab 5:* Untuk penelitian lanjutan, kami menyarankan penambahan modul deteksi sarkasme berbasis *attention layer* atau teknik *data augmentation* berupa variasi pencahayaan ekstrem pada tahap pelatihan.

---

## 🎯 BAGIAN 2: SIMULASI PENGUJIAN SISTEM & REKAYASA KODE (LIVE DEMO)

### Q1: "Sekarang coba kita uji sistem Anda secara langsung. Apa yang terjadi jika saya memasukkan input teks kosong, karakter spesial terlarang (seperti `' OR '1'='1`), atau mengunggah berkas gambar korup berukuran 50 MB? Coba demonstrasikan di layar!"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Memeriksa kesiapan *software engineering*, penanganan galat (*exception handling*), dan aspek keamanan sistem.
* **Demonstrasi & Penjelasan yang Baik:**
  * *Tindakan di Layar:* Buka antarmuka form, masukkan input string SQL Injection atau unggah berkas abnormal, lalu tekan tombol submit.
  * *Penjelasan Lisan:*
    * *"Seperti yang terlihat di layar, sistem tidak mengalami crash (*500 Internal Server Error*). Sistem secara elegan menampilkan pesan notifikasi validasi pengguna (*flash toast*): 'Format berkas tidak valid atau ukuran melebihi batas maksimum 5 MB'."*
    * *"Di sisi arsitektur kode:* Input telah dilindungi oleh middleware validasi server-side (`express-validator` / Django Form Validation). Untuk unggahan berkas, sistem memeriksa *magic bytes* berkas (bukan hanya ekstensi `.jpg` semata) dan memotong proses unggah secara instan jika *stream* melebihi batas limit memori."*

---

### Q2: "Buka dokumen Class Diagram atau skema basis data Anda di Bab 3. Mengapa entitas A dan entitas B dihubungkan dengan relasi Many-to-Many? Dan bagaimana bentuk fisik tabelnya di database?"
**Kunci Pembahasan & Jawaban Komprehensif:**
* **Tujuan Penguji:** Menguji pemahaman pemodelan relasional dan konsep normalisasi basis data.
* **Strategi Menjawab yang Benar:**
  * *"Relasi antara entitas `Mahasiswa` dan entitas `MataKuliah` adalah Many-to-Many ($M:N$) karena satu mahasiswa dapat mengambil banyak mata kuliah, dan satu mata kuliah dapat diambil oleh banyak mahasiswa."*
  * *"Sesuai dengan kaidah Normalisasi Bentuk Ketiga (3NF), relasi $M:N$ tidak dapat diimplementasikan secara langsung dengan menyimpan daftar ID bertumpuk dalam satu kolom (melanggar 1NF / non-atomic values)."*
  * *"Oleh karena itu, dibuat satu tabel perantara (*associative entity / junction table*), yaitu tabel `KRS_Detail` yang memiliki dua foreign key (`id_mahasiswa` dan `id_mata_kuliah`) yang bersama-sama membentuk Composite Primary Key, disertai atribut tambahan transaksi seperti `nilai_akhir` dan `tahun_akademik`."*

---

## 🎯 BAGIAN 3: BANK PERTANYAAN UJIAN LISAN KOMPREHENSIF LINTAS KURIKULUM (ORAL COMPREHENSIVE DEFENSE)

### Q1: [Pilar Struktur Data & Algoritma] "Jelaskan perbedaan struktur data Hash Table dan Binary Search Tree (BST) dalam hal kompleksitas waktu pencarian (Big-O Notation) pada skenario kasus rata-rata dan kasus terburuk!"
**Kunci Pembahasan:**
* **Hash Table:**
  * *Average Case:* $\mathcal{O}(1)$ (konstan) karena menggunakan fungsi hash yang memetakan kunci langsung ke indeks array memori.
  * *Worst Case:* $\mathcal{O}(N)$ (linier) jika fungsi hash menghasilkan banyak tabrakan (*hash collisions*) sehingga semua elemen berkumpul dalam satu bucket linked list (dapat diredam menjadi $\mathcal{O}(\log N)$ jika bucket menggunakan Red-Black Tree seperti pada Java 8 HashMap).
* **Binary Search Tree (BST):**
  * *Average Case:* $\mathcal{O}(\log N)$ jika pohon dalam kondisi seimbang (*balanced tree* seperti AVL atau Red-Black Tree).
  * *Worst Case:* $\mathcal{O}(N)$ jika pohon mengalami kemiringan ekstrem (*skewed tree / degenerate tree*) di mana data disisipkan dalam urutan terurut, sehingga pohon berubah menyerupai linked list biasa.

---

### Q2: [Pilar Rekayasa Perangkat Lunak] "Jelaskan prinsip-prinsip SOLID dalam Pemrograman Berorientasi Objek (OOP) dan sebutkan contoh penerapannya pada arsitektur kode skripsi Anda!"
**Kunci Pembahasan:**
1. **S - Single Responsibility Principle (SRP):** Setiap class hanya memiliki satu alasan untuk berubah (satu tugas spesifik). *Contoh di skripsi:* Memisahkan class `UserController` (menangani HTTP request) dengan class `UserEmailService` (menangani pengiriman email).
2. **O - Open/Closed Principle (OCP):** Perangkat lunak harus terbuka untuk ekstensi tapi tertutup untuk modifikasi. *Contoh di skripsi:* Menambahkan metode pembayaran baru (QRIS) dengan membuat subclass baru dari interface `PaymentMethod` tanpa mengedit kode class `PaymentProcessor` yang sudah stabil.
3. **L - Liskov Substitution Principle (LSP):** Objek dari subclass harus dapat menggantikan objek superclass tanpa merusak kebenaran program.
4. **I - Interface Segregation Principle (ISP):** Klien tidak boleh dipaksa bergantung pada method interface yang tidak digunakannya (interface kecil dan spesifik lebih baik daripada satu interface gemuk).
5. **D - Dependency Inversion Principle (DIP):** Modul tingkat tinggi tidak boleh bergantung langsung pada modul tingkat rendah; keduanya harus bergantung pada abstraksi/interface. *Contoh di skripsi:* Service aplikasi bergantung pada interface `UserRepositoryInterface`, bukan implementasi fisik `MySQLUserRepository`.

---

### Q3: [Pilar Basis Data & Sistem Operasi] "Jelaskan apa itu sifat ACID dalam transaksi basis data, dan apa persamaan/perbedaannya dengan konsep Deadlock di Sistem Operasi?"
**Kunci Pembahasan:**
* **Sifat ACID (Basis Data):**
  * **Atomicity:** Prinsip "all-or-nothing". Seluruh rangkaian operasi dalam satu transaksi wajib selesai sukses seluruhnya, atau dibatalkan total (*rollback*) jika ada satu operasi gagal.
  * **Consistency:** Transaksi membawa database dari satu kondisi valid ke kondisi valid lainnya sesuai aturan kekangan (*integrity constraints*).
  * **Isolation:** Transaksi yang berjalan bersamaan tidak boleh saling mengganggu sebelum transaksi tersebut di-commit.
  * **Durability:** Setelah transaksi berhasil di-commit, perubahannya bersifat permanen di penyimpanan sekunder dan tidak akan hilang meski server mati mendadak.
* **Korelasi Deadlock (Sistem Operasi vs Basis Data):**
  * Keduanya menghadapi masalah **Mutual Exclusion** dan **Hold & Wait** saat dua atau lebih proses/transaksi memperebutkan kunci (*lock*) sumber daya yang sama dalam urutan silang (Proses 1 memegang Kunci A menunggu Kunci B, sementara Proses 2 memegang Kunci B menunggu Kunci A).
  * Di Sistem Operasi, deadlock ditangani via algoritma Bankir (*Deadlock Avoidance*) atau terminasi proses.
  * Di DBMS, deadlock ditangani secara otomatis melalui graf tunggu (*Wait-For Graph*); DBMS mendeteksi siklus dan secara otomatis mengorbankan (*abort/rollback*) salah satu transaksi sebagai *victim* agar transaksi lain dapat melanjutkan proses.

---

### Q4: [Pilar Jaringan Komputer & Keamanan] "Ketika seorang pengguna mengetikkan `https://undip.ac.id` di peramban web dan menekan Enter, jelaskan secara runtut apa yang terjadi dari lapisan aplikasi hingga fisik!"
**Kunci Pembahasan Runtut:**
1. **Resolusi DNS (Domain Name System):** Browser memeriksa cache lokal, kemudian mengirimkan kueri DNS via protokol UDP port 53 ke recursive DNS resolver ISP/Root/TLD nameserver untuk menerjemahkan nama domain `undip.ac.id` menjadi alamat IP publik (misal: `182.255.x.x`).
2. **Koneksi Transport & 3-Way Handshake TCP:** Browser menginisiasi jabat tangan tiga arah (SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK) via protokol TCP port 443 ke server web tujuan.
3. **TLS/SSL Handshake (Enkripsi HTTPS):** Client dan server bernegosiasi versi cipher suite, server mengirimkan sertifikat digital resmi untuk divalidasi oleh Certificate Authority (CA) browser, dan dibentuk kunci enkripsi simetris sesi (*session key*).
4. **Permintaan & Tanggapan HTTP (HTTP GET):** Browser mengirimkan permintaan HTTP GET terenkripsi. Server web (Nginx/Apache) memproses permintaan, mengeksekusi aplikasi backend, mengambil data database, dan mengembalikan HTTP Response dengan status code `200 OK` beserta berkas HTML/CSS/JS.
5. **Rendering di Peramban:** Engine browser mem-parsing HTML menjadi DOM Tree, mem-parsing CSS menjadi CSSOM Tree, menggabungkannya menjadi Render Tree, menghitung tata letak (*Layout/Reflow*), dan menggambar piksel ke layar pengguna (*Painting*).

---

## 🎯 BAGIAN 4: PANDUAN MENTAL & STRATEGI MENGHADAPI MAJELIS PENGUJI

### 1. Manajemen Waktu Presentasi (Alokasi Ideal 15 Menit)
* **Menit 00–03:** Bab I (Latar belakang masalah, urgensi riset, rumusan masalah, dan tujuan).
* **Menit 03–05:** Bab II & III (Tinjauan riset terkait, arsitektur sistem/algoritma, dan metodologi pengujian).
* **Menit 05–10:** Bab IV (Demonstrasi sistem/model, sajian tabel/grafik hasil evaluasi, dan pembahasan kritis).
* **Menit 10–12:** Bab V (Kesimpulan kuantitatif dan saran pengembangan).
* **Menit 12–15:** Cadangan waktu & penutupan presentasi.

### 2. Cara Merespons Pertanyaan Sulit atau Koreksi Dosen
* **Jika Memang Tidak Mengetahui Jawabannya:**
  * *JANGAN:* Mengarang jawaban ngawur atau berdebat tanpa dasar teori.
  * *JAWABAN BIJAK:* *"Terima kasih atas pertanyaan kritis yang sangat mendalam dari Bapak/Ibu Dosen. Sepanjang cakupan penelitian yang saya lakukan, batasan masalah difokuskan pada aspek X. Namun masukan mengenai aspek Y ini merupakan wawasan baru yang sangat berharga dan akan saya cantumkan sebagai poin saran utama serta kajian mendalam pada revisi laporan skripsi saya."*
* **Jika Data Anda Disanggah Penguji:**
  * Jawab dengan menunjukkan bukti logbook empiris di naskah: *"Izin mengklarifikasi Bapak/Ibu, pada halaman 68 tabel 4.2, data pengujian tersebut kami peroleh melalui 10 kali pengulangan eksperimen dengan seed random yang sama, dan kami lampirkan potongan log terminalnya pada Lampiran C."*
