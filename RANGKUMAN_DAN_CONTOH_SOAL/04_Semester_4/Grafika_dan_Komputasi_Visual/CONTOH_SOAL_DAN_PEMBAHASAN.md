# Bank Contoh Soal & Pembahasan: Grafika dan Komputasi Visual

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Grafika dan Komputasi Visual Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Dr. Aris Sugiharto, S.Si., M.Kom., Rismiyati, B.Eng., M.Cs., dkk. & Bank Soal HMIF 2018–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (ALGORITMA PRIMITIF 2D, TRANSFORMASI & CLIPPING)

### Soal UTS 1: Algoritma Pembentukan Garis Bresenham (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan dua buah titik ujung segmen garis pada koordinat piksel layar: $A(2, 3)$ dan $B(10, 8)$.
1. Hitung nilai gradien garis $m$ dan tentukan kasus pergeseran piksel yang berlaku!
2. Tentukan parameter keputusan awal $p_0$!
3. Hitung tabel penentuan piksel $(x_k, y_k)$ yang dinyalakan dari titik $A$ sampai titik $B$ menggunakan **Algoritma Garis Bresenham** secara terperinci!

**Kunci Pembahasan & Solusi:**
1. **Analisis Gradien ($m$):**
   * $\Delta x = x_2 - x_1 = 10 - 2 = 8$
   * $\Delta y = y_2 - y_1 = 8 - 3 = 5$
   * Gradien $m = \frac{\Delta y}{\Delta x} = \frac{5}{8} = 0.625$.
   * Karena $0 < m < 1$, maka garis termasuk ke dalam **Kasus 1**: Penambahan selalu terjadi pada sumbu $x$ ($x_{k+1} = x_k + 1$), sedangkan sumbu $y$ dapat bernilai tetap ($y_{k+1} = y_k$) atau naik satu piksel ($y_{k+1} = y_k + 1$).

2. **Inisialisasi Konstanta:**
   * $2\Delta y = 2(5) = 10$
   * $2\Delta y - 2\Delta x = 2(5) - 2(8) = 10 - 16 = -6$
   * Parameter keputusan awal:
     $$p_0 = 2\Delta y - \Delta x = 10 - 8 = 2$$

3. **Tabel Iterasi Penentuan Piksel:**

| $k$ | $p_k$ | $(x_{k+1}, y_{k+1})$ | Perhitungan $p_{k+1}$ |
|:---:|:---:|:---:|:---|
| Inisial | - | $(2, 3)$ (Titik Awal) | $p_0 = 2$ |
| 0 | $2 \ge 0$ | $(3, 4)$ | $p_1 = p_0 + (2\Delta y - 2\Delta x) = 2 + (-6) = -4$ |
| 1 | $-4 < 0$ | $(4, 4)$ | $p_2 = p_1 + 2\Delta y = -4 + 10 = 6$ |
| 2 | $6 \ge 0$ | $(5, 5)$ | $p_3 = p_2 + (-6) = 6 - 6 = 0$ |
| 3 | $0 \ge 0$ | $(6, 6)$ | $p_4 = p_3 + (-6) = 0 - 6 = -6$ |
| 4 | $-6 < 0$ | $(7, 6)$ | $p_5 = p_4 + 2\Delta y = -6 + 10 = 4$ |
| 5 | $4 \ge 0$ | $(8, 7)$ | $p_6 = p_5 + (-6) = 4 - 6 = -2$ |
| 6 | $-2 < 0$ | $(9, 7)$ | $p_7 = p_6 + 2\Delta y = -2 + 10 = 8$ |
| 7 | $8 \ge 0$ | $(10, 8)$ (Titik Akhir) | Selesai |

*Piksel yang diplot pada frame buffer:* $(2,3), (3,4), (4,4), (5,5), (6,6), (7,6), (8,7), (9,7), (10,8)$.

---

