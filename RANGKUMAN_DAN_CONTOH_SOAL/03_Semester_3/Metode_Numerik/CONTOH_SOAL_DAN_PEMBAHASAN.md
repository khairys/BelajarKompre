# Bank Contoh Soal & Pembahasan: Metode Numerik

> Sumber rujukan: Bank soal UTS & UAS Metode Numerik Departemen Informatika Universitas Diponegoro (Koleksi Pengampu FSM Undip, 2022–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (METODE NEWTON-RAPHSON & GAUSS-SEIDEL)

### Soal UTS 1: Pencarian Akar Persamaan Non-Linier via Newton-Raphson (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan persamaan non-linier:
$$f(x) = x^4 + x - 3 = 0$$
Tentukan akar pendekatan dari fungsi tersebut menggunakan **Metode Newton-Raphson** dengan nilai tebakan awal $x_0 = 1.1$. Lakukan iterasi hingga diperoleh ketelitian galat aproksimasi relatif mutlak $|\epsilon_a| < 0.1\%$ ($0.001$)!

**Kunci Pembahasan & Solusi:**
1. **Turunan Pertama Fungsi:**
   $$f'(x) = \frac{d}{dx}(x^4 + x - 3) = 4x^3 + 1$$
2. **Rumus Rekursif Iterasi Newton-Raphson:**
   $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} = x_n - \frac{x_n^4 + x_n - 3}{4x_n^3 + 1}$$
3. **Langkah-Langkah Perhitungan Iterasi:**
   * **Iterasi 1 ($n = 0, x_0 = 1.1$):**
     * $f(1.1) = (1.1)^4 + 1.1 - 3 = 1.4641 + 1.1 - 3 = -0.4359$
     * $f'(1.1) = 4(1.1)^3 + 1 = 4(1.331) + 1 = 5.324 + 1 = 6.324$
     * $x_1 = 1.1 - \frac{-0.4359}{6.324} = 1.1 + 0.06893 = \mathbf{1.16893}$
   * **Iterasi 2 ($n = 1, x_1 = 1.16893$):**
     * $f(1.16893) = (1.16893)^4 + 1.16893 - 3 = 1.86877 + 1.16893 - 3 = 0.03770$
     * $f'(1.16893) = 4(1.16893)^3 + 1 = 4(1.59701) + 1 = 6.38804 + 1 = 7.38804$
     * $x_2 = 1.16893 - \frac{0.03770}{7.38804} = 1.16893 - 0.00510 = \mathbf{1.16383}$
     * *Cek Galat:* $|\epsilon_a| = \left| \frac{1.16383 - 1.16893}{1.16383} \right| \times 100\% = \left| \frac{-0.00510}{1.16383} \right| \times 100\% = 0.438\% > 0.1\%$ (Lanjut).
   * **Iterasi 3 ($n = 2, x_2 = 1.16383$):**
     * $f(1.16383) = (1.16383)^4 + 1.16383 - 3 = 1.83637 + 1.16383 - 3 = 0.00020$
     * $f'(1.16383) = 4(1.16383)^3 + 1 = 4(1.57618) + 1 = 7.30472$
     * $x_3 = 1.16383 - \frac{0.00020}{7.30472} = 1.16383 - 0.000027 = \mathbf{1.16380}$
     * *Cek Galat:*
       $$|\epsilon_a| = \left| \frac{1.16380 - 1.16383}{1.16380} \right| \times 100\% = 0.0025\% < 0.1\% \quad \mathbf{(Konvergen / Stop!)}$$
4. **Kesimpulan:**
   Akar pendekatan dari persamaan $x^4 + x - 3 = 0$ adalah **$x \approx 1.164$** dengan galat aproksimasi $0.0025\%$.

---

### Soal UTS 2: Solusi SPL Numerik via Metode Iterasi Gauss-Seidel
**Deskripsi Soal:**
Selesaikan sistem persamaan linier berikut menggunakan **Metode Iterasi Gauss-Seidel**:
$$\begin{aligned}
4x_1 - x_2 + x_3 &= 7 \\
x_1 + 5x_2 - 2x_3 &= 10 \\
2x_1 - x_2 + 6x_3 &= 15
\end{aligned}$$
Gunakan nilai awal tebakan $\mathbf{x}^{(0)} = (0, 0, 0)^T$ dan lakukan perhitungan hingga 2 iterasi!

**Kunci Pembahasan & Solusi:**
1. **Uji Dominan Diagonal (*Diagonally Dominant Test*):**
   * Baris 1: $|4| > |-1| + |1| = 2$ (Memenuhi).
   * Baris 2: $|5| > |1| + |-2| = 3$ (Memenuhi).
   * Baris 3: $|6| > |2| + |-1| = 3$ (Memenuhi).
   Karena matriks dominan diagonal pada setiap baris, metode Gauss-Seidel **pasti konvergen**.
