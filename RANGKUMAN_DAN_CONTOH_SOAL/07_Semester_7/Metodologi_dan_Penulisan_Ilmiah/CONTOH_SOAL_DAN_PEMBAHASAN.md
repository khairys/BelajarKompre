# Bank Contoh Soal & Pembahasan: Metodologi dan Penulisan Ilmiah

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Metodologi dan Penulisan Ilmiah Departemen Informatika Universitas Diponegoro (Koleksi Pengampu & Bank Soal HMIF 2023–2026).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (PERUMUSAN MASALAH, RESEARCH GAP & PROPOSAL)

### Soal UTS 1: Perumusan Masalah Riset & Identifikasi Research Gap (Soal Asli UTS Undip)
**Deskripsi Kasus:**
Seorang mahasiswa Informatika ingin meneliti pengenalan jenis hama tanaman padi menggunakan model kecerdasan buatan berbasis *Convolutional Neural Network (CNN)*:
* Penelitian terdahulu (Pratama dkk., 2022) berhasil mencapai akurasi $94\%$ menggunakan arsitektur ResNet-50 pada citra laboratorium dengan pencahayaan terkontrol.
* Namun, ketika model tersebut diuji pada foto lapangan nyata yang diambil langsung oleh petani di sawah dengan latar belakang daun yang kompleks, bayangan matahari, dan sudut miring, akurasi anjlok drastis menjadi $62\%$.
* Mahasiswa berencana mengusulkan modifikasi penambahan mekanisme atensi (*Coordinate Attention Mechanism*) dan teknik augmentasi citra spesifik (*CutMix & AutoAugment*).

**Tugas:**
1. Rumuskan **Latar Belakang Masalah** secara runut menggunakan struktur piramida terbalik!
2. Identifikasi **Kesenjangan Riset (*Research Gap*)** dan klaim **Kebaruan Ilmiah (*Novelty*)** yang diusulkan!
3. Susunlah **2 Rumusan Masalah Ilmiah (*Research Questions*)** yang spesifik dan terukur!
4. Tentukan batasan masalah (*limitations/scope*) penelitian yang jelas!

**Kunci Pembahasan & Solusi:**
1. **Penyusunan Latar Belakang (Piramida Terbalik):**
   * *Paragraf 1 (Konteks Global):* Kerusakan tanaman padi akibat serangan hama di Indonesia menurunkan produktivitas panen hingga 30%, sehingga deteksi dini otomatis sangat krusial.
   * *Paragraf 2 (State-of-the-Art):* Perkembangan deep learning CNN (seperti ResNet-50) telah terbukti efektif mengklasifikasikan citra hama dengan akurasi tinggi di atas 90% pada dataset laboratorium.
   * *Paragraf 3 (Masalah / Gap):* Namun pada kondisi riil di lahan persawahan, variasi pencahayaan ekstrem, bayangan tajam, dan latar belakang kanopi daun yang rumit menyebabkan penurunan akurasi drastis (*generalization drop*).
   * *Paragraf 4 (Solusi Kebaruan):* Diperlukan integrasi mekanisme *Coordinate Attention* yang mampu memfokuskan ekstraksi fitur spasial pada tubuh serangga hama sambil meredam noise latar belakang, dipadukan augmentasi *CutMix*.
2. **Research Gap & Novelty:**
   * *Research Gap:* Kerapuhan (*lack of robustness*) model CNN standar terhadap gangguan variasi lingkungan tak terkontrol pada dataset citra pertanian dunia nyata (*in-the-wild agricultural imagery*).
   * *Novelty:* Hibridisasi arsitektur ResNet dengan *Coordinate Attention Module* yang dioptimasi khusus untuk fitur morfologi serangga skala kecil pada citra sawah kompleks.
3. **Rumusan Masalah (Research Questions):**
   * *RQ-1:* "Bagaimana pengaruh integrasi mekanisme *Coordinate Attention* dan augmentasi *CutMix* terhadap peningkatan ketahanan (*robustness*) dan akurasi klasifikasi citra hama padi pada kondisi lapangan nyata?"
   * *RQ-2:* "Bagaimana performa komparatif arsitektur yang diusulkan dibandingkan dengan model dasar (*baseline*) ResNet-50 dan arsitektur pembanding mutakhir lainnya ditinjau dari metrik Precision, Recall, F1-Score, dan waktu inferensi?"
4. **Batasan Masalah:**
   * Dataset dibatasi pada 5 jenis hama utama tanaman padi di wilayah Jawa Tengah.
   * Citra masukan berupa foto digital berformat RGB dengan resolusi minimal $512 \times 512$ piksel.
   * Evaluasi komputasi tidak mencakup deployment pada perangkat edge IoT mikrokontroler daya rendah.