### Soal UTS 2: Transformasi Geometri 2D Komposit terhadap Titik Pusat Sembarang
**Deskripsi Soal:**
Sebuah segitiga $PQR$ memiliki koordinat titik sudut: $P(3, 2)$, $Q(7, 2)$, dan $R(5, 6)$.
Segitiga tersebut dirotasikan sebesar $90^\circ$ berlawanan arah jarum jam ($\theta = 90^\circ$) dengan titik pusat rotasi pada titik **$P(3, 2)$**, kemudian dilanjutkan dengan translasi sejauh vektor $T = (4, -2)$.
1. Susunlah matriks transformasi komposit homogen $M_{\text{total}}$!
2. Hitung posisi koordinat baru dari ketiga simpul segitiga tersebut ($P', Q', R'$)!

**Kunci Pembahasan & Solusi:**
1. **Penyusunan Matriks Komposit Homogen:**
   Rotasi terhadap titik pusat sembarang $(x_p, y_p) = (3, 2)$ memerlukan 3 tahap, kemudian digabung dengan translasi akhir $T$:
   $$M_{\text{total}} = T_{\text{akhir}} \cdot T(x_p, y_p) \cdot R(90^\circ) \cdot T(-x_p, -y_p)$$
   
   Karena $T_{\text{akhir}}$ dan translasi balik $T(3, 2)$ sama-sama merupakan translasi murni, keduanya dapat digabung menjadi translasi akumulatif $T(3+4, 2+(-2)) = T(7, 0)$:
   * Matriks Translasi Mundur $T(-3, -2)$:
     $$T_1 = \begin{bmatrix} 1 & 0 & -3 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{bmatrix}$$
   * Matriks Rotasi $R(90^\circ)$ ($\cos 90^\circ = 0, \sin 90^\circ = 1$):
     $$R = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
   * Matriks Translasi Maju + Akhir $T(7, 0)$:
     $$T_2 = \begin{bmatrix} 1 & 0 & 7 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
   * Perkalian Matriks Komposit:
     $$M_{\text{total}} = \begin{bmatrix} 1 & 0 & 7 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & -3 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 9 \\ 1 & 0 & -3 \\ 0 & 0 & 1 \end{bmatrix}$$

2. **Perhitungan Simpul Baru:**
   * **Simpul $P(3, 2)$:**
     $$\begin{bmatrix} x_P' \\ y_P' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 9 \\ 1 & 0 & -3 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 0(3) - 1(2) + 9 \\ 1(3) + 0(2) - 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 7 \\ 0 \\ 1 \end{bmatrix} \implies \mathbf{P'(7, 0)}$$
   * **Simpul $Q(7, 2)$:**
     $$\begin{bmatrix} x_Q' \\ y_Q' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 9 \\ 1 & 0 & -3 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 7 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 - 2 + 9 \\ 7 + 0 - 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 7 \\ 4 \\ 1 \end{bmatrix} \implies \mathbf{Q'(7, 4)}$$
   * **Simpul $R(5, 6)$:**
     $$\begin{bmatrix} x_R' \\ y_R' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & -1 & 9 \\ 1 & 0 & -3 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 5 \\ 6 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 - 6 + 9 \\ 5 + 0 - 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix} \implies \mathbf{R'(3, 2)}$$

---

### Soal UTS 3: Algoritma Pemotongan Garis Cohen-Sutherland
**Deskripsi Soal:**
Diberikan batas jendela pemotongan persegi panjang (*clipping window*):
$$x_{\min} = 2, \quad x_{\max} = 8, \quad y_{\min} = 3, \quad y_{\max} = 7$$
Terdapat dua segmen garis:
* Garis 1: $P_1(3, 4)$ ke $P_2(7, 6)$
* Garis 2: $Q_1(0, 5)$ ke $Q_2(10, 5)$
* Garis 3: $R_1(1, 8)$ ke $R_2(6, 9)$

Tentukan status kliping (*Trivial Accept*, *Trivial Reject*, atau *Perlu Pemotongan*) menggunakan kode biner wilayah (Outcode: `TBRL`) dan hitung titik potong untuk segmen yang perlu dipotong!

**Kunci Pembahasan & Solusi:**
1. **Penentuan Outcode untuk Setiap Titik (Urutan Bit: Top Bottom Right Left):**
   * $P_1(3, 4)$: $y \le 7$ (0), $y \ge 3$ (0), $x \le 8$ (0), $x \ge 2$ (0) $\implies \mathbf{0000}$
   * $P_2(7, 6)$: $\implies \mathbf{0000}$
   * $Q_1(0, 5)$: $x < 2$ (Left=1) $\implies \mathbf{0001}$
   * $Q_2(10, 5)$: $x > 8$ (Right=1) $\implies \mathbf{0010}$
   * $R_1(1, 8)$: $y > 7$ (Top=1), $x < 2$ (Left=1) $\implies \mathbf{1001}$
   * $R_2(6, 9)$: $y > 7$ (Top=1) $\implies \mathbf{1000}$

2. **Evaluasi Status Kliping:**
   * **Garis 1 ($P_1 - P_2$):**
     $$\text{Code}(P_1) = 0000 \quad \text{dan} \quad \text{Code}(P_2) = 0000$$
     Kedua ujung bernilai $0000 \implies$ **Trivial Accept** (seluruh garis berada di dalam jendela dan langsung digambar).
   * **Garis 3 ($R_1 - R_2$):**
     $$\text{Code}(R_1) \text{ AND } \text{Code}(R_2) = 1001 \text{ AND } 1000 = \mathbf{1000} \ne 0000$$
     Hasil bitwise AND tidak nol $\implies$ **Trivial Reject** (kedua titik berada di luar batas atas jendela yang sama, garis dibuang sepenuhnya).
   * **Garis 2 ($Q_1 - Q_2$):**
     $$\text{Code}(Q_1) = 0001 \ne 0000, \quad \text{Code}(Q_2) = 0010 \ne 0000$$
     $$\text{Code}(Q_1) \text{ AND } \text{Code}(Q_2) = 0001 \text{ AND } 0010 = \mathbf{0000}$$
     Kondisi ini masuk kategori **Clipping Needed** (garis memotong jendela).
     * Garis bersifat horizontal ($y_1 = y_2 = 5$).
     * Titik potong kiri pada batas $x = x_{\min} = 2 \implies Q_1'(2, 5)$.
     * Titik potong kanan pada batas $x = x_{\max} = 8 \implies Q_2'(8, 5)$.
     * Segmen garis yang digambar adalah dari $(2, 5)$ hingga $(8, 5)$.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (PENGOLAHAN CITRA & FILTER SPASIAL)

### Soal UAS 1: Morfologi Citra (Erosi, Dilasi, Opening, Closing) - Soal Asli UAS Undip 2024
**Deskripsi Soal:**
Diberikan sebuah citra biner ukuran $5 \times 5$ ($A$) dan *Structuring Element* ($B$) berukuran $3 \times 3$ dengan titik pusat (*origin*) di tengah-tengah:
$$A = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}, \quad B = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}$$
1. Hitung hasil operasi **Erosi ($A \ominus B$)**!
2. Hitung hasil operasi **Dilasi ($A \oplus B$)**!
3. Jelaskan kegunaan operasi gabungan **Opening** dan **Closing** dalam reduksi derau (*noise removal*)!

**Kunci Pembahasan & Solusi:**
1. **Hasil Operasi Erosi ($A \ominus B$):**
   * *Prinsip:* Simpul pusat $B$ pada titik $(i, j)$ bernilai 1 jika dan hanya jika **seluruh elemen 1 pada structuring element $B$ tepat menutupi elemen 1 pada citra $A$ (*Fit*)**.
   * Hanya piksel pusat $(2, 2)$ yang bertetangga dengan piksel atas, bawah, kiri, dan kanan yang bernilai 1 secara utuh di citra $A$.
   $$A \ominus B = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$
   *(Erosi mengecilkan objek dan menghapus pulau-pulau piksel kecil terisolasi).*

2. **Hasil Operasi Dilasi ($A \oplus B$):**
   * *Prinsip:* Simpul pusat $B$ pada $(i, j)$ bernilai 1 jika **minimal satu elemen bernilai 1 pada $B$ menyentuh elemen 1 pada citra $A$ (*Hit*)**.
   * Bentuk kotak $3 \times 3$ akan melebar sebesar 1 piksel berbentuk tanda tambah pada setiap sudutnya:
   $$A \oplus B = \begin{bmatrix} 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \end{bmatrix} \quad \text{(melebar hingga pinggiran)}$$

3. **Peran Opening & Closing:**
   * **Opening ($A \circ B = (A \ominus B) \oplus B$):** Erosi dilanjutkan Dilasi. Efektif menghapus derau bintik putih kecil (*foreground noise / salt noise*) dan memutus jembatan tipis tanpa merusak ukuran global objek.
   * **Closing ($A \bullet B = (A \oplus B) \ominus B$):** Dilasi dilanjutkan Erosi. Efektif menutup lubang-lubang hitam kecil di dalam objek (*pepper noise / internal gaps*) dan menyambung retakan objek yang terputus.

---

### Soal UAS 2: Deteksi Tepi Operator Sobel (Konvolusi Matriks)
**Deskripsi Soal:**
Diberikan potongan matriks citra intensitas $3 \times 3$:
$$I = \begin{bmatrix} 50 & 50 & 100 \\ 50 & 60 & 120 \\ 40 & 50 & 110 \end{bmatrix}$$
Gunakan Kernel Sobel Arah Horizontal ($G_x$) dan Vertikal ($G_y$):
$$S_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad S_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$$
1. Hitung nilai respon gradien horizontal ($G_x$) dan vertikal ($G_y$) pada piksel pusat (koordinat $(1, 1)$ bernilai $60$)!
2. Hitung kekuatan gradien tepi total ($|G| \approx |G_x| + |G_y|$)!

**Kunci Pembahasan & Solusi:**
1. **Konvolusi dengan Kernel Sobel:**
   * **Respon Horizontal $G_x$:**
     $$G_x = (-1)(50) + (0)(50) + (1)(100) + (-2)(50) + (0)(60) + (2)(120) + (-1)(40) + (0)(50) + (1)(110)$$
     $$G_x = -50 + 100 - 100 + 240 - 40 + 110 = 260$$
   * **Respon Vertikal $G_y$:**
     $$G_y = (-1)(50) + (-2)(50) + (-1)(100) + (0)(50) + (0)(60) + (0)(120) + (1)(40) + (2)(50) + (1)(110)$$
     $$G_y = -50 - 100 - 100 + 40 + 100 + 110 = -100$$

2. **Kekuatan Gradien Total:**
   $$|G| = \sqrt{G_x^2 + G_y^2} = \sqrt{260^2 + (-100)^2} = \sqrt{67600 + 10000} = \sqrt{77600} \approx 278.56$$
   *Atau dengan aproksimasi cepat Manhattan norm:*
   $$|G|_{\text{approx}} = |G_x| + |G_y| = |260| + |-100| = \mathbf{360}$$
   *Kesimpulan:* Nilai gradien yang sangat tinggi menandakan bahwa di posisi piksel pusat terdapat garis tepi tajam vertikal (perubahan intensitas drastis dari kolom 1 ke kolom 3).

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa Algoritma Garis Bresenham lebih dipilih daripada DDA dalam implementasi hardware GPU modern?"
**Jawaban Komprehensif:**
Algoritma DDA (*Digital Differential Analyzer*) membutuhkan perhitungan aritmetika bilangan pecahan (*floating point division and addition*) pada setiap langkah pergeseran piksel, yang diakhiri fungsi pembulatan (*rounding*). Komputasi pecahan membutuhkan unit FPU (*Floating Point Unit*) yang mengonsumsi siklus clock dan daya listrik lebih besar.
Sebaliknya, **Algoritma Bresenham merumuskan parameter keputusan dalam bentuk aritmetika bilangan bulat murni (*integer arithmetic*)**, di mana setiap iterasi hanya melibatkan operasi penjumlahan sederhana dan operasi geser bit (*bit-shift* untuk perkalian $2\Delta y$). Hal ini memungkinkan instruksi dieksekusi secara instan pada level gerbang logika sirkuit keras (ASIC / GPU Rasterizer) dengan latensi dan konsumsi memori terendah.

### Q2: "Jelaskan perbedaan mendasar antara Gouraud Shading dan Phong Shading serta fenomena artefak visual yang terjadi pada keduanya!"
**Jawaban Komprehensif:**
* **Gouraud Shading (Intensity Interpolation):**
  * Menghitung nilai warna pencahayaan menggunakan model refleksi di setiap vertex poligon.
  * Warna pada bagian dalam poligon dihitung melalui interpolasi linier nilai warna antar simpul.
  * *Kelemahan/Artefak:* Jika sorotan cahaya mengkilap (*specular highlight*) berada tepat di tengah-tengah poligon tanpa menyentuh simpul manapun, highlight tersebut akan lenyap (*missed specular highlight*). Selain itu, muncul garis patahan gradien (*Mach Banding artifact*).
* **Phong Shading (Normal Vector Interpolation):**
  * Bukan warna yang diinterpolasi, melainkan **vektor normal permukaan poligon** yang diinterpolasi secara linier pada setiap piksel.
  * Persamaan pencahayaan dihitung satu per satu di setiap piksel berdasarkan vektor normal hasil interpolasi tersebut.
  * *Kelebihan:* Menghasilkan specular highlight yang akurat dan permukaan kurva yang tampak sangat licin tanpa Mach Banding. Kelemahannya adalah biaya komputasi per-piksel yang jauh lebih tinggi.
