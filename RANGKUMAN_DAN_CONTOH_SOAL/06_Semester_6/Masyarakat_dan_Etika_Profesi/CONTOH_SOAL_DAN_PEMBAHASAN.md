# Bank Contoh Soal & Pembahasan: Masyarakat dan Etika Profesi

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Masyarakat dan Etika Profesi Departemen Informatika Universitas Diponegoro (Koleksi Pengampu & Bank Soal HMIF 2018–2022).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (HAKI, KODE ETIK ACM & LISENSI SOFTWARE)

### Soal UTS 1: Komparasi Hak Cipta vs Paten & Lisensi Open Source (Soal Asli UTS Undip 2021)
**Deskripsi Soal:**
1. Sebutkan dan jelaskan 3 perbedaan mendasar antara **Hak Cipta (*Copyright*)** dan **Paten (*Patent*)** dalam konteks perlindungan hukum produk perangkat lunak (*software*)!
2. Jelaskan konsep lisensi **Copyleft** pada perangkat lunak bebas (seperti GNU General Public License / GPL), dan bandingkan dengan lisensi **Permisif** (seperti MIT License)! Apa konsekuensi hukumnya bagi perusahaan komersial yang memasukkan kode berlisensi GPL ke dalam produk perangkat lunak mereka?

**Kunci Pembahasan & Solusi:**
1. **Tiga Perbedaan Mendasar Hak Cipta vs Paten Perangkat Lunak:**

| Parameter Pembeda | Hak Cipta (*Copyright*) | Paten (*Patent*) |
|:---|:---|:---|
| **Objek yang Dilindungi** | Melindungi **ekspresi bentuk karya** nyata (baris kode sumber, file biner, antarmuka visual teks). Ide atau algoritma di baliknya tidak dilindungi. | Melindungi **invensi teknologi fungsional / cara kerja proses** yang memiliki langkah inventif dan dapat diterapkan industri. |
| **Mekanisme Lahirnya Hak** | **Deklaratif Otomatis:** Hak perlindungan lahir seketika saat kode selesai ditulis/diwujudkan, tanpa kewajiban pendaftaran formal. | **Konstitutif (*First-to-File*):** Hak baru lahir setelah diajukan permohonan pendaftaran resmi dan lulus pemeriksaan substantif kebaruan (*novelty*) oleh DJKI. |
| **Masa Berlaku Perlindungan** | Jangka panjang: Berlaku selama masa hidup pencipta $+ 70$ tahun (atau 50 tahun sejak publikasi untuk badan hukum/software). | Jangka pendek: Berlaku tepat **20 tahun** sejak tanggal penerimaan permohonan dan tidak dapat diperpanjang. |
| **Perlakuan Kode Program** | Kode program komputer murni dilindungi penuh sebagai ciptaan tersendiri. | Kode program komputer murni (*software as such*) **tidak dapat dipatenkan**, kecuali software yang terikat integrasi fisik dengan perangkat keras. |

2. **Perbandingan Lisensi Copyleft vs Permissive:**
   * **Lisensi Copyleft (Contoh: GNU GPL v3):**
     * Menerapkan prinsip *reciprocity / share-alike*: Siapapun bebas menggunakan, memodifikasi, dan menyebarkan kode tersebut, **DENGAN SYARAT MUTLAK** bahwa setiap perangkat lunak turunan (*derivative work*) yang dibuat wajib dilisensikan kembali di bawah lisensi GNU GPL yang sama dan **kode sumbernya wajib dibuka secara bebas ke publik**.
   * **Lisensi Permissive (Contoh: MIT License, Apache 2.0):**
     * Sangat longgar dan ramah bisnis komersial. Pengguna diizinkan menyalin, memodifikasi, bahkan menggabungkan kode tersebut ke dalam produk perangkat lunak berpemilik komersial tertutup (*closed-source proprietary*), asalkan tetap mencantumkan klausul atribusi nama pembuat aslinya (*copyright notice*).
   * **Konsekuensi Hukum bagi Perusahaan Komersial:**
     * Jika sebuah perusahaan secara ceroboh memasukkan library atau modul berlisensi **GNU GPL** ke dalam produk software komersial berbayarnya (*proprietary software*), maka secara hukum produk tersebut dianggap sebagai karya turunan GPL (*GPL Contamination / Viral Effect*).
     * Jika terjadi gugatan hukum di pengadilan (oleh FSF atau komunitas open source), perusahaan **wajib membuka seluruh kode sumber produk komersialnya ke publik secara gratis**, atau diwajibkan menarik seluruh produk tersebut dari peredaran pasar dan membayar ganti rugi pelanggaran lisensi hak cipta.