---

### Soal UTS 2: Penyusunan Matriks State-of-the-Art Tinjauan Pustaka
**Deskripsi Soal:**
Jelaskan fungsi dari **Matriks Komparasi Tinjauan Pustaka (*State-of-the-Art Table*)** dalam Bab II Proposal Skripsi, dan buatlah contoh tabel matriks perbandingan untuk 3 artikel jurnal rujukan utama!

**Kunci Pembahasan & Solusi:**
*Matriks State-of-the-Art* berfungsi memetakan penelitian-penelitian terdahulu yang relevan secara sistematis untuk membuktikan secara visual kepada dosen penguji posisi penelitian peneliti (*where my research stands*), kelemahan metode sebelumnya, serta letak celah riset yang akan diisi oleh penelitian saat ini.

*Contoh Matriks State-of-the-Art:*

| Peneliti & Tahun | Metode yang Digunakan | Dataset / Kasus | Hasil / Metrik | Keterbatasan / Research Gap |
|:---|:---|:---|:---|:---|
| **Pratama et al. (2022) [IEEE]** | ResNet-50 Standar | 5.000 citra hama laboratorium | Akurasi $94.2\%$ | Gagal generalisasi pada citra lapangan nyata dengan noise bayangan matahari. |
| **Kumar & Singh (2023) [Springer]** | YOLOv5 + Data Augmentasi Tradisional | 3.500 citra lapangan terbuka | mAP $76.8\%$ | Waktu inferensi cepat namun sering terjadi salah deteksi (*False Positive*) pada serangga berukuran sangat kecil. |
| **Penelitian yang Diusulkan (2024)** | **ResNet-50 + Coordinate Attention + CutMix** | **5.000 citra lapangan terbuka Undip Agri-Dataset** | *(Target Akurasi $\ge 88\%$, F1 $\ge 0.85$)* | **Mengatasi masalah noise latar belakang dan serangga kecil via atensi spasial dua-arah.** |

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (SITASI IEEE, DESAIN EKSPERIMEN & ETIKA)

### Soal UAS 1: Standar Format Sitasi dan Daftar Pustaka Gaya IEEE
**Deskripsi Soal:**
Diberikan 3 buah sumber referensi akademik:
1. Sebuah artikel jurnal: Ditulis oleh Alan Mathison Turing, berjudul "Computing Machinery and Intelligence", terbit di jurnal *Mind*, Volume 59, Nomor 236, Halaman 433-460, pada tahun 1950, dengan DOI: 10.1093/mind/LIX.236.433.
2. Sebuah makalah konferensi prosiding: Ditulis oleh Kaiming He, Xiangyu Zhang, Shaoqing Ren, dan Jian Sun, berjudul "Deep Residual Learning for Image Recognition", dipresentasikan pada *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, Halaman 770-778, tahun 2016.
3. Sebuah buku teks: Ditulis oleh Stuart Russell dan Peter Norvig, berjudul "Artificial Intelligence: A Modern Approach", Edisi ke-4, diterbitkan oleh Pearson di kota Boston, tahun 2020.

Tuliskan penulisan entri bibliografi daftar pustaka yang benar untuk ketiga sumber di atas sesuai format baku **IEEE Citation Style**!

**Kunci Pembahasan & Solusi:**
*Format Baku Daftar Pustaka Standar IEEE:*
```text
[1] A. M. Turing, "Computing machinery and intelligence," Mind, vol. 59, no. 236, pp. 433-460, 1950, doi: 10.1093/mind/LIX.236.433.

[2] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), 2016, pp. 770-778.

[3] S. Russell and P. Norvig, Artificial Intelligence: A Modern Approach, 4th ed. Boston, MA, USA: Pearson, 2020.
```
*(Aturan Penulisan IEEE: Nama penulis disingkat huruf depan inisial diikuti nama belakang utuh; Judul artikel jurnal/makalah diapit tanda petik ganda; Nama jurnal/buku/prosiding dicetak miring / italic; Penomoran menggunakan kurung siku berurutan).*

---

### Soal UAS 2: Analisis Pelanggaran Etika Ilmiah FFP & Teknik Parafrase
**Deskripsi Soal:**
1. Jelaskan perbedaan antara **Fabrikasi (*Fabrication*)**, **Falsifikasi (*Falsification*)**, dan **Plagiarisme (*Plagiarism*)** dalam penelitian komputasi!
2. Diberikan teks asli dari sebuah jurnal internasional:
   > *"Supervised learning algorithms require large amounts of labeled training data to achieve high classification accuracy, which is often expensive and time-consuming to obtain in medical applications."*
   
   Buatlah **parafrase legal** yang benar dari teks di atas untuk dimasukkan ke dalam skripsi Anda tanpa memicu deteksi kemiripan Turnitin, lengkap dengan sitasi yang tepat!

