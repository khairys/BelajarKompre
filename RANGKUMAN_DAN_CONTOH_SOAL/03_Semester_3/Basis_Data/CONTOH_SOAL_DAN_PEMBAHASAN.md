# Bank Contoh Soal & Pembahasan: Basis Data

> Sumber rujukan: Bank soal UTS & UAS Basis Data Departemen Informatika Universitas Diponegoro (Koleksi HMIF & Dosen Pengampu Basdat, 2018–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (PEMODELAN ERD & ALJABAR RELASIONAL)

### Soal UTS 1: Pemetaan ERD ke Skema Relasional (Kasus Sistem Akademik)
**Deskripsi Soal:**
Diberikan deskripsi sistem akademik jurusan Informatika:
* Sebuah **Jurusan** memiliki banyak **Dosen** dan banyak **Mahasiswa**. Setiap dosen dan mahasiswa hanya terdaftar di tepat satu jurusan.
* Seorang **Dosen** dapat menjadi dosen wali bagi banyak **Mahasiswa**, tetapi seorang mahasiswa hanya memiliki tepat satu dosen wali.
* Seorang **Mahasiswa** dapat mengambil banyak **Mata Kuliah**, dan satu **Mata Kuliah** dapat diambil oleh banyak mahasiswa. Setiap pengambilan mata kuliah menghasilkan atribut `nilai_huruf` dan `semester_ambil`.

**Pertanyaan:**
1. Gambarkan skema relasi antar-entitas beserta kardinalitasnya!
2. Lakukan transformasi pemetaan menjadi skema tabel relasional yang memenuhi kaidah normalisasi dan tentukan Primary Key (PK) serta Foreign Key (FK) dari setiap tabel!

**Kunci Pembahasan & Solusi:**
1. **Analisis Kardinalitas Relasi:**
   * Jurusan $\rightarrow$ Dosen : $1:N$
   * Jurusan $\rightarrow$ Mahasiswa : $1:N$
   * Dosen $\rightarrow$ Mahasiswa (Perwalian) : $1:N$
   * Mahasiswa $\rightarrow$ Mata Kuliah (KRS) : **$M:N$ (Many-to-Many)**
2. **Pemetaan Menjadi Skema Relasional:**
   * **Tabel Jurusan:**
     * `Jurusan` (**id_jurusan** [PK], nama_jurusan)
   * **Tabel Dosen:**
     * `Dosen` (**nip** [PK], nama_dosen, gelar, *id_jurusan* [FK merujuk ke Jurusan])
   * **Tabel Mahasiswa:**
     * `Mahasiswa` (**nim** [PK], nama_mhs, angkatan, *id_jurusan* [FK merujuk ke Jurusan], *nip_wali* [FK merujuk ke Dosen])
   * **Tabel Mata Kuliah:**
     * `MataKuliah` (**kode_mk** [PK], nama_mk, sks)
   * **Tabel Junction (Pecahan Relasi $M:N$ Mahasiswa - Mata Kuliah):**
     * Karena relasi bernilai Many-to-Many dan memiliki atribut relasi (`nilai_huruf`, `semester_ambil`), wajib dibentuk tabel perantara baru bernama `KRS`:
     * `KRS` (**nim** [FK merujuk ke Mahasiswa], **kode_mk** [FK merujuk ke MataKuliah], **semester_ambil**, nilai_huruf)
     * *Primary Key:* Composite PK gabungan `(nim, kode_mk, semester_ambil)`.

---

### Soal UTS 2: Kueri Aljabar Relasional Formal
**Deskripsi Soal:**
Diberikan skema relasi basis data universitas:
* $\text{Mahasiswa}(\underline{\text{NIM}}, \text{Nama}, \text{KotaAsal}, \text{IPK})$
* $\text{KRS}(\underline{\text{NIM}, \text{KodeMK}}, \text{Nilai})$
* $\text{MataKuliah}(\underline{\text{KodeMK}}, \text{NamaMK}, \text{SKS})$

Tuliskan ekspresi operasi **Aljabar Relasional** untuk menampilkan:
1. Nama mahasiswa yang berasal dari kota asal `'Semarang'` dan memiliki $\text{IPK} > 3.50$.
2. Nama mahasiswa yang mengambil mata kuliah `'Basis Data'`.

**Kunci Pembahasan & Solusi:**
1. **Ekspresi Soal 1 (Seleksi & Proyeksi):**
   * Lakukan seleksi baris ($\sigma$) dengan kondisi gabungan, lalu proyeksikan kolom Nama ($\pi$):
   $$\mathbf{\pi_{\text{Nama}} \Big( \sigma_{\text{KotaAsal} = \text{'Semarang'} \,\land\, \text{IPK} > 3.50} (\text{Mahasiswa}) \Big)}$$
2. **Ekspresi Soal 2 (Natural Join & Proyeksi):**
   * Lakukan seleksi pada tabel `MataKuliah` untuk nama mata kuliah `'Basis Data'`.
   * Gabungkan dengan tabel `KRS` berdasarkan kesamaan `KodeMK`.
   * Gabungkan hasilnya dengan tabel `Mahasiswa` berdasarkan kesamaan `NIM`.
   * Proyeksikan kolom `Nama`:
   $$\mathbf{\pi_{\text{Nama}} \Big( \text{Mahasiswa} \bowtie \text{KRS} \bowtie \sigma_{\text{NamaMK} = \text{'Basis Data'}} (\text{MataKuliah}) \Big)}$$

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (NORMALISASI BCNF & SQL LANJUT)

### Soal UAS 1: Dekomposisi Normalisasi (UNF $\to$ 1NF $\to$ 2NF $\to$ 3NF)
**Deskripsi Soal:**
Sebuah klinik memiliki catatan faktur resep obat yang masih belum ternormalisasi (UNF):
`Faktur(NoFaktur, Tanggal, PasienID, NamaPasien, (KodeObat, NamaObat, Harga, Jumlah, Subtotal))`
Diberikan himpunan Ketergantungan Fungsional (*Functional Dependencies*):
* $\text{NoFaktur} \to \text{Tanggal}, \text{PasienID}, \text{NamaPasien}$
* $\text{PasienID} \to \text{NamaPasien}$
* $\text{KodeObat} \to \text{NamaObat}, \text{Harga}$
* $\text{NoFaktur}, \text{KodeObat} \to \text{Jumlah}, \text{Subtotal}$

Lakukan proses normalisasi bertahap hingga mencapai **Bentuk Normal Ketiga (3NF)**!

**Kunci Pembahasan & Solusi:**
1. **Bentuk Normal Pertama (1NF):**
   Hilangkan grup atribut berulang (*repeating groups*) dan tetapkan Primary Key komposit:
   $$\text{Faktur\_1NF}(\underline{\text{NoFaktur}, \text{KodeObat}}, \text{Tanggal}, \text{PasienID}, \text{NamaPasien}, \text{NamaObat}, \text{Harga}, \text{Jumlah}, \text{Subtotal})$$
2. **Bentuk Normal Kedua (2NF):**
   Hilangkan **Ketergantungan Parsial** (atribut yang hanya bergantung pada sebagian Primary Key):
   * $\text{NoFaktur} \to \text{Tanggal}, \text{PasienID}, \text{NamaPasien}$ (bergantung hanya pada `NoFaktur`).
   * $\text{KodeObat} \to \text{NamaObat}, \text{Harga}$ (bergantung hanya pada `KodeObat`).
   * **Hasil Dekomposisi 2NF:**
     * `Faktur` (**NoFaktur**, Tanggal, PasienID, NamaPasien)
     * `Obat` (**KodeObat**, NamaObat, Harga)
     * `DetailFaktur` (**NoFaktur**, **KodeObat**, Jumlah, Subtotal)
3. **Bentuk Normal Ketiga (3NF):**
   Periksa apakah ada **Ketergantungan Transitif** pada tabel-tabel 2NF (atribut non-kunci bergantung pada atribut non-kunci lain):
   * Pada tabel `Faktur`: $\text{NoFaktur} \to \text{PasienID}$, dan $\text{PasienID} \to \text{NamaPasien}$. Terjadi ketergantungan transitif!
   * Dekomposisikan entitas pasien keluar dari tabel faktur:
     * `Pasien` (**PasienID**, NamaPasien)
     * `Faktur` (**NoFaktur**, Tanggal, *PasienID* [FK])
   * Tabel `Obat` dan `DetailFaktur` sudah tidak memiliki ketergantungan transitif.
4. **Hasil Akhir Skema Relasional 3NF:**
   1. `Pasien` (**PasienID**, NamaPasien)
   2. `Faktur` (**NoFaktur**, Tanggal, *PasienID*)
   3. `Obat` (**KodeObat**, NamaObat, Harga)
   4. `DetailFaktur` (**NoFaktur**, **KodeObat**, Jumlah, Subtotal)

---

### Soal UAS 2: Penulisan Kueri SQL Agregasi & Left Outer Join
**Deskripsi Soal:**
Diberikan tabel `Departemen(id_dept, nama_dept)` dan `Pegawai(id_pegawai, nama_pegawai, gaji, id_dept)`.
Tuliskan kueri SQL untuk menampilkan nama departemen beserta **rata-rata gaji** pegawai di setiap departemen tersebut, dengan ketentuan:
1. Departemen yang belum memiliki pegawai sama sekali harus **tetap tampil** dalam laporan (tampilkan rata-rata gaji sebagai $0$ atau `NULL`).
2. Hanya tampilkan departemen yang memiliki rata-rata gaji pegawai **di atas Rp 7.000.000**!
3. Urutkan hasil berdasarkan rata-rata gaji tertinggi!

**Kunci Pembahasan & Solusi (SQL):**
```sql
SELECT 
    d.nama_dept, 
    AVG(p.gaji) AS rata_rata_gaji
FROM 
    Departemen d
LEFT OUTER JOIN 
    Pegawai p ON d.id_dept = p.id_dept
GROUP BY 
    d.id_dept, d.nama_dept
HAVING 
    AVG(p.gaji) > 7000000
ORDER BY 
    rata_rata_gaji DESC;
```
*(Catatan Analisis: Penggunaan `LEFT OUTER JOIN` memastikan departemen tanpa pegawai tidak tereliminasi di awal. Penggunaan `HAVING` mutlak diperlukan karena memfilter hasil kalkulasi fungsi agregat `AVG(gaji)`, bukan baris individual).*

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan apa yang dimaksud dengan sifat ACID dalam transaksi basis data dan berikan contoh kegagalan jika prinsip Atomicity dilanggar!"
**Jawaban Komprehensif:**
Sifat ACID adalah empat pilar penjamin keandalan transaksi:
* **Atomicity:** Prinsip *all-or-nothing*. Seluruh rangkaian perintah dalam satu transaksi wajib selesai tuntas, atau dibatalkan sama sekali jika ada kegagalan.
* **Consistency:** Memastikan transaksi tidak melanggar batasan integritas skema data (*constraints*).
* **Isolation:** Transaksi yang berjalan serentak tidak boleh saling melihat status sementara transaksi lain yang belum di-commit.
* **Durability:** Data yang sudah di-commit dijamin tersimpan permanen dan tahan banting terhadap kerusakan perangkat keras (*crash recovery*).
* **Contoh Kegagalan Atomicity:** Pada transaksi transfer bank Rp 1.000.000 dari rekening A ke rekening B: Saldo A dipotong Rp 1.000.000, namun sebelum saldo B ditambah, sistem mengalami mati listrik mendadak. Jika tidak ada prinsip *Atomicity* (auto-rollback), saldo A telah berkurang namun saldo B tidak bertambah, menyebabkan uang nasabah hilang tertelan sistem.

### Q2: "Mengapa sebuah tabel yang berada dalam bentuk 1NF otomatis memenuhi syarat 2NF jika Primary Key-nya hanya terdiri dari satu kolom atribut tunggal?"
**Jawaban Komprehensif:**
Bentuk Normal Kedua (2NF) melarang adanya **Ketergantungan Parsial (*Partial Dependency*)**, yaitu kondisi di mana suatu atribut non-kunci hanya bergantung pada *sebagian* dari Primary Key.
Ketergantungan parsial secara matematis **hanya mungkin terjadi jika Primary Key berupa kunci komposit (gabungan dua atau lebih atribut)**. Jika Primary Key hanya berupa satu atribut tunggal, maka tidak ada konsep "sebagian kunci"; seluruh atribut non-kunci secara mutlak hanya bergantung pada satu-satunya atribut primary key tersebut. Oleh karena itu, tabel ber-primary key tunggal yang telah memenuhi 1NF secara otomatis dijamin memenuhi 2NF.
