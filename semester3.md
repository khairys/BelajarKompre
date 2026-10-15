# RANGKUMAN LENGKAP SEMESTER 3
## Persiapan Ujian Komprehensif S1 Informatika — Universitas Diponegoro

## GAMBARAN UMUM SEMESTER 3

Semester 3 memperdalam fondasi Informatika yang mulai dibangun pada semester sebelumnya. Pada tahap ini, Anda tidak cukup hanya bisa membuat program. Anda harus memahami cara data disimpan, bagaimana aplikasi berinteraksi dengan manusia, bagaimana algoritma numerik menyelesaikan masalah matematis, bagaimana sistem operasi mengelola proses, dan bagaimana kesimpulan ditarik dari data.

Keenam mata kuliah saling berhubungan:

| Mata kuliah | Fokus utama |
|---|---|
| Basis Data | Menyimpan, mengorganisasikan, dan mengambil data |
| Interaksi Manusia dan Komputer | Merancang sistem yang mudah dan aman digunakan |
| Metode Numerik | Menyelesaikan persoalan matematis secara aproksimatif |
| Sistem Operasi | Mengelola proses, memori, penyimpanan, dan perangkat |
| Statistika | Menganalisis data dan menarik kesimpulan berdasarkan bukti |
| Struktur Data | Mengorganisasikan data agar operasi komputasi efisien |

Catatan kurikulum: repositori menggunakan pembagian semester berdasarkan Kurikulum 2020. Berkas Metode Numerik dan Statistika juga menyebut bahwa keduanya ditempatkan pada Semester 2 dalam Kurikulum 2024. Untuk rangkuman ini, susunan tetap mengikuti folder Semester 3 pada repo Anda.

---

# 1. BASIS DATA

Sumber: [Rangkuman Materi Basis Data](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/Basis_Data/RANGKUMAN_MATERI.md)

Basis Data mempelajari cara menyimpan, mengorganisasikan, menghubungkan, mengambil, dan menjaga konsistensi data. Materi ini merupakan fondasi aplikasi web, aplikasi mobile, sistem transaksi, sistem informasi, dan analisis data.

Contoh sederhana: sebuah sistem akademik perlu menyimpan data mahasiswa, program studi, mata kuliah, dan nilai. Jika setiap data disimpan berulang-ulang dalam banyak file tanpa aturan, data mudah tidak konsisten. Sistem basis data dirancang untuk mengurangi masalah tersebut.

## 1.1. Mengapa basis data dibutuhkan?

Sistem berbasis file biasa memiliki sejumlah kelemahan.

**Redundansi data** terjadi ketika data yang sama disimpan berulang kali. Misalnya, alamat program studi disalin ke setiap catatan mahasiswa.

**Inkonsistensi data** terjadi ketika salinan data yang seharusnya sama memiliki nilai berbeda.

**Isolasi data** membuat informasi tersebar dalam banyak file atau format, sehingga sulit digabungkan.

**Masalah integritas** terjadi ketika data yang tersimpan melanggar aturan bisnis, misalnya nilai mahasiswa berada di luar rentang yang diperbolehkan.

**Masalah akses konkuren** terjadi ketika beberapa pengguna melakukan perubahan secara bersamaan dan hasil akhirnya tidak sesuai harapan.

DBMS (*Database Management System*) menyediakan mekanisme untuk mengatur penyimpanan, query, hak akses, integritas, konkurensi, dan pemulihan data.

## 1.2. Arsitektur tiga skema ANSI-SPARC

Arsitektur tiga skema membagi representasi basis data menjadi tiga tingkat.

**1. External level**

Merupakan sudut pandang pengguna atau aplikasi terhadap data. Pengguna yang berbeda dapat memiliki tampilan berbeda atas basis data yang sama.

Contoh: dosen melihat nilai mahasiswa di kelasnya, sedangkan bagian administrasi melihat data akademik yang lebih luas.

**2. Conceptual level**

Menjelaskan struktur logis seluruh basis data, termasuk entitas, atribut, relasi, dan batasan integritas.

Contoh: tabel `Mahasiswa`, `ProgramStudi`, dan `MataKuliah`, beserta keterkaitannya.

**3. Internal level**

Menjelaskan bagaimana data disimpan secara fisik, termasuk organisasi file, halaman data, dan struktur indeks.

Konsep penting yang mengikuti arsitektur ini adalah **data independence**.

- *Logical data independence*: perubahan skema konseptual dapat dilakukan tanpa harus mengubah seluruh tampilan eksternal.
- *Physical data independence*: perubahan cara penyimpanan fisik dapat dilakukan tanpa mengubah skema logis.

Contoh physical data independence adalah menambahkan indeks untuk mempercepat pencarian tanpa mengubah struktur tabel yang digunakan aplikasi.

## 1.3. Model relasional dan istilah penting

Model relasional merepresentasikan data menggunakan relasi yang secara praktis disajikan sebagai tabel.

Istilah dasarnya:

- **Relasi**: tabel.
- **Tuple**: baris data.
- **Atribut**: kolom.
- **Domain**: himpunan nilai yang diperbolehkan untuk atribut.
- **Degree**: jumlah atribut atau kolom.
- **Cardinality**: jumlah tuple atau baris dalam relasi.

Misalnya, tabel `Mahasiswa` memiliki kolom `nim`, `nama`, dan `ipk`. Jika tabel memiliki tiga kolom dan 100 baris, degree-nya adalah 3 dan cardinality-nya adalah 100.

### Jenis kunci (*keys*)

Kunci digunakan untuk mengidentifikasi data dan menjaga hubungan antartabel.

**Super key** adalah atribut atau kombinasi atribut yang dapat mengidentifikasi baris secara unik.

**Candidate key** adalah super key minimal, yaitu tidak memiliki subset yang masih dapat mengidentifikasi baris secara unik.

**Primary key (PK)** adalah candidate key yang dipilih sebagai identitas utama setiap baris.

**Alternate key** adalah candidate key yang tidak dipilih sebagai primary key.

**Foreign key (FK)** adalah atribut yang merujuk ke kunci pada tabel lain.

Contoh:

`Mahasiswa(nim, nama, id_prodi)`

`ProgramStudi(id_prodi, nama_prodi)`

Dalam contoh tersebut, `nim` dapat menjadi primary key pada tabel Mahasiswa. `id_prodi` menjadi foreign key yang merujuk ke ProgramStudi.

Dua aturan integritas penting:

- **Entity integrity**: primary key tidak boleh bernilai NULL.
- **Referential integrity**: foreign key harus merujuk ke baris yang valid atau bernilai NULL jika memang diperbolehkan oleh desain.

## 1.4. Entity-Relationship Diagram (ERD)

ERD digunakan untuk memodelkan struktur data sebelum implementasi ke tabel.

Komponen utama:

**Entitas** adalah objek yang datanya hendak disimpan. Contohnya Mahasiswa, Dosen, dan MataKuliah.

**Atribut** menjelaskan karakteristik entitas. Contoh atribut Mahasiswa adalah NIM, nama, dan tanggal lahir.

**Relasi** menunjukkan hubungan ant entitas. Contohnya Mahasiswa mengambil MataKuliah.

Jenis atribut yang perlu dikenali:

- *Simple attribute*: tidak dapat dipecah secara bermakna dalam model tersebut.
- *Composite attribute*: dapat dipecah menjadi bagian-bagian yang lebih kecil, misalnya alamat.
- *Single-valued attribute*: mempunyai satu nilai untuk satu entitas.
- *Multivalued attribute*: dapat mempunyai beberapa nilai, misalnya beberapa nomor telepon.
- *Derived attribute*: diturunkan dari atribut lain, misalnya umur dari tanggal lahir.

### Kardinalitas relasi

**One-to-one (1:1)** berarti satu entitas di sisi pertama berhubungan dengan paling banyak satu entitas di sisi kedua, sesuai batasan yang ditetapkan.

**One-to-many (1:N)** berarti satu entitas dapat berhubungan dengan banyak entitas di sisi lain.

**Many-to-many (M:N)** berarti banyak entitas pada kedua sisi dapat saling berhubungan.

### Mengubah ERD menjadi tabel

Aturan pemetaan yang sering diuji:

- Relasi 1:N biasanya direpresentasikan dengan menempatkan foreign key dari sisi 1 di tabel sisi N.
- Relasi M:N memerlukan tabel penghubung atau *junction table*.
- Atribut multivalued biasanya dibuat menjadi tabel terpisah.
- Entitas kuat menjadi tabel yang mempunyai kunci sendiri.
- Entitas lemah bergantung pada entitas pemilik dan biasanya menggunakan kunci pemilik bersama partial key untuk identifikasi.

Contoh relasi mahasiswa dan mata kuliah:

`Mahasiswa(nim, nama)`

`MataKuliah(kode_mk, nama_mk)`

`KRS(nim, kode_mk, semester, nilai)`

KRS menjadi tabel penghubung yang merepresentasikan relasi M:N. Kunci gabungan `(nim, kode_mk, semester)` dapat digunakan jika aturan bisnis mengizinkan satu mahasiswa mengambil mata kuliah yang sama kembali pada semester berbeda.

## 1.5. Aljabar relasional

Aljabar relasional merupakan dasar formal operasi query pada model relasional.

Operator penting:

**Seleksi \(\sigma\)** memilih baris berdasarkan kondisi.

\[
\sigma_{\text{ipk}>3.50}(\text{Mahasiswa})
\]

Artinya: mengambil mahasiswa dengan IPK di atas 3,50.

**Proyeksi \(\pi\)** memilih kolom tertentu.

\[
\pi_{\text{nim,nama}}(\text{Mahasiswa})
\]

Artinya: menghasilkan relasi yang berisi kolom NIM dan nama.

**Cartesian product \(\times\)** menggabungkan setiap baris relasi pertama dengan setiap baris relasi kedua.

Jika relasi pertama memiliki 3 baris dan relasi kedua memiliki 4 baris, hasil perkalian Kartesius memiliki 12 kombinasi sebelum penyaringan.

**Union \(\cup\)** menggabungkan tuple dari relasi yang kompatibel.

**Difference \(-\)** menghasilkan tuple yang ada pada relasi pertama tetapi tidak ada pada relasi kedua.

**Join \(\bowtie\)** menggabungkan baris dari dua relasi berdasarkan kondisi hubungan.

Natural join secara otomatis menggunakan atribut dengan nama yang sama dan menghilangkan duplikasi kolom penghubung pada hasilnya.

