# Bank Contoh Soal & Pembahasan: Struktur Diskrit

> Sumber rujukan: Bank soal UTS & UAS Struktur Diskrit Departemen Informatika Universitas Diponegoro (Koleksi HMIF 2018–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (HIMPUNAN, RELASI, INDUKSI & KOMBINATORIKA)

### Soal UTS 1: Pembuktian dengan Induksi Matematika (Keterbagian)
**Deskripsi Soal:**
Buktikan menggunakan Induksi Matematika bahwa untuk setiap bilangan bulat positif $n \ge 1$:
$$n^3 + 2n \text{ selalu habis dibagi } 3$$

**Kunci Pembahasan & Solusi:**
Misalkan $P(n)$ adalah proposisi: $n^3 + 2n$ habis dibagi 3 (dapat ditulis $n^3 + 2n = 3m$ untuk suatu $m \in \mathbb{Z}$).

1. **Langkah Basis ($n = 1$):**
   * Substitusikan $n = 1$:
     $$1^3 + 2(1) = 1 + 2 = 3$$
   * Karena $3 = 3 \times 1$, maka $P(1)$ **terbukti benar**.
2. **Langkah Induksi:**
   * **Hipotesis Induksi:** Asumsikan $P(k)$ benar untuk suatu bilangan bulat $k \ge 1$, yaitu:
     $$k^3 + 2k = 3m \quad (\text{untuk suatu } m \in \mathbb{Z})$$
   * **Tujuan Pembuktian:** Harus dibuktikan bahwa $P(k+1)$ juga bernilai benar, yaitu:
     $$(k+1)^3 + 2(k+1) \text{ habis dibagi } 3$$
   * **Ekspansi Aljabar:**
     $$\begin{aligned}
     (k+1)^3 + 2(k+1) &= (k^3 + 3k^2 + 3k + 1) + (2k + 2) \\
     &= (k^3 + 2k) + (3k^2 + 3k + 3)
     \end{aligned}$$
   * Berdasarkan hipotesis induksi, substitusikan $k^3 + 2k = 3m$:
     $$\begin{aligned}
     (k+1)^3 + 2(k+1) &= 3m + 3(k^2 + k + 1) \\
     &= 3 \cdot \big[ m + k^2 + k + 1 \big]
     \end{aligned}$$
   * Karena $m, k \in \mathbb{Z}$, maka $(m + k^2 + k + 1)$ merupakan bilangan bulat.
   * Terbukti bahwa $(k+1)^3 + 2(k+1)$ adalah kelipatan 3 (habis dibagi 3).
3. **Kesimpulan:** Berdasarkan prinsip induksi matematika, $n^3 + 2n$ habis dibagi 3 untuk setiap $n \ge 1$. $\blacksquare$

---

### Soal UTS 2: Prinsip Sarang Merpati (Pigeonhole Principle)
**Deskripsi Soal:**
Di sebuah jurusan Informatika terdapat 100 orang mahasiswa. 
1. Berapa jumlah minimum mahasiswa yang pasti lahir pada bulan yang sama?
2. Jika dipilih sekelompok mahasiswa, berapa jumlah minimum mahasiswa yang harus dipilih secara acak agar kita yakin sedikitnya ada 9 orang yang lahir pada hari yang sama dalam seminggu?

**Kunci Pembahasan & Solusi:**
1. **Kasus Bulan Kelahiran:**
   * Objek / Merpati ($N$) = $100$ mahasiswa.
   * Kotak / Sarang ($k$) = $12$ bulan dalam setahun.
   * Berdasarkan *Generalized Pigeonhole Principle*, jumlah minimum mahasiswa yang lahir pada bulan yang sama adalah:
     $$\left\lceil \frac{N}{k} \right\rceil = \left\lceil \frac{100}{12} \right\rceil = \lceil 8.333 \rceil = \mathbf{9 \text{ mahasiswa}}$$
2. **Kasus Hari Kelahiran (Mencari $N$ dari target kemunculan):**
   * Kotak ($k$) = $7$ hari dalam seminggu (Senin s.d. Minggu).
   * Target: $\lceil N / 7 \rceil = 9$.
   * Kasus terburuk (*worst-case scenario*): Setiap 7 hari masing-masing sudah terisi tepat 8 mahasiswa tanpa ada yang mencapai 9.
     $$\text{Kapasitas maksimal sebelum target tercapai} = 7 \times 8 = 56 \text{ mahasiswa}$$
   * Mahasiswa ke-$(56 + 1)$ yang dipilih dipastikan akan masuk ke salah satu hari dan menjadikannya berisi 9 orang.
   * Jadi, jumlah minimum mahasiswa yang harus dipilih adalah: **$57$ mahasiswa**.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (RELASI REKURENS, TEORI BILANGAN & GRAF)

### Soal UAS 1: Menyelesaikan Relasi Rekurens Homogen Linier
**Deskripsi Soal:**
Selesaikan relasi rekurens homogen linier berikut:
$$a_n = 5a_{n-1} - 6a_{n-2} \quad \text{untuk } n \ge 2$$
dengan kondisi batas nilai awal: $a_0 = 1$ dan $a_1 = 4$.

**Kunci Pembahasan & Solusi:**
1. **Menyusun Persamaan Karakteristik:**
   $$r^2 - 5r + 6 = 0$$
2. **Mencari Akar-Akar Karakteristik:**
   $$(r - 2)(r - 3) = 0 \implies r_1 = 2, \quad r_2 = 3$$
   Kedua akar bernilai riil dan berbeda ($r_1 \ne r_2$).
3. **Bentuk Solusi Umum:**
   $$a_n = \alpha_1 (2)^n + \alpha_2 (3)^n$$
4. **Menghitung Konstanta $\alpha_1$ dan $\alpha_2$ dari Nilai Awal:**
   * Untuk $n = 0$:
     $$a_0 = \alpha_1 (2)^0 + \alpha_2 (3)^0 \implies \alpha_1 + \alpha_2 = 1 \quad \text{...(Persamaan 1)}$$
   * Untuk $n = 1$:
     $$a_1 = \alpha_1 (2)^1 + \alpha_2 (3)^1 \implies 2\alpha_1 + 3\alpha_2 = 4 \quad \text{...(Persamaan 2)}$$
   * Kalikan Persamaan 1 dengan 2: $2\alpha_1 + 2\alpha_2 = 2$.
   * Kurangkan ke Persamaan 2:
     $$(2\alpha_1 + 3\alpha_2) - (2\alpha_1 + 2\alpha_2) = 4 - 2 \implies \mathbf{\alpha_2 = 2}$$
   * Substitusikan ke Persamaan 1:
     $$\alpha_1 + 2 = 1 \implies \mathbf{\alpha_1 = -1}$$
5. **Solusi Eksplisit Akhir:**
   $$a_n = -(2)^n + 2(3)^n = \mathbf{2 \cdot 3^n - 2^n}$$
   *(Verifikasi cepat: $a_0 = 2(1) - 1 = 1$; $a_1 = 2(3) - 2 = 4$; $a_2 = 5(4)-6(1)=14$, via rumus $2(9)-4=14$. Benar!)*

---

### Soal UAS 2: Teori Graf & Rumus Euler Graf Planar
**Deskripsi Soal:**
Sebuah graf terhubung planar sederhana memiliki 10 buah simpul (vertex). Setiap simpul pada graf tersebut memiliki derajat yang sama yaitu 3 (graf 3-reguler / kubik).
1. Berapakah jumlah sisi ($E$) pada graf tersebut?
2. Berapakah jumlah wilayah/muka (*face / region*) yang membagi bidang datar tersebut?
3. Apakah graf tersebut dapat digambar pada bidang datar tanpa ada sisi yang saling berpotongan? Jelaskan pembuktiannya!

**Kunci Pembahasan & Solusi:**
1. **Menghitung Jumlah Sisi ($E$) dengan Handshaking Lemma:**
   $$\sum_{v \in V} \text{deg}(v) = 2|E|$$
   Karena terdapat $V = 10$ simpul dan tiap simpul berderajat 3:
   $$10 \times 3 = 2|E| \implies 30 = 2|E| \implies \mathbf{|E| = 15}$$
2. **Menghitung Jumlah Wilayah ($F$) dengan Rumus Euler:**
   $$V - E + F = 2$$
   Substitusikan $V = 10$ dan $E = 15$:
   $$10 - 15 + F = 2 \implies -5 + F = 2 \implies \mathbf{F = 7 \text{ wilayah}}$$
3. **Pemeriksaan Ketaksamaan Planaritas:**
   * Untuk graf terhubung planar sederhana dengan $V \ge 3$, harus memenuhi syarat:
     $$E \le 3V - 6$$
   * Hitung batas maksimum:
     $$3(10) - 6 = 30 - 6 = 24$$
   * Karena $E = 15 \le 24$, ketaksamaan planaritas terpenuhi. Graf tersebut memang **dapat digambar planar** tanpa perpotongan sisi.

---

### Soal UAS 3: Aritmetika Modular & Invers Modulo untuk Kriptografi
**Deskripsi Soal:**
1. Hitunglah nilai $\gcd(154, 35)$ menggunakan Algoritma Pembagian Euclid!
2. Carilah invers perkalian dari $7 \pmod{26}$, yaitu temukan bilangan bulat $x$ sedemikian rupa sehingga $7x \equiv 1 \pmod{26}$.

**Kunci Pembahasan & Solusi:**
1. **Algoritma Euclid untuk $\gcd(154, 35)$:**
   $$\begin{aligned}
   154 &= 4 \times 35 + 14 \\
   35 &= 2 \times 14 + 7 \\
   14 &= 2 \times 7 + 0
   \end{aligned}$$
   Sisa pembagian terakhir yang bukan nol adalah **$7$**. Jadi, $\gcd(154, 35) = 7$.
2. **Mencari Invers Modulo $7x \equiv 1 \pmod{26}$:**
   * Pertama cek $\gcd(7, 26)$:
     $$26 = 3 \times 7 + 5$$
     $$7 = 1 \times 5 + 2$$
     $$5 = 2 \times 2 + 1 \implies \gcd(7, 26) = 1 \text{ (Invers pasti ada)}$$
   * Mundur menggunakan Substitusi Balik (*Extended Euclidean Algorithm*):
     $$1 = 5 - 2 \times 2$$
     Substitusikan $2 = 7 - 1 \times 5$:
     $$1 = 5 - 2(7 - 5) = 3 \times 5 - 2 \times 7$$
     Substitusikan $5 = 26 - 3 \times 7$:
     $$1 = 3(26 - 3 \times 7) - 2 \times 7 = 3 \times 26 - 11 \times 7$$
   * Tulis dalam bentuk modulo 26:
     $$-11 \times 7 \equiv 1 \pmod{26}$$
   * Ubah $-11$ ke residu positif modulo 26:
     $$-11 \equiv -11 + 26 \equiv \mathbf{15} \pmod{26}$$
   * Periksa: $7 \times 15 = 105$. $105 = 4 \times 26 + 1 = 104 + 1 \equiv 1 \pmod{26}$.
   * Jadi, invers perkalian dari $7 \pmod{26}$ adalah **$15$**.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Buktikan secara matematis mengapa pada sembarang graf tak berarah, jumlah simpul yang berderajat ganjil harus selalu genap!"
**Jawaban Komprehensif:**
Berdasarkan *Handshaking Lemma*:
$$\sum_{v \in V} \text{deg}(v) = 2|E|$$
Karena $2|E|$ selalu bilangan genap untuk sembarang $|E|$, maka jumlah seluruh derajat simpul adalah bilangan genap.
Himpunan simpul $V$ dapat dipartisi menjadi dua subset saling lepas: himpunan simpul berderajat genap ($V_{even}$) dan himpunan simpul berderajat ganjil ($V_{odd}$):
$$\sum_{v \in V_{even}} \text{deg}(v) + \sum_{v \in V_{odd}} \text{deg}(v) = 2|E| \quad (\text{genap})$$
Jumlah derajat simpul genap ($\sum_{v \in V_{even}} \text{deg}(v)$) secara definisi selalu menghasilkan bilangan genap.
Agar persamaan menghasilkan bilangan genap, maka suku kedua ($\sum_{v \in V_{odd}} \text{deg}(v)$) **juga harus menghasilkan bilangan genap**.
Penjumlahan sejumlah bilangan ganjil hanya akan bernilai genap jika dan hanya jika **jumlah sukunya (banyaknya simpul ganjil) adalah genap**. Terbukti.

### Q2: "Apa perbedaan mendasar antara Lintasan Euler (*Eulerian Path*) dan Lintasan Hamilton (*Hamiltonian Path*)? Mengapa pencarian lintasan Hamilton masuk ke kelas kompleksitas NP-Complete sedangkan Euler berorde polinomial $O(E)$?"
**Jawaban Komprehensif:**
* **Lintasan Euler:** Mengunjungi setiap **sisi** (*edge*) tepat satu kali. Syarat keberadaannya dapat diverifikasi secara lokal dalam waktu linier $O(V + E)$ cukup dengan memeriksa derajat simpul (tepat 0 atau 2 simpul ganjil).
* **Lintasan Hamilton:** Mengunjungi setiap **simpul** (*vertex*) tepat satu kali. Tidak ada kriteria lokal derajat sederhana yang dapat menjamin keberadaannya. Algoritma penentuannya harus melakukan penelusuran ruang status kombinatorial (*backtracking/branch-and-bound*), yang menjadikannya masalah optimasi bernilai **NP-Complete**.

### Q3: "Mengapa sebuah pohon (*tree*) dengan $n$ simpul selalu memiliki tepat $n - 1$ buah sisi? Bagaimana membuktikannya?"
**Jawaban Komprehensif:**
Dapat dibuktikan dengan **Induksi Matematika** pada jumlah simpul $n$:
* **Basis ($n = 1$):** Graf dengan 1 simpul dan tidak ada sisi memiliki $|E| = 0 = 1 - 1$. Terbukti.
* **Langkah Induksi:** Asumsikan setiap pohon dengan $k$ simpul memiliki $k - 1$ sisi. Untuk pohon dengan $k + 1$ simpul: pohon asiklik terhubung selalu memiliki minimal dua simpul berderajat 1 (daun/leaf). Jika satu daun beserta sisi penghubungnya dihilangkan, graf yang tersisa tetap terhubung dan asiklik (merupakan pohon berukuran $k$). Berdasarkan hipotesis induksi, pohon sisa memiliki $k - 1$ sisi. Ketika daun dan 1 sisinya dikembalikan, jumlah total sisi menjadi $(k - 1) + 1 = k = (k + 1) - 1$. Terbukti.
