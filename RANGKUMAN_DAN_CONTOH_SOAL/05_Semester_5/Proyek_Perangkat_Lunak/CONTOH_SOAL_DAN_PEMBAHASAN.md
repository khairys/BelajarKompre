# Bank Contoh Soal & Pembahasan: Proyek Perangkat Lunak

> **Sumber Rujukan:** Kumpulan Berkas Evaluasi Proyek & Ujian Tengah/Akhir Semester Proyek Perangkat Lunak Departemen Informatika Universitas Diponegoro (Koleksi Dosen Pengampu & Penguji Capstone Project 2017–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (USER STORIES, SPRINT MANAGEMENT & GITFLOW)

### Soal UTS 1: Dekomposisi Kebutuhan & Penulisan User Story Format Gherkin (Soal Asli Evaluasi PPL)
**Deskripsi Soal:**
Dalam proyek pengembangan aplikasi *Platform Monitoring Magang Mahasiswa*, terdapat kebutuhan sistem:
*"Mahasiswa yang sedang magang harus dapat mengunggah laporan logbook mingguan dalam format PDF (maksimal 5 MB), dan dosen pembimbing lapangan dapat memberikan persetujuan atau catatan revisi."*

**Tugas:**
1. Rancanglah **2 buah User Story** yang independen sesuai standar **INVEST** (satu untuk Mahasiswa dan satu untuk Dosen Pembimbing)!
2. Tuliskan **Acceptance Criteria (Kriteria Penerimaan)** lengkap menggunakan format sintaks **Gherkin (*Given - When - Then*)** untuk kedua user story tersebut, mencakup skenario positif (*Happy Path*) dan skenario negatif (*Validation Error*)!

**Kunci Pembahasan & Solusi:**
1. **Perancangan User Stories (Standar INVEST):**
   * **User Story 1 (Mahasiswa):**
     * *Pernyataan:* *"Sebagai seorang Mahasiswa Magang, Saya ingin mengunggah file laporan kegiatan mingguan berformat PDF, Sehingga dosen pembimbing saya dapat memantau aktivitas kerja harian saya."*
     * *Story Points:* 3
   * **User Story 2 (Dosen Pembimbing):**
     * *Pernyataan:* *"Sebagai seorang Dosen Pembimbing, Saya ingin meninjau dan memberikan status verifikasi (Disetujui / Perlu Revisi) beserta catatan umpan balik pada laporan mingguan mahasiswa bimbingan saya, Sehingga mahasiswa mengetahui evaluasi kinerjanya secara transparan."*
     * *Story Points:* 3

2. **Kriteria Penerimaan Format Gherkin:**
   * **Skenario untuk User Story 1 (Unggah Laporan):**
     * *Skenario 1.1 (Happy Path - Berkas Valid):*
       * `GIVEN` Mahasiswa telah login dan berada pada halaman *"Unggah Logbook Minggu ke-4"*
       * `WHEN` Mahasiswa memilih file dokumen berformat `.pdf` berukuran $2.4$ MB dan menekan tombol *"Kirim Laporan"*
       * `THEN` Sistem berhasil menyimpan file ke cloud storage, status logbook berubah menjadi *"Menunggu Review"*, dan muncul pesan notifikasi sukses hijau *"Laporan berhasil diunggah"*.
     * *Skenario 1.2 (Negative Path - Format File Salah):*
       * `GIVEN` Mahasiswa berada pada halaman form unggah logbook
       * `WHEN` Mahasiswa mencoba memilih file berformat `.docx` atau gambar `.jpg`
       * `THEN` Sistem menolak file tersebut, tombol submit dinonaktifkan, dan muncul pesan error merah *"Format file tidak didukung. Harap unggah dokumen berformat PDF"*.
     * *Skenario 1.3 (Negative Path - Ukuran File Melebihi Batas):*
       * `GIVEN` Mahasiswa memilih file `.pdf` dengan ukuran $7.2$ MB (melebihi batas 5 MB)
       * `WHEN` Mahasiswa menekan tombol submit
       * `THEN` Sistem membatalkan proses upload dan menampilkan pesan *"Ukuran file melebihi batas maksimal 5 MB"*.
   * **Skenario untuk User Story 2 (Review Dosen):**
     * *Skenario 2.1 (Persetujuan Dosen):*
       * `GIVEN` Dosen membuka daftar logbook mahasiswa bimbingan berstatus *"Menunggu Review"*
       * `WHEN` Dosen memilih opsi *"Setujui Logbook"* dan menekan tombol konfirmasi
       * `THEN` Status logbook diperbarui di database menjadi *"Disetujui"* dan sistem mengirimkan notifikasi email otomatis ke mahasiswa.

---

### Soal UTS 2: Manajemen Kolaborasi Gitflow & Resolusi Konflik (Merge Conflict)
**Deskripsi Soal:**
Dua orang developer dalam tim PPL sedang mengerjakan fitur secara paralel dari cabang `develop`:
* Developer A membuat branch `feature/fitur-auth` dan mengubah file `routes/api.php` pada baris ke-20.
* Developer B membuat branch `feature/fitur-payment` dan juga menambahkan rute baru pada baris ke-20 pada file yang tepat sama: `routes/api.php`.
* Developer A melakukan push dan PR-nya disetujui serta di-merge lebih dahulu ke `develop`.
* Saat Developer B mencoba melakukan merge ke `develop`, sistem Git menolak dan menampilkan pesan:
  `CONFLICT (content): Merge conflict in routes/api.php`.

**Tugas:**
Tuliskan urutan perintah Git langkah demi langkah yang harus dijalankan oleh Developer B di terminal lokalnya untuk menyelesaikan konflik tersebut secara benar dan aman tanpa menghapus kode milik Developer A!

**Kunci Pembahasan & Solusi:**
Urutan perintah terminal Git:
```bash
# 1. Pindah ke branch fitur lokal Developer B
git checkout feature/fitur-payment

# 2. Ambil pembaruan terkini dari remote repository
git fetch origin

# 3. Lakukan penggabungan (merge) perubahan terbaru cabang develop ke branch fitur lokal
git merge origin/develop

# (Git akan menghentikan proses merge otomatis dan menandai penanda konflik di file)

# 4. Developer B membuka file routes/api.php. Terlihat penanda konflik:
# <<<<<<< HEAD (Perubahan lokal Developer B)
# Route::post('/payment/charge', [PaymentController::class, 'charge']);
# =======
# Route::post('/auth/register', [AuthController::class, 'register']);
# >>>>>>> origin/develop (Perubahan remote Developer A)

# 5. Developer B mengedit file tersebut secara manual: mempertahankan KEDUA rute:
# Route::post('/auth/register', [AuthController::class, 'register']);
# Route::post('/payment/charge', [PaymentController::class, 'charge']);

# 6. Simpan file, lalu tandai konflik telah terselesaikan
git add routes/api.php

# 7. Selesaikan transaksi commit merge
git commit -m "fix(routes): resolve merge conflict between auth and payment endpoints"

# 8. Dorong kembali perubahan yang sudah bersih ke remote repository
git push origin feature/fitur-payment
```
*(Setelah langkah ini, Pull Request Developer B di GitHub/GitLab otomatis berstatus clean / can be merged).*

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (DOCKER & CI/CD PIPELINE)

### Soal UAS 1: Konfigurasi Otomatisasi CI/CD Pipeline (GitHub Actions)
**Deskripsi Soal:**
Buatlah sebuah berkas konfigurasi **GitHub Actions** (`.github/workflows/ci.yml`) untuk proyek backend Node.js / Python yang:
1. Berjalan otomatis setiap kali ada aksi `push` atau `pull_request` menuju branch `develop` dan `main`.
2. Menyiapkan lingkungan runner Ubuntu terbaru dengan versi runtime yang sesuai.
3. Menginstal seluruh dependensi pustaka.
4. Menjalankan linter untuk memeriksa standar penulisan kode.
5. Menjalankan pengujian unit otomatis (*automated unit tests*). Jika ada satu saja test yang gagal, hentikan pipeline dan tolak PR.

**Kunci Pembahasan & Solusi:**
```yaml
# .github/workflows/ci.yml
name: Continuous Integration (CI) Pipeline

# Pemicu Eksekusi Pipeline
on:
  push:
    branches: [ "main", "develop" ]
  pull_request:
    branches: [ "main", "develop" ]

jobs:
  test-and-lint:
    name: Run Linter and Unit Tests
    runs-on: ubuntu-latest

    steps:
      # 1. Unduh kode sumber dari repositori
      - name: Checkout Repository
        uses: actions/checkout@v4

      # 2. Setup Lingkungan Node.js Runtime
      - name: Setup Node.js Environment
        uses: actions/setup-node@v4
        with:
          node-version: 18.x
          cache: 'npm'

      # 3. Instal Dependensi
      - name: Install Dependencies
        run: npm ci

      # 4. Jalankan Pemeriksaan Linter Kode (ESLint)
      - name: Run Code Linter
        run: npm run lint

      # 5. Jalankan Pengujian Unit Otomatis & Cek Coverage
      - name: Run Automated Unit Tests
        run: npm test -- --coverage
```

---

### Soal UAS 2: Orkestrasi Kontainerisasi Multi-Service Menggunakan Docker Compose
**Deskripsi Soal:**
Rancanglah berkas konfigurasi **`docker-compose.yml`** untuk sistem aplikasi PPL yang mengorkestrasi 2 service terhubung:
1. Service `backend`: Dibangun dari `Dockerfile` lokal di folder `./backend`, membuka port internal $8000$ ke port host $8000$, bergantung pada database, dan menggunakan environment variable untuk kredensial database.
2. Service `database`: Menggunakan citra resmi `postgres:15-alpine`, membuka port $5432$, mendefinisikan volume persisten lokal agar data tidak hilang saat kontainer dimatikan, dan menyetel password aman.

**Kunci Pembahasan & Solusi:**
```yaml
version: '3.8'

services:
  database:
    image: postgres:15-alpine
    container_name: ppl_postgres_db
    restart: always
    environment:
      POSTGRES_DB: db_ppl_undip
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: SecretPostgresPassword123!
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - ppl_network

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: ppl_backend_service
    restart: always
    depends_on:
      - database
    ports:
      - "8000:8000"
    environment:
      DB_HOST: database
      DB_PORT: 5432
      DB_NAME: db_ppl_undip
      DB_USER: postgres
      DB_PASSWORD: SecretPostgresPassword123!
      NODE_ENV: production
    networks:
      - ppl_network

volumes:
  postgres_data:
    driver: local

networks:
  ppl_network:
    driver: bridge
```

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa estimasi beban kerja dalam Agile Scrum menggunakan Story Points berbasis Deret Fibonacci daripada langsung menaksir dalam satuan jam atau hari kerja manusia?"
**Jawaban Komprehensif:**
* **Estimasi Relatif vs Absolut:** Menaksir waktu absolut dalam hitungan jam (*man-hours*) sangat tidak akurat karena kecepatan setiap programmer berbeda-beda (seorang *senior engineer* mungkin menyelesaikan satu modul dalam 2 jam, sedangkan *junior engineer* membutuhkan 10 jam). Sebaliknya, **Story Points mengukur kompleksitas relatif, ketidakpastian, dan volume usaha** tugas tersebut dibandingkan tugas patokan dasar.
* **Alasan Menggunakan Deret Fibonacci ($1, 2, 3, 5, 8, 13, 21$):**
  Menggambarkan **Hukum Weber-Fechner** dalam psikologi kognitif: semakin besar ukuran dan ketidakpastian suatu pekerjaan, semakin sulit manusia memperkirakan detail kecilnya. Kita dapat dengan mudah membedakan perbedaan beban antara tugas berbobot 1 dan 2, tetapi memperdebatkan apakah suatu tugas berbobot 14 atau 15 jam adalah perdebatan semu yang membuang waktu. Jika sebuah tugas melompat ke angka 13 atau 21, itu adalah sinyal tegas (*red flag*) bahwa tugas tersebut terlalu raksasa (*Epic*) dan wajib dipecah menjadi beberapa story yang lebih kecil sebelum sprint dimulai.

### Q2: "Apa yang Anda lakukan sebagai Scrum Master jika grafik Sprint Burndown Chart tim Anda menunjukkan garis mendatar (plateau) selama satu minggu berturut-turut di tengah-tengah Sprint?"
**Jawaban Komprehensif:**
* **Diagnosis Masalah:** Garis burndown chart yang mendatar menandakan tidak ada satupun story points yang terselesaikan (*burned down*) menjadi status *Done*, yang mengindikasikan tim sedang mengalami **hambatan kritis (*severe impediment / blocker*)** atau *user stories* yang diambil terlalu besar dan tidak dipecah dengan baik.
* **Tindakan Konkret Scrum Master:**
  1. *Identifikasi Blocker di Daily Standup:* Menginvestigasi apakah ada ketergantungan eksternal yang macet (misal: API pihak ketiga belum siap, server staging mati, atau desain UI/UX belum final).
  2. *Hapus Hambatan (*Remove Impediments*):* Turun tangan langsung menyelesaikan hambatan tersebut atau memfasilitasi komunikasi langsung dengan pihak terkait.
  3. *Dekomposisi Ulang Pekerjaan:* Jika developer terjebak karena cakupan story terlalu luas, fasilitasi pembagian story menjadi unit tugas yang lebih kecil (*sub-tasks*) yang dapat diselesaikan dan di-review per komponen.
  4. *Negosiasi Scope dengan Product Owner:* Jika waktu sprint tersisa sedikit dan estimasi menunjukkan goal tidak akan tercapai, segera komunikasikan dengan Product Owner untuk memangkas story berprioritas rendah dari sprint backlog agar tim dapat fokus menuntaskan story inti dengan kualitas prima.
