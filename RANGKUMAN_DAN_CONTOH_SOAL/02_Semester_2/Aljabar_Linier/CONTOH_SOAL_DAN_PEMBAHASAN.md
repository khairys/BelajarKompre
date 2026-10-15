# Bank Contoh Soal & Pembahasan: Aljabar Linier

> Sumber rujukan: Bank soal UTS & UAS Aljabar Linier Departemen Informatika Universitas Diponegoro (Koleksi HMIF 2020–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (SPL, GAUSS-JORDAN, DETERMINAN & INVERS)

### Soal UTS 1: Sistem Persamaan Linier via Eliminasi Gauss-Jordan
**Deskripsi Soal:**
Selesaikan sistem persamaan linier (SPL) berikut menggunakan metode **Eliminasi Gauss-Jordan** (mengubah matriks terdamping menjadi bentuk eselon baris tereduksi):
$$\begin{aligned}
x_1 + 2x_2 + 3x_3 &= 9 \\
2x_1 - x_2 + x_3 &= 8 \\
3x_1 - x_2 - x_3 &= 3
\end{aligned}$$

**Kunci Pembahasan & Solusi:**
1. **Bentuk Matriks Terdamping (*Augmented Matrix*):**
   $$\left[ \begin{array}{ccc|c} 
   1 & 2 & 3 & 9 \\ 
   2 & -1 & 1 & 8 \\ 
   3 & -1 & -1 & 3 
   \end{array} \right]$$
2. **Langkah 1: Buat nol pada kolom 1 di bawah satu utama baris 1:**
   * $R_2 \leftarrow R_2 - 2R_1$:
     $$[2 - 2(1), \; -1 - 2(2), \; 1 - 2(3) \mid 8 - 2(9)] = [0, \; -5, \; -5 \mid -10]$$
   * $R_3 \leftarrow R_3 - 3R_1$:
     $$[3 - 3(1), \; -1 - 3(2), \; -1 - 3(3) \mid 3 - 3(9)] = [0, \; -7, \; -10 \mid -24]$$
   Matriks menjadi:
   $$\left[ \begin{array}{ccc|c} 
   1 & 2 & 3 & 9 \\ 
   0 & -5 & -5 & -10 \\ 
   0 & -7 & -10 & -24 
   \end{array} \right]$$
3. **Langkah 2: Buat satu utama pada baris 2:**
   * $R_2 \leftarrow -\frac{1}{5} R_2$:
     $$[0, \; 1, \; 1 \mid 2]$$
   Matriks menjadi:
   $$\left[ \begin{array}{ccc|c} 
   1 & 2 & 3 & 9 \\ 
   0 & 1 & 1 & 2 \\ 
   0 & -7 & -10 & -24 
   \end{array} \right]$$
4. **Langkah 3: Nolkan elemen kolom 2 pada baris 1 dan baris 3:**
   * $R_1 \leftarrow R_1 - 2R_2$:
     $$[1 - 0, \; 2 - 2(1), \; 3 - 2(1) \mid 9 - 2(2)] = [1, \; 0, \; 1 \mid 5]$$
   * $R_3 \leftarrow R_3 + 7R_2$:
     $$[0, \; -7 + 7(1), \; -10 + 7(1) \mid -24 + 7(2)] = [0, \; 0, \; -3 \mid -10]$$
     *Tunggu, periksa perhitungan:* $-24 + 14 = -10$.
     Maka $-3x_3 = -10 \implies x_3 = \frac{10}{3}$.
   * Mari buat satu utama di $R_3$: $R_3 \leftarrow -\frac{1}{3} R_3 \implies [0, \; 0, \; 1 \mid \frac{10}{3}]$.
5. **Langkah 4: Nolkan kolom 3 pada baris 1 dan baris 2 (Gauss-Jordan):**
   * $R_1 \leftarrow R_1 - R_3 \implies [1, \; 0, \; 0 \mid 5 - \frac{10}{3} = \frac{5}{3}]$
   * $R_2 \leftarrow R_2 - R_3 \implies [0, \; 1, \; 0 \mid 2 - \frac{10}{3} = -\frac{4}{3}]$
6. **Solusi Akhir:**
   $$\mathbf{x_1 = \frac{5}{3}, \quad x_2 = -\frac{4}{3}, \quad x_3 = \frac{10}{3}}$$
   *(Verifikasi baris 1: $\frac{5}{3} + 2(-\frac{4}{3}) + 3(\frac{10}{3}) = \frac{5 - 8 + 30}{3} = \frac{27}{3} = 9$. Cocok!)*

---

### Soal UTS 2: Invers Matriks Menggunakan Metode Partisi $[A \mid I]$
**Deskripsi Soal:**
Tentukan invers dari matriks $A$ berikut:
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{bmatrix}$$

**Kunci Pembahasan & Solusi:**
1. **Bentuk Matriks Partisi $[A \mid I]$:**
   $$\left[ \begin{array}{ccc|ccc} 
   1 & 2 & 3 & 1 & 0 & 0 \\ 
   0 & 1 & 4 & 0 & 1 & 0 \\ 
   5 & 6 & 0 & 0 & 0 & 1 
   \end{array} \right]$$
2. **OBE Tahap 1:** $R_3 \leftarrow R_3 - 5R_1$:
   $$\left[ \begin{array}{ccc|ccc} 
   1 & 2 & 3 & 1 & 0 & 0 \\ 
   0 & 1 & 4 & 0 & 1 & 0 \\ 
   0 & -4 & -15 & -5 & 0 & 1 
   \end{array} \right]$$
3. **OBE Tahap 2:** $R_3 \leftarrow R_3 + 4R_2$:
   $$\left[ \begin{array}{ccc|ccc} 
   1 & 2 & 3 & 1 & 0 & 0 \\ 
   0 & 1 & 4 & 0 & 1 & 0 \\ 
   0 & 0 & 1 & -5 & 4 & 1 
   \end{array} \right]$$
4. **OBE Tahap 3 (Reduksi Balik dari Kolom 3):**
   * $R_2 \leftarrow R_2 - 4R_3$:
     $$[0, \; 1, \; 0 \mid 0 - 4(-5), \; 1 - 4(4), \; 0 - 4(1)] = [0, \; 1, \; 0 \mid 20, \; -15, \; -4]$$
   * $R_1 \leftarrow R_1 - 3R_3$:
     $$[1, \; 2, \; 0 \mid 1 - 3(-5), \; 0 - 3(4), \; 0 - 3(1)] = [1, \; 2, \; 0 \mid 16, \; -12, \; -3]$$
5. **OBE Tahap 4 (Nolkan Kolom 2 pada Baris 1):**
   * $R_1 \leftarrow R_1 - 2R_2$:
     $$[1, \; 0, \; 0 \mid 16 - 2(20), \; -12 - 2(-15), \; -3 - 2(-4)] = [1, \; 0, \; 0 \mid -24, \; 18, \; 5]$$
6. **Hasil Invers Matriks $A^{-1}$:**
   $$\mathbf{A^{-1} = \begin{bmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{bmatrix}}$$

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (RUANG VEKTOR, NILAI EIGEN & DIAGONALISASI)

### Soal UAS 1: Uji Bebas Linier & Basis Ruang Vektor $\mathbb{R}^3$
**Deskripsi Soal:**
Diberikan tiga vektor di $\mathbb{R}^3$:
$$\mathbf{v}_1 = (1, 2, 3), \quad \mathbf{v}_2 = (0, 1, 2), \quad \mathbf{v}_3 = (0, 0, 1)$$
Buktikan apakah himpunan $S = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ bebas linier dan apakah $S$ membentuk basis untuk $\mathbb{R}^3$!

**Kunci Pembahasan & Solusi:**
1. **Pengujian Bebas Linier:**
   Bentuk kombinasi linier bernilai nol:
   $$c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + c_3 \mathbf{v}_3 = \mathbf{0}$$
   $$c_1 \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} + c_2 \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} + c_3 \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