2. **Formula Rekursif Gauss-Seidel:**
   $$x_1^{(k+1)} = \frac{7 + x_2^{(k)} - x_3^{(k)}}{4}$$
   $$x_2^{(k+1)} = \frac{10 - x_1^{(k+1)} + 2x_3^{(k)}}{5} \quad (\text{langsung gunakan } x_1 \text{ terbaru!})$$
   $$x_3^{(k+1)} = \frac{15 - 2x_1^{(k+1)} + x_2^{(k+1)}}{6} \quad (\text{gunakan } x_1 \text{ dan } x_2 \text{ terbaru!})$$
3. **Eksekusi Iterasi:**
   * **Iterasi 1 (dengan tebakan awal $x_1=0, x_2=0, x_3=0$):**
     * $x_1^{(1)} = \frac{7 + 0 - 0}{4} = \mathbf{1.750}$
     * $x_2^{(1)} = \frac{10 - (1.750) + 2(0)}{5} = \frac{8.250}{5} = \mathbf{1.650}$
     * $x_3^{(1)} = \frac{15 - 2(1.750) + (1.650)}{6} = \frac{15 - 3.500 + 1.650}{6} = \frac{13.150}{6} = \mathbf{2.192}$
   * **Iterasi 2:**
     * $x_1^{(2)} = \frac{7 + (1.650) - (2.192)}{4} = \frac{6.458}{4} = \mathbf{1.615}$
     * $x_2^{(2)} = \frac{10 - (1.615) + 2(2.192)}{5} = \frac{10 - 1.615 + 4.384}{5} = \frac{12.769}{5} = \mathbf{2.554}$
     * $x_3^{(2)} = \frac{15 - 2(1.615) + (2.554)}{6} = \frac{15 - 3.230 + 2.554}{6} = \frac{14.324}{6} = \mathbf{2.387}$
4. **Hasil Taksiran Iterasi ke-2:**
   $$\mathbf{x_1 \approx 1.615, \quad x_2 \approx 2.554, \quad x_3 \approx 2.387}$$

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (INTEGRASI SIMPSON & PDB RUNGE-KUTTA)

### Soal UAS 1: Integrasi Numerik Kaidah Simpson 1/3 Komposit
**Deskripsi Soal:**
Hitunglah nilai aproksimasi integral tentu berikut:
$$I = \int_0^2 \frac{1}{1 + x^2} \, dx$$
menggunakan **Kaidah Simpson 1/3 Komposit** dengan jumlah pias $n = 4$! Hitung pula nilai galat relatifnya jika nilai eksak analitis adalah $\arctan(2) \approx 1.107149$ radian!

**Kunci Pembahasan & Solusi:**
1. **Lebar Pias ($h$):**
   $$h = \frac{b - a}{n} = \frac{2 - 0}{4} = 0.5$$
2. **Tabel Evaluasi Titik Diskret Fungsi $f(x) = \frac{1}{1 + x^2}$:**

| $i$ | $x_i$ | $f(x_i) = \frac{1}{1 + x_i^2}$ | Bobot Simpson 1/3 | Kontribusi Bobot |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0.0 | $\frac{1}{1 + 0} = 1.000000$ | 1 | $1.000000$ |
| 1 | 0.5 | $\frac{1}{1 + 0.25} = 0.800000$ | 4 | $3.200000$ |
| 2 | 1.0 | $\frac{1}{1 + 1} = 0.500000$ | 2 | $1.000000$ |
| 3 | 1.5 | $\frac{1}{1 + 2.25} = 0.307692$ | 4 | $1.230768$ |
| 4 | 2.0 | $\frac{1}{1 + 4} = 0.200000$ | 1 | $0.200000$ |

3. **Hitung Nilai Integral:**
   $$\begin{aligned}
   I_{\text{Simpson}} &= \frac{h}{3} \big[ f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + f(x_4) \big] \\
   &= \frac{0.5}{3} \big[ 1.000000 + 3.200000 + 1.000000 + 1.230768 + 0.200000 \big] \\
   &= \frac{0.5}{3} \times [ 6.630768 ] = \mathbf{1.105128}
   \end{aligned}$$
4. **Analisis Galat Relatif Sejati:**
   $$\epsilon_t = \left| \frac{1.107149 - 1.105128}{1.107149} \right| \times 100\% = \frac{0.002021}{1.107149} \times 100\% \approx \mathbf{0.18\%}$$
   Kaidah Simpson 1/3 menghasilkan akurasi yang luar biasa tinggi (kesalahan di bawah $0.2\%$).

---

### Soal UAS 2: Persamaan Diferensial Biasa via Metode Runge-Kutta Orde 4 (RK4)
**Deskripsi Soal:**
Diberikan masalah nilai awal (PDB):
$$\frac{dy}{dx} = x + y, \quad \text{dengan kondisi awal } y(0) = 1$$
Tentukan nilai estimasi $y(0.2)$ menggunakan **Metode Runge-Kutta Orde 4 (RK4)** dengan satu langkah ukuran ($h = 0.2$)!