Penting untuk membedakan seleksi dan proyeksi: seleksi memilih baris, sedangkan proyeksi memilih kolom.

## 1.6. SQL: DDL, DML, dan query

SQL adalah bahasa yang digunakan untuk mendefinisikan serta memanipulasi basis data relasional.

### DDL — Data Definition Language

DDL digunakan untuk membuat atau mengubah struktur basis data.

Contoh:

```sql
CREATE TABLE Mahasiswa (
    nim VARCHAR(15) PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    ipk DECIMAL(3,2)
        CHECK (ipk >= 0.00 AND ipk <= 4.00)
);
```

Perintah DDL yang perlu dikenali adalah `CREATE`, `ALTER`, dan `DROP`.

### DML — Data Manipulation Language

DML digunakan untuk memanipulasi data, seperti `INSERT`, `UPDATE`, dan `DELETE`. Query `SELECT` digunakan untuk mengambil data.

```sql
SELECT nim, nama, ipk
FROM Mahasiswa
WHERE ipk >= 3.50
ORDER BY ipk DESC;
```

Query tersebut mengambil mahasiswa dengan IPK minimal 3,50 dan mengurutkan hasil dari IPK tertinggi.

### Agregasi dan pengelompokan

Fungsi agregat yang umum:

- `COUNT()` menghitung baris atau nilai yang sesuai.
- `SUM()` menjumlahkan nilai.
- `AVG()` menghitung rata-rata.
- `MIN()` mencari nilai minimum.
- `MAX()` mencari nilai maksimum.

Contoh:

```sql
SELECT id_prodi,
       AVG(ipk) AS rata_ipk,
       COUNT(*) AS total_mahasiswa
FROM Mahasiswa
GROUP BY id_prodi
HAVING COUNT(*) > 10;
```

Query mengelompokkan mahasiswa berdasarkan program studi, menghitung IPK rata-rata, lalu hanya mempertahankan kelompok dengan lebih dari sepuluh baris.

Perbedaan penting:

- `WHERE` menyaring baris sebelum pengelompokan.
- `HAVING` menyaring kelompok setelah agregasi.

### JOIN

Jenis JOIN yang perlu dipahami:

**INNER JOIN** menampilkan pasangan baris yang memenuhi kondisi hubungan.

**LEFT JOIN** menampilkan semua baris tabel kiri, termasuk baris yang tidak memiliki pasangan di tabel kanan.

**RIGHT JOIN** menampilkan semua baris tabel kanan.

**FULL OUTER JOIN** menampilkan semua baris kedua tabel, dengan nilai NULL pada sisi yang tidak memiliki pasangan. Dukungan sintaks ini dapat berbeda antar-DBMS.

Contoh:

```sql
SELECT m.nim, m.nama, p.nama_prodi
FROM Mahasiswa AS m
JOIN ProgramStudi AS p
  ON m.id_prodi = p.id_prodi;
```

### Subquery

Subquery adalah query yang digunakan di dalam query lain. Subquery dapat digunakan bersama `IN`, `EXISTS`, atau operator perbandingan, bergantung bentuk query dan hasil yang diperlukan.

```sql
SELECT nama
FROM Mahasiswa
WHERE ipk > (
    SELECT AVG(ipk)
    FROM Mahasiswa
);
```

Query tersebut mengambil mahasiswa yang IPK-nya lebih tinggi daripada rata-rata IPK seluruh mahasiswa.

## 1.7. Ketergantungan fungsional dan normalisasi

Normalisasi adalah proses mengorganisasikan tabel untuk mengurangi redundansi dan anomali data.

Tiga anomali utama:

- **Insertion anomaly**: data tidak dapat ditambahkan secara wajar tanpa menambahkan informasi lain yang tidak seharusnya diwajibkan.
- **Update anomaly**: satu fakta harus diubah di banyak baris sehingga sebagian pembaruan berpotensi tertinggal.
- **Deletion anomaly**: penghapusan satu baris tanpa sengaja menghilangkan informasi lain yang masih dibutuhkan.

Ketergantungan fungsional \(X\rightarrow Y\) berarti nilai \(X\) menentukan nilai \(Y\) dalam relasi sesuai aturan datanya.

### First Normal Form (1NF)

Setiap atribut harus memiliki nilai atomik menurut domain yang ditentukan, dan kelompok nilai berulang tidak direpresentasikan sebagai satu kolom multivalue.

Contoh buruk: kolom nomor telepon berisi `"0812, 0856, 0877"` sebagai satu nilai.

Solusi yang lebih terstruktur adalah memisahkan nomor telepon ke dalam baris atau tabel yang sesuai dengan kebutuhan model data.

### Second Normal Form (2NF)

Tabel telah memenuhi 1NF dan setiap atribut non-prime bergantung penuh pada setiap candidate key, bukan hanya sebagian dari kunci gabungan.

Masalah 2NF relevan ketika primary key atau candidate key terdiri atas beberapa atribut.

### Third Normal Form (3NF)

Secara informal, tabel telah memenuhi 2NF dan tidak memiliki ketergantungan transitif atribut non-prime terhadap kunci kandidat.

Definisi formal 3NF berkaitan dengan determinan suatu ketergantungan fungsional dan sifat atribut prime. Untuk latihan dasar, fokuskan pada identifikasi ketergantungan parsial serta transitif.

### Boyce–Codd Normal Form (BCNF)

Untuk setiap ketergantungan fungsional nontrivial \(X\rightarrow Y\), \(X\) harus merupakan super key.

BCNF lebih ketat daripada 3NF pada keadaan tertentu.

Normalisasi tidak sekadar memecah tabel sebanyak mungkin. Desain harus tetap menjaga ketergantungan dan memungkinkan data direkonstruksi secara benar.

## 1.8. Transaksi dan ACID

Transaksi adalah satu rangkaian operasi basis data yang diperlakukan sebagai satu unit pekerjaan.

Empat properti ACID:

**Atomicity**: semua operasi dalam transaksi berhasil sebagai satu kesatuan atau dibatalkan.

**Consistency**: transaksi menjaga aturan integritas basis data.

**Isolation**: transaksi yang berjalan bersamaan harus mengikuti tingkat isolasi yang ditentukan DBMS sehingga hasilnya memenuhi jaminan yang diharapkan.

**Durability**: perubahan yang telah di-commit bertahan meskipun terjadi kegagalan yang dicakup oleh jaminan sistem.

Contoh transfer uang: saldo rekening pengirim berkurang dan saldo penerima bertambah. Jika proses gagal di tengah jalan, sistem harus menghindari kondisi ketika uang berkurang dari satu rekening tetapi tidak sampai ke rekening lain.

### Konkurensi dan locking

Saat beberapa transaksi berjalan bersama, DBMS harus mencegah hasil yang tidak konsisten.

Konsep yang perlu dipahami:
- Shared lock dan exclusive lock.
- Lost update.
- Dirty read.
- Non-repeatable read.
- Phantom read.
- Serializability.
- Two-Phase Locking (2PL).

Pada protokol 2PL, transaksi memiliki fase pertumbuhan ketika lock dapat ditambahkan dan fase penyusutan ketika lock dilepas dan tidak ada lock baru yang ditambahkan. Protokol ini digunakan untuk mendukung serializability, tetapi dapat menimbulkan deadlock.

### Target penguasaan Basis Data

Anda harus mampu:
1. Mendesain ERD dan mengubahnya menjadi tabel.
2. Menentukan PK, FK, candidate key, dan kardinalitas.
3. Menulis SQL dari kebutuhan dalam bahasa sehari-hari.
4. Menjelaskan serta menerapkan normalisasi.
5. Menjelaskan ACID, masalah konkurensi, dan 2PL.

---

# 2. INTERAKSI MANUSIA DAN KOMPUTER (IMK)

Sumber: [Rangkuman Materi IMK](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/Interaksi_Manusia_Komputer/RANGKUMAN_MATERI.md)

Interaksi Manusia dan Komputer atau Human-Computer Interaction (HCI) mempelajari hubungan antara manusia, komputer, dan desain sistem interaktif. Tujuannya adalah membuat sistem yang efektif, efisien, mudah dipelajari, aman, dan memuaskan untuk digunakan.

Contoh: sebuah aplikasi pemesanan makanan bisa mempunyai seluruh fitur yang diperlukan, tetapi tetap buruk apabila pengguna tidak memahami cara memilih menu, membayar, atau membatalkan pesanan.

## 2.1. Manusia sebagai pemroses informasi

Desain antarmuka perlu mempertimbangkan keterbatasan persepsi, perhatian, dan memori manusia.

### Memori sensoris

Memori sensoris menyimpan informasi yang ditangkap indera dalam waktu sangat singkat.

- *Iconic memory* berkaitan dengan informasi visual.
- *Echoic memory* berkaitan dengan informasi auditori.

### Memori jangka pendek dan memori kerja

Memori kerja digunakan untuk mempertahankan dan mengolah informasi yang sedang diperlukan.

Materi dasar sering menggunakan pendekatan Miller \(7\pm2\) untuk menjelaskan keterbatasan jumlah *chunk* informasi yang dapat diingat dalam tugas tertentu. Angka tersebut sebaiknya dipahami sebagai prinsip historis yang disederhanakan, bukan ukuran universal kapasitas memori untuk semua jenis tugas.

Implikasi desainnya:
- Kurangi beban mengingat informasi dari halaman sebelumnya.
- Tampilkan pilihan dan status yang relevan.
- Gunakan label yang mudah dikenali.
- Pecah proses rumit menjadi beberapa tahap.

### Memori jangka panjang

Memori jangka panjang menyimpan pengetahuan dan pengalaman lebih lama. Dalam konteks desain, pengguna dapat mengandalkan pengalaman sebelumnya ketika menghadapi antarmuka yang menggunakan pola yang familiar.

Karena itu, konsistensi ikon, label, dan navigasi membantu pengguna memahami sistem tanpa harus mempelajari ulang seluruh interaksi.

## 2.2. Ragam antarmuka

### Command Line Interface (CLI)

Pengguna memasukkan instruksi berupa teks.

Kelebihan:
- Efisien bagi pengguna ahli.
- Mendukung otomasi dan skrip.
- Tidak banyak memerlukan ruang visual.

Kekurangan:
- Sintaks perlu diingat.
- Tidak selalu ramah pengguna pemula.
- Kesalahan perintah dapat membingungkan jika pesan kesalahan buruk.

### Menu-driven interface

Pengguna memilih perintah yang tersedia dalam menu.

