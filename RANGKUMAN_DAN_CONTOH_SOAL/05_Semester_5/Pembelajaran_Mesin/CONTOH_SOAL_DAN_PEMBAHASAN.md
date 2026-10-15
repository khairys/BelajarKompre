# Bank Contoh Soal & Pembahasan: Pembelajaran Mesin

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Pembelajaran Mesin Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Sukmawati Nur Endah, S.Si., M.Kom., Rismiyati, B.Eng., M.Cs., dkk. & Bank Soal HMIF 2018–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (NAIVE BAYES, DECISION TREE & K-NN)

### Soal UTS 1: Klasifikasi Naive Bayes dengan Laplace Smoothing (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan data latih riil kelulusan tepat waktu mahasiswa dengan 10 sampel data:

| No | IPK ($X_1$) | Keaktifan Organisasi ($X_2$) | Status Skripsi ($X_3$) | Lulus Tepat Waktu ($Y$) |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Tinggi | Aktif | Lancar | **Ya** |
| 2 | Tinggi | Pasif | Lancar | **Ya** |
| 3 | Sedang | Aktif | Lancar | **Ya** |
| 4 | Tinggi | Aktif | Terkendala | **Ya** |
| 5 | Sedang | Pasif | Lancar | **Ya** |
| 6 | Rendah | Aktif | Terkendala | **Tidak** |
| 7 | Rendah | Pasif | Terkendala | **Tidak** |
| 8 | Sedang | Pasif | Terkendala | **Tidak** |
| 9 | Rendah | Aktif | Lancar | **Tidak** |
| 10 | Sedang | Aktif | Terkendala | **Tidak** |

Terdapat satu mahasiswa baru dengan data uji ($X_{\text{baru}}$):
$$\mathbf{X_{\text{baru}} = (\text{IPK} = \text{Sedang}, \text{Keaktifan} = \text{Aktif}, \text{Skripsi} = \text{Terkendala})}$$
Gunakan **Naive Bayes Classifier** (dengan **Laplace Smoothing $\alpha = 1$**) untuk memprediksi apakah mahasiswa tersebut akan Lulus Tepat Waktu (**Ya** atau **Tidak**)!

**Kunci Pembahasan & Solusi:**
Total sampel $N = 10$.
Jumlah kelas: $Y = \text{"Ya"} \implies 5$ sampel; $Y = \text{"Tidak"} \implies 5$ sampel.
Jumlah nilai unik: $\text{IPK} = 3$ (Tinggi, Sedang, Rendah); $\text{Keaktifan} = 2$ (Aktif, Pasif); $\text{Skripsi} = 2$ (Lancar, Terkendala).

1. **Probabilitas Prior $P(Y)$ (dengan Laplace Smoothing):**
   $$P(Y = \text{Ya}) = \frac{5 + 1}{10 + 2} = \frac{6}{12} = \mathbf{0.50}$$
   $$P(Y = \text{Tidak}) = \frac{5 + 1}{10 + 2} = \frac{6}{12} = \mathbf{0.50}$$

2. **Probabilitas Likelihood Bersyarat untuk Kelas $Y = \text{Ya}$ ($N_{\text{Ya}} = 5$):**
   * $P(\text{IPK}=\text{Sedang} \mid \text{Ya}) = \frac{\text{Count}(\text{Sedang}, \text{Ya}) + 1}{N_{\text{Ya}} + V_{\text{IPK}}} = \frac{2 + 1}{5 + 3} = \frac{3}{8} = \mathbf{0.375}$
   * $P(\text{Keaktifan}=\text{Aktif} \mid \text{Ya}) = \frac{\text{Count}(\text{Aktif}, \text{Ya}) + 1}{N_{\text{Ya}} + V_{\text{Keaktifan}}} = \frac{3 + 1}{5 + 2} = \frac{4}{7} \approx \mathbf{0.5714}$
   * $P(\text{Skripsi}=\text{Terkendala} \mid \text{Ya}) = \frac{\text{Count}(\text{Terkendala}, \text{Ya}) + 1}{N_{\text{Ya}} + V_{\text{Skripsi}}} = \frac{1 + 1}{5 + 2} = \frac{2}{7} \approx \mathbf{0.2857}$
   * *Posterior Numerator untuk Ya:*
     $$P(\text{Ya} \mid X) \propto P(\text{Ya}) \times \prod P(x_i \mid \text{Ya})$$
     $$P(\text{Ya} \mid X) \propto 0.50 \times 0.375 \times 0.5714 \times 0.2857 \approx \mathbf{0.03061}$$

