# Bank Contoh Soal & Pembahasan: Penambangan Data

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Penambangan Data / Data Mining Departemen Informatika Universitas Diponegoro (Koleksi Pengampu & Bank Soal HMIF 2017–2023).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (CRISP-DM & ATURAN ASOSIASI APRIORI)

### Soal UTS 1: Siklus CRISP-DM pada Prediksi Penyakit Kardiovaskular (Soal Asli UTS Undip 2022)
**Deskripsi Soal:**
Penyakit kardiovaskular (*Cardiovascular Diseases - CVDs*) merupakan penyebab kematian nomor satu secara global (merenggut 17,9 juta jiwa setiap tahun). Sebuah rumah sakit di Semarang ingin membangun model prediktif berbasis penambangan data untuk mendeteksi dini pasien yang berisiko tinggi terkena CVDs berdasarkan rekam medis klinis (tekanan darah, kadar kolesterol, glukosa, indeks massa tubuh/BMI, kebiasaan merokok, dan usia).
Jelaskan penerapan **6 fase metodologi CRISP-DM** yang harus dilakukan oleh tim data science secara komprehensif!

**Kunci Pembahasan & Solusi:**
1. **Fase 1: Business Understanding:**
   * *Tujuan Bisnis:* Menurunkan angka mortalitas serangan jantung mendadak melalui deteksi dini pasien berisiko tinggi.
   * *Sasaran Data Mining:* Membangun model klasifikasi biner yang mampu memprediksi status risiko pasien (`Berisiko Tinggi = 1`, `Normal/Rendah = 0`) dengan memprioritaskan nilai **Recall $\ge 90\%$** untuk mencegah terjadinya *False Negative*.
2. **Fase 2: Data Understanding:**
   * Mengumpulkan 10.000 data historis rekam medis pasien 5 tahun terakhir.
   * Melakukan eksplorasi data (*EDA*): Memeriksa distribusi nilai umur, korelasi antar-fitur numerik (misal: korelasi kolesterol dan tekanan darah sistolik), dan mendeteksi adanya data janggal (seperti tekanan darah bernilai 0).
3. **Fase 3: Data Preparation:**
   * *Cleaning:* Menghapus atau mengimputasi nilai missing value pada kolom kadar glukosa menggunakan median data.
   * *Outlier Treatment:* Memeriksa nilai tekanan darah $> 250$ mmHg menggunakan metode *Interquartile Range (IQR)*.
   * *Feature Engineering:* Menghitung fitur turunan *Body Mass Index (BMI)* dari rasio berat badan terhadap kuadrat tinggi badan.
   * *Encoding & Scaling:* Mengonversi variabel kategoris (gender, merokok) via *One-Hot Encoding* dan menormalisasi variabel numerik menggunakan *Z-score Standardization*.
4. **Fase 4: Modeling:**
   * Memilih beberapa algoritma klasifikasi ensemble: Random Forest, XGBoost, dan LightGBM.
   * Melakukan penalaan hiperparameter (*Hyperparameter Tuning*) menggunakan teknik *GridSearchCV* yang dipadukan dengan *Stratified 5-Fold Cross Validation*.
5. **Fase 5: Evaluation:**
   * Menguji model pada data uji terpisah (*Holdout Test Set*).
   * Mengevaluasi metrik: Confusion Matrix, Recall, Precision, F1-Score, dan AUC-ROC.
   * Melakukan analisis keterjelasan model (*Explainable AI*) menggunakan SHAP (*SHapley Additive exPlanations*) untuk memvalidasi bersama dokter spesialis jantung apakah fitur-fitur yang dianggap paling penting oleh model (seperti usia dan kolesterol LDL) konsisten dengan teori patofisiologi medis.
6. **Fase 6: Deployment:**
   * Mengemas model AI ke dalam bentuk RESTful API backend menggunakan framework FastAPI dan kontainer Docker.
   * Mengintegrasikan API tersebut ke dalam antarmuka Sistem Informasi Manajemen Rumah Sakit (SIMRS) rawat jalan.

---

