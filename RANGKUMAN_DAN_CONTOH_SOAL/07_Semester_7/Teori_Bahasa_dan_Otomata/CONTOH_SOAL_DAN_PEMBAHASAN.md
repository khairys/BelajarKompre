# Bank Contoh Soal & Pembahasan: Teori Bahasa dan Otomata

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Teori Bahasa dan Otomata Departemen Informatika Universitas Diponegoro (Koleksi Pengampu & Bank Soal HMIF 2018–2023).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (KONVERSI NFA KE DFA, MINIMASI & PUMPING LEMMA)

### Soal UTS 1: Konversi NFA ke DFA Menggunakan Algoritma Konstruksi Subset (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan sebuah Non-Deterministic Finite Automata (NFA) $M = (Q, \Sigma, \delta, q_0, F)$ dengan:
* $Q = \{ q_0, q_1, q_2 \}$
* $\Sigma = \{ 0, 1 \}$
* Status Awal $= q_0$
* Status Akhir $F = \{ q_2 \}$
* Tabel Fungsi Transisi $\delta$:

| Status ($q$) | Masukan $0$ | Masukan $1$ |
|:---:|:---:|:---:|
| $\rightarrow \mathbf{q_0}$ | $\{ q_0, q_1 \}$ | $\{ q_0 \}$ |
| $\mathbf{q_1}$ | $\emptyset$ | $\{ q_2 \}$ |
| $* \mathbf{q_2}$ | $\emptyset$ | $\emptyset$ |

*(NFA ini menerima semua string biner yang berakhiran substring `"01"`).*
**Tugas:**
Konversikan NFA di atas menjadi **Deterministic Finite Automata (DFA)** yang ekuivalen menggunakan **Algoritma Konstruksi Subset (*Subset Construction*)**! Tentukan tabel transisi DFA baru, himpunan status penerima (*Final States*), dan gambarkan diagram transisinya!

**Kunci Pembahasan & Solusi:**
1. **Langkah-Langkah Konstruksi Subset:**
   * **Status Awal DFA:**
     $$A = [q_0]$$
   * **Transisi dari Status $A [q_0]$:**
     * $\delta'(A, 0) = \delta(q_0, 0) = \{ q_0, q_1 \} \implies$ Status Baru **$B [q_0, q_1]$**.
     * $\delta'(A, 1) = \delta(q_0, 1) = \{ q_0 \} \implies$ Status **$A [q_0]$**.
   * **Transisi dari Status $B [q_0, q_1]$:**
     * $\delta'(B, 0) = \delta(q_0, 0) \cup \delta(q_1, 0) = \{ q_0, q_1 \} \cup \emptyset = \{ q_0, q_1 \} \implies$ Status **$B [q_0, q_1]$**.
     * $\delta'(B, 1) = \delta(q_0, 1) \cup \delta(q_1, 1) = \{ q_0 \} \cup \{ q_2 \} = \{ q_0, q_2 \} \implies$ Status Baru **$C [q_0, q_2]$**.
   * **Transisi dari Status $C [q_0, q_2]$:**
     * $\delta'(C, 0) = \delta(q_0, 0) \cup \delta(q_2, 0) = \{ q_0, q_1 \} \cup \emptyset = \{ q_0, q_1 \} \implies$ Status **$B [q_0, q_1]$**.
     * $\delta'(C, 1) = \delta(q_0, 1) \cup \delta(q_2, 1) = \{ q_0 \} \cup \emptyset = \{ q_0 \} \implies$ Status **$A [q_0]$**.
   * Tidak ada status baru yang terbentuk. Proses selesai.

2. **Tabel Transisi DFA Hasil Konversi:**