Kelebihannya adalah pengguna lebih banyak mengenali pilihan daripada harus menghafalnya. Namun, menu yang terlalu bertingkat dapat membuat navigasi lambat.

### Form fill-in

Pengguna memasukkan data melalui formulir.

Form perlu menyediakan label jelas, validasi, format input yang sesuai, dan pesan kesalahan yang membantu.

### Direct manipulation

Pengguna berinteraksi langsung dengan representasi visual, misalnya menyeret file ke folder atau memindahkan objek pada kanvas.

Ciri pentingnya meliputi umpan balik segera, tindakan yang terlihat, dan kemampuan membatalkan aksi bila memungkinkan.

## 2.3. Hukum ergonomi dan kognisi

### Fitts's Law

Hukum Fitts memodelkan waktu yang diperlukan untuk mengarahkan gerakan ke target.

\[
MT=a+b\log_2\left(1+\frac{D}{W}\right)
\]

Keterangan:
- \(MT\): waktu gerakan.
- \(D\): jarak menuju target.
- \(W\): lebar target dalam arah gerakan.
- \(a,b\): parameter empiris.

Semakin jauh dan kecil target, umumnya semakin lama target dicapai.

Implikasi: tombol yang sering digunakan perlu memiliki ukuran dan posisi yang sesuai, terutama pada layar sentuh.

### Hick–Hyman Law

Model umum hukum Hick:

\[
T=a+b\log_2(n+1)
\]

dengan \(n\) sebagai jumlah pilihan.

Jumlah pilihan yang lebih besar umumnya meningkatkan waktu pengambilan keputusan. Prinsip ini mendukung pengelompokan opsi dan penyajian informasi secara bertahap.

### Prinsip Gestalt

Prinsip Gestalt menjelaskan cara manusia mengorganisasikan informasi visual.

- **Proximity**: objek berdekatan cenderung dipersepsikan sebagai kelompok.
- **Similarity**: objek yang mirip cenderung dianggap memiliki fungsi atau kategori serupa.
- **Closure**: manusia cenderung melengkapi pola yang belum utuh.
- **Continuity**: mata cenderung mengikuti alur visual yang berkesinambungan.
- **Figure-ground**: pengguna membedakan objek utama dari latar belakang.

Dalam desain UI, pengelompokan yang tepat dan kontras yang memadai membantu pengguna memahami struktur antarmuka.

## 2.4. Affordance, feedback, dan model mental

**Affordance** adalah kemungkinan tindakan yang ditawarkan oleh suatu objek atau antarmuka.

Contoh: tombol yang terlihat dan berperilaku seperti tombol menunjukkan bahwa objek tersebut dapat ditekan.

**Feedback** adalah respons sistem setelah suatu tindakan. Contohnya notifikasi bahwa pembayaran berhasil atau indikator proses ketika berkas sedang diunggah.

**Model mental** adalah pemahaman pengguna tentang cara kerja sebuah sistem. Ketika model mental pengguna berbeda jauh dari perilaku sistem, pengguna mudah salah melakukan tindakan.

Antarmuka yang baik membuat tindakan penting mudah ditemukan dan hasil tindakan mudah dipahami.

## 2.5. User-Centered Design (UCD)

User-Centered Design menempatkan kebutuhan, konteks, keterbatasan, dan umpan balik pengguna sebagai dasar proses desain.

Siklus yang umum digunakan:

1. **Empathize**: memahami pengguna melalui observasi, wawancara, dan data.
2. **Define**: merumuskan masalah pengguna.
3. **Ideate**: menghasilkan alternatif solusi.
4. **Prototype**: membuat representasi solusi.
5. **Test**: menguji solusi kepada pengguna dan memperbaikinya.

Tahap ini bersifat iteratif. Hasil pengujian dapat membuat desainer kembali mengubah perumusan masalah, alur, atau prototipe.

Dua jenis prototipe yang perlu dikenali:

- **Low fidelity**: sketsa atau wireframe sederhana, berfokus pada struktur dan alur.
- **High fidelity**: visual dan interaksi lebih mendekati produk akhir.

Persona dan user journey map membantu menggambarkan kebutuhan, motivasi, masalah, serta pengalaman pengguna dalam menyelesaikan tugas.

## 2.6. Sepuluh heuristik usability Nielsen

Heuristik Nielsen adalah prinsip praktis untuk menemukan masalah usabilitas. Kesepuluh prinsip yang perlu dipahami:

1. **Visibility of system status** — sistem memberikan informasi tentang kondisi yang sedang terjadi.
2. **Match between system and the real world** — sistem menggunakan bahasa dan konsep yang mudah dipahami pengguna.
3. **User control and freedom** — pengguna dapat membatalkan atau keluar dari tindakan yang salah.
4. **Consistency and standards** — istilah dan pola interaksi konsisten.
5. **Error prevention** — desain mengurangi kemungkinan kesalahan.
6. **Recognition rather than recall** — pengguna lebih banyak mengenali pilihan daripada mengingat informasi.
7. **Flexibility and efficiency of use** — sistem dapat mendukung pemula sekaligus pengguna ahli.
8. **Aesthetic and minimalist design** — informasi disajikan tanpa elemen yang tidak perlu.
9. **Help users recognize, diagnose, and recover from errors** — pesan kesalahan menjelaskan masalah dan pemulihannya.
10. **Help and documentation** — bantuan tersedia dan mudah dicari ketika diperlukan.

Contoh penerapan: jika pengguna mengirim formulir dengan format email salah, sistem tidak cukup hanya menampilkan “Error”. Sistem lebih baik menunjukkan kolom yang bermasalah dan format yang benar.

## 2.7. Delapan aturan emas Shneiderman

Delapan aturan yang sering dipelajari dalam desain interaksi adalah:

1. Berusaha menjaga konsistensi.
2. Mendukung penggunaan pintasan bagi pengguna berpengalaman.
3. Memberikan umpan balik yang informatif.
4. Merancang dialog yang menghasilkan penutupan yang jelas.
5. Mencegah dan menangani kesalahan secara sederhana.
6. Memungkinkan pembalikan tindakan dengan mudah.
7. Mendukung kendali pengguna terhadap sistem.
8. Mengurangi beban memori jangka pendek.

Heuristik Nielsen dan aturan emas Shneiderman sama-sama membantu desain UI, tetapi merupakan dua kerangka yang berbeda. Saat menjawab ujian, jelaskan prinsip yang paling relevan dengan kasus yang diberikan.

## 2.8. Usability testing dan SUS

Usability testing menguji apakah pengguna dapat menyelesaikan tugas dengan sistem secara efektif dan efisien.

Metrik yang dapat diamati:
- Tingkat keberhasilan menyelesaikan tugas.
- Waktu penyelesaian tugas.
- Jumlah kesalahan.
- Jumlah bantuan yang diperlukan.
- Kepuasan pengguna.

Metode evaluasi lain meliputi heuristic evaluation, observasi, wawancara, dan kuesioner.

### System Usability Scale (SUS)

SUS terdiri atas 10 pertanyaan standar dengan skala jawaban 1–5.

Perhitungan skor:
- Untuk item bernomor ganjil, kurangi jawaban dengan 1.
- Untuk item bernomor genap, hitung 5 dikurangi jawaban.
- Jumlahkan nilai kontribusi semua item, lalu kalikan 2,5.

\[
SUS=2.5\times\sum_{i=1}^{10}c_i
\]

dengan \(c_i\) sebagai kontribusi skor item yang sudah disesuaikan.

Skor SUS berada pada rentang 0–100. Skor tersebut bukan persentase pengguna yang berhasil menyelesaikan tugas. Interpretasinya perlu mempertimbangkan konteks, norma pembanding, dan metode evaluasi.

### Target penguasaan IMK

Anda harus mampu:
- Menjelaskan keterbatasan kognitif manusia dan implikasinya bagi desain.
- Memilih gaya interaksi yang sesuai untuk pengguna.
- Menerapkan hukum Fitts dan Hick secara konseptual.
- Membedakan UCD, prototyping, dan usability testing.
- Mengidentifikasi pelanggaran heuristik Nielsen atau aturan Shneiderman pada contoh antarmuka.
- Menjelaskan pengumpulan dan interpretasi skor SUS.

---

# 3. METODE NUMERIK

Sumber: [Rangkuman Materi Metode Numerik](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/Metode_Numerik/RANGKUMAN_MATERI.md)

Metode Numerik mempelajari cara memperoleh solusi pendekatan untuk persoalan matematika yang sulit atau tidak praktis diselesaikan secara analitik.

Komputer memakai representasi bilangan dengan presisi terbatas. Karena itu, hasil perhitungan numerik perlu dievaluasi berdasarkan galat, kestabilan, konvergensi, dan toleransi.

## 3.1. Analisis galat

Galat adalah selisih antara nilai acuan dan nilai pendekatan.

Galat sejati:

\[
E_t=x_{\text{sejati}}-x_{\text{aproksimasi}}
\]

Galat relatif sejati dalam persen:

\[
\varepsilon_t=
\left|
\frac{x_{\text{sejati}}-x_{\text{aproksimasi}}}
{x_{\text{sejati}}}
\right|\times100\%
\]

Galat relatif aproksimasi digunakan ketika nilai sejati tidak diketahui, tetapi dua hasil iterasi berturut-turut tersedia:

\[
\varepsilon_a=
\left|
\frac{x_{n+1}-x_n}{x_{n+1}}
\right|\times100\%
\]

Galat aproksimasi ini hanya dapat digunakan ketika penyebut terdefinisi. Kriteria penghentian biasanya membandingkannya dengan toleransi yang ditentukan.

Dua sumber galat utama:
- **Truncation error**: timbul karena pendekatan terhadap proses atau deret yang secara teori tidak berhingga.
- **Round-off error**: timbul karena presisi terbatas representasi bilangan pada komputer.

Metode yang menghasilkan banyak digit bukan berarti semua digit tersebut akurat. Akurasi perlu dievaluasi dengan konteks persoalan dan kondisi numeriknya.

## 3.2. Pencarian akar persamaan nonlinier

Tujuannya adalah menemukan nilai \(x\) yang memenuhi:

\[
f(x)=0
\]

Persamaan nonlinier dapat muncul dalam analisis rangkaian, simulasi, optimasi, dan pemodelan matematis.

### Bisection method

Bisection membagi interval yang mengurung akar menjadi dua bagian.

Syarat standar: fungsi kontinu dan nilai pada kedua ujung interval mempunyai tanda berlawanan, yaitu:

\[
f(a)f(b)<0
\]

Titik tengah:

\[
x_r=\frac{a+b}{2}
\]

Kemudian periksa tanda fungsi di titik tengah. Pilih setengah interval yang masih mengurung perubahan tanda.

Contoh awal: \(f(x)=x^2-2\) pada interval \([1,2]\).

- \(f(1)=-1\)
- \(f(2)=2\)
- Titik tengah \(x_r=1.5\), dengan \(f(1.5)=0.25\).

Karena tanda \(f(1)\) dan \(f(1.5)\) berlawanan, interval baru adalah \([1,1.5]\).

Bisection memiliki konvergensi yang terjamin untuk kondisi tersebut, tetapi biasanya lebih lambat daripada beberapa metode terbuka.

### Regula falsi

Regula falsi juga mempertahankan interval yang mengurung akar, tetapi menggunakan garis lurus yang menghubungkan nilai fungsi di kedua ujung.

\[
x_r=a-\frac{f(a)(b-a)}{f(b)-f(a)}
\]

Metode ini menggunakan informasi nilai fungsi untuk memperkirakan lokasi akar, bukan selalu mengambil titik tengah.

### Newton–Raphson

Metode Newton–Raphson menggunakan turunan fungsi untuk memperbarui tebakan.

\[
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
\]

Kelebihannya adalah dapat konvergen cepat jika tebakan awal baik dan syarat metode terpenuhi.

Kelemahannya:
- Memerlukan turunan.
- Jika \(f'(x_n)=0\), rumus tidak dapat digunakan pada langkah tersebut.
- Tebakan awal buruk dapat menyebabkan divergensi atau konvergensi ke akar yang tidak diinginkan.

### Metode secant

Metode secant mendekati turunan menggunakan dua tebakan terakhir.

\[
x_{n+1}=x_n-
f(x_n)\frac{x_n-x_{n-1}}{f(x_n)-f(x_{n-1})}
\]

Metode ini tidak memerlukan turunan analitik, tetapi tidak memiliki jaminan konvergensi yang sama dengan bisection pada semua kondisi.

Perbedaan utamanya:

| Metode | Informasi yang digunakan | Karakteristik |
|---|---|---|
| Bisection | Interval dengan perubahan tanda | Andal, konvergensi relatif lambat |
| Regula falsi | Interval dan nilai fungsi di ujung | Menjaga pengurungan akar |
| Newton–Raphson | Satu tebakan dan turunan | Biasanya cepat, sensitif terhadap tebakan awal |
| Secant | Dua tebakan terakhir | Mengaproksimasi turunan tanpa menghitungnya secara langsung |

## 3.3. Penyelesaian sistem persamaan linier secara numerik

Sistem dapat ditulis sebagai:

\[
A\mathbf{x}=\mathbf{b}
\]

Metode eliminasi Gauss melakukan penghilangan variabel secara bertahap hingga diperoleh sistem yang dapat diselesaikan dengan substitusi balik.

**Partial pivoting** menukar baris untuk menempatkan elemen dengan nilai absolut besar pada posisi pivot. Tujuannya mengurangi risiko pembagian dengan nilai mendekati nol dan meningkatkan kestabilan numerik.

### Metode Jacobi

Jacobi menghitung nilai variabel baru menggunakan nilai variabel dari iterasi sebelumnya.

### Metode Gauss–Seidel

Gauss–Seidel menggunakan nilai terbaru yang telah dihitung di iterasi saat ini untuk menghitung variabel selanjutnya.

Untuk sistem dengan \(a_{ii}\neq0\), pembaruan Gauss–Seidel adalah:

\[
x_i^{(k+1)}
=\frac{1}{a_{ii}}
\left(
b_i
-\sum_{j<i}a_{ij}x_j^{(k+1)}
-\sum_{j>i}a_{ij}x_j^{(k)}
\right)
\]

Perbedaan utama: Jacobi menggunakan seluruh nilai iterasi lama, sedangkan Gauss–Seidel langsung memanfaatkan nilai terbaru yang tersedia.

Dominasi diagonal yang ketat merupakan salah satu kondisi cukup yang sering digunakan untuk menjamin konvergensi kedua metode tersebut.

## 3.4. Interpolasi polinomial

Interpolasi digunakan untuk memperkirakan nilai fungsi di antara titik-titik data yang diketahui.

Jika tersedia \(n+1\) titik dengan nilai \(x\) berbeda, terdapat polinomial berderajat paling tinggi \(n\) yang melalui seluruh titik tersebut.

### Lagrange interpolation

\[
P_n(x)=\sum_{i=0}^{n}y_iL_i(x)
\]

dengan:

\[
L_i(x)=
\prod_{\substack{j=0\\j\neq i}}^n
\frac{x-x_j}{x_i-x_j}
\]

Polinomial Lagrange dibangun dari fungsi basis yang bernilai 1 pada satu titik dan 0 pada titik lainnya.

### Newton divided differences

Interpolasi Newton menggunakan beda terbagi untuk menyusun polinomial secara bertahap.

Keuntungannya, jika titik data baru ditambahkan, polinomial dapat diperluas tanpa harus membangun seluruhnya dari awal.

Interpolasi berbeda dari ekstrapolasi. Interpolasi memperkirakan nilai di dalam rentang data yang tersedia, sedangkan ekstrapolasi memperkirakan di luar rentang tersebut dan umumnya lebih berisiko.

## 3.5. Integrasi numerik

Integrasi numerik memperkirakan:

\[
\int_a^b f(x)\,dx
\]

dengan menggunakan sejumlah nilai fungsi. Interval dibagi menjadi \(n\) pias:

\[
h=\frac{b-a}{n}
\]

### Kaidah trapesium komposit

\[
\int_a^b f(x)\,dx
\approx
\frac{h}{2}
\left[
f(x_0)+
2\sum_{i=1}^{n-1}f(x_i)+
f(x_n)
\right]
\]

Metode ini memperkirakan kurva menggunakan potongan garis lurus. Galat pemotongan komposit umumnya berorde \(O(h^2)\) untuk fungsi yang cukup mulus.

### Kaidah Simpson 1/3 komposit

\[
\int_a^b f(x)\,dx
\approx
\frac{h}{3}
\left[
f(x_0)+f(x_n)
+4\sum_{\text{i ganjil}}f(x_i)
+2\sum_{\substack{\text{i genap}\\0<i<n}}f(x_i)
\right]
\]

Syarat pentingnya adalah jumlah pias \(n\) harus genap. Simpson 1/3 menggunakan pendekatan parabola dan untuk fungsi yang cukup mulus memiliki galat komposit berorde \(O(h^4)\).

Jika jumlah pias tidak memenuhi syarat Simpson 1/3, pembagian interval harus disusun ulang atau dikombinasikan dengan aturan lain yang sesuai, bukan mengabaikan syaratnya.

## 3.6. Diferensiasi numerik

Beda hingga memperkirakan turunan berdasarkan nilai fungsi di titik-titik berdekatan.

**Beda maju:**

\[
f'(x)\approx\frac{f(x+h)-f(x)}{h}
\]

**Beda mundur:**

\[
f'(x)\approx\frac{f(x)-f(x-h)}{h}
\]

**Beda pusat:**

\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]

Beda maju dan mundur memiliki galat truncation orde \(O(h)\), sedangkan beda pusat memiliki galat orde \(O(h^2)\) untuk kondisi kemulusan yang sesuai.

Beda pusat sering lebih akurat pada ukuran langkah yang sama, tetapi pilihan metode juga bergantung pada ketersediaan data dan batas domain.

## 3.7. Persamaan diferensial biasa (PDB)

PDB dapat ditulis sebagai:

\[
\frac{dy}{dx}=f(x,y)
\]

Untuk masalah nilai awal, diketahui nilai awal \(y_0\) pada \(x_0\), kemudian dicari pendekatan nilai pada titik-titik berikutnya.

### Metode Euler

\[
y_{n+1}=y_n+h f(x_n,y_n)
\]

Euler memperbarui nilai \(y\) berdasarkan kemiringan pada titik awal interval. Metode ini sederhana, tetapi biasanya kurang akurat jika dibandingkan dengan metode berorde lebih tinggi pada ukuran langkah yang sama.

### Runge–Kutta orde 4 (RK4)

RK4 menggunakan empat estimasi kemiringan.

\[
\begin{aligned}
k_1&=f(x_n,y_n)\\
k_2&=f\left(x_n+\frac h2,y_n+\frac h2k_1\right)\\
k_3&=f\left(x_n+\frac h2,y_n+\frac h2k_2\right)\\
k_4&=f(x_n+h,y_n+hk_3)
\end{aligned}
\]

Pembaruan solusi:

\[
y_{n+1}=y_n+\frac h6(k_1+2k_2+2k_3+k_4)
\]

RK4 biasanya memberikan akurasi yang lebih tinggi daripada Euler pada ukuran langkah yang sama, dengan biaya perhitungan tambahan.

### Target penguasaan Metode Numerik

Anda harus mampu:
1. Menghitung galat dan menentukan kriteria berhenti.
2. Melakukan iterasi pencarian akar.
3. Menyelesaikan satu atau lebih iterasi Jacobi atau Gauss–Seidel.
4. Menghitung interpolasi dari titik data.
5. Menerapkan trapesium dan Simpson.
6. Menggunakan beda hingga untuk memperkirakan turunan.
7. Menyelesaikan langkah Euler atau RK4 pada soal PDB.

---

# 4. SISTEM OPERASI

Sumber: [Rangkuman Materi Sistem Operasi](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/Sistem_Operasi/RANGKUMAN_MATERI.md)

Sistem operasi (Operating System atau OS) mengatur penggunaan CPU, memori, penyimpanan, dan perangkat I/O. OS menyediakan layanan bagi aplikasi dan menjaga agar proses-proses dapat berbagi sumber daya secara terkontrol.

Contoh sistem operasi ialah Linux, Windows, macOS, Android, dan iOS.

## 4.1. User mode dan kernel mode

Sistem operasi menggunakan pemisahan hak akses untuk mengurangi risiko aplikasi merusak sistem.

**User mode** digunakan untuk menjalankan aplikasi dengan hak akses terbatas.

**Kernel mode** memberikan hak yang diperlukan untuk menjalankan operasi sistem yang memiliki privilese.

Aplikasi biasanya meminta layanan OS melalui **system call**, misalnya operasi membuka file atau membuat proses. Mekanisme trap atau transisi sistem yang sesuai digunakan untuk meminta layanan kernel.

