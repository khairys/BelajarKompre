# Bank Contoh Soal & Pembahasan: Uji Perangkat Lunak

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Uji Perangkat Lunak Departemen Informatika Universitas Diponegoro (Koleksi Pengampu & Bank Soal HMIF 2021–2026).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (BLACK-BOX TESTING & DECISION TABLE)

### Soal UTS 1: Desain Pengujian Black-Box (Equivalence Partitioning & BVA)
**Deskripsi Soal:**
Sebuah modul registrasi akun pada sistem perbankan memiliki kolom masukan:
* **Umur Nasabah Calon Pembuat Rekening ($U$):** Syarat nasabah mandiri adalah minimal berusia $17$ tahun dan maksimal berusia $65$ tahun. Masukan berupa bilangan bulat (*integer*).

**Tugas:**
1. Tentukan **Kelas-Kelas Partisi Ekuivalensi (*Equivalence Partitions*)** yang terdiri dari partisi valid dan partisi invalid!
2. Rancanglah tabel kasus uji menggunakan teknik **Boundary Value Analysis (BVA)** dengan menguji 6 titik batas ($\min - 1, \min, \min + 1, \max - 1, \max, \max + 1$)! Tentukan nilai uji, status kelas, dan hasil yang diharapkan (*Expected Output*)!

**Kunci Pembahasan & Solusi:**
1. **Identifikasi Partisi Ekuivalensi (EP):**
   * *Partisi Invalid 1 (Terlalu Muda):* $U < 17$ (misal: $U = 10$)
   * *Partisi Valid (Rentang Sah):* $17 \le U \le 65$ (misal: $U = 30$)
   * *Partisi Invalid 2 (Terlalu Tua):* $U > 65$ (misal: $U = 75$)
   * *Partisi Invalid 3 (Non-Numerik / Negatif):* $U < 0$ atau input huruf/simbol.

2. **Tabel Kasus Uji Boundary Value Analysis (BVA):**
   * Titik Batas Bawah ($\min = 17$): $16, 17, 18$
   * Titik Batas Atas ($\max = 65$): $64, 65, 66$

| Test ID | Nilai Uji ($U$) | Kategori Batas | Jenis Partisi | Hasil yang Diharapkan (*Expected Output*) |
|:---:|:---:|:---|:---:|:---|
| **TC-01** | 16 | $\min - 1$ | **Invalid** | Sistem menolak: Tampilkan pesan error *"Usia minimal 17 tahun"* |
| **TC-02** | 17 | $\min$ | **Valid** | Sistem menerima pendaftaran rekening |
| **TC-03** | 18 | $\min + 1$ | **Valid** | Sistem menerima pendaftaran rekening |
| **TC-04** | 64 | $\max - 1$ | **Valid** | Sistem menerima pendaftaran rekening |
| **TC-05** | 65 | $\max$ | **Valid** | Sistem menerima pendaftaran rekening |
| **TC-06** | 66 | $\max + 1$ | **Invalid** | Sistem menolak: Tampilkan pesan error *"Usia maksimal 65 tahun"* |

---

### Soal UTS 2: Pengujian Berbasis Logika: Tabel Keputusan (Decision Table Testing)
**Deskripsi Soal:**
Sebuah toko online menerapkan aturan diskon belanja:
* Kondisi 1: Apakah pembeli merupakan Anggota Premium (*Member*)? (Ya/Tidak)
* Kondisi 2: Apakah total belanja $\ge$ Rp 500.000,-? (Ya/Tidak)
* Kondisi 3: Apakah pembeli memiliki Kupon Promo Spesial? (Ya/Tidak)
Aturan Aksi:
* Jika Member dan Belanja $\ge$ Rp 500.000,- $\implies$ Diskon $20\%$.
* Jika Member tetapi Belanja $<$ Rp 500.000,- $\implies$ Diskon $10\%$.
* Jika Non-Member tetapi Belanja $\ge$ Rp 500.000,- $\implies$ Diskon $5\%$.
* Jika memiliki Kupon Promo Spesial, diskon ditambah ekstra $5\%$ untuk semua kondisi di atas.
* Jika Non-Member, Belanja $<$ Rp 500.000,-, dan tanpa kupon $\implies$ Tidak ada diskon ($0\%$).

