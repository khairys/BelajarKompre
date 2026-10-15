# Bank Contoh Soal & Pembahasan: Statistika

> Sumber rujukan: Kurasi modul resmi, latihan terstruktur, dan bank soal standar Ujian Komprehensif Statistika Departemen Informatika Universitas Diponegoro.

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (STATISTIKA DESKRIPTIF, TEOREMA BAYES & DISTRIBUSI)

### Soal UTS 1: Penerapan Teorema Bayes pada Sistem Filter Spam Email
**Deskripsi Soal:**
Sebuah sistem penyaring email (*spam filter*) di server Informatika Undip memproses ribuan surel masuk setiap hari. Dari data historis diketahui bahwa:
* $20\%$ dari seluruh surel yang masuk adalah **Spam** ($P(\text{Spam}) = 0.20$), dan $80\%$ sisanya adalah email penting/bukan spam ($P(\text{BukanSpam}) = 0.80$).
* Dari email yang tergolong Spam, $80\%$ di antaranya memuat kata kunci `"promo"` ($P(\text{Promo} \mid \text{Spam}) = 0.80$).
* Dari email yang Bukan Spam, hanya $5\%$ yang memuat kata kunci `"promo"` ($P(\text{Promo} \mid \text{BukanSpam}) = 0.05$).

Sebuah email baru masuk ke server dan terdeteksi mengandung kata `"promo"`. Berapakah probabilitas posterior bahwa email tersebut **benar-benar merupakan Spam**?

**Kunci Pembahasan & Solusi:**
1. **Identifikasi Variabel Probabilitas:**
   * Prior Probability: $P(S) = 0.20, \quad P(B) = 0.80$
   * Likelihood: $P(P \mid S) = 0.80, \quad P(P \mid B) = 0.05$
2. **Hitung Probabilitas Total Kejadian Kata `"promo"` ($P(\text{Promo})$):**
   $$\begin{aligned}
   P(P) &= P(P \mid S) \cdot P(S) + P(P \mid B) \cdot P(B) \\
   &= (0.80 \times 0.20) + (0.05 \times 0.80) \\
   &= 0.16 + 0.04 = \mathbf{0.20}
   \end{aligned}$$
3. **Hitung Probabilitas Posterior Menggunakan Teorema Bayes:**
   $$P(S \mid P) = \frac{P(P \mid S) \cdot P(S)}{P(P)} = \frac{0.80 \times 0.20}{0.20} = \frac{0.16}{0.20} = \mathbf{0.80 \text{ atau } 80\%}$$
4. **Kesimpulan:**
   Jika sebuah email baru memuat kata `"promo"`, probabilitas bahwa email tersebut adalah spam melonjak dari semula hanya $20\%$ (prior) menjadi **$80\%$ (posterior)**.

---

### Soal UTS 2: Distribusi Probabilitas Binomial pada Keandalan Jaringan
**Deskripsi Soal:**
Sebuah protokol komunikasi jaringan mengirimkan data dalam kelompok berisi $n = 10$ paket data secara independen. Probabilitas sebuah paket data mengalami kerusakan (*corrupted / error*) selama transmisi adalah $p = 0.10$.
1. Berapakah peluang tepat terdapat $2$ paket data yang rusak dalam satu kali transmisi?
2. Berapakah peluang transmisi berhasil sempurna tanpa ada satu pun paket yang rusak ($P(X = 0)$)?

**Kunci Pembahasan & Solusi:**
1. **Peluang Tepat 2 Paket Rusak ($X = 2$):**
   Variabel acak $X \sim B(n=10, p=0.10)$.
   $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}$$
   $$\begin{aligned}
   P(X = 2) &= \binom{10}{2} (0.10)^2 (0.90)^{10 - 2} \\
   &= \frac{10 \times 9}{2 \times 1} \times (0.01) \times (0.90)^8 \\
   &= 45 \times 0.01 \times 0.430467 \\
   &= 0.45 \times 0.430467 \approx \mathbf{0.1937 \text{ atau } 19.37\%}
   \end{aligned}$$