2. **Bentuk Matriks Kolom:**
   $$A = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 2 & 1 \end{bmatrix}$$
   Matriks ini adalah matriks segitiga bawah. Determinan matriks segitiga adalah hasil kali elemen diagonal utamanya:
   $$\det(A) = 1 \times 1 \times 1 = 1 \ne 0$$
3. **Kesimpulan Bebas Linier & Basis:**
   * Karena $\det(A) \ne 0$, maka satu-satunya solusi sistem adalah solusi trivial $c_1 = c_2 = c_3 = 0$. Dengan demikian, himpunan $S$ **Bebas Linier**.
   * Karena $S$ terdiri dari 3 vektor bebas linier di ruang vektor $\mathbb{R}^3$ yang berdimensi 3 ($\dim(\mathbb{R}^3) = 3$), maka berdasarkan teorema dimensi, himpunan $S$ secara otomatis merentang $\mathbb{R}^3$ dan **terbukti membentuk sebuah Basis untuk $\mathbb{R}^3$**.

---

### Soal UAS 2: Nilai Eigen, Vektor Eigen & Diagonalisasi Matriks
**Deskripsi Soal:**
Diberikan matriks $A$:
$$A = \begin{bmatrix} 4 & -2 \\ 1 & 1 \end{bmatrix}$$
1. Tentukan seluruh nilai eigen ($\lambda$) dari matriks $A$.
2. Tentukan vektor-vektor eigen yang bersesuaian dengan setiap nilai eigen tersebut.
3. Carilah matriks pendiagonal $P$ dan matriks diagonal $D$ sedemikian rupa sehingga $P^{-1} A P = D$.

