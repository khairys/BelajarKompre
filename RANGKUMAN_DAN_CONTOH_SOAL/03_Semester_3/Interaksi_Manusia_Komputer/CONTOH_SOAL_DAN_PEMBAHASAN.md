# Bank Contoh Soal & Pembahasan: Interaksi Manusia dan Komputer

> Sumber rujukan: Bank soal UTS & UAS Interaksi Manusia dan Komputer Departemen Informatika Universitas Diponegoro (Koleksi HMIF 2018–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (RAGAM DIALOG, FITTS'S LAW & GESTALT)

### Soal UTS 1: Analisis Komparatif Ragam Gaya Interaksi (Soal Asli UTS Undip 2024)
**Deskripsi Soal:**
Sebutkan dan jelaskan 4 jenis/model dialog interaksi antara manusia dan komputer (Command Line Interface, Menu Selection, Form Fill-in, dan Direct Manipulation). Analisislah masing-masing kelebihan, kelemahan, serta profil pengguna yang paling cocok untuk model dialog tersebut!

**Kunci Pembahasan & Solusi:**
1. **Command Line Interface (CLI):**
   * *Mekanisme:* Pengguna mengetikkan perintah teks eksplisit berbasis sintaks tertentu pada terminal.
   * *Kelebihan:* Sangat cepat dan fleksibel bagi pengguna mahir (*expert users*), hemat memori dan sumber daya komputasi, mudah diotomasi via skrip *shell/bash*.
   * *Kekurangan:* *Learning curve* terjal, menuntut pengguna mengingat nama perintah dan parameter tanpa panduan visual (*recall-heavy*), rawan kesalahan pengetikan (*typo*).
   * *Profil Pengguna:* *System Administrator*, *DevOps Engineer*, dan programmer tingkat lanjut.
2. **Sistem Menu (*Menu Selection*):**
   * *Mekanisme:* Pengguna memilih satu opsi dari daftar pilihan yang terorganisasi secara visual (menu bar, dropdown, hamburger menu).
   * *Kelebihan:* Mengubah beban mengingat menjadi mengenali (*recognition rather than recall*), membatasi kemungkinan input tidak valid, struktur alur terdefinisi dengan jelas.
   * *Kekurangan:* Dapat memperlambat eksekusi jika hierarki menu bertingkat terlalu dalam (*deep nesting*), memakan banyak ruang layar.
   * *Profil Pengguna:* Pengguna umum (*novice to intermediate users*).
3. **Pengisian Formulir (*Form Fill-in*):**
   * *Mekanisme:* Menampilkan bidang-bidang isian (*text fields, radio buttons, checkboxes*) yang menyerupai formulir kertas fisik.
   * *Kelebihan:* Format pengumpulan data multi-atribut sangat terstruktur, mudah dipahami pengguna awam, mendukung validasi data di sisi klien (*real-time validation*).
   * *Kekurangan:* Membutuhkan pengetikan data yang cukup banyak, memakan ruang layar, menjemukan jika formulir terlalu panjang tanpa panduan bertahap (*multi-step wizard*).
   * *Profil Pengguna:* Pengguna aplikasi administratif, pendaftaran akun, dan transaksi perbankan.
4. **Manipulasi Langsung (*Direct Manipulation*):**
   * *Mekanisme:* Interaksi berbasis objek visual dengan aksi fisik langsung menggunakan penunjuk (menyeret berkas ke ikon tempat sampah / *drag-and-drop*, mencubit layar untuk *zoom*).
   * *Kelebihan:* Analogi fisik yang intuitif, dampak aksi langsung terlihat seketika (*instant visual feedback*), aksi bersifat reversibel (*mudah di-Undo*), waktu pelatihan sangat singkat.
   * *Kekurangan:* Sulit memprogram aksi komputasi makro/otomatisasi abstrak, membutuhkan layar dan kartu grafis berdaya komputasi lebih tinggi.
   * *Profil Pengguna:* Pengguna awam, anak-anak, hingga desainer grafis dan pengguna ponsel pintar layar sentuh.

---

### Soal UTS 2: Penerapan Hukum Fitts pada Desain Antarmuka Aplikasi Mobile
**Deskripsi Soal:**
Hukum Fitts dirumuskan sebagai $MT = a + b \log_2 \left( \frac{2D}{W} \right)$.
1. Jelaskan arti dari parameter $D$ dan $W$ dalam formula tersebut!
2. Berdasarkan hukum ini, mengapa peletakan tombol navigasi utama (*Bottom Navigation Bar*) dan tombol aksi utama (*Floating Action Button*) di bagian bawah layar ponsel pintar jauh lebih ergonomis dibandingkan meletakkannya di sudut kiri atas layar?

**Kunci Pembahasan & Solusi:**
1. **Arti Parameter Formula Fitts:**
   * $D$ (*Distance*): Jarak fisik yang harus ditempuh oleh jari jemari atau kursor dari posisi awalnya menuju target sasaran.
   * $W$ (*Width*): Lebar atau ukuran luas area target sentuh tombol sasaran sepanjang sumbu gerakan.
   * Nilai $\log_2(2D/W)$ disebut sebagai **Indeks Kesulitan (*Index of Difficulty - ID*)**. Semakin kecil jarak $D$ dan semakin besar ukuran target $W$, maka waktu pergerakan (*Movement Time - MT*) akan semakin cepat dan minim kesalahan meleset.
2. **Analisis Ergonomi Ponsel Pintar:**
   * Sebagian besar pengguna memegang ponsel pintar dengan satu tangan, di mana posisi istirahat ibu jari berada di paruh bawah layar ponsel (*Thumb Zone*).
   * Meletakkan tombol di **bagian bawah layar** meminimalkan nilai jarak tempuh ($D \approx 0$). Akibatnya, waktu reaksi pengguna menjadi instan dan tidak melelahkan otot tangan.
   * Sebaliknya, sudut kiri atas layar memiliki jarak $D$ terjauh dari jangkauan ibu jari dan mengharuskan pengguna meregangkan jari atau menggunakan tangan kedua (*two-handed grip*), yang meningkatkan waktu pergerakan dan risiko ponsel tergelincir jatuh.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (EVALUASI HEURISTIK NIELSEN & SKOR SUS)

### Soal UAS 1: Audit Usabilitas Berdasarkan 10 Heuristik Jakob Nielsen
**Deskripsi Soal:**
Sebuah portal sistem informasi akademik kampus memiliki beberapa kelemahan antarmuka berikut:
1. Ketika mahasiswa menekan tombol "Kirim KRS", layar menjadi beku (*freeze*) berwarna putih tanpa ada animasi loading atau teks apa pun selama 15 detik, sehingga mahasiswa mengklik tombol tersebut berulang kali.
2. Ketika mahasiswa tidak sengaja menekan tombol "Hapus Rencana Studi", seluruh data mata kuliah langsung terhapus seketika tanpa ada jendela dialog konfirmasi dan tidak ada opsi untuk membatalkan (*Undo*).
3. Ketika terjadi kesalahan server saat login, sistem memunculkan kotak pesan bertuliskan: *"Fatal Exception: NullPointerException at org.undip.auth.impl line 348"*.

Tentukan prinsip **Heuristik Jakob Nielsen** mana yang dilanggar oleh masing-masing kasus di atas, dan berikan rekomendasi solusi desain perbaikannya!

**Kunci Pembahasan & Solusi:**
1. **Kasus 1: Melanggar Heuristik #1 - *Visibility of System Status***
   * *Analisis:* Sistem gagal memberikan umpan balik tepat waktu tentang apa yang sedang diproses di latar belakang.
   * *Rekomendasi:* Tampilkan animasi indikator loading (*spinner*) atau *progress bar*, dan nonaktifkan (*disable*) tombol kirim sementara waktu agar tidak terjadi pengiriman formulir ganda.
2. **Kasus 2: Melanggar Heuristik #3 (*User Control and Freedom*) & Heuristik #5 (*Error Prevention*)**
   * *Analisis:* Sistem tidak mencegah terjadinya kesalahan fatal dan tidak menyediakan "pintu darurat" pemulihan bagi pengguna.
   * *Rekomendasi:* Berikan jendela dialog konfirmasi sebelum aksi destruktif dijalankan (*"Apakah Anda yakin ingin menghapus seluruh rencana studi?"*) serta sediakan tombol pembatalan aksi (*Undo snackbar notification*) selama 10 detik pasca-penghapusan.
3. **Kasus 3: Melanggar Heuristik #9 - *Help Users Recognize, Diagnose, and Recover from Errors***
   * *Analisis:* Pesan error menggunakan bahasa kode internal pengembang yang membingungkan orang awam dan tidak menawarkan solusi.
   * *Rekomendasi:* Ubah pesan kesalahan menjadi bahasa manusiawi yang empatik dan solutif, misalnya: *"Gagal masuk ke sistem: Kata sandi yang Anda masukkan salah. Silakan periksa kembali tombol Caps Lock Anda atau klik 'Lupa Kata Sandi' untuk mereset."*

---

### Soal UAS 2: Perhitungan dan Interpretasi Skor System Usability Scale (SUS)
**Deskripsi Soal:**
Sebuah prototipe aplikasi mobile diuji kepada seorang responden menggunakan kuesioner **System Usability Scale (SUS)** dengan skala Likert 1 (Sangat Tidak Setuju) hingga 5 (Sangat Setuju). Responden memberikan skor penilaian pada 10 butir pertanyaan sebagai berikut:
* Butir Ganjil (Positif): $Q_1 = 4, \; Q_3 = 5, \; Q_5 = 4, \; Q_7 = 5, \; Q_9 = 4$
* Butir Genap (Negatif): $Q_2 = 2, \; Q_4 = 1, \; Q_6 = 2, \; Q_8 = 1, \; Q_{10} = 2$

1. Hitunglah total skor akhir SUS dari responden tersebut menggunakan rumus konversi baku SUS!
2. Apakah aplikasi tersebut dapat dikategorikan layak (*acceptable*) berdasarkan standar rata-rata usabilitas industri? Jelaskan interpretasinya!

**Kunci Pembahasan & Solusi:**
1. **Rumus Perhitungan Skor SUS:**
   * Untuk setiap butir pertanyaan ganjil ($1, 3, 5, 7, 9$), kontribusi skor adalah: $\text{Skor} - 1$.
     $$\text{Total Ganjil} = (4 - 1) + (5 - 1) + (4 - 1) + (5 - 1) + (4 - 1) = 3 + 4 + 3 + 4 + 3 = \mathbf{17}$$
   * Untuk setiap butir pertanyaan genap ($2, 4, 6, 8, 10$), kontribusi skor adalah: $5 - \text{Skor}$.
     $$\text{Total Genap} = (5 - 2) + (5 - 1) + (5 - 2) + (5 - 1) + (5 - 2) = 3 + 4 + 3 + 4 + 3 = \mathbf{17}$$
   * Jumlahkan total kontribusi skor, lalu kalikan dengan faktor skala **$2.5$**:
     $$\text{Skor SUS Akhir} = (\text{Total Ganjil} + \text{Total Genap}) \times 2.5 = (17 + 17) \times 2.5 = 34 \times 2.5 = \mathbf{85}$$
2. **Interpretasi Hasil Pengujian:**
   * Skor SUS yang diperoleh adalah **$85$**.
   * Standar rata-rata usabilitas industri global (*global benchmark*) adalah **$68$**.
   * Karena skor $85 > 68$, aplikasi ini berada jauh di atas rata-rata industri dan masuk dalam kategori **Acceptable (Sangat Layak Digunakan)**.
   * Berdasarkan kurva penilaian baku (*Sauro-Lewis Grade Scale*), skor 85 mendapat predikat **Grade A (Excellent / Sangat Memuaskan)**, yang menandakan bahwa pengguna merasa sistem sangat mudah dipelajari, konsisten, dan minim hambatan kognitif.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan mengapa prinsip 'Recognition Rather Than Recall' sangat penting dalam perancangan antarmuka perangkat lunak!"
**Jawaban Komprehensif:**
Prinsip ini berakar langsung pada psikologi kognitif manusia:
* *Recall* (Mengingat kembali tanpa petunjuk) membutuhkan kerja keras memori jangka pendek (*Short-Term Memory* yang terbatas $7 \pm 2$ chunks) untuk merekonstruksi informasi dari memori jangka panjang tanpa stimulus visual (contoh: mengingat perintah Linux `tar -zxvf`).
* *Recognition* (Mengenali dengan melihat petunjuk visual) memanfaatkan memori perseptual visual di mana otak hanya perlu mencocokkan stimulus di layar dengan asosiasi yang sudah tersimpan (contoh: melihat menu dropdown atau ikon folder).
Antarmuka yang baik mengurangi beban kerja mental (*cognitive load*) pengguna dengan cara menyajikan semua opsi, riwayat pencarian, dan alat bantu secara visual di layar sehingga pengguna cukup mengenali tanpa harus memeras ingatan.

### Q2: "Apa yang dimaksud dengan Dark Patterns dalam desain User Experience (UX) dan sebutkan contohnya?"
**Jawaban Komprehensif:**
*Dark Patterns* adalah trik manipulasi antarmuka yang sengaja dirancang oleh pengembang untuk mengelabui atau memaksa pengguna melakukan hal yang sebenarnya tidak ingin mereka lakukan demi keuntungan sepihak bisnis (*unethical design*).
Contoh umum:
1. **Roach Motel:** Sangat mudah untuk mendaftar langganan berbayar (*1-click subscribe*), tetapi tombol untuk berhenti berlangganan (*cancel subscription*) disembunyikan secara sengaja di balik menu berliku-liku atau mengharuskan panggilan telepon langsung.
2. **Confirmshaming:** Memanipulasi emosi atau rasa bersalah pengguna saat menolak penawaran (contoh tombol penolakan pop-up bertuliskan: *"Tidak, saya tidak peduli dengan lingkungan hidup"* alih-alih sekadar tombol *"Batal"*).
3. **Sneak into Basket:** Memasukkan produk tambahan (seperti asuransi perjalanan) secara diam-diam ke dalam keranjang belanja saat *checkout* dengan mencentang kotak persetujuan secara default.
