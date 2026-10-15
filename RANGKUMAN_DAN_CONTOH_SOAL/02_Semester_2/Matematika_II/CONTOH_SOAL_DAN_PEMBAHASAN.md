# Bank Contoh Soal & Pembahasan: Matematika II (Kalkulus Peubah Banyak)

> Sumber rujukan: Bank soal UTS & UAS Matematika II Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Matematika FSM Undip, 2020–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (TURUNAN PARSIAL, CLAIRAUT & METODE LAGRANGE)

### Soal UTS 1: Turunan Parsial Campuran & Uji Teorema Clairaut (Soal Asli UTS Undip 2024)
**Deskripsi Soal:**
Diberikan fungsi multivariabel berikut:
$$f(x, y) = \sqrt{x^2 + y^2} + e^{xy} + x \sin y$$
1. Tentukan turunan parsial pertama terhadap $x$ ($f_x$) dan terhadap $y$ ($f_y$).
2. Hitunglah turunan parsial kedua campuran $f_{xy}$ dan $f_{yx}$, lalu buktikan apakah berlaku $f_{xy} = f_{yx}$ serta jelaskan landasan teoretisnya!

**Kunci Pembahasan & Solusi:**
1. **Mencari Turunan Parsial Pertama:**
   * **Menghitung $f_x = \frac{\partial f}{\partial x}$ ($y$ dianggap konstanta):**
     * Suku 1: $\frac{\partial}{\partial x}(x^2 + y^2)^{1/2} = \frac{1}{2}(x^2 + y^2)^{-1/2} \cdot 2x = \frac{x}{\sqrt{x^2 + y^2}}$
     * Suku 2: $\frac{\partial}{\partial x}(e^{xy}) = y \cdot e^{xy}$ (karena turunan eksponen terhadap $x$ adalah $y$)
     * Suku 3: $\frac{\partial}{\partial x}(x \sin y) = \sin y$
     $$\mathbf{f_x = \frac{x}{\sqrt{x^2 + y^2}} + y e^{xy} + \sin y}$$
   * **Menghitung $f_y = \frac{\partial f}{\partial y}$ ($x$ dianggap konstanta):**
     * Suku 1: $\frac{\partial}{\partial y}(x^2 + y^2)^{1/2} = \frac{y}{\sqrt{x^2 + y^2}}$
     * Suku 2: $\frac{\partial}{\partial y}(e^{xy}) = x \cdot e^{xy}$
     * Suku 3: $\frac{\partial}{\partial y}(x \sin y) = x \cos y$
     $$\mathbf{f_y = \frac{y}{\sqrt{x^2 + y^2}} + x e^{xy} + x \cos y}$$
2. **Mencari Turunan Parsial Kedua Campuran:**
   * **Menghitung $f_{xy} = \frac{\partial}{\partial y}(f_x)$:**
     * Turunkan $\frac{x}{\sqrt{x^2 + y^2}} = x(x^2 + y^2)^{-1/2}$ terhadap $y$:
       $$x \left( -\frac{1}{2}(x^2 + y^2)^{-3/2} \cdot 2y \right) = -\frac{xy}{(x^2 + y^2)^{3/2}}$$
     * Turunkan $y e^{xy}$ terhadap $y$ menggunakan aturan perkalian $(uv)'$:
       $$(1) \cdot e^{xy} + y \cdot (x e^{xy}) = e^{xy} + xy e^{xy}$$
     * Turunkan $\sin y$ terhadap $y$: $\cos y$.
     $$\mathbf{f_{xy} = -\frac{xy}{(x^2 + y^2)^{3/2}} + e^{xy} + xy e^{xy} + \cos y}$$
   * **Menghitung $f_{yx} = \frac{\partial}{\partial x}(f_y)$:**
     * Turunkan $\frac{y}{\sqrt{x^2 + y^2}} = y(x^2 + y^2)^{-1/2}$ terhadap $x$:
       $$y \left( -\frac{1}{2}(x^2 + y^2)^{-3/2} \cdot 2x \right) = -\frac{xy}{(x^2 + y^2)^{3/2}}$$
     * Turunkan $x e^{xy}$ terhadap $x$ menggunakan aturan perkalian $(uv)'$:
       $$(1) \cdot e^{xy} + x \cdot (y e^{xy}) = e^{xy} + xy e^{xy}$$
     * Turunkan $x \cos y$ terhadap $x$: $\cos y$.
     $$\mathbf{f_{yx} = -\frac{xy}{(x^2 + y^2)^{3/2}} + e^{xy} + xy e^{xy} + \cos y}$$
3. **Kesimpulan & Penjelasan Teoretis:**
   Terlihat dengan jelas bahwa **$f_{xy} \equiv f_{yx}$**.
   Hal ini sesuai dengan **Teorema Clairaut (Schwarz)**, yang menyatakan bahwa jika turunan parsial kedua dari suatu fungsi peubah banyak terdefinisi dan kontinu pada suatu himpunan terbuka di sekitar titik evaluasi, maka operator diferensial parsial bersifat komutatif: $\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y}$.