Pemisahan ini merupakan bagian penting dari proteksi dan isolasi proses.

## 4.2. Proses dan thread

Proses adalah program yang sedang dieksekusi beserta keadaan dan sumber daya yang terkait dengannya.

Process Control Block (PCB) menyimpan informasi penting seperti:
- PID.
- Program counter.
- Register CPU.
- Status proses.
- Informasi penjadwalan.
- Informasi memori.
- Status operasi I/O.

Status proses dasar:

**New → Ready → Running → Waiting/Blocked → Ready → Running → Terminated**

Tidak setiap proses mengikuti satu urutan tanpa variasi, tetapi status tersebut menggambarkan jalur umum selama eksekusi.

### Context switching

Context switching merupakan perpindahan CPU dari satu konteks proses atau thread ke konteks lainnya.

OS menyimpan keadaan eksekusi proses yang sebelumnya berjalan, kemudian memuat keadaan proses selanjutnya.

Operasi ini menimbulkan overhead karena CPU melakukan pekerjaan administratif sebelum melanjutkan komputasi aplikasi.

### Proses versus thread

Proses memiliki ruang alamat sendiri sebagai dasar isolasi. Thread yang berada dalam proses yang sama umumnya berbagi kode, data, dan sumber daya proses, tetapi mempunyai register, stack, dan konteks eksekusi sendiri.

Thread dapat lebih ringan dibandingkan proses terpisah, tetapi akses ke data bersama menimbulkan kebutuhan sinkronisasi.

## 4.3. Penjadwalan CPU

Penjadwalan CPU menentukan proses yang mendapat giliran menggunakan prosesor.

Metrik penting:

**Turnaround time**

\[
TAT=\text{Completion Time}-\text{Arrival Time}
\]

**Waiting time**

Total waktu yang dihabiskan dalam ready queue, tidak termasuk waktu eksekusi CPU dan waktu menunggu operasi yang terblokir.

**Response time**

Waktu dari kedatangan proses hingga pertama kali memperoleh CPU.

### First-Come, First-Served (FCFS)

Proses dijalankan berdasarkan urutan kedatangan. FCFS sederhana, tetapi dapat menyebabkan *convoy effect*: proses pendek harus menunggu di belakang proses panjang.

### Shortest Job First (SJF)

Memilih proses dengan perkiraan CPU burst terpendek. SJF non-preemptive dapat menghasilkan rata-rata waiting time minimum secara teoritis jika informasi burst tersedia.

Keterbatasannya adalah durasi eksekusi berikutnya tidak selalu diketahui sebelumnya.

### Shortest Remaining Time First (SRTF)

Versi preemptive dari SJF. Jika proses baru datang dengan sisa burst lebih pendek, proses yang sedang berjalan dapat dipreempt.

### Round Robin (RR)

Setiap proses mendapat jatah waktu bernama time quantum.

Jika proses belum selesai ketika quantum habis, proses kembali ke ready queue.

- Quantum terlalu besar membuat perilaku mendekati FCFS.
- Quantum terlalu kecil meningkatkan overhead context switching.

### Priority scheduling

CPU diberikan kepada proses berdasarkan prioritas. Jika proses berprioritas rendah terus tertunda, dapat terjadi starvation.

Aging mengurangi risiko ini dengan menaikkan prioritas proses yang menunggu terlalu lama.

Untuk soal penjadwalan, selalu gambar Gantt chart terlebih dahulu, lalu hitung completion time, turnaround time, waiting time, dan response time sesuai definisinya.

## 4.4. Sinkronisasi proses

Ketika beberapa proses atau thread mengakses data bersama, urutan eksekusi dapat memengaruhi hasil. Situasi ini disebut **race condition**.

Bagian kode yang mengakses sumber daya bersama dan membutuhkan perlindungan disebut critical section.

Solusi critical section idealnya memenuhi:

1. **Mutual exclusion**: maksimal satu proses yang memenuhi syarat dapat berada dalam critical section untuk sumber daya yang dilindungi.
2. **Progress**: proses yang ingin masuk tidak tertunda tanpa alasan ketika critical section kosong dan keputusan dapat dibuat.
3. **Bounded waiting**: waktu atau jumlah giliran tunggu memiliki batas yang sesuai untuk menghindari starvation.

### Mutex

Mutex merupakan mekanisme penguncian untuk memberi akses eksklusif terhadap sumber daya yang dilindungi.

### Semaphore

Semaphore merupakan mekanisme sinkronisasi dengan operasi atomik `wait` dan `signal`, yang sering dinyatakan pula sebagai \(P\) dan \(V\).

Sebuah semaphore counting dapat membatasi berapa banyak proses yang boleh menggunakan sekumpulan sumber daya secara bersamaan.

Kesalahan penggunaan lock dan semaphore dapat menyebabkan deadlock, starvation, atau race condition.

## 4.5. Deadlock

Deadlock terjadi ketika sekumpulan proses terblokir karena saling menunggu sumber daya yang dipegang oleh proses lain di dalam kelompok tersebut.

Empat kondisi Coffman adalah:

1. **Mutual exclusion:** sumber daya tidak dapat dipakai bersama secara bebas.
2. **Hold and wait:** proses memegang sumber daya sambil menunggu sumber daya lain.
3. **No preemption:** sumber daya tidak bisa dirampas secara paksa menurut model yang sedang digunakan.
4. **Circular wait:** terdapat siklus saling menunggu.

Keempat kondisi tersebut harus hadir bersamaan agar deadlock dapat terjadi pada model klasik.

Pendekatan penanganan deadlock:
- **Prevention**: merancang sistem agar setidaknya satu kondisi Coffman tidak terpenuhi.
- **Avoidance**: hanya mengalokasikan sumber daya jika keadaan sistem tetap aman.
- **Detection and recovery**: mendeteksi deadlock dan melakukan pemulihan, misalnya dengan menghentikan proses tertentu.

Banker's Algorithm merupakan contoh algoritma penghindaran deadlock yang memeriksa keadaan aman berdasarkan kebutuhan dan alokasi sumber daya.

## 4.6. Manajemen memori dan paging

OS mengelola pembagian RAM bagi proses dan memetakan alamat yang digunakan program ke lokasi fisik.

**MMU (Memory Management Unit)** membantu menerjemahkan alamat logis atau virtual menjadi alamat fisik.

Dalam paging:
- Memori logis dibagi menjadi page.
- Memori fisik dibagi menjadi frame.
- Page table menghubungkan nomor page ke nomor frame.

Alamat logis dapat dipandang sebagai:

\[
[\text{Page Number}\mid\text{Page Offset}]
\]

Offset menunjukkan posisi di dalam page. Jika ukuran page adalah \(2^d\) byte, maka offset memerlukan \(d\) bit.

Paging menghilangkan fragmentasi eksternal akibat kebutuhan blok kontigu untuk proses, tetapi tetap dapat menghasilkan fragmentasi internal, misalnya pada page terakhir yang tidak terisi penuh.

## 4.7. Memori virtual dan page replacement

Memori virtual memungkinkan proses menggunakan ruang alamat yang lebih besar daripada bagian RAM yang sedang dialokasikan kepadanya. Sebagian halaman dapat disimpan di media sekunder dan dimuat saat diperlukan.

**Demand paging** memuat halaman ke RAM ketika halaman itu benar-benar diperlukan.

Jika halaman yang dibutuhkan belum berada di RAM, terjadi **page fault**. OS memeriksa akses, mengambil halaman dari penyimpanan jika valid, memperbarui page table, kemudian melanjutkan proses.

Jika tidak tersedia frame kosong, OS mungkin harus mengganti halaman yang berada di RAM.

### Algoritma page replacement

**FIFO** mengganti halaman yang paling lama berada di memori. FIFO dapat mengalami Belady's anomaly, yaitu jumlah page fault meningkat ketika jumlah frame ditambah pada rangkaian referensi tertentu.

**LRU** mengganti halaman yang paling lama tidak digunakan. LRU memanfaatkan prinsip lokalitas temporal.

**Optimal** mengganti halaman yang penggunaannya berikutnya paling jauh di masa depan. Algoritma ini menjadi pembanding teoretis karena umumnya tidak dapat diterapkan secara langsung untuk mengetahui seluruh referensi masa depan.

Latihan penting adalah membuat tabel referensi halaman, isi setiap frame, dan menghitung jumlah page fault.

## 4.8. Sistem berkas dan penyimpanan

Sistem berkas mengatur penamaan, penyimpanan, akses, dan metadata file.

Konsep penting:
- File dan direktori.
- Struktur metadata.
- Alokasi ruang penyimpanan.
- Hak akses.
- Manajemen ruang kosong.
- Operasi baca dan tulis.
- Konsistensi serta pemulihan setelah kegagalan.

Penjadwalan disk mengatur urutan permintaan I/O untuk mengurangi gerakan head pada model hard disk mekanis.

Algoritma yang perlu dikenali:
- **FCFS**: melayani permintaan berdasarkan urutan.
- **SSTF**: memilih permintaan dengan jarak seek terdekat.
- **SCAN**: bergerak ke satu arah sambil melayani permintaan yang dilewati, kemudian berbalik.
- **LOOK**: serupa SCAN, tetapi berbalik pada permintaan terakhir di arah itu, tanpa harus menuju batas fisik disk.

SSTF dapat menghasilkan waktu seek rata-rata yang baik pada kondisi tertentu, tetapi berpotensi membuat permintaan yang jauh mengalami starvation.

### Target penguasaan Sistem Operasi

Anda perlu mampu:
1. Menjelaskan proses, thread, PCB, dan context switching.
2. Menghitung metrik penjadwalan CPU.
3. Menjelaskan race condition serta sinkronisasi.
4. Menganalisis kondisi deadlock.
5. Menjelaskan paging dan menerjemahkan alamat secara konseptual.
6. Menelusuri FIFO, LRU, dan Optimal pada soal page replacement.
7. Membandingkan algoritma penjadwalan disk.

---

# 5. STATISTIKA

Sumber: [Rangkuman Materi Statistika](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/Statistika/RANGKUMAN_MATERI.md)

Statistika menyediakan metode untuk merangkum data, mengukur ketidakpastian, menguji dugaan, dan membangun model hubungan antarvariabel.

Dalam Informatika, statistika digunakan untuk mengevaluasi algoritma, membandingkan latensi sistem, menganalisis performa model machine learning, dan mempelajari pola penggunaan aplikasi.

