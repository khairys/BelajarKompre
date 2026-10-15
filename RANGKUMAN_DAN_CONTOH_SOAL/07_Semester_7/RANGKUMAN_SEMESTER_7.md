# RANGKUMAN LENGKAP SEMESTER 7
## Persiapan Ujian Komprehensif S1 Informatika — Universitas Diponegoro

Semester 7 mempersiapkan mahasiswa untuk bekerja dengan pengetahuan yang lebih mandiri dan abstrak. Metodologi dan Penulisan Ilmiah melatih kemampuan mengidentifikasi masalah riset, menilai bukti, dan menyusun argumen ilmiah. Penambangan Data membahas cara menemukan pola yang berguna dari data. Teori Bahasa dan Otomata mempelajari fondasi matematis bahasa formal, model mesin, serta batas kemampuan komputasi.

Ketiganya membutuhkan cara berpikir yang berbeda: penelitian menuntut argumen dan bukti yang transparan; data mining menuntut alur pengolahan data dan evaluasi yang benar; sedangkan teori otomata menuntut definisi formal, konstruksi, dan pembuktian.

## Gambaran Umum Semester 7

| Mata kuliah | Fokus utama |
|---|---|
| Metodologi dan Penulisan Ilmiah | Research gap, rumusan masalah, tinjauan pustaka, desain eksperimen, integritas akademik, dan penulisan artikel |
| Penambangan Data | CRISP-DM, prapemrosesan, association rules, Apriori, FP-Growth, ensemble, DBSCAN, text mining |
| Teori Bahasa dan Otomata | Hierarki Chomsky, DFA/NFA, ekspresi reguler, pumping lemma, CFG, PDA, Turing machine, dan komputabilitas |

Hubungan antarmata kuliah dapat dilihat pada sebuah penelitian analisis komentar. Metodologi Riset menentukan pertanyaan, dataset, variabel, eksperimen, dan cara pelaporan. Data Mining menyediakan proses menyiapkan data, memilih metode, dan mengevaluasi temuan. Teori Bahasa dan Otomata memberi landasan untuk memahami ekspresi reguler, bahasa formal, parsing, dan batas model komputasi.

**Catatan kurikulum:** susunan ini mengikuti folder Semester 7 pada repositori BelajarKompre. Untuk aturan proposal, batas kemiripan, publikasi, dan administrasi akademik, verifikasi kembali panduan resmi yang berlaku bagi angkatan Anda.

---

# 1. METODOLOGI DAN PENULISAN ILMIAH

Sumber: [Rangkuman Materi Metodologi dan Penulisan Ilmiah](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/07_Semester_7/Metodologi_dan_Penulisan_Ilmiah/RANGKUMAN_MATERI.md)

## 1.1. Apa yang membuat penelitian menjadi ilmiah?

Penelitian ilmiah adalah proses sistematis untuk menjawab pertanyaan atau membangun pengetahuan menggunakan bukti dan metode yang dapat dipertanggungjawabkan. Penelitian Informatika tidak selalu harus membuat aplikasi baru. Kontribusinya dapat berupa teori, algoritma, evaluasi empiris, metode pengukuran, analisis keamanan, rekayasa sistem, atau pengetahuan baru tentang perilaku teknologi.

Sifat penelitian ilmiah yang perlu dipahami:
- **Rasional:** argumen mengikuti logika dan didukung alasan yang dapat dievaluasi.
- **Sistematis:** tahapan dan prosedur mengikuti rancangan yang jelas.
- **Empiris atau formal:** klaim didukung data/observasi bila bersifat empiris, atau pembuktian matematis bila bersifat formal.
- **Transparan:** metode, asumsi, data yang digunakan, dan keterbatasan diterangkan.
- **Replikatif:** peneliti lain memiliki informasi yang cukup untuk mengulang proses atau memeriksa hasil, dengan memperhatikan keterbatasan akses data.
- **Kritis:** hasil tidak diterima hanya karena terlihat masuk akal; klaim diuji terhadap bukti dan penjelasan alternatif.

### Paradigma penelitian Informatika

1. **Penelitian teoretis/formal:** menggunakan logika dan matematika untuk membuktikan sifat, batas, atau kebenaran suatu konsep. Contoh: pembuktian kompleksitas algoritma atau sifat protokol.
2. **Penelitian eksperimental/empiris:** mengukur kinerja metode atau model melalui eksperimen. Contoh: perbandingan algoritma pada dataset dengan metrik, baseline, dan prosedur evaluasi yang konsisten.
3. **Penelitian rekayasa / Design Science Research (DSR):** merancang artefak seperti sistem, model, metode, atau prototipe untuk memecahkan masalah, kemudian mengevaluasinya secara terstruktur.

Sebuah skripsi dapat menggabungkan paradigma, tetapi kontribusi dan bukti keberhasilannya tetap harus dinyatakan dengan jelas. Membangun website untuk organisasi dapat menjadi proyek rekayasa yang bermanfaat, tetapi tidak otomatis menjadi penelitian ilmiah. Agar menjadi penelitian, perlu ada masalah yang dianalisis, dasar pemilihan metode, evaluasi, serta pengetahuan atau kontribusi yang dapat dipertanggungjawabkan.

## 1.2. Masalah penelitian, rumusan masalah, dan tujuan

Masalah penelitian harus lebih spesifik daripada topik umum. “Kecerdasan buatan untuk pendidikan” terlalu luas. Masalah yang lebih terukur, misalnya: “Bagaimana perbedaan kinerja dua strategi pemilihan fitur dalam mengklasifikasikan komentar pendek berbahasa Indonesia ketika data pelatihan terbatas?”

Rumusan masalah yang baik:
- Menyebutkan objek atau fenomena yang akan diteliti.
- Dapat dijawab melalui metode dan sumber data yang realistis.
- Memiliki ruang lingkup yang jelas.
- Menghasilkan jawaban yang bisa dinilai dengan bukti, bukan sekadar opini.
- Selaras dengan tujuan, variabel, metode, serta metrik evaluasi.

**Batasan masalah** tidak digunakan untuk menghindari persoalan inti; batasan menjelaskan bagian yang sengaja tidak diteliti agar pekerjaan tetap terfokus. **Tujuan penelitian** menjelaskan hasil yang hendak dicapai. **Manfaat** menerangkan siapa yang dapat menggunakan hasil dan dalam bentuk apa. Ketiganya harus konsisten dengan rumusan masalah.

### Research gap dan novelty

**Research gap** adalah kesenjangan pada pengetahuan, bukti, metode, atau penerapan yang belum cukup dijawab oleh penelitian sebelumnya. **Novelty** merupakan unsur baru atau kontribusi yang dihasilkan penelitian. Gap dan novelty berkaitan, tetapi tidak sama: gap menjelaskan hal yang belum terjawab; novelty menjelaskan kontribusi yang ditawarkan untuk menjawabnya.

Jenis gap yang kerap dipakai:
1. **Contradictory evidence gap:** penelitian sebelumnya memberikan temuan berbeda atau bertentangan.
2. **Methodological gap:** metode sebelumnya memiliki keterbatasan atau belum dievaluasi pada kondisi yang relevan.
3. **Knowledge gap:** pemahaman terhadap fenomena tertentu belum memadai.
4. **Application gap:** metode yang sudah dikenal belum cukup dievaluasi dalam domain, populasi, bahasa, atau konteks tertentu.