2. **Peluang Transmisi Berhasil Sempurna ($X = 0$):**
   $$\begin{aligned}
   P(X = 0) &= \binom{10}{0} (0.10)^0 (0.90)^{10} \\
   &= 1 \times 1 \times (0.90)^{10} \approx \mathbf{0.3487 \text{ atau } 34.87\%}
   \end{aligned}$$

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (UJI HIPOTESIS & REGRESI LINIER)

### Soal UAS 1: Uji Hipotesis Satu Sampel (Uji t) Latensi Server
**Deskripsi Soal:**
Sebuah tim pengembang mengklaim bahwa pembaruan arsitektur sistem operasi mikro berhasil menurunkan rata-rata latensi respons server menjadi **kurang dari 200 ms** ($\mu < 200$). 
Untuk menguji klaim tersebut, dilakukan pengujian independen terhadap $n = 25$ sampel permintaan. Diperoleh rata-rata sampel latensi $\bar{x} = 194\text{ ms}$ dengan standar deviasi sampel $s = 15\text{ ms}$.
Ujilah apakah klaim pengembang tersebut signifikan secara statistik pada tingkat signifikansi $\alpha = 0.05$! *(Diketahui nilai kritis $t_{0.05, df=24} = -1.711$).*

**Kunci Pembahasan & Solusi:**
1. **Formulasi Hipotesis Statistik (Uji Satu Sisi Kiri):**
   * $H_0 : \mu \ge 200\text{ ms}$ (Pembaruan tidak berhasil menurunkan latensi di bawah 200 ms).
   * $H_1 : \mu < 200\text{ ms}$ (Pembaruan berhasil menurunkan latensi di bawah 200 ms).
2. **Tingkat Signifikansi & Derajat Bebas:**
   * $\alpha = 0.05$
   * Derajat bebas: $df = n - 1 = 25 - 1 = 24$.
   * Daerah Kritis Penolakan $H_0$: Tolak $H_0$ jika $t_{\text{hitung}} < -t_{\text{kritis}} = -1.711$.
3. **Hitung Nilai Statistik Uji $t$:**
   $$t_{\text{hitung}} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{194 - 200}{15 / \sqrt{25}} = \frac{-6}{15 / 5} = \frac{-6}{3} = \mathbf{-2.000}$$
4. **Keputusan Uji Statistik:**
   Karena $t_{\text{hitung}} = -2.000 < -1.711$ (nilai uji jatuh di dalam daerah penolakan kritis $H_0$), maka **$H_0$ DITOLAK**.
5. **Kesimpulan Akademik:**
   Pada tingkat signifikansi $5\%$, terdapat bukti empiris statistik yang cukup untuk menyimpulkan bahwa pembaruan arsitektur sistem berhasil menurunkan rata-rata latensi server menjadi kurang dari 200 ms.

---

### Soal UAS 2: Model Regresi Linier Sederhana & Korelasi Pearson
**Deskripsi Soal:**
Peneliti ingin memodelkan pengaruh ukuran file masukan ($X$, dalam Megabyte) terhadap waktu pemrosesan enkripsi algoritma ($Y$, dalam milidetik). Dari 5 data eksperimen diperoleh ringkasan statistik:
$n = 5, \; \sum X = 15, \; \sum Y = 35, \; \sum X^2 = 55, \; \sum Y^2 = 255, \; \sum XY = 118$.
1. Hitunglah nilai **Koefisien Korelasi Pearson ($r$)** dan jelaskan maknanya!
2. Bentuklah persamaan garis regresi linier sederhana $\hat{Y} = a + bX$ menggunakan metode *Ordinary Least Squares*!
3. Prediksikan estimasi waktu enkripsi jika ukuran file masukan adalah $X = 6\text{ MB}$!