Catatan repo: folder materi Statistika berisi 23 berkas materi, tetapi inventaris repo mencatat tidak ada berkas bank soal mentah khusus mata kuliah tersebut. Oleh karena itu, latihan dari rumus dan contoh berikut penting untuk melengkapi pemahaman.

## 5.1. Populasi, sampel, dan skala pengukuran

**Populasi** adalah keseluruhan objek yang hendak dipelajari.

**Sampel** adalah sebagian anggota populasi yang digunakan untuk analisis.

Sampel yang baik perlu mewakili populasi yang dituju. Sampel yang besar tidak otomatis bebas bias jika proses pengambilannya tidak sesuai.

Empat skala pengukuran:

**Nominal** — kategori tanpa urutan, misalnya sistem operasi atau jenis jaringan.

**Ordinal** — kategori yang mempunyai urutan, tetapi jarak antarlevel belum tentu setara, misalnya tingkat kepuasan.

**Interval** — data dengan selisih yang bermakna, tetapi tanpa nol absolut, misalnya suhu Celsius.

**Rasio** — data dengan nol absolut, misalnya waktu eksekusi, ukuran berkas, dan penggunaan memori.

Skala pengukuran memengaruhi operasi statistik yang tepat untuk data tersebut.

## 5.2. Statistika deskriptif

Statistika deskriptif merangkum data yang diamati.

### Mean

Rata-rata aritmetika:

\[
\bar{x}=\frac{1}{n}\sum_{i=1}^n x_i
\]

Mean menggunakan seluruh nilai, sehingga dapat berubah banyak ketika ada pencilan ekstrem.

### Median

Median adalah nilai tengah setelah data diurutkan. Median lebih tahan terhadap pencilan dibandingkan mean.

### Modus

Modus adalah nilai yang paling sering muncul.

### Varians dan standar deviasi

Varians sampel:

\[
s^2=\frac{1}{n-1}\sum_{i=1}^n(x_i-\bar{x})^2
\]

Standar deviasi:

\[
s=\sqrt{s^2}
\]

Varians menyatakan penyebaran dalam satuan kuadrat, sedangkan standar deviasi mempunyai satuan yang sama dengan data asli.

Penyebut \(n-1\) digunakan pada varians sampel dalam estimasi konvensional varians populasi. Varians populasi jika seluruh anggota populasi diketahui biasanya menggunakan penyebut \(N\).

### Kuartil dan pencilan

Kuartil pertama adalah \(Q_1\), sedangkan kuartil ketiga adalah \(Q_3\).

Interquartile Range:

\[
IQR=Q_3-Q_1
\]

Aturan praktis pencilan:

\[
x<Q_1-1.5IQR
\]

atau

\[
x>Q_3+1.5IQR
\]

Nilai di luar batas tersebut ditandai sebagai kemungkinan pencilan berdasarkan aturan IQR, bukan otomatis dianggap kesalahan data.

## 5.3. Teori probabilitas

Probabilitas mengukur kemungkinan terjadinya suatu kejadian.

Batas dasarnya:

\[
0\leq P(A)\leq1
\]

Probabilitas ruang sampel adalah 1.

Untuk dua kejadian:

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B)
\]

Jika A dan B saling eksklusif, maka \(P(A\cap B)=0\).

### Probabilitas bersyarat

Probabilitas A terjadi dengan syarat B telah terjadi:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
\]

dengan \(P(B)>0\).

Jangan menyamakan \(P(A\mid B)\) dengan \(P(B\mid A)\). Keduanya mengondisikan kejadian yang berbeda.

### Teorema Bayes

\[
P(A_i\mid B)=
\frac{P(B\mid A_i)P(A_i)}
{\sum_j P(B\mid A_j)P(A_j)}
\]

Keterangan:
- \(P(A_i)\): prior.
- \(P(B\mid A_i)\): likelihood.
- \(P(A_i\mid B)\): posterior.

Bayes menjadi dasar metode probabilistik seperti Naive Bayes. Contohnya, sistem menyusun probabilitas kelas suatu pesan setelah mengamati kata-kata di dalam pesan tersebut.

## 5.4. Distribusi probabilitas

Distribusi menjelaskan kemungkinan nilai sebuah variabel acak.

### Binomial

Distribusi binomial sesuai untuk jumlah keberhasilan dalam \(n\) percobaan Bernoulli independen dengan probabilitas keberhasilan \(p\) yang sama.

\[
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
\]

Rata-rata dan varians:

\[
\mu=np,\qquad \sigma^2=np(1-p)
\]

Contoh: menghitung probabilitas jumlah perangkat yang gagal dalam sejumlah uji independen dengan tingkat kegagalan yang sama.

### Poisson

Distribusi Poisson digunakan untuk menghitung banyaknya kejadian dalam interval waktu atau ruang ketika asumsi modelnya sesuai.

\[
P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}
\]

Rata-rata dan varians distribusi adalah \(\lambda\).

Contoh: memodelkan jumlah permintaan yang datang ke server dalam interval waktu tertentu berdasarkan laju kedatangan rata-rata.

### Normal

Distribusi normal memiliki bentuk kurva lonceng simetris.

\[
X\sim N(\mu,\sigma^2)
\]

Nilai \(X\) dapat distandardisasi menggunakan:

\[
Z=\frac{X-\mu}{\sigma}
\]

Distribusi Z memiliki mean 0 dan standar deviasi 1.

Aturan empiris untuk distribusi normal:
- Sekitar 68% nilai berada dalam satu standar deviasi dari mean.
- Sekitar 95% berada dalam dua standar deviasi.
- Sekitar 99,7% berada dalam tiga standar deviasi.

Aturan ini bersifat pendekatan, bukan batas probabilitas yang persis.

## 5.5. Central Limit Theorem (CLT)

CLT menjelaskan bahwa, di bawah asumsi tertentu, distribusi rata-rata sampel mendekati distribusi normal saat ukuran sampel cukup besar.

Jika populasi memiliki mean \(\mu\) dan varians \(\sigma^2\), maka rata-rata sampel memiliki:

\[
E(\bar X)=\mu
\]

\[
\operatorname{Var}(\bar X)=\frac{\sigma^2}{n}
\]

Sehingga standar error rata-rata sampel adalah:

\[
SE=\frac{\sigma}{\sqrt n}
\]

CLT penting karena memungkinkan inferensi tentang mean meskipun distribusi populasi tidak normal, selama syarat penerapannya cukup terpenuhi. Angka \(n\geq30\) sering digunakan sebagai aturan praktis awal, tetapi bukan syarat universal yang selalu memadai.

## 5.6. Selang kepercayaan

Selang kepercayaan memberikan rentang estimasi parameter berdasarkan sampel.

Jika standar deviasi populasi \(\sigma\) diketahui, selang kepercayaan untuk mean dapat menggunakan distribusi Z:

\[
\bar{x}\pm z_{\alpha/2}\frac{\sigma}{\sqrt n}
\]

Jika \(\sigma\) tidak diketahui dan asumsi model sesuai, gunakan distribusi t dengan derajat bebas \(n-1\):

\[
\bar{x}\pm t_{\alpha/2,n-1}\frac{s}{\sqrt n}
\]

Selang 95% menggunakan tingkat signifikansi total 5% untuk prosedur dua sisi standar.

Interpretasi yang tepat: dalam pengulangan sampling dan pembentukan interval dengan prosedur yang sama, sekitar 95% interval akan mencakup parameter sebenarnya jika asumsi model terpenuhi. Bukan berarti parameter yang tetap tersebut mempunyai probabilitas 95% berada dalam interval tertentu setelah interval diamati.

## 5.7. Uji hipotesis

Uji hipotesis menggunakan data sampel untuk mengevaluasi klaim mengenai populasi.

**Hipotesis nol \(H_0\)** biasanya menyatakan tidak ada perbedaan, tidak ada pengaruh, atau parameter memiliki nilai tertentu.

**Hipotesis alternatif \(H_1\)** menyatakan kondisi yang berbeda dari \(H_0\).

Langkah konseptual:
1. Rumuskan \(H_0\) dan \(H_1\).
2. Tentukan tingkat signifikansi \(\alpha\).
3. Pilih uji sesuai jenis data, desain, dan asumsi.
4. Hitung statistik uji atau p-value.
5. Ambil keputusan dan tulis interpretasinya dalam konteks masalah.

Jika:

\[
p\text{-value}\leq\alpha
\]

maka \(H_0\) ditolak pada tingkat signifikansi tersebut.

P-value bukan probabilitas bahwa \(H_0\) benar. P-value mengukur seberapa ekstrem data yang diamati, atau yang lebih ekstrem, jika \(H_0\) dan asumsi model benar.

### Kesalahan tipe I dan tipe II

- **Type I error (\(\alpha\))**: menolak \(H_0\) yang sebenarnya benar.
- **Type II error (\(\beta\))**: gagal menolak \(H_0\) yang sebenarnya salah.

Power uji adalah \(1-\beta\), yaitu probabilitas mendeteksi efek yang ditentukan ketika efek tersebut benar-benar ada di bawah kondisi model.

## 5.8. t-test dan perbandingan kelompok

Uji t digunakan pada sejumlah persoalan inferensi mean ketika kondisi penerapannya sesuai.

Contoh penggunaan:
- Membandingkan mean dengan nilai acuan.
- Membandingkan dua kelompok independen.
- Membandingkan pengukuran berpasangan, misalnya waktu respon sebelum dan sesudah optimasi pada unit yang sama.

Pemilihan uji harus mempertimbangkan apakah sampel independen atau berpasangan, asumsi distribusi, varians, serta ukuran sampel.

## 5.9. Analisis variansi (ANOVA)

One-way ANOVA digunakan untuk mengevaluasi apakah terdapat perbedaan mean di antara lebih dari dua kelompok dalam desain yang sesuai.

Variasi total dibagi menjadi variasi antarkelompok dan dalam kelompok:

\[
SS_{\text{Total}}
=SS_{\text{Between}}+SS_{\text{Within}}
\]

Statistik uji:

\[
F=
\frac{MS_{\text{Between}}}
{MS_{\text{Within}}}
\]

dengan:

\[
MS_{\text{Between}}=\frac{SS_{\text{Between}}}{k-1}
\]

\[
MS_{\text{Within}}=\frac{SS_{\text{Within}}}{N-k}
\]

\(k\) merupakan jumlah kelompok dan \(N\) merupakan jumlah seluruh observasi.