Bangunlah **Tabel Keputusan (*Decision Table*)** lengkap dengan seluruh kombinasi aturan ($2^3 = 8$ aturan) beserta aksi keluaran diskon yang dihasilkan!

**Kunci Pembahasan & Solusi:**

| Elemen Evaluasi | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Kondisi:** | | | | | | | | |
| 1. Anggota Premium (*Member*) | Y | Y | Y | Y | T | T | T | T |
| 2. Total Belanja $\ge$ Rp 500.000,- | Y | Y | T | T | Y | Y | T | T |
| 3. Memiliki Kupon Spesial | Y | T | Y | T | Y | T | Y | T |
| **Aksi (Diskon Akhir):** | | | | | | | | |
| Diskon $0\%$ | - | - | - | - | - | - | - | **X** |
| Diskon $5\%$ | - | - | - | - | - | **X** | **X** | - |
| Diskon $10\%$ | - | - | - | **X** | **X** | - | - | - |
| Diskon $15\%$ | - | - | **X** | - | - | - | - | - |
| Diskon $20\%$ | - | **X** | - | - | - | - | - | - |
| Diskon $25\%$ ($20\% + 5\%$) | **X** | - | - | - | - | - | - | - |

*(Hasil Decision Table menghasilkan tepat 8 kasus uji yang mencakup seluruh permutasi aturan bisnis secara matematis tanpa ada yang terlewat).*

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (WHITE-BOX COMPLEXITY & MUTATION TESTING)

### Soal UAS 1: Control Flow Graph & Cyclomatic Complexity (Soal Asli UTS/UAS Undip 2023)
**Deskripsi Soal:**
Diberikan algoritma pemeriksaan bilangan prima dalam fungsi Java berikut:
```java
1: public boolean cekPrima(int bil) {
2:     if (bil <= 1) {
3:         return false;
4:     }
5:     int i = 2;
6:     while (i * i <= bil) {
7:         if (bil % i == 0) {
8:             return false;
9:         }
10:        i++;
11:    }
12:    return true;
13: }
```
1. Gambarkan **Control Flow Graph (CFG)** dari kode di atas!
2. Hitung nilai **Cyclomatic Complexity ($V(G)$)** menggunakan 3 rumus berbeda!
3. Daftarkan himpunan **Jalur Basis Independen (*Basis Paths*)** yang wajib dieksekusi!

**Kunci Pembahasan & Solusi:**
1. **Identifikasi Simpul (Nodes) & Sisi (Edges) pada CFG:**
   * Node 1: Entry / Inisialisasi (Baris 1)
   * Node 2: Evaluasi Predikat `if (bil <= 1)` (Baris 2)
   * Node 3: `return false` (Baris 3–4)
   * Node 4: Inisialisasi loop `int i = 2` (Baris 5)
   * Node 5: Evaluasi Predikat Loop `while (i * i <= bil)` (Baris 6)
   * Node 6: Evaluasi Predikat Kondisi `if (bil % i == 0)` (Baris 7)
   * Node 7: `return false` (Baris 8–9)
   * Node 8: Inkrementasi `i++` (Baris 10–11)
   * Node 9: `return true` (Baris 12–13)
   * *Edges:* $(1 \rightarrow 2), (2 \rightarrow 3), (2 \rightarrow 4), (4 \rightarrow 5), (5 \rightarrow 6), (5 \rightarrow 9), (6 \rightarrow 7), (6 \rightarrow 8), (8 \rightarrow 5)$.
   * *Total:* Jumlah Nodes ($N$) $= 9$, Jumlah Edges ($E$) $= 11$.