Untuk menemukan gap, jangan hanya mencari paper yang menyebut “future work”. Baca pertanyaan, data, metode, hasil, keterbatasan, dan asumsi penelitian terdahulu. Cari pola pada beberapa penelitian, lalu tentukan apakah kekurangan itu penting dan dapat diuji.

Klaim novelty harus proporsional. “Belum pernah ada yang membuat aplikasi X” bukan klaim ilmiah yang kuat jika kontribusinya sekadar implementasi fitur standar. Sebaliknya, evaluasi sistematis yang mengungkap bagaimana metode berubah kinerjanya di bawah kondisi tertentu dapat bernilai ilmiah meskipun tidak menciptakan arsitektur baru.

## 1.3. Menyusun pertanyaan dan hipotesis penelitian

**Research Question (RQ)** mengubah masalah umum menjadi pertanyaan yang dapat dijawab lewat rancangan penelitian. Contoh:
- RQ1: Seberapa baik masing-masing metode mendeteksi kelas target pada data uji yang tidak terlihat saat pelatihan?
- RQ2: Bagaimana performa berubah ketika ukuran data latih dikurangi?
- RQ3: Apakah perbedaan kinerja tetap terlihat pada beberapa pembagian data atau skenario pengujian?

**Hipotesis** adalah pernyataan yang dapat diuji tentang hubungan atau perbedaan yang diperkirakan. Hipotesis nol sering menyatakan tidak ada perbedaan/efek menurut model statistik tertentu; hipotesis alternatif menyatakan pola yang berlawanan. Tidak semua penelitian Informatika harus memakai hipotesis statistik formal. Studi eksploratif atau design science dapat menggunakan RQ dan kriteria evaluasi tanpa memaksakan hipotesis yang tidak sesuai.

Bedakan:
- **Pertanyaan penelitian:** apa yang ingin diketahui?
- **Tujuan:** apa yang akan dilakukan untuk menjawab pertanyaan?
- **Hipotesis:** hasil atau hubungan apa yang diperkirakan dapat diuji?
- **Metrik:** bagaimana keluaran penelitian akan diukur?
- **Kriteria keberhasilan:** bukti apa yang cukup untuk menyatakan tujuan tercapai?

## 1.4. Systematic Literature Review (SLR)

Systematic Literature Review mengidentifikasi, memilih, menilai, dan mensintesis publikasi relevan menggunakan prosedur yang transparan dan dapat direplikasi. SLR lebih terstruktur dibanding pencarian bacaan secara informal.

Tahapan umum:
1. Tentukan pertanyaan review.
2. Rancang search string menggunakan kata kunci dan operator Boolean AND/OR.
3. Pilih basis data ilmiah relevan seperti IEEE Xplore, ACM Digital Library, Scopus, ScienceDirect, atau Google Scholar sesuai kebutuhan dan akses.
4. Tetapkan kriteria inklusi dan eksklusi sebelum seleksi.
5. Hapus duplikasi, saring judul/abstrak, lalu telaah teks lengkap sesuai aturan.
6. Nilai kualitas studi bila rancangan review membutuhkannya.
7. Ekstrak data dengan formulir yang konsisten.
8. Sintesis bukti dalam tabel komparasi serta uraian analitis.
9. Laporkan proses pencarian dan seleksi secara transparan.

### Search string dan seleksi literatur

Operator **AND** mempersempit hasil agar istilah harus muncul bersama; **OR** memperluas cakupan untuk sinonim atau istilah terkait; tanda kutip sering dipakai untuk frasa persis, bergantung fasilitas pencarian. Contoh konseptual:

~~~text
("text classification" OR "comment classification")
AND (robustness OR obfuscation)
AND (Indonesian OR "low-resource language")
~~~

String di atas hanya ilustrasi dan perlu disesuaikan dengan sintaks setiap basis data. Simpan tanggal pencarian, query, sumber database, jumlah hasil, aturan penyaringan, alasan eksklusi, dan jumlah artikel yang masuk ke sintesis. Dokumentasi ini membuat proses lebih dapat diaudit.

### Matriks komparasi penelitian

Kolom yang berguna antara lain:
- Referensi dan tahun.
- Masalah serta tujuan.
- Dataset, bahasa, domain, dan ukuran data.
- Metode/model serta baseline.
- Cara pembagian data dan validasi.
- Metrik evaluasi.
- Temuan utama.
- Keterbatasan.
- Relevansi terhadap RQ penelitian saat ini.

Matriks bukan sekadar tempat menyalin abstrak. Gunakan perbandingan untuk menemukan pola, ketidaksepakatan, batas bukti, dan peluang riset. Perbedaan angka antarpaper tidak selalu berarti satu metode lebih baik jika dataset, split, preprocessing, metrik, atau setting eksperimennya tidak setara.

## 1.5. Desain eksperimen dan variabel

Rancangan eksperimen perlu menerangkan bagaimana pertanyaan penelitian diterjemahkan menjadi prosedur yang dapat diuji.

- **Variabel independen:** faktor yang dimanipulasi atau dibandingkan, seperti model, ukuran data, atau tingkat transformasi input.
- **Variabel dependen:** keluaran yang diukur, seperti F1-score, latency, error rate, atau penggunaan memori.
- **Variabel kontrol:** faktor yang dijaga tetap atau diatur secara konsisten, seperti pembagian data, perangkat, preprocessing, jumlah percobaan, dan batas tuning.
- **Confounding factor:** faktor lain yang memengaruhi keluaran sehingga atribusi sebab-akibat menjadi sulit.

Contoh eksperimen perbandingan model: model A dan B dilatih menggunakan training split yang sama, tuning dilakukan pada validation split, dan keduanya diuji pada test split yang sama. Bila setiap model menggunakan split berbeda atau informasi test digunakan saat tuning, perbandingan menjadi kurang adil.

### Baseline dan fairness

Baseline adalah metode pembanding untuk menilai apakah suatu metode benar-benar memberi manfaat. Pilih baseline yang relevan dengan tugas, bukan sengaja memilih metode yang terlalu lemah. Perbandingan yang adil memerlukan data dan preprocessing yang sesuai, aturan tuning yang dinyatakan, metrik yang tepat, serta anggaran eksperimen yang masuk akal.

Untuk eksperimen ML, pisahkan training, validation, dan test. Transformasi yang belajar dari data—seperti standardisasi atau pemilihan fitur—harus dipasang berdasarkan training set pada setiap fold, bukan pada keseluruhan data. Jika dataset memiliki kelompok atau urutan waktu, split acak biasa dapat menyebabkan kebocoran; gunakan split berdasarkan group atau waktu bila sesuai konteks.

### Validitas penelitian

- **Internal validity:** seberapa kuat kesimpulan bahwa perbedaan berasal dari faktor yang diteliti, bukan confounder.
- **External validity:** seberapa jauh hasil dapat digeneralisasi ke data atau kondisi lain.
- **Construct validity:** apakah pengukuran benar-benar merepresentasikan konsep yang dimaksud.
- **Conclusion validity:** apakah analisis dan data cukup mendukung kesimpulan yang dibuat.

Keterbatasan bukan pengakuan bahwa penelitian gagal. Menyatakan batas dataset, kelas yang kurang terwakili, potensi bias label, keterbatasan hardware, atau asumsi metode justru meningkatkan transparansi ilmiah.

## 1.6. Sistematika proposal skripsi dan artikel