---

### Soal UTS 2: Penerapan Kode Etik Rekayasa Perangkat Lunak ACM / IEEE-CS
**Deskripsi Soal:**
Seorang Senior Software Engineer di sebuah perusahaan startup teknologi medis diminta oleh manajemen atas (*C-Level*) untuk mempercepat perilisan perangkat lunak monitor infus rumah sakit. Engineer tersebut menemukan adanya *memory leak bug* langka yang terjadi setiap sistem berjalan nonstop selama 72 jam, yang berpotensi menyebabkan dosis obat overdosis pada pasien. Manajemen menolak penundaan rilis karena akan kehilangan kontrak bernilai miliaran rupiah dan mengancam memecat sang engineer jika ia membocorkan masalah ini.
Evaluasi dilema etika di atas menggunakan **Kode Etik ACM / IEEE-CS**:
1. Prinsip manakah dari 8 prinsip etika yang menjadi kewajiban moral tertinggi bagi sang engineer?
2. Tindakan etis apa yang wajib diambil oleh sang engineer secara berjenjang?

**Kunci Pembahasan & Solusi:**
1. **Kewajiban Moral Tertinggi:**
   * **Prinsip 1: PUBLIC (Kepentingan Publik).**
     Kode Etik ACM/IEEE secara eksplisit menetapkan aturan mutlak: *"Software engineers shall act consistently with the public interest."* (Insinyur perangkat lunak wajib menempatkan keselamatan, kesehatan, dan kesejahteraan masyarakat publik di atas kepentingan pribadi, kepentingan klien, maupun kepentingan atasan).
   * Nyawa pasien berada dalam bahaya nyata (*safety-critical hazard*). Oleh karena itu, kepentingan finansial kontrak perusahaan harus dikorbankan demi melindungi keselamatan pasien.
2. **Tindakan Etis Berjenjang yang Wajib Diambil:**
   * *Langkah 1 (Dokumentasi Formal Internal):* Menulis laporan teknis resmi (*audit trail*) secara tertulis dan terperinci kepada pimpinan manajemen dan direksi, membuktikan bahaya matematis memory leak bug tersebut dan secara tegas menolak menandatangani persetujuan rilis produk (*refuse to sign-off release*).
   * *Langkah 2 (Eskalasi Komite Etik):* Membawa isu tersebut ke komite audit kepatuhan internal perusahaan atau dewan komisaris.
   * *Langkah 3 (Whistleblowing Eksternal):* Jika manajemen tetap memaksakan rilis produk dan mengabaikan keselamatan publik, sang insinyur memiliki kewajiban moral dan etika profesi untuk menjadi *Whistleblower* dengan melaporkan bahaya cacat produk tersebut kepada otoritas pengawas obat dan alat kesehatan (seperti BPOM / Kementerian Kesehatan) guna mencegah kematian massal pasien.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (ANALISIS DELIK UU ITE & PRIVASI UU PDP)

### Soal UAS 1: Analisis Yuridis Pidana Kejahatan Siber UU ITE
**Deskripsi Soal:**
Seorang mantan administrator sistem (Doni) merasa sakit hati karena diberhentikan secara sepihak dari sebuah platform e-commerce. Doni memanfaatkan akun kredensial cadangan tersembunyi (*backdoor*) miliknya untuk masuk ke server basis data perusahaan di luar jam kerja, mengunduh data 50.000 riwayat transaksi kartu kredit nasabah, lalu mengubah script landing page situs utama dengan pesan makian (*web defacement*), serta menghapus indeks database pembayaran sehingga server transaksi lumpuh total selama 12 jam.
Identifikasi pasal-pasal dalam **Undang-Undang Informasi dan Transaksi Elektronik (UU ITE)** yang dilanggar oleh Doni beserta unsur-unsur delik pidananya!