Jika uji ANOVA signifikan, kesimpulannya adalah terdapat bukti bahwa setidaknya satu mean kelompok berbeda. ANOVA sendiri tidak menunjukkan kelompok mana yang berbeda; analisis lanjutan yang sesuai mungkin diperlukan.

## 5.10. Korelasi Pearson dan regresi linier

### Korelasi Pearson

Koefisien Pearson \(r\) mengukur arah dan kekuatan hubungan linier antara dua variabel numerik.

\[
-1\leq r\leq1
\]

Interpretasi umum:
- \(r>0\): hubungan linier positif.
- \(r<0\): hubungan linier negatif.
- \(r\) mendekati 0: hubungan linier lemah atau tidak ada, walaupun hubungan nonlinier masih mungkin.

Korelasi tidak membuktikan sebab-akibat.

### Regresi linier sederhana

Regresi linier memodelkan hubungan mean suatu variabel respons dengan prediktor.

\[
\hat Y=a+bX
\]

\(a\) adalah intercept, sedangkan \(b\) adalah slope.

Slope menunjukkan perubahan nilai prediksi \(Y\) untuk setiap kenaikan satu satuan \(X\), di dalam model tersebut.

Dalam regresi kuadrat terkecil sederhana:

\[
b=\frac{n\sum xy-(\sum x)(\sum y)}
{n\sum x^2-(\sum x)^2}
\]

\[
a=\bar y-b\bar x
\]

Contoh: menganalisis hubungan jumlah pengguna aktif dengan konsumsi memori, atau hubungan jumlah request dengan latensi server.

### Target penguasaan Statistika

Anda harus mampu:
1. Menghitung mean, median, varians, standar deviasi, dan IQR.
2. Menentukan skala pengukuran data.
3. Menyelesaikan persoalan probabilitas dan Bayes.
4. Memilih distribusi binomial, Poisson, atau normal yang sesuai.
5. Menghitung atau menginterpretasikan selang kepercayaan dan uji hipotesis.
6. Memahami tujuan ANOVA.
7. Menghitung dan menafsirkan korelasi serta regresi linier.

---

# 6. STRUKTUR DATA

Sumber: [Rangkuman Materi Struktur Data](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/Struktur_Data/RANGKUMAN_MATERI.md)

Struktur Data membahas cara mengorganisasikan data di memori agar operasi pencarian, penyisipan, penghapusan, dan traversal dapat dilakukan secara efisien.

Jika Algoritma dan Pemrograman mengajarkan cara menulis instruksi, Struktur Data membantu menentukan representasi data yang cocok untuk instruksi tersebut.

## 6.1. Abstract Data Type (ADT)

ADT memisahkan spesifikasi perilaku struktur data dari implementasinya.

Contohnya, Stack dapat didefinisikan melalui operasi:
- `CreateEmpty`
- `IsEmpty`
- `Push`
- `Pop`
- `Top`

Pengguna ADT memahami kontrak operasi tanpa perlu mengetahui seluruh detail representasi internal.

ADT dapat direpresentasikan menggunakan array atau linked list, selama implementasi memenuhi perilaku yang ditentukan.

Pada bahasa C, pemisahan antarmuka dan implementasi dapat direalisasikan melalui berkas header `.h` dan source `.c`.

## 6.2. Stack

Stack menggunakan prinsip LIFO (*Last In, First Out*). Elemen yang masuk terakhir dikeluarkan pertama.

Contoh sehari-hari: tumpukan piring. Piring yang paling terakhir diletakkan di atas biasanya menjadi yang pertama diambil.

Operasi:
- `Push`: memasukkan elemen ke puncak.
- `Pop`: mengambil dan menghapus elemen dari puncak.
- `Top` atau `Peek`: melihat elemen puncak tanpa menghapusnya.
- `IsEmpty`: memeriksa apakah stack kosong.

Pada implementasi yang dirancang dengan baik, operasi push dan pop umumnya O(1).

Aplikasi Stack:
- Call stack saat fungsi dipanggil.
- Konversi ekspresi infix ke postfix.
- Evaluasi ekspresi.
- Fitur undo dan redo.
- Backtracking.

### Infix dan postfix

Infix menempatkan operator di antara operand, misalnya:

\[
A+B\times C
\]

Postfix menempatkan operator setelah operand, misalnya:

`A B C * +`

Bentuk postfix mengurangi kebutuhan tanda kurung karena urutan evaluasi ditentukan oleh posisi operator.

## 6.3. Queue

Queue menggunakan prinsip FIFO (*First In, First Out*). Elemen yang masuk lebih dahulu dikeluarkan lebih dahulu.

Operasi utamanya:
- `Enqueue`: menambahkan elemen pada bagian belakang.
- `Dequeue`: mengambil elemen dari bagian depan.
- `Front`: melihat elemen paling depan.
- `IsEmpty`: memeriksa apakah queue kosong.

Aplikasi queue:
- Antrean printer.
- Antrean request.
- Penjadwalan Round Robin.
- Breadth-First Search (BFS).

### Circular queue

Pada queue berbasis array, penghapusan berulang dapat meninggalkan ruang kosong di depan array. Circular queue menggunakan indeks melingkar agar ruang tersebut dapat dipakai kembali.

Dengan indeks berbasis nol, pembaruan indeks sering ditulis:

\[
\text{index baru}=(\text{index lama}+1)\bmod N
\]

dengan \(N\) sebagai kapasitas array.

Implementasi harus membedakan keadaan kosong dan penuh. Hal ini dapat dilakukan dengan menyimpan jumlah elemen, memanfaatkan satu slot kosong, atau menggunakan penanda tambahan.

## 6.4. Linked list

Linked list menyimpan elemen pada node yang dihubungkan melalui pointer. Node tidak harus bersebelahan dalam memori.

### Single linked list

Setiap node biasanya berisi data dan pointer `next`.

Operasi:
- InsertFirst.
- InsertAfter.
- InsertLast.
- DeleteFirst.
- DeleteAfter.
- DeleteLast.
- Search.

Penyisipan di awal bisa dilakukan dalam O(1), karena hanya memerlukan pembaruan pointer. Penyisipan di akhir membutuhkan O(n) jika program harus menelusuri seluruh list karena tidak mempunyai pointer tail.

Contoh struktur pada C:

```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;
```

Ketika node dialokasikan secara dinamis, program perlu mengelola alokasi dan dealokasi agar tidak menimbulkan memory leak.

### Double linked list

Setiap node memiliki `next` dan `prev`. Traversal dapat dilakukan maju dan mundur.

Jika node yang hendak dihapus sudah diketahui dan operasi tidak memerlukan pencarian pendahulu, penyambungan kembali pointer dapat dilakukan dalam O(1).

### Circular linked list

Pointer pada node terakhir mengarah kembali ke node pertama. Struktur ini berguna untuk traversal berulang, selama algoritma memiliki kondisi berhenti yang tepat.

## 6.5. Binary tree dan traversal

Binary tree merupakan struktur hierarkis yang setiap node-nya memiliki paling banyak dua anak: kiri dan kanan.

Istilah:
- **Root**: node akar.
- **Parent**: node induk.
- **Child**: node anak.
- **Leaf**: node tanpa anak.
- **Subtree**: pohon yang terbentuk dari suatu node beserta keturunannya.
- **Height**: panjang jalur terpanjang dari node ke daun menurut konvensi pengukuran yang digunakan.

Empat metode traversal:

**Preorder:** Root → Left → Right.

**Inorder:** Left → Root → Right.

**Postorder:** Left → Right → Root.

**Level-order:** mengunjungi node per tingkat, biasanya memakai queue.

Preorder berguna untuk menghasilkan representasi prefix pada situasi tertentu. Postorder dapat dipakai saat menghancurkan pohon dari daun ke akar. Inorder pada BST dengan aturan pengurutan yang konsisten menghasilkan nilai dalam urutan menaik.

## 6.6. Binary Search Tree (BST)

BST adalah binary tree dengan aturan bahwa semua kunci pada subtree kiri lebih kecil daripada kunci node, sedangkan semua kunci pada subtree kanan lebih besar, sesuai konvensi penanganan duplikasi yang dipilih.

Operasi search, insert, dan delete mengikuti struktur tersebut.

Jika pohon seimbang, tinggi pohon sekitar O(log n), sehingga pencarian dapat dilakukan dalam O(log n).

Jika pohon sangat condong, tingginya dapat mendekati n dan kompleksitas operasi memburuk menjadi O(n).

### Penghapusan pada BST

Ada tiga kasus:

**Kasus 1: node tanpa anak.** Node bisa dihapus langsung.

**Kasus 2: node memiliki satu anak.** Node diganti oleh anak tunggalnya.

**Kasus 3: node memiliki dua anak.** Nilainya diganti dengan inorder successor, yaitu nilai terkecil pada subtree kanan, atau inorder predecessor, yaitu nilai terbesar pada subtree kiri. Node pengganti tersebut kemudian dihapus dari posisi semula.

## 6.7. AVL tree

AVL tree merupakan BST yang mempertahankan keseimbangan tinggi subtree.

Balance factor:

\[
BF(N)=h(\text{subtree kiri})-h(\text{subtree kanan})
\]

Untuk AVL yang seimbang, nilai BF setiap node harus berada pada \(\{-1,0,1\}\).

Jika penyisipan atau penghapusan menyebabkan BF menjadi di luar rentang tersebut, rotasi digunakan untuk menyeimbangkan pohon.

Empat kasus rotasi:

- **LL (Left-Left)**: rotasi kanan.
- **RR (Right-Right)**: rotasi kiri.
- **LR (Left-Right)**: rotasi kiri pada anak, kemudian rotasi kanan pada node.
- **RL (Right-Left)**: rotasi kanan pada anak, kemudian rotasi kiri pada node.

AVL menjamin operasi pencarian, penyisipan, dan penghapusan O(log n) dalam batasan struktur seimbangnya.

Untuk ujian, jangan hanya menghafal nama rotasi. Latih penentuan kasus berdasarkan jalur penyisipan dan perubahan balance factor.

## 6.8. Heap dan priority queue

Heap adalah complete binary tree yang memenuhi aturan urutan heap.

**Max-heap:** nilai parent lebih besar daripada atau sama dengan nilai anak.

**Min-heap:** nilai parent lebih kecil daripada atau sama dengan nilai anak.

Complete binary tree dapat disimpan dalam array. Dengan indeks berbasis satu:

\[
\text{Parent}(i)=\lfloor i/2\rfloor
\]

\[
\text{LeftChild}(i)=2i
\]