| Status DFA | Himpunan Elemen NFA | Masukan $0$ | Masukan $1$ | Status Akhir? |
|:---:|:---:|:---:|:---:|:---:|
| $\rightarrow \mathbf{A}$ | $\{ q_0 \}$ | $B$ | $A$ | Bukan |
| $\mathbf{B}$ | $\{ q_0, q_1 \}$ | $B$ | $C$ | Bukan |
| $* \mathbf{C}$ | $\{ q_0, q_2 \}$ | $B$ | $A$ | **FINAL STATE (karena memuat $q_2$)** |

3. **Verifikasi:**
   * String `"01"`: $A \xrightarrow{0} B \xrightarrow{1} C$ (Diterima / Valid!).
   * String `"1001"`: $A \xrightarrow{1} A \xrightarrow{0} B \xrightarrow{0} B \xrightarrow{1} C$ (Diterima / Valid!).
   * String `"010"`: $A \xrightarrow{0} B \xrightarrow{1} C \xrightarrow{0} B$ (Bukan Final State $\implies$ Ditolak / Valid!).

---

### Soal UTS 2: Pembuktian Bahasa Non-Reguler Menggunakan Pumping Lemma
**Deskripsi Soal:**
Buktikan secara formal menggunakan **Pumping Lemma** bahwa bahasa:
$$L = \{ 0^n 1^n \mid n \ge 0 \}$$
**BUKAN merupakan bahasa reguler!**

**Kunci Pembahasan & Solusi:**
Pembuktian dilakukan menggunakan metode kontradiksi (*Proof by Contradiction*):
1. **Asumsi Awal:** Asumsikan bahwa $L$ adalah bahasa reguler.
2. **Ketetapan Pumping Lemma:** Berdasarkan Pumping Lemma, harus ada konstanta panjang pemompaan integer $p \ge 1$.
3. **Pemilihan String $w$:**
   Pilih sebuah string $w \in L$ dengan panjang $\ge p$:
   $$w = 0^p 1^p$$
   (Panjang $|w| = 2p \ge p$). Jelas bahwa $w$ adalah anggota sah bahasa $L$.
4. **Pembagian Tiga Bagian ($w = xyz$):**
   Kondisi Pumping Lemma mensyaratkan:
   * $|xy| \le p$
   * $|y| \ge 1$ (panjang $y > 0$)
   Karena $|xy| \le p$, maka sub-string $xy$ **secara mutlak seluruhnya hanya terdiri dari simbol angka $0$**.
   Dengan demikian, bagian $y$ pasti berbentuk:
   $$y = 0^k \quad \text{untuk suatu integer } 1 \le k \le p$$
   Sehingga dekomposisinya adalah: $x = 0^{p - k - m}, \; y = 0^k, \; z = 0^m 1^p$.