---

### Soal UTS 2: Optimasi Berkendala Metode Pengali Lagrange (Soal Asli UTS Undip 2024)
**Deskripsi Soal:**
Dengan menggunakan metode **Pengali Lagrange (*Lagrange Multipliers*)**, tentukan nilai minimum dari fungsi objektif:
$$f(x, y, z) = x^2 + y^2 + z^2$$
yang dibatasi oleh kendala linier:
$$x + y + z = 3$$

**Kunci Pembahasan & Solusi:**
1. **Identifikasi Fungsi Objektif & Fungsi Kendala:**
   * Fungsi objektif: $f(x, y, z) = x^2 + y^2 + z^2$ (merepresentasikan kuadrat jarak titik $(x, y, z)$ dari titik asal $(0,0,0)$).
   * Fungsi kendala: $g(x, y, z) = x + y + z - 3 = 0$.
2. **Hitung Vektor Gradien $\nabla f$ dan $\nabla g$:**
   $$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right\rangle = \langle 2x, 2y, 2z \rangle$$
   $$\nabla g = \left\langle \frac{\partial g}{\partial x}, \frac{\partial g}{\partial y}, \frac{\partial g}{\partial z} \right\rangle = \langle 1, 1, 1 \rangle$$
3. **Persamaan Lagrange ($\nabla f = \lambda \nabla g$):**
   $$\langle 2x, 2y, 2z \rangle = \lambda \langle 1, 1, 1 \rangle$$
   Diperoleh sistem persamaan:
   * (1) $2x = \lambda \implies x = \frac{\lambda}{2}$
   * (2) $2y = \lambda \implies y = \frac{\lambda}{2}$
   * (3) $2z = \lambda \implies z = \frac{\lambda}{2}$
   Maka: $x = y = z$.
4. **Substitusikan ke Persamaan Kendala:**
   $$x + y + z = 3 \implies x + x + x = 3 \implies 3x = 3 \implies \mathbf{x = 1}$$
   Karena $x = y = z$, maka:
   $$\mathbf{x = 1, \quad y = 1, \quad z = 1}$$
   *(Nilai pengali $\lambda = 2(1) = 2$).*
5. **Hitung Nilai Minimum Fungsi:**
   $$f_{\min} = f(1, 1, 1) = 1^2 + 1^2 + 1^2 = \mathbf{3}$$
   Titik kritis berada pada koordinat $(1, 1, 1)$ dengan **nilai minimum $= 3$**.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (INTEGRAL LIPAT DUA KARTESIUS & POLAR)

### Soal UAS 1: Perhitungan Volume Padat Menggunakan Integral Lipat Dua
**Deskripsi Soal:**
Sebuah prisma pejal memiliki alas segitiga pada bidang $xy$ yang dibatasi oleh sumbu-$X$, garis $y = 2x$, dan garis vertikal $x = 2$. Bagian atas prisma tersebut ditutup oleh bidang datar:
$$z = f(x, y) = 4 - 2x - y$$
Tentukan volume prisma tersebut menggunakan **Integral Lipat Dua (*Double Integrals*)**!

**Kunci Pembahasan & Solusi:**
1. **Menentukan Batas Integrasi Daerah Alas $R$ (Tipe I):**
   * Sumbu-$X$ merepresentasikan garis $y = 0$.
   * Batas $x$ bergerak dari titik potong garis $y=2x$ dengan sumbu-$X$ (yaitu $x = 0$) hingga garis batas $x = 2$.
   * Untuk setiap nilai $x$ tertentu, $y$ bergerak dari batas bawah $y = 0$ hingga batas atas $y = 2x$.
   $$R = \{(x, y) \mid 0 \le x \le 2, \; 0 \le y \le 2x\}$$
2. **Merumuskan Integral Lipat Dua:**
   $$V = \iint_R z \, dA = \int_{x=0}^2 \left[ \int_{y=0}^{2x} (4 - 2x - y) \, dy \right] dx$$
3. **Langkah 1: Evaluasi Integral Dalam terhadap $y$:**
   $$\begin{aligned}
   \int_0^{2x} (4 - 2x - y) \, dy &= \left[ 4y - 2xy - \frac{1}{2}y^2 \right]_{y=0}^{2x} \\
   &= \left( 4(2x) - 2x(2x) - \frac{1}{2}(2x)^2 \right) - 0 \\
   &= 8x - 4x^2 - 2x^2 \\
   &= 8x - 6x^2
   \end{aligned}$$