### Soal UTS 2: Perhitungan Algoritma Apriori (Support, Confidence & Lift Ratio)
**Deskripsi Soal:**
Diberikan basis data 5 transaksi belanja pada sebuah minimarket:
* Transaksi 1: `{ Roti, Susu }`
* Transaksi 2: `{ Roti, Popok, Bir, Telur }`
* Transaksi 3: `{ Susu, Popok, Bir, Minyak }`
* Transaksi 4: `{ Roti, Susu, Popok, Bir }`
* Transaksi 5: `{ Roti, Susu, Popok, Telur }`

Ambang batas minimum ditetapkan:
* **Minimum Support ($\text{minsup}$) $= 60\%$** (atau minimal muncul pada $3$ transaksi).
* **Minimum Confidence ($\text{minconf}$) $= 75\%$**.

**Tugas:**
1. Temukan seluruh **Frequent Itemsets** menggunakan Algoritma Apriori langkah demi langkah!
2. Bangun aturan asosiasi dari *Frequent 2-Itemsets* `{ Popok, Bir }`, hitung nilai **Support**, **Confidence**, dan **Lift Ratio**-nya!

**Kunci Pembahasan & Solusi:**
Total transaksi $N = 5$. Syarat lolos $\text{minsup} \ge 3$ transaksi.

1. **Iterasi 1 (1-Itemset):**
   * `{ Roti }`: 4 transaksi $\implies 80\%$ (Lolos)
   * `{ Susu }`: 4 transaksi $\implies 80\%$ (Lolos)
   * `{ Popok }`: 4 transaksi $\implies 80\%$ (Lolos)
   * `{ Bir }`: 3 transaksi $\implies 60\%$ (Lolos)
   * `{ Telur }`: 2 transaksi $\implies 40\%$ (Gagal / Dipangkas)
   * `{ Minyak }`: 1 transaksi $\implies 20\%$ (Gagal / Dipangkas)
   * **$L_1$ Frequent 1-Itemset:** `{ Roti }, { Susu }, { Popok }, { Bir }`.

2. **Iterasi 2 (2-Itemset):**
   Bangkirkan kandidat $C_2$ dari pasangan elemen $L_1$:
   * `{ Roti, Susu }`: Transaksi 1, 4, 5 $\implies 3/5 = 60\%$ (Lolos)
   * `{ Roti, Popok }`: Transaksi 2, 4, 5 $\implies 3/5 = 60\%$ (Lolos)
   * `{ Roti, Bir }`: Transaksi 2, 4 $\implies 2/5 = 40\%$ (Gagal)
   * `{ Susu, Popok }`: Transaksi 3, 4, 5 $\implies 3/5 = 60\%$ (Lolos)
   * `{ Susu, Bir }`: Transaksi 3, 4 $\implies 2/5 = 40\%$ (Gagal)
   * `{ Popok, Bir }`: Transaksi 2, 3, 4 $\implies 3/5 = \mathbf{60\%}$ (Lolos)
   * **$L_2$ Frequent 2-Itemset:** `{ Roti, Susu }, { Roti, Popok }, { Susu, Popok }, { Popok, Bir }`.

3. **Iterasi 3 (3-Itemset):**
   Kandidat yang mungkin: `{ Roti, Susu, Popok }`:
   * Muncul pada: Transaksi 4, 5 $\implies 2/5 = 40\%$ (Kurang dari 60% $\implies$ Gagal).
   * Tidak ada 3-itemset yang memenuhi syarat. Algoritma berhenti.

4. **Pembentukan Aturan Asosiasi dari $\{ \text{Popok}, \text{Bir} \}$:**
   * **Aturan: $\text{Bir} \implies \text{Popok}$**
     * $\text{Support}(\text{Bir} \implies \text{Popok}) = \frac{\text{Count}(\text{Bir} \cup \text{Popok})}{5} = \frac{3}{5} = \mathbf{60\%}$
     * $\text{Confidence} = \frac{\text{Count}(\text{Bir} \cup \text{Popok})}{\text{Count}(\text{Bir})} = \frac{3}{3} = \mathbf{100\%}$
       *(Memenuhi $\text{minconf} \ge 75\%$).*
     * **Lift Ratio:**
       $$\text{Lift} = \frac{\text{Confidence}}{\text{Support}(\text{Popok})} = \frac{1.00}{4/5} = \frac{1.00}{0.80} = \mathbf{1.25}$$
   * *Interpretasi Bisnis:* Nilai $\text{Lift} = 1.25 > 1$ membuktikan adanya **hubungan asosiasi positif yang kuat**. Konsumen yang membeli Bir memiliki kecenderungan $1.25$ kali lebih besar untuk membeli Popok dibandingkan pembeli umum. Minimarket direkomendasikan menempatkan rak popok bayi di dekat rak minuman bir (*studi kasus legendaris Walmart*).

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (DBSCAN CLUSTERING & TEXT MINING TF-IDF)