Secara umum proposal memuat tiga bab utama, mengikuti pedoman institusi:
- **Bab I — Pendahuluan:** latar belakang, masalah, rumusan masalah, batasan, tujuan, manfaat, dan struktur dokumen.
- **Bab II — Tinjauan pustaka dan landasan teori:** penelitian terdahulu, konsep relevan, hubungan antarpenelitian, serta posisi gap dan kontribusi.
- **Bab III — Metodologi penelitian:** desain, data, alat/bahan, tahapan, baseline, skenario eksperimen, metrik, dan metode analisis.

Isi persis dan format bab harus mengikuti template resmi. Judul bagian tidak boleh dipilih hanya karena kebiasaan; pastikan setiap bagian diperlukan untuk menjelaskan penelitian.

Untuk artikel ilmiah, struktur yang umum ialah **IMRaD**:
- **Introduction:** masalah, konteks, gap, tujuan, dan kontribusi.
- **Methods:** data, rancangan, prosedur, model, dan evaluasi.
- **Results:** hasil pengamatan tanpa mengaburkan angka penting.
- **Discussion:** makna hasil, perbandingan dengan penelitian sebelumnya, penjelasan yang mungkin, dan keterbatasan.

Kesimpulan merangkum jawaban terhadap pertanyaan penelitian berdasarkan hasil. Klaim pada kesimpulan harus konsisten dengan hasil yang benar-benar diuji.

## 1.7. Sitasi, pengelolaan referensi, dan integritas akademik

Gaya IEEE biasanya memakai nomor sitasi berurutan dalam tanda kurung siku, misalnya [1], dengan detail bibliografi pada daftar referensi. Ikuti template publikasi atau panduan kampus karena aturan rincinya dapat berbeda untuk buku, artikel jurnal, prosiding, situs, dataset, dan software.

Mendeley dan Zotero membantu menyimpan metadata, menyusun pustaka, dan menyisipkan sitasi, tetapi peneliti tetap bertanggung jawab memeriksa nama penulis, judul, tahun, venue, halaman, DOI, dan format referensi. Sitasi yang dihasilkan otomatis dapat memiliki metadata keliru.

Tiga pelanggaran integritas utama sering diringkas sebagai FFP:
1. **Fabrication:** mengarang data atau hasil yang tidak pernah diperoleh.
2. **Falsification:** memanipulasi proses, instrumen, atau data secara tidak semestinya agar hasil terlihat mendukung klaim.
3. **Plagiarism:** menggunakan kata-kata, gagasan, gambar, kode, atau data pihak lain tanpa pengakuan sumber yang patut.

Mengutip sumber tidak berarti semua penggunaan menjadi otomatis diizinkan; hak cipta, lisensi, privasi, dan syarat penggunaan dataset tetap perlu diperhatikan. Jangan mengubah hasil buruk hanya agar hipotesis “berhasil”. Laporkan metodologi, hasil, variasi, dan keterbatasan secara jujur.

Dokumen sumber repo mencantumkan ambang kemiripan Turnitin di bawah 20% sebagai salah satu persyaratan yang dirangkum. Ambang dan aturan pengecualian dapat berubah, sehingga angka tersebut tidak boleh dianggap sebagai kebijakan universal atau jaminan bebas plagiarisme; verifikasi aturan terkini dari fakultas/departemen. Indeks kemiripan juga bukan penentu plagiarisme secara otomatis: isi yang cocok tetap perlu dinilai konteks dan atribusinya.

## 1.8. Menyajikan dan mempertahankan penelitian

Presentasi ilmiah sebaiknya mengalir dari masalah ke bukti:
1. Mengapa masalah penting?
2. Apa yang belum terjawab penelitian sebelumnya?
3. Apa pertanyaan dan kontribusi penelitian?
4. Bagaimana metode serta eksperimen dirancang?
5. Apa hasil utamanya?
6. Apa yang dapat dan tidak dapat disimpulkan?
7. Apa keterbatasan dan arah lanjutan?

Untuk menjawab pertanyaan penguji, bedakan fakta, pilihan desain, asumsi, dan hasil empiris. Jika tidak mengetahui jawaban, jelaskan batas pengetahuan dan bagaimana memverifikasinya; jangan mengarang justifikasi setelah melihat hasil.

### Target penguasaan Metodologi dan Penulisan Ilmiah

Anda seharusnya dapat membedakan proyek implementasi dan penelitian, merumuskan RQ yang dapat dijawab, menjelaskan gap/novelty, merancang pencarian SLR, menyusun matriks literatur, menentukan variabel dan baseline yang adil, menjelaskan validitas penelitian, menyusun proposal Bab I–III, menerapkan sitasi yang benar, dan mempertahankan hasil secara jujur.

---

# 2. PENAMBANGAN DATA

Sumber: [Rangkuman Materi Penambangan Data](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/07_Semester_7/Penambangan_Data/RANGKUMAN_MATERI.md)

## 2.1. Konsep data mining dan KDD

Data mining berusaha menemukan pola, hubungan, tren, kelompok, atau anomali yang berguna dari data. Hasilnya tidak otomatis menjadi pengetahuan valid: pola perlu diuji, dinilai dari kualitas data, dan dihubungkan dengan konteks masalah.

**KDD (Knowledge Discovery in Databases)** merupakan proses menyeluruh dari pemilihan dan prapemrosesan data hingga interpretasi pengetahuan. **Data mining** sering merujuk pada langkah analitik/pemodelan di dalam proses tersebut. **CRISP-DM** adalah kerangka kerja proses proyek data mining yang dikenal luas.

### Enam fase CRISP-DM

1. **Business Understanding:** memahami tujuan bisnis dan mendefinisikan masalah data secara operasional.
2. **Data Understanding:** mengumpulkan data, meneliti distribusi, kualitas, hubungan, serta anomali.
3. **Data Preparation:** memilih, membersihkan, menggabungkan, mengubah, dan menyiapkan fitur.
4. **Modeling:** memilih metode, melatih model, serta menyetel parameter.
5. **Evaluation:** menilai apakah hasil model menjawab tujuan bisnis dan tidak hanya cocok pada data latih.
6. **Deployment:** mengintegrasikan hasil ke proses, produk, API, dashboard, atau keputusan organisasi, lalu merencanakan pemeliharaan.

CRISP-DM bersifat iteratif. Hasil evaluation dapat mengharuskan tim kembali ke pemahaman bisnis, pengumpulan data, atau modeling. Fase deployment juga tidak selalu berupa layanan produksi; pelaporan dan penggunaan hasil oleh analis dapat menjadi bentuk delivery tergantung tujuan proyek.

## 2.2. Data preprocessing

Data mentah sering memiliki nilai hilang, duplikasi, noise, format yang tidak konsisten, ketidakseimbangan kelas, dan fitur dengan skala berbeda. Kesalahan preprocessing dapat mendominasi hasil model, sehingga tahap ini harus didokumentasikan.

### Missing values

Pilihan penanganan:
- Menghapus baris/kolom bila kehilangan data masih dapat diterima dan tidak menimbulkan bias besar.
- Mengimputasi mean/median untuk fitur numerik atau modus untuk kategori sesuai distribusi serta tujuan.
- Menggunakan metode yang lebih kompleks seperti k-NN imputation atau MICE bila asumsi dan biaya komputasinya masuk akal.
- Mempertahankan indikator bahwa nilai awalnya hilang bila missingness memiliki makna.