3. **Probabilitas Likelihood Bersyarat untuk Kelas $Y = \text{Tidak}$ ($N_{\text{Tidak}} = 5$):**
   * $P(\text{IPK}=\text{Sedang} \mid \text{Tidak}) = \frac{\text{Count}(\text{Sedang}, \text{Tidak}) + 1}{N_{\text{Tidak}} + V_{\text{IPK}}} = \frac{2 + 1}{5 + 3} = \frac{3}{8} = \mathbf{0.375}$
   * $P(\text{Keaktifan}=\text{Aktif} \mid \text{Tidak}) = \frac{\text{Count}(\text{Aktif}, \text{Tidak}) + 1}{N_{\text{Tidak}} + V_{\text{Keaktifan}}} = \frac{3 + 1}{5 + 2} = \frac{4}{7} \approx \mathbf{0.5714}$
   * $P(\text{Skripsi}=\text{Terkendala} \mid \text{Tidak}) = \frac{\text{Count}(\text{Terkendala}, \text{Tidak}) + 1}{N_{\text{Tidak}} + V_{\text{Skripsi}}} = \frac{4 + 1}{5 + 2} = \frac{5}{7} \approx \mathbf{0.7143}$
   * *Posterior Numerator untuk Tidak:*
     $$P(\text{Tidak} \mid X) \propto P(\text{Tidak}) \times \prod P(x_i \mid \text{Tidak})$$
     $$P(\text{Tidak} \mid X) \propto 0.50 \times 0.375 \times 0.5714 \times 0.7143 \approx \mathbf{0.07652}$$

4. **Keputusan Klasifikasi:**
   Karena $P(\text{Tidak} \mid X) = 0.07652 > P(\text{Ya} \mid X) = 0.03061$, maka model memprediksi mahasiswa tersebut:
   $$\mathbf{\hat{Y} = \text{"TIDAK LULUS TEPAT WAKTU"}}$$
   *(Probabilitas normalisasi: $P(\text{Tidak}) = \frac{0.07652}{0.07652 + 0.03061} \approx \mathbf{71.4\%}$).*

---

### Soal UTS 2: Perhitungan Information Gain Pemilihan Akar Decision Tree (ID3)
**Deskripsi Soal:**
Dari kumpulan data 14 hari aktivitas tenis, diketahui status keputusan bermain (*Play Tennis*): **9 hari "Yes"** dan **5 hari "No"**.
Atribut cuaca (*Outlook*) memiliki 3 kategori nilai:
* *Sunny (Cerah):* 2 "Yes", 3 "No" (Total 5)
* *Overcast (Mendung):* 4 "Yes", 0 "No" (Total 4)
* *Rain (Hujan):* 3 "Yes", 2 "No" (Total 5)

Hitung nilai **Entropi Awal $H(S)$** dan **Information Gain $IG(S, \text{Outlook})$**!

**Kunci Pembahasan & Solusi:**
1. **Entropi Awal Dataset $S$ ($9+, 5-$):**
   $$H(S) = -\left(\frac{9}{14} \log_2 \frac{9}{14}\right) - \left(\frac{5}{14} \log_2 \frac{5}{14}\right)$$
   $$H(S) = -(0.6429 \times (-0.6374)) - (0.3571 \times (-1.4855)) = 0.4098 + 0.5305 = \mathbf{0.9403}$$

2. **Entropi Masing-Masing Cabang Atribut Outlook:**
   * **Cabang Sunny ($2+, 3-$):**
     $$H(S_{\text{Sunny}}) = -\left(\frac{2}{5} \log_2 \frac{2}{5}\right) - \left(\frac{3}{5} \log_2 \frac{3}{5}\right) = -(0.4 \times (-1.3219)) - (0.6 \times (-0.7370)) = \mathbf{0.9710}$$
   * **Cabang Overcast ($4+, 0-$):**
     Karena bersifat murni homogen (semua Yes), maka:
     $$H(S_{\text{Overcast}}) = \mathbf{0.0}$$
   * **Cabang Rain ($3+, 2-$):**
     $$H(S_{\text{Rain}}) = -\left(\frac{3}{5} \log_2 \frac{3}{5}\right) - \left(\frac{2}{5} \log_2 \frac{2}{5}\right) = \mathbf{0.9710}$$

3. **Perhitungan Information Gain ($IG(S, \text{Outlook})$):**
   $$IG(S, \text{Outlook}) = H(S) - \left[ \frac{5}{14} H(S_{\text{Sunny}}) + \frac{4}{14} H(S_{\text{Overcast}}) + \frac{5}{14} H(S_{\text{Rain}}) \right]$$
   $$IG(S, \text{Outlook}) = 0.9403 - \left[ \frac{5}{14}(0.9710) + \frac{4}{14}(0) + \frac{5}{14}(0.9710) \right]$$
   $$IG(S, \text{Outlook}) = 0.9403 - [0.3468 + 0 + 0.3468] = 0.9403 - 0.6936 = \mathbf{0.2467}$$
   *(Information Gain sebesar 0.2467 ini kemudian dibandingkan dengan atribut lain seperti Humidity dan Wind untuk menentukan pemenang akar utama).*

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (K-MEANS CLUSTERING & EVALUASI CONFUSION MATRIX)