**Kunci Pembahasan & Solusi:**
1. **Koefisien Korelasi Pearson ($r$):**
   $$r = \frac{n \sum XY - (\sum X)(\sum Y)}{\sqrt{[n\sum X^2 - (\sum X)^2][n\sum Y^2 - (\sum Y)^2]}}$$
   $$\begin{aligned}
   \text{Pembilang} &= 5(118) - (15)(35) = 590 - 525 = 65 \\
   \text{Penyebut} &= \sqrt{[5(55) - (15)^2][5(255) - (35)^2]} = \sqrt{[275 - 225][1275 - 1225]} \\
   &= \sqrt{50 \times 50} = 50 \\
   r &= \frac{65}{50} = \mathbf{0.9286}
   \end{aligned}$$
   *Makna:* Nilai $r = +0.929$ menunjukkan hubungan linier positif yang **sangat kuat** antara ukuran file dengan waktu enkripsi (semakin besar file, waktu enkripsi meningkat linier).
2. **Membentuk Persamaan Garis Regresi ($\hat{Y} = a + bX$):**
   * **Kemiringan ($b$):**
     $$b = \frac{n \sum XY - (\sum X)(\sum Y)}{n \sum X^2 - (\sum X)^2} = \frac{65}{50} = \mathbf{1.30}$$
   * **Titik Potong Intersep ($a$):**
     $$\bar{X} = \frac{15}{5} = 3, \quad \bar{Y} = \frac{35}{5} = 7$$
     $$a = \bar{Y} - b\bar{X} = 7 - (1.30 \times 3) = 7 - 3.9 = \mathbf{3.10}$$
   * **Persamaan Garis Regresi:**
     $$\mathbf{\hat{Y} = 3.10 + 1.30 X}$$
3. **Prediksi Waktu Enkripsi untuk $X = 6\text{ MB}$:**
   $$\hat{Y} = 3.10 + 1.30(6) = 3.10 + 7.80 = \mathbf{10.90\text{ ms}}$$

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan apa yang dinyatakan oleh Teorema Limit Pusat (Central Limit Theorem) dan mengapa teorema ini sangat penting dalam riset inferensial?"
**Jawaban Komprehensif:**
* **Inti Teorema:** Teorema Limit Pusat menyatakan bahwa apabila sampel acak berukuran cukup besar ($n \ge 30$) ditarik berulang kali dari sembarang populasi dengan bentuk distribusi apa pun (bahkan jika populasi aslinya berbentuk miring/skewed, seragam, atau bimodal), maka distribusi rata-rata sampelnya ($\bar{X}$) akan selalu berkonvergensi mengikuti **Distribusi Normal**.
* **Urgensi dalam Riset:** Teorema ini menjadi fondasi sahnya penggunaan uji statistik parametrik (seperti Uji Z, Uji t, dan ANOVA) pada sampel data dunia nyata tanpa peneliti harus mencemaskan apakah bentuk distribusi populasi aslinya normal atau tidak, asalkan ukuran sampel pengamatan memenuhi $n \ge 30$.

### Q2: "Dalam pengujian hipotesis statistik, jelaskan perbedaan antara Galat Tipe I (Type I Error) dan Galat Tipe II (Type II Error), serta berikan analoginya dalam deteksi malware!"
**Jawaban Komprehensif:**
* **Galat Tipe I ($\alpha$ / False Positive):** Kondisi ketika kita menolak Hipotesis Nol ($H_0$) padahal kenyataannya $H_0$ tersebut benar.
  * *Analogi Antivirus/Malware:* Antivirus menandai dan menghapus berkas program yang sepenuhnya aman/bersih sebagai virus (*false alarm*).
* **Galat Tipe II ($\beta$ / False Negative):** Kondisi ketika kita gagal menolak/menerima Hipotesis Nol ($H_0$) padahal kenyataannya $H_0$ tersebut salah.
  * *Analogi Antivirus/Malware:* Antivirus gagal mendeteksi malware berbahaya dan membiarkannya berjalan leluasa karena menganggapnya sebagai program normal.
Dalam sistem keamanan siber dan medis, Galat Tipe II biasanya dianggap jauh lebih berbahaya daripada Galat Tipe I.
