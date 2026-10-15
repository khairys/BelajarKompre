# Bank Contoh Soal & Pembahasan: Analisis dan Strategi Algoritma

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Analisis dan Strategi Algoritma Departemen Informatika Universitas Diponegoro (Koleksi Dosen Pengampu & Bank Soal HMIF 2017–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (TEOREMA MASTER & GREEDY HUFFMAN)

### Soal UTS 1: Analisis Relasi Rekurensi Menggunakan Teorema Master (Soal Asli UTS Undip)
**Deskripsi Soal:**
Tentukan kompleksitas asimptotik fungsi waktu $T(n)$ dari 3 buah algoritma rekursif berikut menggunakan **Teorema Master**:
1. $T(n) = 4T(n/2) + n$
2. $T(n) = 4T(n/2) + n^2$
3. $T(n) = 4T(n/2) + n^3$

**Kunci Pembahasan & Solusi:**
Bentuk umum Teorema Master:
$$T(n) = a T(n/b) + f(n), \quad \text{dengan } f(n) = \Theta(n^d)$$
Pada ketiga persamaan di atas: $a = 4, b = 2$.
Nilai pembanding kritis:
$$\log_b(a) = \log_2(4) = \mathbf{2}$$

1. **Kasus 1: $T(n) = 4T(n/2) + n$**
   * Di sini $f(n) = n^1 \implies d = 1$.
   * Bandingkan $d$ dengan $\log_b(a)$: $d = 1 < \log_b(a) = 2$.
   * Sesuai **Kasus 1 Teorema Master**, suku rekursif mendominasi:
     $$T(n) = \Theta(n^{\log_b(a)}) = \mathbf{\Theta(n^2)}$$

2. **Kasus 2: $T(n) = 4T(n/2) + n^2$**
   * Di sini $f(n) = n^2 \implies d = 2$.
   * Bandingkan $d$ dengan $\log_b(a)$: $d = 2 == \log_b(a) = 2$.
   * Sesuai **Kasus 2 Teorema Master**, beban kerja seimbang di setiap level:
     $$T(n) = \Theta(n^d \log n) = \mathbf{\Theta(n^2 \log n)}$$

3. **Kasus 3: $T(n) = 4T(n/2) + n^3$**
   * Di sini $f(n) = n^3 \implies d = 3$.
   * Bandingkan $d$ dengan $\log_b(a)$: $d = 3 > \log_b(a) = 2$.
   * Periksa kondisi keteraturan (*regularity condition*): $a f(n/b) \le c f(n) \implies 4(n/2)^3 = \frac{1}{2} n^3 \le c n^3$ (terpenuhi untuk $c = 1/2 < 1$).
   * Sesuai **Kasus 3 Teorema Master**, suku partisi/penggabungan mendominasi:
     $$T(n) = \Theta(n^d) = \mathbf{\Theta(n^3)}$$

---

### Soal UTS 2: Algoritma Kompresi Data Greedy Huffman Coding
**Deskripsi Soal:**
Sebuah file teks memuat 5 karakter unik dengan frekuensi kemunculan sebagai berikut:
* `A`: 30 kali, `B`: 25 kali, `C`: 20 kali, `D`: 15 kali, `E`: 10 kali (Total 100 karakter).
1. Gambarkan langkah pembentukan **Pohon Biner Huffman** langkah demi langkah menggunakan antrean prioritas *Min-Heap*!
2. Tentukan kode biner prefix-free untuk masing-masing karakter (cabang kiri $= 0$, cabang kanan $= 1$)!
3. Hitung jumlah bit total yang dibutuhkan untuk menyimpan teks tersebut setelah dikompresi, dan bandingkan dengan representasi kode ASCII 8-bit tetap (*Fixed-Length Code*)!

**Kunci Pembahasan & Solusi:**
1. **Langkah Pembentukan Pohon Huffman:**
   * *Status Awal:* Min-Heap $\{ E(10), D(15), C(20), B(25), A(30) \}$.
   * *Gabungan 1:* Ambil dua terkecil: $E(10)$ dan $D(15) \implies$ Simpul baru $N_1(25)$.
     * Heap: $\{ C(20), B(25), N_1(25), A(30) \}$.
   * *Gabungan 2:* Ambil dua terkecil: $C(20)$ dan $B(25) \implies$ Simpul baru $N_2(45)$.
     * Heap: $\{ N_1(25), A(30), N_2(45) \}$.
   * *Gabungan 3:* Ambil dua terkecil: $N_1(25)$ dan $A(30) \implies$ Simpul baru $N_3(55)$.
     * Heap: $\{ N_2(45), N_3(55) \}$.
   * *Gabungan 4 (Akar Utama):* Gabungkan $N_2(45)$ dan $N_3(55) \implies$ Akar $Root(100)$.

2. **Penentuan Kode Biner Karakter:**
   ```text
                  Root(100)
                 /         \
             0 /             \ 1
            N2(45)          N3(55)
           /      \        /      \
        0 /      1 \    0 /        \ 1
        C(20)   B(25)  N1(25)     A(30)
                       /    \
                    0 /      \ 1
                    E(10)   D(15)
   ```
   * **C** (Kiri - Kiri) $\implies \mathbf{00}$ (Panjang 2 bit)
   * **B** (Kiri - Kanan) $\implies \mathbf{01}$ (Panjang 2 bit)
   * **A** (Kanan - Kanan) $\implies \mathbf{11}$ (Panjang 2 bit)
   * **E** (Kanan - Kiri - Kiri) $\implies \mathbf{100}$ (Panjang 3 bit)
   * **D** (Kanan - Kiri - Kanan) $\implies \mathbf{101}$ (Panjang 3 bit)

3. **Perhitungan Efisiensi Kompresi:**
   * **Ukuran Asli dengan Kode ASCII 8-bit:**
     $$\text{Ukuran Asli} = 100 \times 8 \text{ bit} = \mathbf{800 \text{ bit}}$$
   * **Ukuran Setelah Kompresi Huffman:**
     $$\text{Ukuran Huffman} = (30 \times 2) + (25 \times 2) + (20 \times 2) + (15 \times 3) + (10 \times 3)$$
     $$\text{Ukuran Huffman} = 60 + 50 + 40 + 45 + 30 = \mathbf{225 \text{ bit}}$$
   * **Rasio Penghematan Ukuran:**
     $$\text{Penghematan} = \frac{800 - 225}{800} \times 100\% = \frac{575}{800} \times 100\% \approx \mathbf{71.875\%}$$

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (DYNAMIC PROGRAMMING & BACKTRACKING)

### Soal UAS 1: 0/1 Knapsack Problem Menggunakan Pemrograman Dinamis (Soal Asli UAS Undip)
**Deskripsi Soal:**
Diberikan kapasitas tas ransel maksimal $W = 6$ kg dan 3 buah barang:
* Barang 1 ($i=1$): Bobot $w_1 = 2$ kg, Nilai $v_1 = 3$ juta
* Barang 2 ($i=2$): Bobot $w_2 = 3$ kg, Nilai $v_2 = 4$ juta
* Barang 3 ($i=3$): Bobot $w_3 = 4$ kg, Nilai $v_3 = 5$ juta
(Barang tidak boleh dipotong / harus diambil utuh atau tidak sama sekali).

1. Bangunlah tabel **Dynamic Programming $K[i, w]$** berukuran $4 \times 7$ secara terperinci!
2. Berapa nilai maksimal keuntungan yang dapat dimasukkan ke dalam tas ransel?
3. Lakukan penelusuran balik (*backtracking*) pada tabel untuk mengidentifikasi kombinasi barang mana saja yang terpilih!

**Kunci Pembahasan & Solusi:**
1. **Pembangunan Tabel DP $K[i, w]$:**
   Rumus transisi:
   $$K[i, w] = \max(K[i-1, w], \; v_i + K[i-1, w - w_i]) \quad \text{jika } w_i \le w$$

| Barang ($i$) | Bobot ($w_i$) | Nilai ($v_i$) | $w=0$ | $w=1$ | $w=2$ | $w=3$ | $w=4$ | $w=5$ | $w=6$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$i=0$ (Tanpa barang)** | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **$i=1$** | 2 | 3 | 0 | 0 | 3 | 3 | 3 | 3 | 3 |
| **$i=2$** | 3 | 4 | 0 | 0 | 3 | 4 | 4 | 7 | 7 |
| **$i=3$** | 4 | 5 | 0 | 0 | 3 | 4 | 5 | 7 | **7** |

*Detail perhitungan penting:*
* Pada $i=2, w=5$: $\max(K[1, 5], v_2 + K[1, 5-3]) = \max(3, 4 + 3) = \mathbf{7}$.
* Pada $i=3, w=6$: $\max(K[2, 6], v_3 + K[2, 6-4]) = \max(7, 5 + 3) = \max(7, 8) \implies$ Koreksi: untuk $w=6$, $5 + K[2, 2] = 5 + 3 = 8$!
  * Maka nilai pada $i=3, w=6$ adalah $\mathbf{8}$! (Bukan 7).

*Tabel Akhir yang Benar:*

| Barang ($i$) | $w_i$ | $v_i$ | $w=0$ | $w=1$ | $w=2$ | $w=3$ | $w=4$ | $w=5$ | $w=6$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$i=0$** | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **$i=1$** | 2 | 3 | 0 | 0 | 3 | 3 | 3 | 3 | 3 |
| **$i=2$** | 3 | 4 | 0 | 0 | 3 | 4 | 4 | 7 | 7 |
| **$i=3$** | 4 | 5 | 0 | 0 | 3 | 4 | 5 | 7 | **8** |

2. **Nilai Maksimal Keuntungan:** Nilai pada sel kanan bawah $K[3, 6] = \mathbf{8 \text{ juta rupiah}}$.

3. **Rekonstruksi Penelusuran Balik Barang Terpilih:**
   * Mulai dari sel $K[3, 6] = 8$.
   * Bandingkan dengan sel atasnya $K[2, 6] = 7$.
   * Karena $K[3, 6] \ne K[2, 6]$, maka **Barang 3 TERPILIH!**
   * Sisa kapasitas ransel: $w = 6 - w_3 = 6 - 4 = 2$.
   * Pindah ke sel $K[2, 2] = 3$.
   * Bandingkan dengan sel atasnya $K[1, 2] = 3$.
   * Karena $K[2, 2] == K[1, 2]$, maka **Barang 2 TIDAK TERPILIH**.
   * Pindah ke sel $K[1, 2] = 3$.
   * Bandingkan dengan sel atasnya $K[0, 2] = 0$.
   * Karena $K[1, 2] \ne K[0, 2]$, maka **Barang 1 TERPILIH!**
   * Sisa kapasitas: $w = 2 - w_1 = 2 - 2 = 0$. Selesai.
   * *Himpunan Barang Terpilih:* **Barang 1 dan Barang 3** (Total bobot $= 2 + 4 = 6$ kg, Total nilai $= 3 + 5 = 8$ juta).

---

### Soal UAS 2: Algoritma Runut-Balik (Backtracking) Masalah 4-Queens
**Deskripsi Soal:**
Pada papan catur $4 \times 4$, tempatkan 4 buah ratu ($Q_1, Q_2, Q_3, Q_4$) sedemikian rupa sehingga tidak ada dua ratu yang saling serang.
Representasikan solusi sebagai vektor $X = [x_1, x_2, x_3, x_4]$ di mana $x_i$ adalah nomor kolom penempatan ratu baris ke-$i$.
Tuliskan satu solusi valid dan buktikan dengan fungsi pembatas diagonal $|x_i - x_j| \ne |i - j|$!

**Kunci Pembahasan & Solusi:**
1. **Solusi Valid yang Ditemukan oleh Backtracking:**
   $$X = [2, 4, 1, 3]$$
   * Ratu 1 di Baris 1, Kolom 2.
   * Ratu 2 di Baris 2, Kolom 4.
   * Ratu 3 di Baris 3, Kolom 1.
   * Ratu 4 di Baris 4, Kolom 3.

2. **Pembuktian Kondisi Pembatas Aman (*Bounding Function*):**
   * Kolom unik (tidak ada serangan vertikal): $\{2, 4, 1, 3\}$ semuanya berbeda.
   * Baris unik (tidak ada serangan horizontal): Setiap baris hanya diisi 1 ratu.
   * **Pengujian Serangan Diagonal ($|x_i - x_j| \ne |i - j|$):**
     * Pasangan $(Q_1, Q_2)$: $|2 - 4| = 2 \ne |1 - 2| = 1$ (Aman)
     * Pasangan $(Q_1, Q_3)$: $|2 - 1| = 1 \ne |1 - 3| = 2$ (Aman)
     * Pasangan $(Q_1, Q_4)$: $|2 - 3| = 1 \ne |1 - 4| = 3$ (Aman)
     * Pasangan $(Q_2, Q_3)$: $|4 - 1| = 3 \ne |2 - 3| = 1$ (Aman)
     * Pasangan $(Q_2, Q_4)$: $|4 - 3| = 1 \ne |2 - 4| = 2$ (Aman)
     * Pasangan $(Q_3, Q_4)$: $|1 - 3| = 2 \ne |3 - 4| = 1$ (Aman)
   * Seluruh pasangan terbukti aman dari serangan diagonal. Solusi $X = [2, 4, 1, 3]$ adalah solusi sah.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan perbedaan mendasar antara Algoritma Greedy dan Pemrograman Dinamis (Dynamic Programming), serta mengapa strategi Greedy gagal menghasilkan solusi optimal pada masalah 0/1 Knapsack?"
**Jawaban Komprehensif:**
* **Perbedaan Prinsip:**
  * **Algoritma Greedy:** Mengambil keputusan terbaik secara lokal (*myopic choice*) pada setiap langkah tanpa pernah mempertimbangkan konsekuensi masa depan dan **tidak pernah mengubah keputusan masa lalu (*No Backtracking / Commits irrevocably*)**.
  * **Dynamic Programming:** Mengevaluasi seluruh kemungkinan kombinasi keputusan optimal sub-masalah secara komprehensif, menyimpan hasilnya dalam tabel memoization, sehingga keputusan saat ini memperhitungkan solusi masa depan secara menyeluruh.
* **Mengapa Greedy Gagal pada 0/1 Knapsack:**
  Pada 0/1 Knapsack, barang tidak boleh dipotong. Jika kita menggunakan strategi Greedy berbasis densitas nilai tertinggi ($v_i/w_i$), kita mungkin memilih barang bernilai densitas tinggi namun berbobot canggung yang menyisakan ruang kosong di ransel yang tidak dapat diisi oleh barang lain. Akibatnya, kombinasi beberapa barang dengan densitas lebih rendah yang mengisi ransel secara pas dan penuh dapat menghasilkan total nilai keuntungan yang jauh lebih besar.

### Q2: "Jelaskan apa perbedaan antara strategi pemangkasan pohon pencarian pada Algoritma Runut-Balik (Backtracking) dan Algoritma Branch and Bound!"
**Jawaban Komprehensif:**
* **Backtracking:**
  1. Menelusuri pohon ruang status menggunakan strategi **Depth-First Search (DFS)**.
  2. Digunakan terutama untuk mencari solusi kelayakan (*feasibility problems*, seperti puzzle N-Queens, Sudoku, pewarnaan graf).
  3. Pemangkasan (*pruning*) dilakukan segera saat suatu simpul melanggar kendala (*constraint violation / dead-end*).
* **Branch and Bound:**
  1. Menelusuri pohon ruang status menggunakan strategi **Breadth-First Search (BFS)** atau **Best-First Search** menggunakan antrean prioritas (*Priority Queue*).
  2. Digunakan secara eksklusif untuk **masalah optimasi (Minimasi biaya atau Maksimasi keuntungan)**, seperti TSP atau Integer Programming.
  3. Pemangkasan dilakukan berdasarkan **fungsi matematis batas bawah (*Lower Bound*) atau batas atas (*Upper Bound*)**. Suatu cabang dipangkas bukan karena melanggar aturan, melainkan karena secara matematis terbukti nilai terbaik yang bisa dicapai dari cabang tersebut sudah lebih buruk daripada solusi optimal sementara yang telah ditemukan.