**Kunci Pembahasan & Solusi:**
1. **Perbedaan Pelanggaran FFP:**
   * **Fabrikasi (Fabrication):** Mengarang atau membuat data eksperimen palsu. *Contoh di IT:* Peneliti tidak pernah melatih model AI atau tidak pernah menguji program ke responden, namun mengisi tabel akurasi di skripsi dengan angka-angka karangan sendiri.
   * **Falsifikasi (Falsification):** Memanipulasi proses riset atau mengubah data hasil uji yang sebenarnya. *Contoh di IT:* Model deep learning peneliti sebenarnya menghasilkan 15 data uji salah deteksi, tetapi peneliti sengaja menghapus data yang salah tersebut dari tabel hasil agar akurasi tampak sempurna 100%.
   * **Plagiarisme (Plagiarism):** Mengambil ide, kata-kata, kode sumber, atau diagram milik orang lain dan mengakuinya sebagai karya cipta sendiri tanpa menyebutkan sumber rujukan secara sah.
2. **Teknik Parafrase Legal yang Benar:**
   * *Trik Parafrase:* Ubah struktur kalimat (dari aktif ke pasif atau sebaliknya), gunakan sinonim akademis yang tepat, dan ubah sudut pandang alur gagasan tanpa menghilangkan makna asli.
   * *Contoh Parafrase yang Sah:*
     > *"Tingginya biaya dan lamanya waktu yang dibutuhkan untuk proses anotasi data klinis sering kali menjadi tantangan utama dalam implementasi kecerdasan buatan medis, mengingat metode pembelajaran terbimbing sangat bergantung pada ketersediaan data berlabel dalam volume masif [4]."*
     *(Parafrase ini berhasil mengubah total struktur sintaksis kata, namun tetap mempertahankan intisari gagasan dan menyertakan sitasi formal `[4]`).*

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Coba jelaskan dalam 2 menit: Apa masalah penelitian skripsi Anda, mengapa masalah itu penting diselesaikan sekarang, dan apa bukti bahwa metode yang Anda usulkan benar-benar baru (memiliki novelty)?"
**Jawaban Komprehensif (Strategi Elevator Pitch Skripsi):**
* *"Bapak/Ibu Penguji, masalah utama yang saya angkat adalah rendahnya ketahanan model deteksi objek lalu lintas pada kondisi cuaca hujan lebat malam hari, di mana akurasi model baseline YOLOv8 turun hingga $35\%$ akibat pembiasan cahaya lampu dan tetesan air pada lensa kamera."*
* *"Masalah ini sangat mendesak diselesaikan karena menyangkut sistem navigasi keselamatan kendaraan otonom cerdas untuk mencegah tabrakan fatal di jalan raya."*
* *"Kebaruan (*novelty*) dari penelitian saya terletak pada perancangan modul prapemrosesan adaptif berbasis *Physics-Informed De-raining Filter* yang diintegrasikan langsung pada lapisan *backbone feature extraction* jaringan neural. Berdasarkan tinjauan pustaka sistematis terhadap 25 artikel jurnal Scopus/IEEE 3 tahun terakhir, pendekatan hibrida integrasi fisik-optik pada arsitektur YOLO ini belum pernah diusulkan sebelumnya."*

### Q2: "Mengapa Anda memilih metrik evaluasi F1-Score dan AUC-ROC untuk mengevaluasi model skripsi Anda, alih-alih hanya menggunakan metrik Akurasi standar?"
**Jawaban Komprehensif:**
* *"Karena dataset transaksi penipuan (*credit card fraud*) yang saya gunakan dalam skripsi ini memiliki karakteristik distribusi kelas yang sangat timpang (*highly imbalanced class distribution*), yaitu terdapat $99.2\%$ transaksi normal dan hanya $0.8\%$ transaksi penipuan."*
* *"Jika saya hanya menggunakan metrik Akurasi, model dummy yang memprediksi seluruh transaksi sebagai normal tanpa memproses apapun akan secara otomatis memperoleh akurasi semu sebesar $99.2\%$, namun gagal mendeteksi satupun penipuan (Recall $= 0\%$)."*
* *"Oleh karena itu, saya menggunakan **F1-Score** karena metrik ini menghitung rata-rata harmonik antara Presisi dan Recall secara seimbang. Selain itu, saya menggunakan kurva **AUC-ROC** untuk mengukur kemampuan diskriminasi model dalam memisahkan kedua kelas pada berbagai ambang batas klasifikasi (*classification thresholds*), yang membuktikan keandalan model bebas dari bias kelas mayoritas."*