**Kunci Pembahasan & Solusi:**
Tindakan Doni secara yuridis memenuhi unsur-unsur tindak pidana siber dalam UU ITE:
1. **Pelanggaran Pasal 30 UU ITE (Akses Ilegal / Unauthorized Access):**
   * *Ayat (1):* Mengakses komputer atau sistem elektronik milik orang lain secara tanpa hak atau melawan hukum (menggunakan akun backdoor di luar izin wewenang kerja).
   * *Ayat (2):* Mengakses sistem dengan tujuan untuk memperoleh informasi elektronik rahasia (mengunduh 50.000 data kartu kredit nasabah).
   * *Ayat (3):* Menerobos sistem pengamanan elektronik.
2. **Pelanggaran Pasal 32 UU ITE (Perusakan dan Pemindahan Data Ilegal):**
   * *Ayat (1):* Mengubah, menambah, mengurangi, merusak, atau memindahkan data elektronik milik orang lain secara tanpa hak (mengganti landing page / defacement, memodifikasi script server).
   * *Ayat (2):* Memindahkan data rahasia ke tempat yang tidak berhak (mentransfer database kartu kredit ke komputer pribadi).
3. **Pelanggaran Pasal 33 UU ITE (Gangguan Sistem / System Interference):**
   * Melakukan tindakan apapun yang berakibat terganggunya sistem elektronik atau mengakibatkan sistem tidak berfungsi sebagaimana mestinya (menghapus indeks database yang melumpuhkan layanan transaksi pembayaran selama 12 jam).
   * *Konsekuensi Hukum:* Doni dapat dikenakan dakwaan pasal berlapis (*kumulatif*) dengan ancaman pidana penjara maksimal 10 tahun dan denda hingga Rp 10 miliar.

---

### Soal UAS 2: Hak Asasi Subjek Data Berdasarkan UU Perlindungan Data Pribadi (UU PDP No. 27/2022)
**Deskripsi Soal:**
Seorang pengguna aplikasi pinjaman online memutuskan untuk melunasi seluruh kewajibannya dan menutup akunnya secara permanen. Pengguna tersebut kemudian mengajukan permohonan resmi kepada perusahaan aplikasi tersebut untuk menghapus seluruh foto KTP, rekaman wajah biometrik, dan riwayat kontak telepon dari server perusahaan. Namun, pihak aplikasi menolak dengan alasan *"Data tersebut adalah milik perusahaan untuk arsip selamanya"*.
Evaluasi kasus di atas berdasarkan ketentuan **UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi (UU PDP)**!
1. Apakah penolakan perusahaan tersebut dibenarkan secara hukum?
2. Sebutkan hak subjek data pribadi yang dilanggar perusahaan!
3. Sanksi administratif apa yang dapat dijatuhkan kepada perusahaan pengendali data pribadi yang melanggar aturan tersebut?

**Kunci Pembahasan & Solusi:**
1. **Keabsahan Penolakan Perusahaan:**
   Penolakan perusahaan tersebut **TIDAK DIBENARKAN SECARA HUKUM (Melanggar Hukum UU PDP)**. Berdasarkan asas kedaulatan data, data pribadi bukanlah hak milik mutlak perusahaan, melainkan hak asasi subjek data yang dititipkan pemrosesannya berdasarkan persetujuan (*consent*). Ketika hubungan hukum/kontrak pinjaman telah tuntas dan tujuan pemrosesan data telah tercapai, perusahaan wajib menghentikan pemrosesan dan menghapus data tersebut.
2. **Hak Subjek Data yang Dilanggar (Pasal 8 & 9 UU PDP):**
   * **Hak untuk Menarik Kembali Persetujuan (*Withdrawal of Consent*):** Subjek data berhak menarik kembali persetujuan pemrosesan data pribadinya kapan saja.
   * **Hak Penghapusan dan Pemusnahan Data (*Right to Erasure / Right to be Forgotten*):** Subjek data berhak menuntut penghapusan dan/atau pemusnahan data pribadi miliknya yang tidak lagi relevan dengan tujuan awal pengumpulannya.