### Soal UAS 1: Algoritma Klastering Berbasis Kerapatan (DBSCAN)
**Deskripsi Soal:**
Diberikan himpunan 6 titik data pada ruang koordinat 2D:
$p_1(1, 2), \; p_2(2, 2), \; p_3(2, 3), \; p_4(8, 7), \; p_5(8, 8), \; p_6(25, 25)$.
Parameter DBSCAN disetel: **$\epsilon = 1.5$** dan **$MinPts = 3$** (menggunakan jarak Euclidean).
1. Hitung jumlah tetangga di dalam radius $\epsilon$ untuk setiap titik!
2. Klasifikasikan masing-masing titik ke dalam kategori: **Core Point**, **Border Point**, atau **Noise**!
3. Tentukan klaster yang terbentuk dan titik mana yang dinyatakan sebagai outlier!

**Kunci Pembahasan & Solusi:**
1. **Analisis Lingkungan Radius $\epsilon = 1.5$ ($MinPts = 3$):**
   * Jarak $p_1(1,2)$ ke $p_2(2,2) = 1.0 \le 1.5$.
   * Jarak $p_2(2,2)$ ke $p_3(2,3) = 1.0 \le 1.5$.
   * Jarak $p_1(1,2)$ ke $p_3(2,3) = \sqrt{1^2 + 1^2} = \sqrt{2} \approx 1.414 \le 1.5$.
   * Maka titik $p_1, p_2, p_3$ saling bertetangga satu sama lain.
   * Jarak $p_4(8,7)$ ke $p_5(8,8) = 1.0 \le 1.5$.
   * Titik $p_6(25, 25)$ tidak memiliki tetangga lain (jarak terdekat ke $p_5 \approx 24.1$).

2. **Klasifikasi Tipe Titik:**
   * **Titik $p_1$:** Tetangga di dalam $\epsilon$: $\{ p_1, p_2, p_3 \}$ (Total 3 titik). Karena jumlah tetangga $\ge MinPts$ ($3 \ge 3$) $\implies$ **CORE POINT**.
   * **Titik $p_2$:** Tetangga di dalam $\epsilon$: $\{ p_1, p_2, p_3 \}$ (Total 3 titik) $\implies$ **CORE POINT**.
   * **Titik $p_3$:** Tetangga di dalam $\epsilon$: $\{ p_1, p_2, p_3 \}$ (Total 3 titik) $\implies$ **CORE POINT**.
   * **Titik $p_4$:** Tetangga di dalam $\epsilon$: $\{ p_4, p_5 \}$ (Total 2 titik). Karena $2 < MinPts$ ($2 < 3$), dan bukan tetangga dari core point manapun $\implies$ **NOISE**.
   * **Titik $p_5$:** Tetangga di dalam $\epsilon$: $\{ p_4, p_5 \}$ (Total 2 titik) $\implies$ **NOISE**.
   * **Titik $p_6$:** Hanya dirinya sendiri $\{ p_6 \}$ (Total 1 titik) $\implies$ **NOISE**.

3. **Hasil Pembentukan Klaster:**
   * **Klaster 1:** $\{ p_1, p_2, p_3 \}$ (Membentuk satu klaster padat karena saling *density-connected*).
   * **Titik Noise / Outlier:** $\{ p_4, p_5, p_6 \}$.

---

### Soal UAS 2: Pembobotan Kata TF-IDF dan Cosine Similarity pada Text Mining
**Deskripsi Soal:**
Diberikan sebuah korpus kecil yang memuat total $|D| = 100$ dokumen berita.
Terdapat kata kunci (*term*) **$t = \text{"gempa"}$**.
* Kata "gempa" muncul sebanyak **$5$ kali** di dalam Dokumen A ($\text{TF}(t, A) = 5$).
* Kata "gempa" muncul pada total **$10$ dokumen** di seluruh korpus ($\text{DF}(t) = 10$).