5. **Pemompaan Kasus (*Pumping Step*):**
   Pumping Lemma menyatakan bahwa untuk SETIAP integer $i \ge 0$, string terpompa $w' = x y^i z$ harus tetap berada di dalam bahasa $L$ ($w' \in L$).
   Mari kita uji untuk nilai **$i = 2$** (atau $i = 0$):
   $$w' = x y^2 z = x y y z$$
   Karena kita menduplikasi $y = 0^k$, maka jumlah angka $0$ bertambah sebanyak $k$ buah:
   $$w' = 0^{p+k} 1^p$$
   Karena $k \ge 1$, maka jumlah angka $0$ ($p+k$) **TIDAK SAMA** dengan jumlah angka $1$ ($p$):
   $$p + k \ne p$$
   Dengan demikian:
   $$\mathbf{w' \notin L}$$
6. **Kesimpulan Kontradiksi:**
   Hasil $w' \notin L$ bertentangan (*kontradiksi*) dengan premis dasar Pumping Lemma.
   Oleh karena itu, asumsi awal bahwa $L$ adalah bahasa reguler terbukti SALAH.
   **Terbukti secara sah bahwa $L = \{ 0^n 1^n \mid n \ge 0 \}$ BUKAN BAHASA REGULER.**

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (AMBIGUITAS CFG, CNF & MESIN TURING)

### Soal UAS 1: Pembuktian Ambiguitas Context-Free Grammar (CFG)
**Deskripsi Soal:**
Diberikan tata bahasa bebas konteks (*CFG*) $G$ untuk ekspresi aritmetika dengan aturan produksi:
$$E \to E + E \mid E \times E \mid id$$
Buktikan bahwa tata bahasa $G$ tersebut bersifat **AMBIGU (*Ambiguous*)** untuk string masukan:
$$\mathbf{w = id + id \times id}$$

**Kunci Pembahasan & Solusi:**
Suatu CFG terbukti ambigu jika terdapat minimal satu string yang memiliki minimal **dua Pohon Parse (*Parse Trees*) yang berbeda secara struktural**:
* **Pohon Parse 1 (Mengutamakan Perkalian Lebih Dulu):**
  * Derivasi Paling Kiri:
    $$E \implies E + E \implies id + E \implies id + E \times E \implies id + id \times E \implies id + id \times id$$
  * Struktur Pohon: Simpul akar adalah operator `+`. Sub-pohon kiri menghasilkan `id`. Sub-pohon kanan memuat cabang perkalian `E * E`.
  * Makna Semantik: $id + (id \times id)$.
* **Pohon Parse 2 (Mengutamakan Penjumlahan Lebih Dulu):**
  * Derivasi Paling Kiri Alternatif:
    $$E \implies E \times E \implies E + E \times E \implies id + E \times E \implies id + id \times E \implies id + id \times id$$
  * Struktur Pohon: Simpul akar adalah operator `*`. Sub-pohon kiri memuat cabang penjumlahan `E + E`. Sub-pohon kanan menghasilkan `id`.
  * Makna Semantik: $(id + id) \times id$.

*Kesimpulan:* Karena string $id + id \times id$ memiliki **dua pohon parse yang berbeda secara sintaksis dan menghasilkan semantik prioritas operator yang bertentangan**, maka terbukti mutlak bahwa tata bahasa $G$ bersifat **AMBIGU**.

---

### Soal UAS 2: Perancangan Transisi Mesin Turing untuk Bahasa $L = \{a^n b^n \mid n \ge 1\}$
**Deskripsi Soal:**
Rancanglah logika kerja dan tabel transisi sebuah **Mesin Turing (Turing Machine)** satu pita yang menerima bahasa:
$$L = \{ a^n b^n \mid n \ge 1 \}$$
(String diawali sejumlah simbol $a$ dan diikuti oleh simbol $b$ dalam jumlah yang tepat sama, diakhiri simbol kosong / blank $B$).

**Kunci Pembahasan & Solusi:**
1. **Strategi Algoritma Pencocokan Pita:**
   * Status $q_0$: Cari simbol $a$ paling kiri yang belum ditandai, ubah $a$ menjadi penanda $X$, lalu bergerak ke kanan ($R$) beralih ke status $q_1$.
   * Status $q_1$: Lewati semua simbol $a$ dan $Y$ hingga menemukan simbol $b$ pertama yang belum ditandai.
   * Saat menemukan $b$, ubah $b$ menjadi penanda $Y$, lalu bergerak ke kiri ($L$) beralih ke status $q_2$.
   * Status $q_2$: Bergerak mundur ke kiri melewati semua $Y$ dan $a$ hingga membentur penanda $X$, lalu geser satu langkah ke kanan ($R$) dan kembali ke status $q_0$ untuk mencari pasangan berikutnya.
   * Jika pada status $q_0$ membaca simbol $Y$ (semua $a$ telah habis ditandai menjadi $X$), beralih ke status $q_3$ untuk memverifikasi apakah masih ada simbol $b$ yang tersisa. Jika hanya tersisa simbol $Y$ dan membentur blank $B$, mesin berpindah ke status penerima **$q_4$ (Accept / HALT)**.

2. **Tabel Fungsi Transisi $\delta(q, \text{simbol}) = (\text{status baru}, \text{tulis simbol}, \text{arah gerak})$:**

| Status Saat Ini | Membaca '$a$' | Membaca '$b$' | Membaca '$X$' | Membaca '$Y$' | Membaca '$B$' (Blank) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\rightarrow \mathbf{q_0}$ | $(q_1, X, R)$ | - | - | $(q_3, Y, R)$ | - |
| $\mathbf{q_1}$ | $(q_1, a, R)$ | $(q_2, Y, L)$ | - | $(q_1, Y, R)$ | - |
| $\mathbf{q_2}$ | $(q_2, a, L)$ | - | $(q_0, X, R)$ | $(q_2, Y, L)$ | - |
| $\mathbf{q_3}$ | - | - | - | $(q_3, Y, R)$ | $* (q_4, B, R)$ (ACCEPT) |
| $* \mathbf{q_4}$ | - | - | - | - | - |

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa Finite State Automata (FSA) tidak mampu mengenali bahasa palindrom atau bahasa bersarang seperti pengecekan tanda kurung seimbang ((), (())), sedangkan Pushdown Automata (PDA) mampu?"
**Jawaban Komprehensif:**
* **Keterbatasan Memori FSA:** Finite State Automata hanya memiliki memori internal berupa sejumlah status berhingga (*finite states*) tanpa memori eksternal tambahan. Untuk memeriksa tanda kurung seimbang atau bahasa berpasangan $0^n 1^n$, mesin harus "menghitung" berapa banyak tanda kurung buka yang telah masuk agar dapat mencocokkannya dengan tanda kurung tutup. Karena panjang string bisa tak berhingga ($n \to \infty$), FSA akan membutuhkan jumlah status tak berhingga, yang melanggar definisi *finite*.
* **Keunggulan PDA:** Pushdown Automata dilengkapi dengan **satu struktur data memori tumpukan (*Stack: LIFO*)** dengan kapasitas kedalaman tak terbatas. Setiap kali membaca tanda kurung buka `(`, PDA melakukan operasi **Push** simbol ke dalam stack; dan setiap kali membaca tanda kurung tutup `)`, PDA melakukan operasi **Pop** dari stack. Jika pada akhir string stack tepat kosong (*empty stack*) dan berada pada status penerima, maka string dinyatakan valid seimbang secara deterministik.

### Q2: "Jelaskan apa itu The Halting Problem yang dirumuskan oleh Alan Turing, dan apa implikasi filosofis terbesarnya terhadap batasan kemampuan komputer modern?"
**Jawaban Komprehensif:**
* **Definisi Halting Problem:** Masalah keputusan (*Decision Problem*) untuk menentukan: *"Diberikan deskripsi sembarang program komputer $P$ dan masukan $I$, apakah program $P$ tersebut pada akhirnya akan berhenti (*halt*) atau akan berjalan terus menerus selamanya dalam loop tak berhingga (*infinite loop*)?"*
* **Bukti Turing:** Menggunakan teknik diagonalisasi Cantor dan penalaran kontradiksi (*Self-referential Paradox*), Alan Turing membuktikan secara matematis bahwa **mustahil ada satu algoritma universal yang dapat menyelesaikan Halting Problem dengan benar untuk seluruh kemungkinan program**.
* **Implikasi Filosofis & Komputasi Terbesar:**
  1. Membuktikan bahwa **komputer tidak mahakuasa**. Terdapat batasan matematis intrinsik di alam semesta mengenai apa yang dapat dihitung (*Computable*) dan apa yang tidak dapat dihitung (*Uncomputable / Undecidable*).
  2. Dalam rekayasa perangkat lunak praktis, hal ini membuktikan bahwa kita tidak akan pernah bisa membuat sebuah compiler atau software debugger otomatis yang 100% sempurna mampu mendeteksi apakah setiap kode program bebas dari infinite loop atau deadlock sebelum program tersebut dieksekusi nyata.