\[
\text{RightChild}(i)=2i+1
\]

Pada indeks berbasis nol, rumusnya berbeda; karena itu, konvensi indeks harus diperhatikan.

Operasi penting:
- Peek pada root: O(1).
- Insert: O(log n).
- Extract minimum atau maksimum: O(log n).
- Heapify-down: O(log n).
- Build-heap bottom-up: O(n).

Heapsort menggunakan heap untuk mengurutkan data dengan jaminan kompleksitas waktu O(n log n) dan penggunaan ruang tambahan konstan pada implementasi in-place yang sesuai.

Priority queue menggunakan prioritas untuk menentukan elemen mana yang akan dikeluarkan lebih dahulu, bukan sekadar urutan kedatangannya.

## 6.9. Hash table

Hash table menyimpan pasangan kunci dan nilai dengan memetakan kunci ke indeks array menggunakan fungsi hash:

\[
h(k)\rightarrow\text{indeks}
\]

Tujuannya adalah menyediakan akses yang cepat. Pencarian, penyisipan, dan penghapusan rata-rata dapat mendekati O(1) dengan distribusi hash yang baik dan penanganan collision yang sesuai.

### Collision

Collision terjadi ketika dua kunci dipetakan ke indeks yang sama.

Metode penanganannya:

**Separate chaining**: setiap slot menyimpan struktur tambahan, misalnya linked list, yang berisi elemen-elemen dengan hash sama.

**Open addressing**: elemen collision ditempatkan di slot lain dalam tabel.

Strategi open addressing meliputi:
- Linear probing.
- Quadratic probing.
- Double hashing.

Kinerja hash table sangat dipengaruhi fungsi hash, distribusi kunci, load factor, dan strategi penanganan collision.

### Target penguasaan Struktur Data

Anda perlu mampu:
1. Menjelaskan kontrak dan implementasi ADT.
2. Menelusuri operasi Stack dan Queue.
3. Menulis atau membaca operasi linked list berbasis pointer.
4. Melakukan traversal binary tree.
5. Menyisipkan dan menghapus node BST.
6. Menentukan rotasi AVL.
7. Menjalankan insert dan delete pada heap.
8. Menangani collision pada hash table.
9. Membandingkan kompleksitas setiap struktur data.

---

# 7. HUBUNGAN ANTARMATA KULIAH SEMESTER 3

Keenam mata kuliah ini saling melengkapi dalam pengembangan sistem komputasi.

**Struktur Data dan Sistem Operasi:** Stack, queue, dan linked list membantu memahami struktur yang digunakan dalam proses, antrean, dan pengelolaan sumber daya.

**Basis Data dan Struktur Data:** Keduanya mengorganisasikan informasi, tetapi pada lapisan berbeda. Struktur data berfokus pada representasi serta operasi dalam program, sedangkan basis data mengelola data persisten beserta query, integritas, dan transaksi.

**Statistika dan Metode Numerik:** Statistika menganalisis ketidakpastian dan membuat inferensi dari sampel, sementara metode numerik menghitung pendekatan solusi terhadap persoalan matematis. Keduanya dapat digunakan bersama dalam analisis data.

**IMK dan Basis Data:** Sistem yang mudah digunakan tetap perlu menyimpan data secara benar. Antarmuka yang baik tidak menggantikan kebutuhan akan model data dan integritas yang tepat.

Contoh integrasi: aplikasi akademik yang menyediakan pencarian nilai dapat menggunakan antarmuka berdasarkan prinsip IMK, query SQL untuk mengambil data, struktur data dalam implementasi program, OS untuk mengelola proses, dan statistika untuk menganalisis distribusi nilai.

---

# 8. RUMUS DAN KONSEP WAJIB DIINGAT

## Basis Data
- PK mengidentifikasi baris secara unik.
- FK menjaga hubungan antartabel.
- 1:N: FK biasanya ditempatkan pada tabel sisi N.
- M:N: gunakan tabel penghubung.
- `WHERE` menyaring baris; `HAVING` menyaring kelompok.
- ACID: Atomicity, Consistency, Isolation, Durability.

## Interaksi Manusia dan Komputer
- Fitts's Law: \(MT=a+b\log_2(1+D/W)\).
- Hick–Hyman Law: \(T=a+b\log_2(n+1)\).
- Sepuluh heuristik Nielsen.
- Delapan aturan emas Shneiderman.
- SUS: sesuaikan kontribusi 10 item, jumlahkan, kalikan 2,5.

## Metode Numerik
- Bisection: \(x_r=(a+b)/2\).
- Newton–Raphson: \(x_{n+1}=x_n-f(x_n)/f'(x_n)\).
- Gauss–Seidel: gunakan nilai terbaru dalam iterasi saat ini.
- Trapesium dan Simpson untuk integrasi numerik.
- Beda pusat untuk diferensiasi: \([f(x+h)-f(x-h)]/(2h)\).
- Euler: \(y_{n+1}=y_n+hf(x_n,y_n)\).
- RK4: rata-rata tertimbang empat kemiringan.

## Sistem Operasi
- Turnaround time: waktu selesai dikurangi waktu kedatangan.
- Waiting time: total waktu menunggu di ready queue.
- Empat kondisi Coffman untuk deadlock.
- Page dan frame, page fault, FIFO, LRU, serta Optimal.
- Mutex dan semaphore untuk sinkronisasi.

## Statistika
- Mean: \(\bar{x}=\sum x_i/n\).
- Varians sampel: \(s^2=\sum(x_i-\bar{x})^2/(n-1)\).
- Probabilitas bersyarat: \(P(A\mid B)=P(A\cap B)/P(B)\).
- Bayes untuk memperbarui probabilitas berdasarkan bukti.
- Binomial, Poisson, normal, dan Z-score.
- Keputusan uji hipotesis berbasis p-value dan tingkat signifikansi.
- ANOVA untuk membandingkan lebih dari dua mean pada desain yang sesuai.
- Korelasi bukan bukti sebab-akibat.

## Struktur Data
- Stack: LIFO.
- Queue: FIFO.
- Preorder: Root–Left–Right.
- Inorder: Left–Root–Right.
- Postorder: Left–Right–Root.
- BST dapat menjadi O(n) ketika sangat condong.
- AVL mempertahankan tinggi seimbang.
- Heap adalah complete binary tree yang memenuhi aturan min-heap atau max-heap.
- Hash table: rata-rata mendekati O(1) jika distribusi dan penanganan collision memadai.

---

# 9. CHECKLIST PERSIAPAN UJIAN SEMESTER 3

## Basis Data
- [ ] Saya mampu mengonversi ERD ke tabel relasional.
- [ ] Saya dapat menentukan primary key, foreign key, dan kardinalitas.
- [ ] Saya mampu menulis SQL dengan JOIN, GROUP BY, HAVING, dan subquery.
- [ ] Saya bisa menjelaskan 1NF, 2NF, 3NF, dan BCNF.
- [ ] Saya mampu menerangkan ACID dan masalah transaksi konkuren.

## IMK
- [ ] Saya dapat menjelaskan memori dan model mental pengguna.
- [ ] Saya bisa membandingkan CLI, menu, form, dan direct manipulation.
- [ ] Saya memahami Fitts's Law dan Hick–Hyman Law.
- [ ] Saya dapat mengidentifikasi pelanggaran heuristik Nielsen.
- [ ] Saya memahami UCD, usability testing, dan perhitungan SUS.

## Metode Numerik
- [ ] Saya dapat menghitung galat relatif.
- [ ] Saya dapat melakukan iterasi bisection atau Newton–Raphson.
- [ ] Saya memahami perbedaan Jacobi dan Gauss–Seidel.
- [ ] Saya dapat menghitung interpolasi.
- [ ] Saya dapat mengerjakan integral trapesium dan Simpson.
- [ ] Saya dapat melakukan satu langkah Euler atau RK4.

## Sistem Operasi
- [ ] Saya memahami status proses dan perbedaan proses dengan thread.
- [ ] Saya dapat membuat Gantt chart penjadwalan CPU.
- [ ] Saya dapat menghitung turnaround dan waiting time.
- [ ] Saya memahami critical section, mutex, dan semaphore.
- [ ] Saya dapat menjelaskan empat kondisi deadlock.
- [ ] Saya dapat menelusuri page replacement.

## Statistika
- [ ] Saya dapat menghitung mean, median, varians, dan standar deviasi.
- [ ] Saya mampu menyelesaikan probabilitas bersyarat dan Bayes.
- [ ] Saya dapat mengenali distribusi binomial, Poisson, dan normal.
- [ ] Saya memahami selang kepercayaan dan uji hipotesis.
- [ ] Saya dapat menjelaskan tujuan ANOVA.
- [ ] Saya mampu menginterpretasikan korelasi dan regresi.

## Struktur Data
- [ ] Saya dapat menelusuri push, pop, enqueue, dan dequeue.
- [ ] Saya memahami pointer pada linked list.
- [ ] Saya mampu menjalankan traversal pohon.
- [ ] Saya dapat menyelesaikan operasi BST.
- [ ] Saya dapat menentukan rotasi AVL.
- [ ] Saya memahami heapify dan priority queue.
- [ ] Saya dapat menjelaskan penanganan collision pada hash table.

---

# PENUTUP SEMESTER 3

Semester 3 memperkuat pemahaman Anda tentang bagaimana data direpresentasikan, diproses, diuji, dan disimpan.

Jika hanya menghafal definisi, Anda mungkin bisa menjawab soal teori dasar, tetapi akan kesulitan ketika penguji memberikan skenario. Karena itu, gunakan dua pendekatan untuk setiap mata kuliah:

1. **Penguasaan konsep:** jelaskan mengapa metode atau struktur tertentu diperlukan dan dalam kondisi apa metode itu digunakan.
2. **Penguasaan prosedur:** lakukan perhitungan, penelusuran algoritma, penyusunan query, atau analisis kasus hingga memperoleh hasil.

Untuk latihan setelah membaca rangkuman, buka berkas `CONTOH_SOAL_DAN_PEMBAHASAN.md` pada folder masing-masing mata kuliah di repo. Utamakan soal yang meminta langkah penyelesaian, bukan hanya pilihan definisi.

Tujuan akhir Anda bukan sekadar mengingat materi Semester 3, melainkan mampu menjelaskan alasan suatu solusi dipilih, cara kerjanya, kompleksitas atau keterbatasannya, serta bagaimana solusi itu diterapkan pada sistem Informatika nyata.