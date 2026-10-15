# Bank Contoh Soal & Pembahasan: Matematika I (Kalkulus I)

> Sumber rujukan: Bank soal UTS & UAS Matematika I Departemen Informatika Universitas Diponegoro (Koleksi Dosen Pengampu: Dr. Sunarsih, M.Si. & Solikhin, M.Sc., 2018–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (PERTIDAKSAMAAN, TURUNAN & OPTIMASI)

### Soal UTS 1: Pertidaksamaan Rasional (Soal Asli UTS Undip)
**Deskripsi Soal:**
Tentukan himpunan penyelesaian dari pertidaksamaan berikut dan gambarkan garis bilangannya:
$$x - \frac{7}{x} \le 1$$

**Kunci Pembahasan & Solusi:**
1. **Langkah 1: Pindahkan semua suku ke ruas kiri sehingga ruas kanan menjadi nol:**
   $$x - 1 - \frac{7}{x} \le 0$$
2. **Langkah 2: Samakan penyebut:**
   $$\frac{x(x - 1) - 7}{x} \le 0 \implies \frac{x^2 - x - 7}{x} \le 0$$
3. **Langkah 3: Tentukan titik-titik pembuat nol:**
   * **Pembuat nol pembilang ($x^2 - x - 7 = 0$):**
     Gunakan rumus kuadratik ($abc$):
     $$x_{1, 2} = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(-7)}}{2(1)} = \frac{1 \pm \sqrt{1 + 28}}{2} = \frac{1 \pm \sqrt{29}}{2}$$
     * $x_1 = \frac{1 - \sqrt{29}}{2} \approx \frac{1 - 5.385}{2} = -2.19$
     * $x_2 = \frac{1 + \sqrt{29}}{2} \approx \frac{1 + 5.385}{2} = 3.19$
   * **Pembuat nol penyebut ($x = 0$):**
     Syarat penyebut tidak boleh nol ($x \ne 0$). Titik $x = 0$ bertindak sebagai batas interval terbuka (*open circle*).
4. **Langkah 4: Uji Tanda Interval pada Garis Bilangan:**
   Titik pemecah terurut: $x_1 \approx -2.19$, $0$, dan $x_2 \approx 3.19$.
   * Interval $(-\infty, x_1]$: Misal $x = -3 \implies \frac{(-3)^2 - (-3) - 7}{-3} = \frac{9 + 3 - 7}{-3} = \frac{5}{-3} < 0$ (**Negatif / Memenuhi**).
   * Interval $[x_1, 0)$: Misal $x = -1 \implies \frac{1 - (-1) - 7}{-1} = \frac{-5}{-1} = 5 > 0$ (**Positif**).
   * Interval $(0, x_2]$: Misal $x = 1 \implies \frac{1 - 1 - 7}{1} = -7 < 0$ (**Negatif / Memenuhi**).
   * Interval $[x_2, \infty)$: Misal $x = 4 \implies \frac{16 - 4 - 7}{4} = \frac{5}{4} > 0$ (**Positif**).
5. **Himpunan Penyelesaian (HP):**
   $$\mathbf{HP = \left(-\infty, \frac{1 - \sqrt{29}}{2}\right] \cup \left(0, \frac{1 + \sqrt{29}}{2}\right]}$$
   *(Catatan Kompre: Titik $0$ wajib menggunakan kurung biasa `)` karena merupakan pembuat nol penyebut).*

---

### Soal UTS 2: Turunan Implisit Orde Satu & Dua (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan persamaan implisit:
$$y^3 + 7y - x^3 = 0$$
Carilah $\frac{dy}{dx}$ dan $\frac{d^2y}{dx^2}$!

**Kunci Pembahasan & Solusi:**
1. **Mencari Turunan Pertama $\frac{dy}{dx}$:**
   Turunkan kedua ruas terhadap $x$:
   $$\frac{d}{dx}(y^3) + \frac{d}{dx}(7y) - \frac{d}{dx}(x^3) = 0$$
   $$3y^2 \frac{dy}{dx} + 7 \frac{dy}{dx} - 3x^2 = 0$$
   Faktorkan $\frac{dy}{dx}$:
   $$\frac{dy}{dx} \big( 3y^2 + 7 \big) = 3x^2 \implies \mathbf{\frac{dy}{dx} = \frac{3x^2}{3y^2 + 7}}$$
2. **Mencari Turunan Kedua $\frac{d^2y}{dx^2}$:**
   Turunkan $\frac{dy}{dx}$ menggunakan aturan turunan pecahan $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:
   * Misalkan $u = 3x^2 \implies u' = 6x$
   * Misalkan $v = 3y^2 + 7 \implies v' = 6y \frac{dy}{dx}$
   $$\frac{d^2y}{dx^2} = \frac{6x(3y^2 + 7) - 3x^2 \left( 6y \frac{dy}{dx} \right)}{(3y^2 + 7)^2}$$
   Substitusikan $\frac{dy}{dx} = \frac{3x^2}{3y^2 + 7}$:
   $$\frac{d^2y}{dx^2} = \frac{6x(3y^2 + 7) - 18x^2 y \left( \frac{3x^2}{3y^2 + 7} \right)}{(3y^2 + 7)^2}$$
   Samakan penyebut pada pembilang:
   $$\mathbf{\frac{d^2y}{dx^2} = \frac{6x(3y^2 + 7)^2 - 54x^4 y}{(3y^2 + 7)^3}}$$

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (TEKNIK PENGINTEGRALAN & VOLUME BENDA PUTAR)