Hitung nilai bobot **$\text{TF-IDF}(t, A)$** menggunakan logaritma basis 10!

**Kunci Pembahasan & Solusi:**
1. **Perhitungan Inverse Document Frequency (IDF):**
   $$\text{IDF}(t) = \log_{10}\left(\frac{|D|}{\text{DF}(t)}\right) = \log_{10}\left(\frac{100}{10}\right) = \log_{10}(10) = \mathbf{1.0}$$

2. **Perhitungan Bobot TF-IDF:**
   $$\text{TF-IDF}(t, A) = \text{TF}(t, A) \times \text{IDF}(t) = 5 \times 1.0 = \mathbf{5.0}$$

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa Algoritma FP-Growth jauh lebih efisien dibandingkan Algoritma Apriori dalam menambang aturan asosiasi pada basis data transaksi berskala raksasa?"
**Jawaban Komprehensif:**
* **Kelemahan Mendasar Algoritma Apriori:**
  1. *Pemindaian Basis Data Berulang-Ulang:* Jika frequent itemset terpanjang berukuran $k$, Apriori harus membaca (*full table scan*) disk basis data sebanyak $k$ kali. Pada dataset transaksi berskala petabyte, I/O disk berulang ini sangat lambat.
  2. *Ledakan Jumlah Kandidat (*Candidate Generation Explosion*):* Menghasilkan jutaan kombinasi kandidat itemset perantara di memori RAM ($C_k = L_{k-1} \bowtie L_{k-1}$) yang sebagian besar pada akhirnya akan dibuang karena tidak memenuhi minsup.
* **Keunggulan Algoritma FP-Growth:**
  1. *Hanya Melakukan 2 Kali Pemindaian Disk:* Basis data hanya dibaca tepat dua kali untuk membangun struktur pohon ringkas yang disebut **FP-Tree (*Frequent Pattern Tree*)**.
  2. *Bebas dari Pembangkitan Kandidat (*No Candidate Generation*):* FP-Tree memadatkan data transaksi sehingga pola-pola yang berbagi awalan item yang sama tumpang tindih pada simpul yang sama. Proses penambangan dilakukan langsung di memori melalui pencarian rekursif *Conditional FP-Tree*, menghasilkan peningkatan kecepatan eksekusi puluhan hingga ratusan kali lipat.

### Q2: "Jelaskan perbedaan mendasar antara pendekatan Ensemble Bagging (seperti Random Forest) dan Boosting (seperti XGBoost), serta kapan masing-masing pendekatan efektif digunakan!"
**Jawaban Komprehensif:**
* **Bagging (Bootstrap Aggregating - e.g., Random Forest):**
  * *Cara Kerja:* Membangun puluhan/ratusan pohon keputusan **secara paralel dan independen** dari sampel data acak (*bootstrapping*) dan subset fitur acak. Prediksi akhir ditentukan melalui voting mayoritas (*classification*) atau rata-rata (*regression*).
  * *Tujuan Utama:* Mereduksi nilai **VARIANCE** (mencegah *Overfitting* pada pohon yang terlalu dalam).
  * *Kapan Digunakan:* Sangat andal pada dataset dengan banyak fitur noise dan bekerja sangat baik tanpa memerlukan penyetelan hiperparameter yang rumit.
* **Boosting (e.g., XGBoost, Gradient Boosting, AdaBoost):**
  * *Cara Kerja:* Membangun pohon keputusan **secara sekuensial bertahap**. Setiap pohon baru dilatih secara spesifik untuk **mengoreksi kesalahan galat (*residual errors*)** yang dilakukan oleh pohon-pohon sebelumnya dengan memberikan bobot lebih besar pada data yang salah diprediksi.
  * *Tujuan Utama:* Mereduksi nilai **BIAS** dan **VARIANCE** secara simultan.
  * *Kapan Digunakan:* Menjadi standar juara pada kompetisi data science (Kaggle) untuk data tabular terstruktur karena menghasilkan akurasi prediksi tertinggi, namun lebih sensitif terhadap outlier dan membutuhkan tuning parameter regulerisasi yang hati-hati agar tidak overfit.