2. **Perhitungan Cyclomatic Complexity ($V(G)$):**
   * **Rumus 1 (Edges & Nodes):**
     $$V(G) = E - N + 2P = 11 - 9 + 2(1) = \mathbf{4}$$
   * **Rumus 2 (Simpul Predikat):**
     Terdapat 3 simpul percabangan predikat: Node 2 (`if`), Node 5 (`while`), Node 6 (`if`).
     $$V(G) = P + 1 = 3 + 1 = \mathbf{4}$$
   * **Rumus 3 (Jumlah Wilayah Tertutup / Regions):**
     Terdapat 3 region tertutup di dalam graf $+ 1$ region luar bebas $\implies \mathbf{4}$.
   * *Kesimpulan:* Nilai kompleksitas siklomatis adalah **4**, yang berarti tepat dibutuhkan **4 jalur basis independen** untuk mencapai cakupan cabang 100%.

3. **Himpunan Jalur Basis Independen (*Basis Paths*):**
   * **Jalur 1:** $1 \rightarrow 2 \rightarrow 3$ (Kasus: `bil <= 1`, misal: `bil = 1` $\implies$ Return `false`).
   * **Jalur 2:** $1 \rightarrow 2 \rightarrow 4 \rightarrow 5 \rightarrow 9$ (Kasus: Loop langsung tidak terpenuhi `i*i > bil`, misal: `bil = 2` $\implies$ Return `true`).
   * **Jalur 3:** $1 \rightarrow 2 \rightarrow 4 \rightarrow 5 \rightarrow 6 \rightarrow 7$ (Kasus: Masuk loop dan menemukan faktor pembagi, misal: `bil = 4` $\implies$ Return `false`).
   * **Jalur 4:** $1 \rightarrow 2 \rightarrow 4 \rightarrow 5 \rightarrow 6 \rightarrow 8 \rightarrow 5 \rightarrow 9$ (Kasus: Masuk loop, tidak habis dibagi pada iterasi pertama, lalu keluar loop, misal: `bil = 5` $\implies$ Return `true`).

---

### Soal UAS 2: Pengujian Mutasi (Mutation Testing) & Analisis Skor Mutan
**Deskripsi Soal:**
Diberikan fungsi asli:
```java
public int hitungDiskon(int total) {
    if (total > 100000) {  // Baris Asli
        return total - 10000;
    }
    return total;
}
```
Generator mutasi menyuntikkan 3 buah mutan (*Mutants*):
* **Mutant 1:** Mengubah operator relasional menjadi: `if (total >= 100000)`
* **Mutant 2:** Mengubah operator aritmetika menjadi: `return total + 10000;`
* **Mutant 3:** Mengubah operator relasional menjadi: `if (total < 100000)`

Terdapat sebuah Test Suite yang hanya memuat **satu kasus uji tunggal**:
`Test Case A: total = 150000, Expected Output = 140000`.
1. Evaluasi apakah Test Case A berhasil membunuh (*kill*) Mutant 1, Mutant 2, dan Mutant 3!
2. Hitung nilai **Mutation Score** dari Test Suite tersebut!
3. Usulkan kasus uji tambahan agar seluruh mutan dapat terbunuh 100%!

**Kunci Pembahasan & Solusi:**
1. **Evaluasi Eksekusi Test Case A (`total = 150000`):**
   * *Program Asli:* $150000 > 100000$ (True) $\implies$ Return $150000 - 10000 = 140000$ (**PASS**).
   * *Mutant 1 (`total >= 100000`):* $150000 \ge 100000$ (True) $\implies$ Return $140000$. Hasil mutan sama persis dengan hasil asli $\implies$ Test Case A **GAGAL MEMBUNUH Mutant 1 (*Mutant 1 SURVIVES / LIVE*)**.
   * *Mutant 2 (`return total + 10000`):* Return $150000 + 10000 = 160000$. Hasil berbeda dari Expected ($140000$) $\implies$ Test case gagal (*assertion error*) $\implies$ **Mutant 2 BERHASIL DIBUNUH (*KILLED*)**.
   * *Mutant 3 (`total < 100000`):* $150000 < 100000$ (False) $\implies$ Return $150000$. Hasil berbeda dari Expected $\implies$ **Mutant 3 BERHASIL DIBUNUH (*KILLED*)**.

