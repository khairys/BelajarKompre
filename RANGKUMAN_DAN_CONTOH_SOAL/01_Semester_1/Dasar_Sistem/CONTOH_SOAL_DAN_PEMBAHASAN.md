# Bank Contoh Soal & Pembahasan: Dasar Sistem

> Sumber rujukan: Bank soal UTS & UAS Dasar Sistem Departemen Informatika Universitas Diponegoro (Koleksi HMIF 2018–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (SISTEM BILANGAN, K-MAP & KOMBINASIONAL)

### Soal UTS 1: Operasi Aritmetika Biner Komplemen Dua (2's Complement)
**Deskripsi Soal:**
Hitunglah operasi pengurangan desimal berikut: $(+42)_{10} - (+65)_{10}$ menggunakan sistem biner bertanda Komplemen Dua (*2's Complement*) dengan alokasi register 8 bit. Tunjukkan langkah-langkah pembentukan komplemen dua, proses penjumlahan, dan periksa apakah terjadi kondisi *overflow*!

**Kunci Pembahasan & Solusi:**
1. **Representasi Biner Positif:**
   * $(42)_{10} = 32 + 8 + 2 = (0010\,1010)_2$
   * $(65)_{10} = 64 + 1 = (0100\,0001)_2$
2. **Membentuk Nilai Negatif $(-65)_{10}$ via Komplemen Dua:**
   * Ambil representasi $+65$: `0100 0001`
   * Balik semua bit (Komplemen 1): `1011 1110`
   * Tambahkan 1 (Komplemen 2):
     $$\begin{array}{r@{\quad}l}
     1011\,1110 & \\
     +\quad\quad\quad 1 & \\
     \hline
     1011\,1111 & = (-65)_{10}
     \end{array}$$
3. **Lakukan Operasi Penjumlahan: $(+42) + (-65)$:**
   $$\begin{array}{r@{\quad}l}
   0010\,1010 & (+42) \\
   +\quad 1011\,1111 & (-65) \\
   \hline
   1110\,1001 &
   \end{array}$$
4. **Interpretasi Hasil & Pemeriksaan Overflow:**
   * Bit paling kiri (MSB) bernilai `1`, berarti hasil bertanda negatif.
   * Untuk mencari nilai absolut desimalnya, lakukan komplemen 2 kembali:
     * Balik bit `1110 1001` $\rightarrow$ `0001 0110`
     * Tambah 1: `0001 0110 + 1 = 0001 0111` $= 16 + 4 + 2 + 1 = 23_{10}$.
     * Hasil akhir: **$-23_{10}$** (Benar: $42 - 65 = -23$).
   * **Deteksi Overflow:** Operasi melibatkan penjumlahan dua bilangan berbeda tanda (positif + negatif). Overflow *mustahil* terjadi pada penjumlahan tanda berlawanan. *Overflow Flag* $V = 0$.

---

### Soal UTS 2: Minimisasi Fungsi Boolean dengan K-Map & Gerbang NAND Universal
**Deskripsi Soal:**
Diberikan fungsi Boolean 4 variabel:
$$f(A, B, C, D) = \sum m(1, 3, 5, 7, 9) + d(6, 13, 15)$$
1. Gambarkan peta Karnaugh (K-Map) 4 variabel untuk fungsi tersebut.
2. Tentukan ekspresi Sum-of-Products (SOP) yang paling minimal.
3. Gambarkan skema rangkaian logika hanya menggunakan gerbang **NAND 2-input**.

**Kunci Pembahasan & Solusi:**
1. **Pemetaan K-Map 4 Variabel ($AB \backslash CD$):**

| $AB \backslash CD$ | 00 (0) | 01 (1) | 11 (3) | 10 (2) |
|:---:|:---:|:---:|:---:|:---:|
| **00** | 0 | **1** ($m_1$) | **1** ($m_3$) | 0 |
| **01** | 0 | **1** ($m_5$) | **1** ($m_7$) | X ($d_6$) |
| **11** | 0 | X ($d_{13}$) | X ($d_{15}$) | 0 |
| **10** | 0 | **1** ($m_9$) | 0 | 0 |

2. **Pengelompokan (Grouping):**
   * **Grup 1 (Ukuran 8):** Kolom $CD = 01$ dan $CD = 11$ pada baris $AB = 00, 01, 11$. Namun perhatikan: $m_9$ ($1001$) hanya ada di kolom $CD=01$.
   * **Kelompok Termudah & Terbesar:**
     * Kelompok 4 sel vertikal kolom $CD=01$ ($m_1, m_5, d_{13}, m_9$): menghasilkan term $\overline{C}D$.
     * Kelompok 4 sel kotak baris $AB=00, 01$ kolom $CD=01, 11$ ($m_1, m_3, m_5, m_7$): menghasilkan term $\overline{A}D$.
     * Alternatif: Seluruh minterm tercakup oleh dua kelompok ukuran 4 ini.
   * **Hasil Minimal SOP:**
     $$f(A, B, C, D) = \overline{A}D + \overline{C}D = D(\overline{A} + \overline{C})$$
3. **Konversi ke Gerbang NAND Saja:**
   * Terapkan involusi ganda (hukum De Morgan ganda):
     $$f = \overline{\overline{\overline{A}D + \overline{C}D}} = \overline{\overline{(\overline{A}D)} \cdot \overline{(\overline{C}D)}}$$
   * Rangkaian membutuhkan:
     * Inverter untuk $A$ dan $C$ (menggunakan NAND dengan kedua input disatukan: $\overline{A} = \overline{A \cdot A}$).
     * 2 gerbang NAND untuk menghasilkan $\overline{\overline{A}D}$ dan $\overline{\overline{C}D}$.
     * 1 gerbang NAND output untuk menggabungkan keduanya.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (RANGKAIAN SEKUENSIAL & COUNTER)

### Soal UAS 1: Desain Counter Sinkron Modulo-6 menggunakan JK Flip-Flop
**Deskripsi Soal:**
Rancanglah sebuah pencacah (*counter*) sinkron yang menghitung urutan siklik modulo-6:
$$0 \rightarrow 1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow 0 \dots$$
menggunakan **JK Flip-Flop** dengan pemicuan tepi clock (*clock edge-triggered*).

**Kunci Pembahasan & Solusi:**
1. **Jumlah Flip-Flop:** Karena jumlah status $N = 6$, dibutuhkan $k = 3$ Flip-Flop ($2^2 < 6 \le 2^3$). Sebut output FF sebagai $Q_A, Q_B, Q_C$ di mana $Q_C$ adalah LSB.
2. **Tabel Eksitasi JK Flip-Flop Acuan:**
   * $0 \rightarrow 0 : J=0, K=X$
   * $0 \rightarrow 1 : J=1, K=X$
   * $1 \rightarrow 0 : J=X, K=1$
   * $1 \rightarrow 1 : J=X, K=0$
3. **State Transition & Excitation Table:**

| Present State ($Q_A Q_B Q_C$) | Next State ($Q_A^+ Q_B^+ Q_C^+$) | $J_A$ | $K_A$ | $J_B$ | $K_B$ | $J_C$ | $K_C$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 000 (0) | 001 (1) | 0 | X | 0 | X | 1 | X |
| 001 (1) | 010 (2) | 0 | X | 1 | X | X | 1 |
| 010 (2) | 011 (3) | 0 | X | X | 0 | 1 | X |
| 011 (3) | 100 (4) | 1 | X | X | 1 | X | 1 |
| 100 (4) | 101 (5) | X | 0 | 0 | X | 1 | X |
| 101 (5) | 000 (0) | X | 1 | 0 | X | X | 1 |
| 110 (Unused) | ddd | X | X | X | X | X | X |
| 111 (Unused) | ddd | X | X | X | X | X | X |

4. **Minimisasi K-Map untuk Input JK:**
   * **Untuk $Q_C$:** $J_C = 1$, $K_C = 1$ (karena $Q_C$ selalu berganti status 0-1-0-1... di setiap clock!).
   * **Untuk $Q_B$:**
     * $J_B$: bernilai 1 saat $001$, X saat $010, 011, 100, 101, 110, 111$. Dikelompokkan dengan Don't Care $\rightarrow J_B = Q_C \overline{Q_A}$.
     * $K_B$: bernilai 1 saat $011$, 0 saat $010$, X lainnya $\rightarrow K_B = Q_C$.
   * **Untuk $Q_A$:**
     * $J_A$: bernilai 1 saat $011 \rightarrow J_A = Q_B Q_C$.
     * $K_A$: bernilai 1 saat $101 \rightarrow K_A = Q_C$.
5. **Kesimpulan Persamaan Input:**
   * Flip-Flop C: $J_C = 1, \quad K_C = 1$
   * Flip-Flop B: $J_B = \overline{Q_A} \cdot Q_C, \quad K_B = Q_C$
   * Flip-Flop A: $J_A = Q_B \cdot Q_C, \quad K_A = Q_C$
   * Seluruh clock pin ketiga Flip-Flop dihubungkan serentak ke sumber clock utama (*Synchronous*).

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa sistem komputer modern menggunakan komplemen dua (2's complement) untuk bilangan bertanda, bukan komplemen satu atau sign-and-magnitude?"
**Jawaban Komprehensif:**
1. **Keunikan Nilai Nol:** Pada sign-and-magnitude dan komplemen satu, terdapat dua nilai nol ($+0$ dan $-0$), yang membuang satu kemungkinan kombinasi bit dan memperumit logika pembanding aritmetika di ALU. Pada komplemen dua, nilai nol bersifat tunggal (`0000 0000`).
2. **Kesederhanaan Sirkuit Perangkat Keras:** Pengurangan $A - B$ dapat dieksekusi langsung sebagai penjumlahan $A + (-B)$ dengan rangkaian Adder standar tanpa perlu logika penyesuaian *end-around carry* seperti pada komplemen satu.

### Q2: "Jelaskan perbedaan mendasar antara Rangkaian Logika Kombinasional dan Rangkaian Logika Sekuensial!"
**Jawaban Komprehensif:**
* **Kombinasional:** Output pada suatu waktu *hanya* ditentukan oleh kombinasi nilai input pada waktu yang sama. Rangkaian tidak memiliki elemen penyimpan (*memoryless*) dan tidak memiliki jalur umpan balik (*feedback loop*). Contoh: Half/Full Adder, Multiplexer, Decoder.
* **Sekuensial:** Output tidak hanya ditentukan oleh input saat ini, tetapi juga oleh status/keadaan sistem sebelumnya (*past state*). Memiliki memori berupa Flip-Flop/Latch dan memiliki loop umpan balik tertutup yang dikendalikan pulsa pewaktu (*clock*). Contoh: Counter, Register, Mesin FSM (*Finite State Machine*).

### Q3: "Mengapa gerbang NAND dan NOR disebut sebagai Universal Gates?"
**Jawaban Komprehensif:**
Karena gerbang NAND saja (atau NOR saja) dapat digunakan untuk merekonstruksi ketiga gerbang logika dasar pembentuk aljabar Boolean:
* NOT: Satukan kedua input NAND ($\overline{A \cdot A} = \overline{A}$).
* AND: Sambungkan output NAND ke sebuah NOT-NAND ($\overline{\overline{AB}} = AB$).
* OR: Terapkan hukum De Morgan $\overline{\overline{A} \cdot \overline{B}} = A + B$.
Secara ekonomis pada fabrikasi silikon (CMOS), gerbang NAND memerlukan jumlah transistor lebih sedikit dan memiliki kecepatan propagasi lebih cepat daripada gerbang AND murni.

### Q4: "Jelaskan perbedaan antara Static RAM (SRAM) dan Dynamic RAM (DRAM) serta penggunaannya dalam arsitektur komputer!"
**Jawaban Komprehensif:**
* **SRAM:** Disusun dari 4 hingga 6 transistor (bistable latch per bit). Tidak memerlukan sirkuit penyegar (*refresh cycle*), sangat cepat (akses sub-nanodetik), tetapi ukuran fisiknya besar dan mahal. Digunakan untuk **Cache CPU (L1, L2, L3)**.
* **DRAM:** Disusun dari 1 transistor dan 1 kapasitor (1T-1C per bit). Muatan listrik pada kapasitor mengalami kebocoran seiring waktu sehingga membutuhkan sirkuit refresh secara periodik ribuan kali per detik. Kepadatan bit sangat tinggi dan murah. Digunakan untuk **Memori Utama (RAM sistem)**.