### Soal UAS 1: Simulasi Iterasi K-Means Clustering (Soal Asli UAS Undip 2022)
**Deskripsi Soal:**
Diberikan 4 buah objek data 2D:
* $A(1, 1), \quad B(2, 1), \quad C(4, 3), \quad D(5, 4)$

Ditentukan $K = 2$ klaster dengan centroid awal diinisialisasi pada data:
$$C_1 = A(1, 1) \quad \text{dan} \quad C_2 = B(2, 1)$$
Lakukan perhitungan **Iterasi Pertama Algoritma K-Means**:
1. Hitung matriks jarak Euclidean dari setiap data ke kedua centroid!
2. Tentukan pembagian anggota klaster pada iterasi pertama!
3. Hitung posisi koordinat centroid baru ($C_1^{\text{baru}}$ dan $C_2^{\text{baru}}$)!

**Kunci Pembahasan & Solusi:**
1. **Perhitungan Jarak Euclidean $d = \sqrt{(x - x_c)^2 + (y - y_c)^2}$:**
   * **Data $A(1, 1)$:**
     * $d(A, C_1) = \sqrt{(1-1)^2 + (1-1)^2} = 0$
     * $d(A, C_2) = \sqrt{(1-2)^2 + (1-1)^2} = 1$
     * Karena $0 < 1 \implies$ Masuk ke **Klaster 1**.
   * **Data $B(2, 1)$:**
     * $d(B, C_1) = \sqrt{(2-1)^2 + (1-1)^2} = 1$
     * $d(B, C_2) = \sqrt{(2-2)^2 + (1-1)^2} = 0$
     * Karena $0 < 1 \implies$ Masuk ke **Klaster 2**.
   * **Data $C(4, 3)$:**
     * $d(C, C_1) = \sqrt{(4-1)^2 + (3-1)^2} = \sqrt{9 + 4} = \sqrt{13} \approx 3.61$
     * $d(C, C_2) = \sqrt{(4-2)^2 + (3-1)^2} = \sqrt{4 + 4} = \sqrt{8} \approx 2.83$
     * Karena $2.83 < 3.61 \implies$ Masuk ke **Klaster 2**.
   * **Data $D(5, 4)$:**
     * $d(D, C_1) = \sqrt{(5-1)^2 + (4-1)^2} = \sqrt{16 + 9} = \sqrt{25} = 5$
     * $d(D, C_2) = \sqrt{(5-2)^2 + (4-1)^2} = \sqrt{9 + 9} = \sqrt{18} \approx 4.24$
     * Karena $4.24 < 5 \implies$ Masuk ke **Klaster 2**.

2. **Hasil Pembagian Klaster Iterasi 1:**
   * **Klaster 1:** $\{ A \}$
   * **Klaster 2:** $\{ B, C, D \}$

3. **Perhitungan Posisi Centroid Baru:**
   * $C_1^{\text{baru}} = \text{Mean}(\{A\}) = \mathbf{(1.0, 1.0)}$
   * $C_2^{\text{baru}} = \text{Mean}(\{B, C, D\}) = \left( \frac{2 + 4 + 5}{3}, \frac{1 + 3 + 4}{3} \right) = \left( \frac{11}{3}, \frac{8}{3} \right) \approx \mathbf{(3.67, 2.67)}$

---

### Soal UAS 2: Evaluasi Model Klasifikasi Medis (Confusion Matrix & F1-Score)
**Deskripsi Soal:**
Sebuah model AI diagnosis deteksi kanker payudara diuji pada $1.000$ pasien dan menghasilkan tabel kontingensi (*Confusion Matrix*) berikut:
* Pasien aktual memiliki kanker (Positif): Model memprediksi $80$ orang kanker (**TP** $= 80$) dan salah memprediksi $20$ orang sebagai sehat (**FN** $= 20$).
* Pasien aktual sehat (Negatif): Model memprediksi $850$ orang sehat (**TN** $= 850$) dan salah memprediksi $50$ orang sebagai kanker (**FP** $= 50$).

**Tugas:**
1. Hitung nilai **Accuracy**, **Precision**, **Recall (Sensitivity)**, dan **F1-Score**!
2. Jika dokter ingin meminimalkan pasien kanker yang terlewat tidak terobati (*lolos dari diagnosis*), metrik evaluasi manakah yang paling krusial diprioritaskan? Mengapa nilai Accuracy sebesar $93\%$ pada kasus ini dapat menyesatkan?