2. **Perhitungan Mutation Score:**
   $$\text{Mutation Score} = \frac{\text{Jumlah Mutan Terbunuh}}{\text{Total Mutan}} \times 100\% = \frac{2}{3} \times 100\% \approx \mathbf{66.67\%}$$

3. **Perbaikan Test Suite (Membunuh Mutant 1):**
   * Mutant 1 hanya berbeda dari program asli tepat pada titik batas: `total = 100000`.
   * *Kasus Uji Tambahan (Test Case B):* `total = 100000, Expected Output = 100000`.
     * Pada program asli: $100000 > 100000$ (False) $\implies$ Return $100000$ (Pass).
     * Pada Mutant 1: $100000 \ge 100000$ (True) $\implies$ Return $90000$ (Fail / Error!).
   * Dengan penambahan Test Case B, Mutant 1 berhasil dibunuh, dan Mutation Score mencapai **$100\%$**.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa cakupan kode (Code Coverage) 100% pada Unit Testing tidak menjamin bahwa perangkat lunak bebas dari bug?"
**Jawaban Komprehensif:**
Mencapai 100% *Statement* atau *Branch Coverage* hanya membuktikan bahwa setiap baris kode yang ditulis programmer telah sempat dieksekusi minimal satu kali oleh test case. Namun, cakupan kode memiliki keterbatasan fundamental:
1. *Tidak Menguji Kode yang Hilang (*Missing Code / Omission Defects*):* Jika programmer lupa mengimplementasikan validasi input (misal lupa memeriksa apakah parameter bernilai negatif atau null), coverage tetap bisa bernilai 100%, tetapi bug fatal tetap bersarang saat data null masuk di produksi.
2. *Kelemahan Asersi (*Weak Assertions*):* Kode test case mungkin mengeksekusi fungsi tanpa memeriksa apakah nilai kembaliannya benar secara logika (*asserting nothing*).
3. *Tidak Menangkap Cacat Non-Fungsional:* Coverage tidak menguji masalah kebocoran memori (*memory leaks*), kerentanan keamanan siber (*concurrency race conditions*), atau performa sistem di bawah beban ribuan pengguna serentak.

### Q2: "Jelaskan apa perbedaan antara Verifikasi (Verification) dan Validasi (Validation) dalam konteks penjaminan mutu perangkat lunak, serta berikan contoh konkret kasus di mana perangkat lunak lolos verifikasi tetapi gagal dalam validasi!"
**Jawaban Komprehensif:**
* **Verifikasi (*Verification* - "Are we building the product right?"):**
  Proses evaluasi statis dan dinamis untuk memastikan bahwa perangkat lunak yang dibangun mematuhi aturan spesifikasi teknis, standar arsitektur, dan bebas cacat sintaks/logika.
* **Validasi (*Validation* - "Are we building the right product?"):**
  Proses pengujian perangkat lunak di akhir untuk memastikan bahwa produk benar-benar memuaskan kebutuhan operasional dan memecahkan masalah riil pengguna di dunia nyata.
* **Contoh Kasus Nyata (Lolos Verifikasi tapi Gagal Validasi):**
  Sebuah tim membangun aplikasi presensi perkuliahan mahasiswa berbasis pemindaian QR-Code:
  * *Verifikasi Lolos:* Semua unit test lulus, fungsionalitas kamera QR-code bekerja 100% sempurna tanpa bug, dan data tersimpan rapi di database sesuai dokumen SRS.
  * *Validasi Gagal Total:* Saat diuji coba di ruang kelas riil berkapasitas 100 mahasiswa, koneksi internet di ruang kelas lemah dan ruangan minim cahaya sehingga kamera smartphone gagal membaca QR code di layar proyektor. Mahasiswa terlambat masuk kelas dan dosen menolak menggunakan aplikasi tersebut. Produk benar secara teknis (terverifikasi), tetapi gagal memecahkan masalah pengguna (tidak tervalidasi).