**Kunci Pembahasan & Solusi:**
1. **Fungsi Kemiringan:** $f(x, y) = x + y$, dengan $x_0 = 0, y_0 = 1, h = 0.2$.
2. **Hitung Keempat Nilai Kemiringan $k$:**
   * **$k_1$:**
     $$k_1 = f(x_0, y_0) = 0 + 1 = \mathbf{1.0000}$$
   * **$k_2$ (di titik tengah $x_0 + h/2, y_0 + (h/2)k_1$):**
     $$x = 0 + \frac{0.2}{2} = 0.1, \quad y = 1 + (0.1)(1.0) = 1.1$$
     $$k_2 = f(0.1, 1.1) = 0.1 + 1.1 = \mathbf{1.2000}$$
   * **$k_3$ (di titik tengah dengan $k_2$):**
     $$x = 0.1, \quad y = 1 + (0.1)(1.2) = 1.12$$
     $$k_3 = f(0.1, 1.12) = 0.1 + 1.12 = \mathbf{1.2200}$$
   * **$k_4$ (di titik akhir $x_0 + h, y_0 + h \cdot k_3$):**
     $$x = 0 + 0.2 = 0.2, \quad y = 1 + (0.2)(1.22) = 1 + 0.244 = 1.244$$
     $$k_4 = f(0.2, 1.244) = 0.2 + 1.244 = \mathbf{1.4440}$$
3. **Kombinasi Tertimbang Rata-Rata RK4:**
   $$\begin{aligned}
   y(0.2) &= y_0 + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4) \\
   &= 1 + \frac{0.2}{6} \big[ 1.0000 + 2(1.2000) + 2(1.2200) + 1.4440 \big] \\
   &= 1 + \frac{0.2}{6} \big[ 1.0000 + 2.4000 + 2.4400 + 1.4440 \big] \\
   &= 1 + \frac{0.2}{6} \big[ 7.2840 \big] \\
   &= 1 + 0.2428 = \mathbf{1.2428}
   \end{aligned}$$
   *(Verifikasi analitis: Solusi eksak PDB adalah $y(x) = 2e^x - x - 1$. Untuk $x = 0.2 \implies y(0.2) = 2e^{0.2} - 0.2 - 1 = 2(1.2214) - 1.2 = 1.2428$. Hasil RK4 tepat sama hingga 4 tempat desimal!).*

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa Metode Newton-Raphson memiliki konvergensi kuadratik dan dalam kondisi apa metode ini dapat gagal konvergen (divergen)?"
**Jawaban Komprehensif:**
* **Konvergensi Kuadratik:** Berdasarkan ekspansi deret Taylor di sekitar akar sejati $r$, galat pada iterasi berikutnya sebanding dengan kuadrat galat iterasi saat ini: $e_{n+1} \approx C \cdot e_n^2$. Artinya, jika pada iterasi saat ini galat bernilai $10^{-2}$, maka pada iterasi berikutnya galat menyusut drastis menjadi sekitar $10^{-4}$, melipatgandakan jumlah digit presisi setiap langkah.
* **Kondisi Kegagalan Divergen:**
  1. Jika turunan pertama bernilai nol atau sangat mendekati nol ($f'(x_n) \approx 0$), rumus membagi dengan nol dan garis singgung menjadi sejajar sumbu-$X$, melempar tebakan berikutnya ke tak hingga.
  2. Jika tebakan awal berada di dekat titik infleksi ($f''(x) = 0$), metode dapat terjebak dalam osilasi siklus tak berujung (*infinite limit cycle*).
  3. Jika kurva memiliki beberapa akar berdekatan, tebakan awal yang sedikit melenceng dapat meloncat ke akar lain yang tidak diinginkan.

### Q2: "Mengapa Metode Gauss-Seidel umumnya lebih cepat konvergen daripada Metode Jacobi dalam menyelesaikan SPL secara numerik?"
**Jawaban Komprehensif:**
Pada **Metode Jacobi**, seluruh nilai variabel baru pada iterasi $(k+1)$ dihitung murni hanya berdasarkan nilai variabel lama dari iterasi sebelumnya $(k)$, sehingga pembaruan data terjadi secara serentak di akhir siklus.
Sebaliknya, pada **Metode Gauss-Seidel**, segera setelah sebuah variabel (misalnya $x_1$) selesai dihitung nilainya pada iterasi saat ini, nilai baru yang lebih akurat tersebut **langsung digunakan seketika** di baris berikutnya untuk menghitung $x_2, x_3$, dan seterusnya dalam iterasi yang sama. Pemanfaatan informasi teranyar ini mempercepat penyusutan vektor residu galat, sehingga secara teoritis laju konvergensi Gauss-Seidel sekitar **dua kali lebih cepat** dibandingkan metode Jacobi.