**Kunci Pembahasan & Solusi:**
1. **Perhitungan Metrik:**
   * **Accuracy:**
     $$\text{Acc} = \frac{\text{TP} + \text{TN}}{\text{Total}} = \frac{80 + 850}{1000} = \frac{930}{1000} = \mathbf{93.0\%}$$
   * **Precision:**
     $$\text{Prec} = \frac{\text{TP}}{\text{TP} + \text{FP}} = \frac{80}{80 + 50} = \frac{80}{130} \approx \mathbf{61.54\%}$$
   * **Recall (Sensitivity):**
     $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} = \frac{80}{80 + 20} = \frac{80}{100} = \mathbf{80.0\%}$$
   * **F1-Score:**
     $$\text{F1} = 2 \times \frac{\text{Prec} \times \text{Recall}}{\text{Prec} + \text{Recall}} = 2 \times \frac{0.6154 \times 0.80}{0.6154 + 0.80} = 2 \times \frac{0.4923}{1.4154} \approx \mathbf{69.57\%}$$

2. **Analisis Kritis Diagnostik:**
   * Metrik yang paling krusial adalah **RECALL (Sensitivity)**. Pada ranah medis diagnosis penyakit mematikan, kesalahan jenis **False Negative (FN)** berakibat fatal: pasien penderita kanker diberitahu bahwa ia sehat, sehingga kanker tidak diobati hingga stadium terminal.
   * **Mengapa Akurasi Menyesatkan:** Dataset ini bersifat tidak seimbang (*Imbalanced Dataset*, 900 sehat vs 100 kanker). Model *dummy* bodoh yang memprediksi SEMUA pasien sehat tanpa memeriksa apapun akan tetap mendapatkan akurasi semu sebesar $90\%$, namun model tersebut memiliki nilai Recall $0\%$ (membunuh 100 pasien kanker). Oleh karena itu, metrik F1-Score dan Recall menjadi standar evaluasi wajib.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan apa yang dimaksud dengan Bias-Variance Tradeoff dan bagaimana Anda mendiagnosis apakah model Machine Learning Anda sedang mengalami Overfitting atau Underfitting?"
**Jawaban Komprehensif:**
* **Bias-Variance Tradeoff:** Dilema optimasi dalam meminimalkan dua sumber galat model machine learning yang saling bertolak belakang:
  * **Bias (Underfitting):** Terjadi ketika asumsi model terlalu sederhana untuk menangkap kompleksitas hubungan data nyata. Diagnosis: Akurasi pada data latih (*training score*) dan data uji (*validation score*) sama-sama rendah.
  * **Variance (Overfitting):** Terjadi ketika model terlalu fleksibel dan kompleks sehingga menghafal detail derau acak (*random noise*) pada data latih. Diagnosis: Akurasi pada data latih sangat tinggi mendekati 100%, tetapi akurasi pada data validasi/uji anjlok drastis (*Generalization Gap* yang lebar).
* **Solusi Penyeimbang:** Mereduksi overfitting dapat dilakukan dengan: menambah jumlah sampel data latih, memangkas fitur (*feature selection* / PCA), memperkecil kedalaman pohon (*pruning*), atau menambahkan parameter penalti regulerisasi L1 (Lasso) atau L2 (Ridge).

### Q2: "Bagaimana cara kerja Kernel Trick pada Support Vector Machine (SVM) dalam menyelesaikan klasifikasi data non-linier tanpa meledakkan kompleksitas komputasi?"
**Jawaban Komprehensif:**
Ketika data tidak dapat dipisahkan oleh garis lurus atau bidang datar pada ruang masukan asli berdimensi rendah ($X$), teorema Cover menyatakan bahwa jika data tersebut dipetakan ke dalam ruang fitur berdimensi lebih tinggi ($\Phi(X)$), data tersebut akan menjadi terpisahkan secara linier dengan probabilitas tinggi.
Namun, menghitung fungsi pemetaan $\Phi(X)$ secara eksplisit ke dimensi tak berhingga (seperti pada Kernel RBF/Gaussian) akan menyebabkan komputasi meledak (*curse of dimensionality*).
Di sinilah **Kernel Trick** bekerja:
* Pada formulasi dual SVM, algoritma pelatihan hanya membutuhkan operasi **perkalian titik (*dot product*) antar-vektor**: $\langle \Phi(x_i), \Phi(x_j) \rangle$.
* **Fungsi Kernel $K(x_i, x_j)$ menghitung hasil perkalian titik di ruang dimensi tinggi tersebut secara langsung menggunakan koordinat data di ruang dimensi rendah aslinya**, tanpa pernah perlu mengetahui bentuk eksplisit atau koordinat dari $\Phi(X)$. Hal ini memungkinkan SVM membentuk batas keputusan kurva yang sangat rumit dengan efisiensi komputasi yang tetap rendah.