**Kunci Pembahasan & Solusi:**
1. **Persamaan Karakteristik $\det(\lambda I - A) = 0$:**
   $$\det \begin{bmatrix} \lambda - 4 & 2 \\ -1 & \lambda - 1 \end{bmatrix} = 0$$
   $$(\lambda - 4)(\lambda - 1) - (2)(-1) = 0$$
   $$\lambda^2 - 5\lambda + 4 + 2 = 0 \implies \lambda^2 - 5\lambda + 6 = 0$$
   $$(\lambda - 2)(\lambda - 3) = 0$$
   Diperoleh dua nilai eigen yang berbeda: **$\lambda_1 = 2$** dan **$\lambda_2 = 3$**.
2. **Mencari Vektor Eigen untuk $\lambda_1 = 2$:**
   Selesaikan sistem homogen $(2I - A)\mathbf{x} = \mathbf{0}$:
   $$\begin{bmatrix} -2 & 2 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
   Dari baris 1: $-2x_1 + 2x_2 = 0 \implies x_1 = x_2$.
   Pilih parameter bebas $x_2 = 1 \implies \mathbf{p}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
3. **Mencari Vektor Eigen untuk $\lambda_2 = 3$:**
   Selesaikan sistem homogen $(3I - A)\mathbf{x} = \mathbf{0}$:
   $$\begin{bmatrix} -1 & 2 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
   Dari baris 1: $-x_1 + 2x_2 = 0 \implies x_1 = 2x_2$.
   Pilih parameter bebas $x_2 = 1 \implies \mathbf{p}_2 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$.
4. **Membentuk Matriks $P$ dan $D$:**
   * Matriks $P$ dibentuk dari vektor-vektor eigen sebagai kolom:
     $$\mathbf{P = \begin{bmatrix} 1 & 2 \\ 1 & 1 \end{bmatrix}}$$
   * Matriks diagonal $D$ memuat nilai-nilai eigen pada diagonal utama:
     $$\mathbf{D = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}}$$
   * Karena kedua nilai eigen berbeda, vektor eigen pasti bebas linier, sehingga matriks $A$ **terbukti dapat didiagonalisasi** ($P^{-1}AP = D$).

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan makna geometris dari Vektor Eigen dan Nilai Eigen!"
**Jawaban Komprehensif:**
Ketika suatu matriks transformasi linier $A$ diterapkan pada sembarang vektor $\mathbf{x}$, umumnya vektor tersebut akan mengalami rotasi (perubahan arah) sekaligus penskalaan (perubahan panjang).
Namun, **vektor eigen** adalah vektor istimewa yang arah orientasinya **tidak berubah sama sekali** setelah dikenai transformasi linier oleh matriks $A$; vektor tersebut hanya mengalami peregangan atau pemendekan sejajar garis asalnya.
Faktor pengali kelipatan panjang peregangan/pemendekan tersebut adalah **nilai eigen ($\lambda$)** ($A\mathbf{x} = \lambda \mathbf{x}$). Jika $\lambda > 1$ vektor memanjang, jika $0 < \lambda < 1$ memendek, dan jika $\lambda < 0$ arahnya berbalik $180^\circ$.

### Q2: "Mengapa konsep Dekomposisi Nilai Eigen / SVD sangat penting dalam algoritma Principal Component Analysis (PCA) pada Data Science?"
**Jawaban Komprehensif:**
Dalam sains data, dataset berdimensi sangat tinggi sering kali memuat korelasi antar-fitur (*multicollinearity*) dan derau (*noise*).
Algoritma PCA:
1. Menghitung matriks kovarians data $\Sigma$.
2. Menghitung nilai eigen dan vektor eigen dari $\Sigma$.
3. **Vektor eigen** mewakili sumbu-sumbu koordinat baru (*Principal Components*) yang saling ortogonal (bebas korelasi).
4. **Nilai eigen** yang bersesuaian mencerminkan seberapa besar varians informasi data yang berhasil ditangkap oleh sumbu tersebut.
Dengan memilih $k$ vektor eigen yang memiliki nilai eigen terbesar, kita dapat memproyeksikan data ribuan dimensi ke hanya beberapa dimensi utama dengan mempertahankan mayoritas varians informasi penting data asli.