3. **Sanksi Administratif bagi Perusahaan Pelanggar (Pasal 57 UU PDP):**
   Lembaga Otoritas Pengawas Perlindungan Data Pribadi berwenang menjatuhkan sanksi administratif berupa:
   * Peringatan tertulis resmi.
   * Penghentian sementara seluruh kegiatan pemrosesan data pribadi.
   * Perintah pemusnahan data pribadi seketika.
   * **Denda Administratif maksimal sebesar $2\%$ dari total pendapatan tahunan (*annual turnover*)** perusahaan yang bersangkutan.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan apa itu Bias Algoritmik dalam sistem kecerdasan buatan (AI) modern, bagaimana bias tersebut dapat melanggar prinsip keadilan etika, dan apa tanggung jawab profesional seorang data scientist untuk mencegahnya?"
**Jawaban Komprehensif:**
* **Definisi Bias Algoritmik:** Terjadinya diskriminasi sistematis dan tidak adil dalam keluaran model AI terhadap kelompok ras, gender, agama, atau status sosio-ekonomi tertentu. Bias terjadi bukan karena mesin memiliki niat jahat, melainkan karena **data latih historis (*historical training data*)** yang diumpankan ke model sudah memuat prasangka sosial masa lalu manusia (contoh: model AI penyaring CV rekrutmen yang secara tidak sadar mendiskriminasi pelamar wanita karena data manajer sukses 20 tahun terakhir di perusahaan tersebut didominasi pria).
* **Pelanggaran Keadilan Etika (*Justice & Fairness*):** Menolak hak seseorang atas pekerjaan, kredit perbankan, atau asuransi semata-mata karena label demografis yang tidak relevan dengan kualifikasi meritokratis nyata.
* **Tanggung Jawab Profesional Data Scientist:**
  1. *Audit Kualitas Data Latih:* Melakukan pembersihan data (*data debiasing*) dan menyeimbangkan proporsi representasi kelompok minoritas sebelum pelatihan model.
  2. *Uji Disparitas Kinerja (*Fairness Metrics*):* Memeriksa metrik *Equalized Odds* dan *Demographic Parity* untuk memastikan akurasi model setara di semua subkelompok.
  3. *Menerapkan Explainable AI (XAI):* Memastikan keputusan model dapat dijelaskan logikanya kepada manusia dan menyediakan jalur banding manual (*Human-in-the-loop*).

### Q2: "Apa perbedaan antara Etika Utilitarianisme dan Etika Deontologi Kantian saat seorang insinyur sistem keselamatan mengaudit perangkat lunak mobil otonom yang menghadapi situasi darurat kecelakaan yang tak terhindarkan (Trolley Problem)?"
**Jawaban Komprehensif:**
* **Berdasarkan Sudut Pandang Utilitarianisme:**
  Sistem mobil otonom diprogram untuk mengevaluasi kalkulasi matematis utilitas korban seminimal mungkin: jika membanting setir ke kiri menabrak 1 orang pejalan kaki dapat menyelamatkan 5 orang penumpang di dalam mobil, maka algoritma utilitarian **akan memilih membanting setir menabrak 1 orang tersebut demi menyelamatkan jumlah nyawa terbanyak (5 nyawa > 1 nyawa)**.
* **Berdasarkan Sudut Pandang Deontologi Kantian:**
  Kantian menolak keras pemikiran bahwa satu orang manusia boleh dikorbankan sebagai alat (*means*) untuk menyelamatkan orang lain. Memprogram mobil untuk sengaja mengorbankan pejalan kaki yang tidak bersalah adalah pelanggaran moral mutlak (*Categorical Imperative*). Pendekatan Kantian menuntut mobil mengerem darurat sekuat tenaga pada jalurnya tanpa melakukan manuver diskriminatif membidik target korban tertentu, karena hak hidup setiap individu manusia adalah suci dan tidak boleh diperdagangkan dalam kalkulasi aritmetika keuntungan.