4. **Langkah 2: Evaluasi Integral Luar terhadap $x$:**
   $$\begin{aligned}
   V &= \int_0^2 (8x - 6x^2) \, dx \\
   &= \left[ 4x^2 - 2x^3 \right]_0^2 \\
   &= \big( 4(2^2) - 2(2^3) \big) - 0 \\
   &= \big( 4(4) - 2(8) \big) \\
   &= 16 - 16 = 0
   \end{aligned}$$
   *Catatan Analisis Geometri:* Bidang $z = 4 - 2x - y$ bernilai $0$ tepat di hipotenusa segitiga saat $y = 4 - 2x$. Di titik $(2, 4)$, $z = 4 - 4 - 4 = -4$ (masuk ke bawah bidang $xy$). Jika diminta volume geometris absolut padat ruang antara dua permukaan, integrasikan daerah yang memiliki $z \ge 0$.

---

### Soal UAS 2: Integral Lipat Dua dalam Koordinat Polar (Kutub)
**Deskripsi Soal:**
Hitunglah integral lipat dua berikut:
$$\iint_R e^{-(x^2 + y^2)} \, dA$$
di mana daerah $R$ adalah piringan lingkaran berpusat di titik asal dengan jari-jari $2$, yaitu $R = \{(x, y) \mid x^2 + y^2 \le 4\}$.

**Kunci Pembahasan & Solusi:**
1. **Konversi ke Koordinat Polar:**
   * $x^2 + y^2 = r^2$
   * Elemen diferensial luas: $dA = \mathbf{r \, dr \, d\theta}$
   * Batas jari-jari: $r$ dari $0$ hingga $2$.
   * Batas sudut: $\theta$ dari $0$ hingga $2\pi$ (satu lingkaran penuh).
2. **Menyusun Integral Polar:**
   $$\iint_R e^{-(x^2 + y^2)} \, dA = \int_{\theta=0}^{2\pi} \int_{r=0}^2 e^{-r^2} \cdot r \, dr \, d\theta$$
3. **Eksekusi Pengintegralan:**
   * Substitusi untuk integral $r$: Misalkan $u = -r^2 \implies du = -2r \, dr \implies r \, dr = -\frac{1}{2} du$.
   * Saat $r = 0 \implies u = 0$. Saat $r = 2 \implies u = -4$.
   $$\int_0^2 e^{-r^2} r \, dr = -\frac{1}{2} \int_0^{-4} e^u \, du = \frac{1}{2} \int_{-4}^0 e^u \, du = \frac{1}{2} \left[ e^u \right]_{-4}^0 = \frac{1}{2} (1 - e^{-4})$$
   * Integrasi terhadap $\theta$:
     $$\int_0^{2\pi} d\theta = 2\pi$$
4. **Hasil Akhir:**
   $$\text{Hasil} = 2\pi \times \frac{1}{2}(1 - e^{-4}) = \mathbf{\pi (1 - e^{-4}) \approx 3.084}$$

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa vektor gradien $\nabla f$ selalu menunjuk ke arah laju kenaikan fungsi yang paling curam (steepest ascent)?"
**Jawaban Komprehensif:**
Berdasarkan definisi, turunan berarah pada arah vektor satuan $\mathbf{u}$ adalah perkalian dot:
$$D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \|\nabla f\| \|\mathbf{u}\| \cos \theta = \|\nabla f\| \cos \theta \quad (\text{karena } \|\mathbf{u}\| = 1)$$
Nilai $D_{\mathbf{u}} f$ akan mencapai nilai **maksimum terbesar** ketika $\cos \theta = 1$, yang terjadi jika dan hanya jika $\theta = 0^\circ$ (yaitu saat vektor arah $\mathbf{u}$ searah persis dengan vektor gradien $\nabla f$).
Oleh karena itu, arah vektor gradien $\nabla f$ terbukti secara matematis merupakan arah laju kenaikan nilai fungsi yang paling curam (*steepest ascent*), dan nilainya adalah $\|\nabla f\|$.

### Q2: "Bagaimana cara kerja uji determinan Hessian dalam mengidentifikasi Titik Pelana (Saddle Point) pada fungsi peubah banyak?"
**Jawaban Komprehensif:**
Determinan Hessian $D = f_{xx} f_{yy} - (f_{xy})^2$ mengukur kecekungan kurva pada berbagai arah irisan bidang:
* Jika $D > 0$, maka kecekungan kurva pada arah sumbu-$X$ dan sumbu-$Y$ bertanda sama (keduanya melengkung ke atas $\implies$ minimum lokal, atau keduanya melengkung ke bawah $\implies$ maksimum lokal).
* Namun, jika **$D < 0$**, fungsi memiliki kecekungan yang berlawanan tanda pada arah yang berbeda (misalnya melengkung ke atas pada arah sumbu-$X$ seperti mangkuk, namun melengkung ke bawah pada arah sumbu-$Y$ seperti puncak bukit). Kondisi topologi permukaan yang menyerupai pelana kuda ini disebut **Titik Pelana (*Saddle Point*)**, di mana gradiennya nol namun titik tersebut bukan nilai ekstrem lokal.