### Soal UAS 1: Integral Pecahan Rasional (Partial Fractions)
**Deskripsi Soal:**
Hitunglah integral tak tentu berikut:
$$\int \frac{5x - 3}{x^2 - 2x - 3} \, dx$$

**Kunci Pembahasan & Solusi:**
1. **Faktorkan Penyebut:**
   $$x^2 - 2x - 3 = (x - 3)(x + 1)$$
2. **Dekomposisi Pecahan Parsial:**
   $$\frac{5x - 3}{(x - 3)(x + 1)} = \frac{A}{x - 3} + \frac{B}{x + 1}$$
   Kalikan kedua ruas dengan $(x - 3)(x + 1)$:
   $$5x - 3 = A(x + 1) + B(x - 3)$$
3. **Mencari Nilai Koefisien $A$ dan $B$:**
   * Substitusikan pembuat nol $x = 3$:
     $$5(3) - 3 = A(3 + 1) + B(0) \implies 12 = 4A \implies \mathbf{A = 3}$$
   * Substitusikan pembuat nol $x = -1$:
     $$5(-1) - 3 = A(0) + B(-1 - 3) \implies -8 = -4B \implies \mathbf{B = 2}$$
4. **Eksekusi Pengintegralan:**
   $$\begin{aligned}
   \int \frac{5x - 3}{x^2 - 2x - 3} \, dx &= \int \frac{3}{x - 3} \, dx + \int \frac{2}{x + 1} \, dx \\
   &= 3\ln|x - 3| + 2\ln|x + 1| + C \\
   &= \mathbf{\ln\big( |x - 3|^3 \cdot |x + 1|^2 \big) + C}
   \end{aligned}$$

---

### Soal UAS 2: Volume Benda Putar (Metode Cakram & Cincin)
**Deskripsi Soal:**
Hitunglah volume benda putar yang terbentuk jika daerah yang dibatasi oleh kurva parabola $y = x^2$ dan garis linier $y = 2x$ diputar mengelilingi sumbu-$X$ sejauh $360^\circ$!

**Kunci Pembahasan & Solusi:**
1. **Tentukan Titik Potong Kedua Kurva (Batas Integrasi):**
   $$x^2 = 2x \implies x^2 - 2x = 0 \implies x(x - 2) = 0$$
   Maka batas integrasi adalah $x = 0$ hingga $x = 2$.
2. **Tentukan Jari-Jari Luar ($R$) dan Jari-Jari Dalam ($r$):**
   Pada interval $[0, 2]$, garis $y = 2x$ berada di atas parabola $y = x^2$ (misal pada $x = 1$, $y_{\text{garis}} = 2 > y_{\text{parabola}} = 1$).
   * Jari-jari luar: $R(x) = 2x$
   * Jari-jari dalam: $r(x) = x^2$
3. **Rumus Volume Metode Cincin (*Washer Method*):**
   $$V = \pi \int_a^b \Big( [R(x)]^2 - [r(x)]^2 \Big) \, dx$$
4. **Hitung Integrasi:**
   $$\begin{aligned}
   V &= \pi \int_0^2 \Big( (2x)^2 - (x^2)^2 \Big) \, dx \\
   &= \pi \int_0^2 \big( 4x^2 - x^4 \big) \, dx \\
   &= \pi \left[ \frac{4}{3}x^3 - \frac{1}{5}x^5 \right]_0^2 \\
   &= \pi \left[ \left( \frac{4}{3}(8) - \frac{1}{5}(32) \right) - 0 \right] \\
   &= \pi \left[ \frac{32}{3} - \frac{32}{5} \right] = 32\pi \left( \frac{5 - 3}{15} \right) = \mathbf{\frac{64\pi}{15} \text{ satuan volume}}
   \end{aligned}$$

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Sebutkan 3 syarat mutlak suatu fungsi $f(x)$ dikatakan kontinu di titik $x = c$!"
**Jawaban Komprehensif:**
Suatu fungsi $f(x)$ dikatakan kontinu pada $x = c$ jika dan hanya jika memenuhi ketiga syarat berikut sekaligus:
1. $f(c)$ **terdefinisi** (nilai fungsinya ada di bilangan real, bukan $0/0$ atau tak hingga).
2. $\lim_{x \to c} f(x)$ **ada** (artinya limit kiri sama dengan limit kanan: $\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x)$).
3. Nilai limit tepat sama dengan nilai fungsi di titik tersebut: $\lim_{x \to c} f(x) = f(c)$.

### Q2: "Mengapa konsep Aturan Rantai (*Chain Rule*) pada kalkulus turunan menjadi tulang punggung algoritma Machine Learning / Deep Learning?"
**Jawaban Komprehensif:**
Dalam *neural network*, output akhir dihasilkan melalui komposisi bertingkat banyak layer:
$$\hat{y} = f_L(f_{L-1}(\dots f_1(X \cdot W_1) \dots ))$$
Untuk melatih model menggunakan *Gradient Descent*, kita harus menghitung turunan parsial dari fungsi kerugian (*loss*) $\mathcal{L}$ terhadap setiap bobot parameter $W_i$ di layer terdalam:
$$\frac{\partial \mathcal{L}}{\partial W_i} = \frac{\partial \mathcal{L}}{\partial a_L} \cdot \frac{\partial a_L}{\partial a_{L-1}} \cdots \frac{\partial a_{i+1}}{\partial a_i} \cdot \frac{\partial a_i}{\partial W_i}$$
Aturan rantai kalkulus memungkinkan penghitungan gradien error ini dipropagasikan secara efisien ke arah belakang dari output ke input (*Backpropagation*), menghindari penghitungan ulang berulang (*dynamic programming on derivative graphs*).