Jangan menerapkan aturan “selalu hapus jika >50% hilang” tanpa analisis. Keputusan bergantung pada jumlah sampel, pentingnya fitur, mekanisme missingness, dan bias yang dapat muncul. Nilai yang hilang tidak selalu terjadi secara acak.

### Scaling

**Min-Max normalization** memetakan data ke rentang target:

\[
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}(new_{\max}-new_{\min})+new_{\min}
\]

Untuk rentang [0,1]:

\[
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
\]

**Z-score standardization** memusatkan fitur dan mengukurnya berdasarkan simpangan baku:

\[
z=\frac{x-\mu}{\sigma}
\]

Min-Max mempertahankan urutan relatif pada rentang yang dipetakan tetapi sensitif terhadap outlier. Z-score tidak memaksa nilai ke batas tertentu dan juga dapat terpengaruh outlier. Scaling terutama penting untuk metode berbasis jarak, optimisasi gradien, atau penalti parameter; tidak selalu dibutuhkan untuk decision tree berbasis threshold.

**Pencegahan leakage:** parameter scaling, imputasi, encoding, dan pemilihan fitur harus dipelajari pada training data, kemudian diterapkan ke validation/test. Pada cross-validation, setiap fold harus memiliki preprocessing yang hanya belajar dari bagian latih fold itu.

### Outlier dan pembersihan data

Outlier adalah pengamatan yang jauh dari pola umum, tetapi tidak otomatis salah. Outlier bisa berasal dari kesalahan pencatatan, kejadian langka yang sah, atau kelas kasus yang justru penting. Identifikasi melalui statistik, visualisasi, aturan domain, atau metode deteksi; tentukan apakah akan diperbaiki, dipertahankan, ditransformasi, atau dikeluarkan berdasarkan alasan yang dapat dijelaskan.

### Principal Component Analysis (PCA)

PCA mengubah fitur yang saling berkorelasi menjadi kombinasi linear baru yang saling ortogonal, yaitu principal components, diurutkan berdasarkan variansi yang dijelaskan. Secara konseptual:
1. Pusatkan atau standardisasi data sesuai skala fitur.
2. Hitung matriks kovarians atau pendekatan yang sesuai.
3. Lakukan eigenvalue decomposition atau SVD.
4. Urutkan komponen berdasarkan variansi yang dijelaskan.
5. Proyeksikan data ke sejumlah komponen terpilih.

PCA dapat mengurangi dimensi dan membantu efisiensi, tetapi kehilangan sebagian informasi serta mengurangi interpretabilitas fitur. PCA tanpa label bukan berarti setiap komponen relevan bagi target klasifikasi; variansi tinggi tidak selalu sama dengan daya prediktif tinggi.

## 2.3. Association Rule Mining

Association Rule Mining mencari hubungan kemunculan bersama antaritem. Contoh pada transaksi belanja: \(\{roti\}\rightarrow\{susu\}\). Aturan menunjukkan pola asosiasi, bukan otomatis hubungan sebab-akibat.

Misalkan:
- X adalah antecedent (kondisi awal),
- Y adalah consequent (hasil pada sisi kanan),
- X dan Y merupakan himpunan item yang tidak saling tumpang tindih pada bentuk aturan umum.

### Support

Support menilai proporsi transaksi yang memuat X dan Y sekaligus:

\[
Support(X\rightarrow Y)=P(X\cup Y)
=\frac{\#Transaksi\ memuat\ X\ dan\ Y}{N}
\]

### Confidence

Confidence mengukur proporsi transaksi yang memuat Y di antara transaksi yang memuat X:

\[
Confidence(X\rightarrow Y)=P(Y\mid X)
=\frac{Support(X\cup Y)}{Support(X)}
\]

Confidence tinggi belum tentu menunjukkan hubungan yang menarik jika Y memang sangat sering muncul dalam seluruh transaksi.

### Lift

Lift membandingkan confidence terhadap frekuensi dasar consequent:

\[
Lift(X\rightarrow Y)=
\frac{Confidence(X\rightarrow Y)}{Support(Y)}
=\frac{P(X\cup Y)}{P(X)P(Y)}
\]

- Lift = 1: X dan Y independen menurut model asosiasi tersebut.
- Lift > 1: asosiasi positif.
- Lift < 1: asosiasi negatif.

### Contoh perhitungan

Terdapat 100 transaksi. Item X muncul pada 40 transaksi, Y muncul pada 50 transaksi, dan keduanya muncul bersama pada 30 transaksi.

\[
Support(X\rightarrow Y)=30/100=0{,}30
\]

\[
Confidence(X\rightarrow Y)=30/40=0{,}75
\]

\[
Lift=0{,}75/0{,}50=1{,}5
\]

Artinya 30% transaksi memuat X dan Y; 75% transaksi yang memuat X juga memuat Y; pola ini 1,5 kali lebih sering dibanding ekspektasi independensi menurut rasio lift. Ini tetap asosiasi, bukan bukti bahwa X menyebabkan pembelian Y.

## 2.4. Apriori dan downward-closure property

Apriori mencari frequent itemsets melalui generasi kandidat dan penghitungan support. Properti utama adalah **downward closure**: jika sebuah itemset sering (*frequent*), setiap subset non-kosongnya juga harus sering.

Konsekuensinya: jika sebuah itemset tidak memenuhi minimum support, semua superset yang mengandungnya tidak mungkin frequent dan dapat dipangkas sebelum dihitung lebih lanjut.

Alur sederhana:
1. Hitung itemset ukuran 1 dan buang item yang tidak memenuhi minimum support.
2. Gabungkan frequent itemsets untuk menghasilkan kandidat ukuran berikutnya.
3. Pangkas kandidat jika ada subset yang diketahui tidak frequent.
4. Hitung support kandidat pada transaksi.
5. Ulangi sampai tidak ada kandidat frequent baru.
6. Dari frequent itemsets, bentuk aturan dan evaluasi confidence/lift sesuai ambang yang dipilih.

Kelemahan Apriori adalah banyaknya kandidat dan pemindaian database berulang kali. Pada data dengan banyak kombinasi, tahap kandidat dapat mahal dalam waktu dan memori.

## 2.5. FP-Growth

FP-Growth mencari frequent itemsets tanpa membangkitkan kandidat sebanyak Apriori. Alur umumnya:
1. Pindai database untuk mendapatkan frekuensi tiap item.
2. Buang item yang tidak memenuhi minimum support.
3. Urutkan item transaksi berdasarkan frekuensi global (menurut aturan implementasi).
4. Bentuk **FP-Tree** yang berbagi prefix antartransaksi.
5. Gunakan header table dan node links untuk menelusuri item.
6. Bangun conditional pattern base dan conditional FP-tree untuk menemukan pola frequent secara rekursif.

Keunggulan utama FP-Growth ialah mengompresi transaksi dengan prefix yang sama dan menghindari pembangkitan kandidat eksplisit yang ekstensif. Namun, efektivitasnya bergantung pada karakter data, tingkat pengulangan prefix, ukuran tree, dan memori yang tersedia.

| Aspek | Apriori | FP-Growth |
|---|---|---|
| Strategi | Generasi kandidat lalu hitung support | Kompresi ke FP-tree dan pertumbuhan pola |
| Database scan | Dapat berulang untuk tiap tingkat | Umumnya dua scan utama sebelum penambangan tree, tergantung implementasi |
| Kekuatan | Konsep sederhana dan mudah ditelusuri | Menghindari kandidat yang sangat banyak |
| Tantangan | Ledakan jumlah kandidat | Tree dan conditional pattern dapat menghabiskan memori |

## 2.6. Ensemble learning: bagging, Random Forest, boosting

Ensemble menggabungkan beberapa model untuk menghasilkan prediksi yang diharapkan lebih kuat daripada model tunggal.

### Bagging

Bagging (*Bootstrap Aggregating*) melatih model pada sampel bootstrap yang berbeda dan menggabungkan prediksinya, misalnya melalui voting atau rata-rata. Bagging terutama dapat mengurangi variance pada model yang tidak stabil.

### Random Forest

Random Forest merupakan ensemble pohon keputusan yang menggunakan sampel bootstrap dan subset fitur acak ketika mempertimbangkan split. Pengacakan mengurangi korelasi antar pohon; prediksi klasifikasi biasanya menggunakan voting, sedangkan regresi menggunakan rata-rata.

Kelebihan:
- Dapat memodelkan hubungan nonlinier dan interaksi fitur.
- Tidak membutuhkan scaling fitur numerik dalam cara yang sama dengan model jarak.
- Memberikan ukuran kepentingan fitur, meskipun interpretasinya memiliki bias/keterbatasan.

Kekurangan:
- Model dapat besar dan prediksi lebih berat daripada satu pohon.
- Penjelasan prediksi individu lebih sulit dibanding pohon sederhana.
- Feature importance bukan otomatis penjelasan kausal.

### Boosting dan XGBoost

Boosting membangun model secara berurutan, dengan model baru memperbaiki kesalahan atau residual yang belum ditangani model sebelumnya. Gradient boosting menggunakan gradien fungsi loss untuk mengarahkan perbaikan. XGBoost merupakan implementasi gradient boosting yang dilengkapi optimisasi, regularisasi, dan fitur engineering sistem.

Secara umum:
- **Bagging** melatih model pada sampel yang bervariasi dan menggabungkan prediksi, sering untuk mengurangi variance.
- **Boosting** melatih model secara bertahap sehingga setiap tahap memperbaiki model sebelumnya; performa bisa tinggi, tetapi tuning dan regularisasi perlu diperhatikan.

Kedua metode tidak otomatis mengatasi data leakage, label yang salah, bias sampling, atau dataset yang tidak representatif. Pemilihan model harus berdasarkan validasi dan tujuan bisnis.

## 2.7. DBSCAN: clustering berbasis kepadatan

DBSCAN membentuk klaster dari daerah dengan kepadatan tinggi dan dapat menandai titik yang tidak termasuk klaster sebagai noise. Dua parameter utama:
- **Epsilon (\(\varepsilon\)):** radius lingkungan.
- **MinPts:** jumlah titik minimum di lingkungan agar titik dianggap core sesuai definisi implementasi.

Tipe titik:
- **Core point:** memiliki jumlah tetangga dalam radius yang memenuhi syarat kepadatan.
- **Border point:** jumlah tetangganya sendiri tidak cukup menjadi core, tetapi berada dalam lingkungan core point dan dapat menjadi bagian klaster.
- **Noise point:** tidak dapat dihubungkan ke klaster berdasarkan parameter tersebut.

Kelebihan DBSCAN: tidak perlu menentukan jumlah klaster K di awal, dapat menemukan bentuk klaster non-bulat, dan memiliki konsep noise. Keterbatasan: hasil sensitif terhadap skala fitur dan parameter; satu pasangan epsilon/MinPts sulit mewakili klaster dengan kepadatan yang sangat berbeda. Karena itu, normalisasi serta pemilihan parameter perlu dijelaskan.

## 2.8. Text mining dan TF-IDF

Text mining mengekstrak informasi atau pola dari teks tidak terstruktur. Tahap preprocessing perlu disesuaikan dengan bahasa, tujuan, dan sifat data:
1. Membersihkan data yang tidak relevan dengan tetap mempertahankan informasi yang mungkin penting.
2. Normalisasi ejaan/format bila relevan.
3. Tokenisasi.
4. Penanganan stopwords jika tepat.
5. Stemming atau lemmatization bila membantu tujuan analisis.
6. Mengubah teks menjadi representasi numerik.
7. Melakukan klasifikasi, clustering, pengukuran kemiripan, atau analisis lain.

Tidak semua preprocessing harus diterapkan. Stopword removal atau stemming dapat menghilangkan petunjuk penting dalam tugas seperti analisis sentimen, deteksi negasi, atau deteksi penyamaran kata. Bandingkan keputusan preprocessing dengan eksperimen yang terkontrol.

### TF-IDF

TF-IDF memberi bobot yang mencerminkan frekuensi suatu istilah di dokumen dan kelangkaannya di seluruh korpus.

Salah satu bentuk umum:

\[
TFIDF(t,d)=TF(t,d)\times IDF(t)
\]

\[
IDF(t)=\log\left(\frac{N}{df(t)}\right)
\]

N adalah jumlah dokumen dan \(df(t)\) jumlah dokumen yang mengandung istilah t. Implementasi dapat memakai smoothing, normalisasi, atau definisi TF berbeda; tuliskan konfigurasi yang digunakan. Istilah yang sangat sering muncul di semua dokumen biasanya memperoleh bobot IDF lebih rendah.

Vektor TF-IDF dapat digunakan untuk klasifikasi linear atau kemiripan dokumen, tetapi representasi bag-of-words/TF-IDF tidak secara langsung mempertahankan semua struktur urutan dan makna semantik kalimat.

### Cosine similarity

Kemiripan kosinus mengukur kesamaan arah dua vektor:

\[
cos(\theta)=\frac{A\cdot B}{\|A\|\|B\|}
\]

Pada vektor bernilai nonnegatif seperti TF-IDF, nilai mendekati 1 menunjukkan pola istilah yang relatif mirip, nilai dekat 0 menunjukkan sedikit kesamaan arah, dengan interpretasi tetap bergantung pada representasi dan normalisasi. Jika salah satu vektor nol, rumus perlu ditangani secara khusus karena normanya nol.

## 2.9. Evaluasi dan interpretasi hasil data mining

Kualitas temuan dapat dinilai melalui metrik klasifikasi, kualitas cluster, validitas aturan asosiasi, serta manfaat operasional. Jangan memilih satu metrik hanya karena hasilnya tinggi.

Untuk klasifikasi, metrik umum:
- **Accuracy:** persentase seluruh sampel yang diprediksi benar.
- **Precision:** dari yang diprediksi positif, proporsi yang benar-benar positif.
- **Recall:** dari seluruh aktual positif, proporsi yang ditemukan.
- **F1:** rata-rata harmonik precision dan recall.

\[
Precision=\frac{TP}{TP+FP}
\]

\[
Recall=\frac{TP}{TP+FN}
\]

\[
F1=2\frac{Precision\times Recall}{Precision+Recall}
\]

Dataset tidak seimbang dapat membuat accuracy menyesatkan. Pilih metrik sesuai biaya false positive dan false negative. Pada clustering, gunakan metrik kuantitatif yang sesuai jika tersedia, serta evaluasi domain/interpretasi cluster. Pada association rule, support, confidence, dan lift memberi informasi berbeda; confidence saja tidak cukup.

### Target penguasaan Penambangan Data

Anda seharusnya mampu menggambarkan siklus CRISP-DM, menangani missing values dan scaling tanpa leakage, menjelaskan PCA, menghitung support/confidence/lift, menelusuri Apriori dan FP-Growth, membedakan bagging dan boosting, menjelaskan DBSCAN, membentuk TF-IDF, serta menafsirkan metrik evaluasi sesuai tujuan.

---

# 3. TEORI BAHASA DAN OTOMATA

Sumber: [Rangkuman Materi Teori Bahasa dan Otomata](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/07_Semester_7/Teori_Bahasa_dan_Otomata/RANGKUMAN_MATERI.md)

## 3.1. Alfabet, string, bahasa, dan tata bahasa

**Alfabet** \(\Sigma\) adalah himpunan simbol yang terbatas, misalnya \(\Sigma=\{0,1\}\). **String** atau kata adalah urutan simbol dari alfabet. String kosong ditulis \(\epsilon\), dan panjang string w ditulis \(|w|\). **Bahasa formal** adalah himpunan string atas suatu alfabet, yaitu \(L\subseteq\Sigma^*\), dengan \(\Sigma^*\) himpunan seluruh string hingga termasuk string kosong.

**Grammar/tata bahasa** mendeskripsikan bagaimana string dalam bahasa dapat dibentuk melalui aturan produksi. **Automaton** merupakan model mesin abstrak untuk menerima atau mengenali string berdasarkan transisi state. Bahasa formal dan otomata menjadi landasan lexical analysis, parsing, kompilator, protokol, validasi format, dan teori komputabilitas.

## 3.2. Hierarki Chomsky

Hierarki Chomsky membedakan kelas tata bahasa berdasarkan pembatasan aturan produksinya serta model mesin pengenalnya.

| Tipe | Kelas bahasa | Model pengenal umum | Intuisi |
|---|---|---|---|
| Tipe 3 | Regular | Finite-state automaton | Memori terbatas pada state |
| Tipe 2 | Context-free | Pushdown automaton | Memori stack |
| Tipe 1 | Context-sensitive | Linear bounded automaton | Memori terbatas secara linear terhadap input |
| Tipe 0 | Recursively enumerable | Turing machine | Model komputasi umum dengan pita tak terbatas secara konseptual |

Dalam hierarki standar, setiap kelas di atas mengandung kelas yang lebih rendah secara inklusif: regular ⊆ context-free ⊆ context-sensitive ⊆ recursively enumerable. Inklusi tersebut tidak berarti kelas-kelasnya sama; ada bahasa yang dapat dikenali oleh model lebih kuat tetapi tidak oleh model yang lebih terbatas.

## 3.3. Deterministic Finite Automaton (DFA)

DFA didefinisikan sebagai 5-tuple:

\[
M=(Q,\Sigma,\delta,q_0,F)
\]

dengan:
- \(Q\): himpunan state.
- \(\Sigma\): alfabet input.
- \(\delta:Q\times\Sigma\rightarrow Q\): fungsi transisi.
- \(q_0\): state awal.
- \(F\subseteq Q\): himpunan state akhir/accepting.

DFA memproses input satu simbol demi satu simbol dan selalu mempunyai tepat satu transisi untuk tiap pasangan state dan simbol dalam definisi formalnya. String diterima apabila setelah seluruh simbol dibaca, mesin berada pada state final.

### Cara menelusuri DFA

1. Mulai dari \(q_0\).
2. Baca simbol pertama.
3. Ikuti transisi yang sesuai dengan state dan simbol tersebut.
4. Ulangi sampai semua simbol dibaca.
5. Terima string jika state akhir berada di F; selain itu, tolak.

Contoh konseptual: bahasa string biner yang berakhir dengan 1. Mesin dapat memiliki state yang menyatakan apakah simbol terakhir yang dibaca adalah 1; setelah seluruh input dibaca, state yang merepresentasikan “berakhir dengan 1” menjadi accepting. State harus merepresentasikan informasi relevan dari prefix, bukan menyimpan seluruh input.

## 3.4. NFA dan epsilon-NFA

**Nondeterministic Finite Automaton (NFA)** memungkinkan satu state dan simbol menghasilkan nol, satu, atau beberapa state tujuan. String diterima jika terdapat setidaknya satu jalur komputasi yang berakhir pada accepting state setelah input diproses.

NFA dapat didefinisikan dengan fungsi transisi yang menghasilkan subset state:

\[
\delta:Q\times\Sigma\rightarrow 2^Q
\]

Pada **epsilon-NFA**, transisi \(\epsilon\) dapat mengubah state tanpa mengonsumsi simbol input. Secara intuitif, mesin dapat mengeksplorasi beberapa pilihan secara konseptual; ini tidak berarti NFA secara komputasional lebih kuat daripada DFA untuk bahasa yang dapat dikenali. Keduanya mengenali tepat kelas bahasa reguler.

### Konversi NFA ke DFA (subset construction)

Setiap state DFA hasil konversi mewakili sekumpulan state NFA.
1. State awal DFA adalah state awal NFA, atau epsilon-closure dari state tersebut jika epsilon transition ada.
2. Untuk setiap subset state dan simbol input, gabungkan seluruh state tujuan NFA dari anggota subset.
3. Jika epsilon transition ada, tambahkan epsilon-closure atas hasilnya.
4. Setiap subset yang memuat setidaknya satu accepting state NFA menjadi accepting state DFA.
5. Ulangi hingga tidak ada subset baru.

Jumlah maksimum state DFA hasil konversi adalah \(2^{|Q|}\), meskipun dalam praktik beberapa subset mungkin tidak dapat dicapai. Karena itu, NFA yang kecil dapat menghasilkan DFA dengan jumlah state jauh lebih besar.

## 3.5. Minimasi DFA dan Myhill–Nerode

DFA minimisasi mencari mesin ekuivalen yang memakai jumlah state minimum. Dua state dapat digabungkan bila tidak ada suffix yang membedakan perilaku penerimaannya: dari kedua state itu, string lanjutan apa pun harus menghasilkan keputusan terima/tolak yang sama.

Metode tabel pasangan dapat dijelaskan sebagai berikut:
1. Hapus state yang tidak dapat dicapai dari state awal.
2. Tandai pasangan yang terdiri dari satu accepting state dan satu non-accepting state; pasangan itu jelas dapat dibedakan.
3. Untuk pasangan belum ditandai, periksa setiap simbol. Jika transisi keduanya menuju pasangan yang telah dibedakan, tandai pasangan awal.
4. Ulangi sampai tidak ada tanda baru.
5. Gabungkan pasangan state yang tetap tidak terbedakan.

**Teorema Myhill–Nerode** menghubungkan jumlah kelas ekuivalensi relasi indistinguishability dengan jumlah state DFA minimal. Untuk pembuktian formal, gagasan kuncinya ialah dua prefix ekuivalen jika setiap suffix memberikan hasil penerimaan yang sama.

Kesalahan umum adalah menggabungkan state yang sekilas memiliki transisi mirip tanpa membuktikan bahwa semua suffix menghasilkan perilaku sama.

## 3.6. Regular expression dan Teorema Arden

Ekspresi reguler mendeskripsikan bahasa reguler dengan operasi utama:
- **Union** (\(|\) atau \(\cup\)): string berasal dari salah satu bahasa.
- **Concatenation:** string dari bahasa pertama diikuti string dari bahasa kedua.
- **Kleene star** (\(^*\)): nol atau lebih pengulangan, termasuk string kosong.
- **Kleene plus** (\(^+\)): satu atau lebih pengulangan pada notasi yang umum.

Ekspresi reguler dapat digunakan untuk mendeskripsikan pola teks, token bahasa pemrograman, format string, dan validasi sederhana. Namun, regex dalam library pemrograman dapat mempunyai ekstensi praktis di luar definisi formal reguler; kemampuan tiap mesin regex perlu dibedakan dari teori formal.

### Teorema Arden

Persamaan bahasa berbentuk:

\[
X=AX\cup B
\]

mempunyai solusi \(X=A^*B\) jika \(\epsilon\notin A\). Ini adalah bentuk standar yang digunakan untuk menyelesaikan persamaan bahasa reguler dan membantu menurunkan ekspresi reguler dari automata. Jika kondisi epsilon tidak terpenuhi, solusi unik tidak otomatis dapat diklaim hanya menggunakan bentuk tersebut; syarat teorema harus diperiksa.

## 3.7. Pumping Lemma untuk bahasa reguler

Pumping lemma memberikan sifat yang harus dipenuhi setiap bahasa reguler. Jika L reguler, ada panjang pemompaan \(p\ge1\) sehingga setiap string \(w\in L\) dengan \(|w|\ge p\) dapat dibagi menjadi:

\[
w=xyz
\]

dengan syarat:
1. \(|y|\ge1\), jadi bagian y tidak kosong.
2. \(|xy|\le p\), sehingga bagian yang dapat dipompa berada dalam prefix awal yang dibatasi.
3. Untuk setiap \(i\ge0\), \(xy^iz\in L\).

Pumping lemma lazim dipakai untuk **membuktikan bahasa tidak reguler** melalui kontradiksi:
1. Asumsikan bahasa reguler.
2. Ambil panjang pumping p yang dijamin.
3. Pilih string w yang berada di L dan cukup panjang.
4. Pertimbangkan semua pembagian yang memenuhi \(|y|\ge1\) dan \(|xy|\le p\).
5. Tunjukkan bahwa ada pilihan pemompaan, misalnya \(i=0\) atau \(i=2\), yang menyebabkan string keluar dari L.
6. Kontradiksi, sehingga asumsi bahasa reguler ditolak.

Contoh klasik:

\[
L=\{0^n1^n\mid n\ge0\}
\]

Bahasa ini membutuhkan jumlah nol dan satu yang sama. Jika dipilih \(w=0^p1^p\), karena \(|xy|\le p\), bagian y hanya berisi nol. Menghapus y dengan \(i=0\) membuat jumlah nol lebih sedikit daripada jumlah satu, sehingga string hasil tidak lagi berada di L. Hal ini bertentangan dengan pumping lemma dan menunjukkan L bukan bahasa reguler.

**Batas penting:** pumping lemma dapat membantu membuktikan bahasa tidak reguler, tetapi gagal menemukan pembagian yang melanggar lemma bukan bukti bahwa suatu bahasa reguler. Untuk membuktikan regularitas, gunakan konstruksi DFA/NFA, ekspresi reguler, atau metode pembuktian lain yang sesuai.

## 3.8. Context-Free Grammar (CFG)

CFG didefinisikan sebagai 4-tuple:

\[
G=(V,T,P,S)
\]

dengan:
- \(V\): variabel/nonterminal.
- \(T\): terminal, dengan himpunan terminal terpisah dari nonterminal.
- \(P\): aturan produksi.
- \(S\): simbol awal.

Sisi kiri produksi CFG berupa satu nonterminal dan sisi kanannya merupakan string terminal/nonterminal, termasuk kemungkinan epsilon sesuai grammar yang dibahas.

Derivasi menunjukkan bagaimana simbol awal menghasilkan suatu string. **Leftmost derivation** selalu mengganti nonterminal paling kiri terlebih dahulu; **rightmost derivation** mengganti nonterminal paling kanan. Parse tree menggambarkan struktur derivasi.

### Ambiguitas CFG

CFG ambigu jika setidaknya satu string memiliki lebih dari satu parse tree yang berbeda, atau lebih dari satu leftmost derivation untuk string tersebut. Ambiguitas penting dalam bahasa pemrograman karena ekspresi yang sama dapat ditafsirkan dengan urutan operasi berbeda.

Contohnya, grammar ekspresi yang tidak menetapkan prioritas dan asosiasi operator bisa membuat ekspresi seperti \(a+b*c\) memiliki lebih dari satu struktur. Ambiguitas dapat diselesaikan dengan aturan grammar yang menetapkan prioritas operator dan asosiasi.

Tidak semua bahasa context-free mempunyai grammar yang tidak ambigu. Bahasa yang tidak dapat dihasilkan oleh grammar CFG non-ambigu disebut inherently ambiguous.

### Chomsky Normal Form (CNF)

Bentuk normal Chomsky membatasi produksi, dalam bentuk standar, pada:

\[
A\rightarrow BC
\]

atau

\[
A\rightarrow a
\]

dengan A, B, C nonterminal dan a terminal. Produksi epsilon dapat diizinkan secara khusus untuk simbol awal jika bahasa memuat epsilon dan syarat formal tertentu dipenuhi. Konvensi pengecualian ini harus dinyatakan ketika mengubah grammar.

CNF berguna dalam algoritma parsing seperti CYK. Sebelum konversi, transformasi umumnya meliputi menghilangkan produksi epsilon (sesuai aturan), unit production, simbol yang tidak produktif/tidak terjangkau, lalu mengubah produksi agar sesuai CNF.

## 3.9. Pushdown Automaton (PDA)

PDA memperluas finite automaton dengan sebuah **stack** berprinsip LIFO (last in, first out). Stack memungkinkan mesin menyimpan informasi bertingkat seperti pencocokan tanda kurung atau struktur bersarang, yang tidak dapat ditangani oleh finite-state memory biasa untuk bahasa umum semacam itu.

PDA sering didefinisikan sebagai 7-tuple:

\[
M=(Q,\Sigma,\Gamma,\delta,q_0,Z_0,F)
\]

dengan:
- \(Q\): state.
- \(\Sigma\): alfabet input.
- \(\Gamma\): alfabet stack.
- \(\delta\): fungsi transisi PDA.
- \(q_0\): state awal.
- \(Z_0\): simbol awal stack.
- \(F\): accepting states, pada definisi yang menggunakan penerimaan berdasarkan state final.

Operasi stack meliputi:
- **Push:** menambahkan simbol ke puncak stack.
- **Pop:** menghapus simbol puncak.
- **Top/read:** memeriksa simbol puncak menurut model transisi.

### Contoh intuisi bahasa \(0^n1^n\)

PDA dapat mendorong satu simbol stack untuk setiap 0 yang dibaca. Setelah input beralih ke 1, mesin mem-pop satu simbol untuk setiap 1. Input dapat diterima jika jumlahnya seimbang dan seluruh 0 muncul sebelum 1, sesuai aturan penerimaan mesin. Stack tidak menyimpan urutan seluruh input; stack menghitung kebutuhan pencocokan secara bertingkat.

CFG dan nondeterministic PDA memiliki kemampuan yang ekuivalen dalam pengenalan bahasa context-free. PDA deterministik tidak mengenali seluruh bahasa context-free yang dapat dikenali oleh nondeterministic PDA; nondeterminisme penting dalam perbedaan kelas kemampuan ini.

## 3.10. Mesin Turing dan komputabilitas

Mesin Turing adalah model komputasi abstrak dengan finite control, pita (tape) yang menyimpan simbol, kepala baca/tulis, dan aturan transisi. Mesin dapat membaca simbol, menulis simbol, berpindah ke kiri/kanan, mengubah state, lalu berhenti atau berjalan selamanya.

Mesin Turing digunakan untuk merumuskan kemampuan komputasi secara umum. Model ini lebih kuat daripada finite-state automata dan PDA dalam hierarki bahasa standar karena memiliki pita kerja yang lebih umum.

Istilah kunci:
- **Decidable/recursive language:** terdapat algoritma/mesin yang selalu berhenti dan memberikan keputusan benar untuk setiap input.
- **Recognizable/recursively enumerable language:** terdapat mesin yang menerima semua string anggota; untuk string bukan anggota, mesin dapat menolak atau berjalan tanpa berhenti bergantung definisinya.
- **Undecidable problem:** tidak ada algoritma umum yang selalu berhenti dan menyelesaikan keputusan dengan benar untuk seluruh input.

### Halting Problem

Halting problem menanyakan apakah program/mesin tertentu akan berhenti ketika diberikan input tertentu. Secara umum, tidak ada algoritma yang dapat menjawab pertanyaan tersebut dengan benar untuk semua mesin dan input.

Gagasan bukti ketak-terputuskan menggunakan kontradiksi dan diagonalization: andaikan terdapat prosedur universal yang selalu benar memutuskan apakah mesin berhenti. Bentuk mesin lain yang sengaja berperilaku berlawanan dengan jawaban prosedur tersebut pada deskripsi dirinya sendiri, lalu timbul kontradiksi. Implikasinya, tidak semua persoalan dapat diselesaikan oleh algoritma umum, meski banyak kasus praktis dapat dianalisis atau dibatasi.

**Undecidable tidak sama dengan sulit/mahal.** Masalah undecidable tidak memiliki algoritma keputusan umum yang selalu selesai, sedangkan masalah yang mahal mungkin tetap decidable tetapi memerlukan waktu sangat besar.

### Target penguasaan Teori Bahasa dan Otomata

Anda seharusnya dapat mendefinisikan alfabet/string/bahasa, membangun DFA, mengonversi NFA ke DFA, meminimasi state, menulis regex formal, menggunakan pumping lemma untuk non-regularity, melakukan derivasi CFG dan mengenali ambiguitas, menjelaskan CNF dan PDA, serta membedakan decidable, recognizable, dan undecidable.

---

# 4. SINTESIS SEMESTER 7

Semester 7 mempertemukan tiga pola berpikir:
- **Metodologi ilmiah:** mendefinisikan masalah, mengkritik bukti, merancang evaluasi, dan melaporkan hasil secara transparan.
- **Data Mining:** mengubah data mentah menjadi pola yang dievaluasi untuk kebutuhan tertentu.
- **Teori Bahasa dan Otomata:** memformalkan bahasa serta menunjukkan kemampuan dan batas sebuah model komputasi.

Sebagai contoh, penelitian klasifikasi teks memerlukan RQ yang jelas, definisi kelas dan sumber data yang dapat dipertanggungjawabkan, preprocessing tanpa leakage, baseline yang adil, metrik yang sesuai, serta pelaporan keterbatasan. Teori bahasa dapat membantu memahami pencocokan pola reguler dan batas automata sederhana, sedangkan data mining menyediakan proses eksperimen dan penemuan pola.

Namun, jangan menyamakan metode yang berbeda. Regex formal cocok untuk bahasa reguler dan pola tertentu; ia bukan pengganti model semantik umum. Association rules mengukur asosiasi, bukan sebab-akibat. Hasil eksperimen pada satu dataset bukan bukti bahwa metode akan selalu unggul pada semua domain.

## 5. RUMUS DAN DEFINISI KUNCI

| Konsep | Rumus/aturan |
|---|---|
| Z-score | \(z=(x-\mu)/\sigma\) |
| Min-Max | \(x'=(x-x_{\min})/(x_{\max}-x_{\min})\) untuk rentang [0,1] |
| Support | \(P(X\cup Y)\) |
| Confidence | \(P(Y\mid X)=Support(X\cup Y)/Support(X)\) |
| Lift | \(Confidence(X\rightarrow Y)/Support(Y)\) |
| Cosine similarity | \((A\cdot B)/(\|A\|\|B\|)\) |
| DFA | \(M=(Q,\Sigma,\delta,q_0,F)\) |
| CFG | \(G=(V,T,P,S)\) |
| PDA | \(M=(Q,\Sigma,\Gamma,\delta,q_0,Z_0,F)\) |
| Pumping lemma reguler | \(w=xyz,\ |y|\ge1,\ |xy|\le p,\ xy^iz\in L\) untuk semua \(i\ge0\), bila L reguler |
| CNF | \(A\rightarrow BC\) atau \(A\rightarrow a\), dengan pengecualian epsilon untuk start symbol sesuai aturan |
| Evaluation ML | Pilih metrik sesuai kelas target dan biaya error; hindari leakage |

## 6. CHECKLIST SEBELUM UJIAN

- [ ] Membedakan proyek implementasi, penelitian empiris, penelitian formal, dan Design Science Research.
- [ ] Merumuskan research question, tujuan, gap, novelty, serta batasan yang saling konsisten.
- [ ] Menjelaskan tahap SLR dan membuat matriks komparasi penelitian.
- [ ] Memilih variabel, baseline, split data, dan metrik evaluasi yang adil.
- [ ] Membedakan internal, external, construct, dan conclusion validity.
- [ ] Menjelaskan IMRaD, gaya sitasi, dan fabrikasi/falsifikasi/plagiarisme.
- [ ] Menguraikan keenam fase CRISP-DM.
- [ ] Menangani missing values, outlier, scaling, dan PCA dengan asumsi yang jelas.
- [ ] Menghitung support, confidence, dan lift dari tabel transaksi.
- [ ] Menjelaskan downward closure dan menelusuri Apriori.
- [ ] Membandingkan Apriori dengan FP-Growth.
- [ ] Membedakan bagging/Random Forest dan boosting/XGBoost.
- [ ] Menjelaskan core, border, noise, epsilon, dan MinPts pada DBSCAN.
- [ ] Menghitung TF-IDF dan cosine similarity secara konseptual atau numerik.
- [ ] Mendefinisikan DFA, menelusuri string, dan mengonversi NFA ke DFA.
- [ ] Menjelaskan minimasi DFA dan prinsip Myhill–Nerode.
- [ ] Menggunakan pumping lemma untuk menunjukkan contoh bahasa bukan reguler.
- [ ] Melakukan derivasi grammar, menjelaskan ambiguitas, dan mengenali produksi CNF.
- [ ] Menjelaskan fungsi stack pada PDA dan mesin Turing.
- [ ] Membedakan bahasa decidable, recognizable, serta problem undecidable.

**Strategi belajar:** untuk materi riset, latih menjelaskan alasan metodologis dan bukti yang mendukung klaim. Untuk Data Mining, kerjakan contoh angka kecil sebelum memilih algoritma untuk dataset besar. Untuk Teori Bahasa dan Otomata, gambar diagram state/pohon derivasi dan tunjukkan langkah konstruksi secara formal; jawaban akhir saja sering tidak cukup membuktikan bahwa prosesnya benar.
