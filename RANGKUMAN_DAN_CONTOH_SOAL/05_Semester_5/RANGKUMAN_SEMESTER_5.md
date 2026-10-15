# RANGKUMAN LENGKAP SEMESTER 5
## Persiapan Ujian Komprehensif S1 Informatika — Universitas Diponegoro

Semester 5 menghubungkan ilmu komputasi dengan penerapan nyata: melindungi sistem dan data, membangun aplikasi lintas platform, membuat model prediktif, mengelola proyek perangkat lunak, serta menggunakan teknologi untuk mendukung strategi bisnis. Beberapa mata kuliah menekankan rumus dan algoritma, sementara yang lain menuntut kemampuan menganalisis situasi dan mengambil keputusan yang dapat dipertanggungjawabkan.

Rangkuman ini mengikuti struktur mata kuliah pada folder Semester 5 di repositori BelajarKompre. Materi diuraikan dari konsep dasar hingga rumus, contoh penerapan, perbandingan penting, dan kemampuan yang harus dikuasai untuk ujian komprehensif.

## Gambaran Umum Semester 5

| Mata kuliah | Fokus utama |
|---|---|
| Keamanan dan Jaminan Informasi | Menilai risiko dan menjaga kerahasiaan, integritas, ketersediaan, identitas, serta kepercayaan sistem |
| Kewirausahaan | Memvalidasi peluang, merancang model bisnis, memasarkan produk, dan menghitung kelayakan finansial |
| Komputasi Tersebar dan Paralel | Mengatur komputasi lintas mesin, sinkronisasi, konsensus, paralelisme, dan pemrosesan data besar |
| Pembelajaran Mesin | Belajar pola dari data untuk klasifikasi, prediksi, pengelompokan, dan evaluasi model |
| Pengembangan Berbasis Platform | Membangun aplikasi web klien-server, REST API, dan aplikasi mobile Android |
| Proyek Perangkat Lunak | Mengorganisasi pengembangan produk dalam tim melalui Scrum, Git, CI/CD, container, dan UAT |
| Sistem Informasi | Mengintegrasikan manusia, proses, dan teknologi untuk memperbaiki keputusan serta daya saing organisasi |

Hubungan antarmata kuliah terlihat dalam sebuah produk digital. Pembelajaran Mesin dapat menyediakan model klasifikasi; Pengembangan Berbasis Platform menyajikannya melalui web atau mobile; Keamanan dan Jaminan Informasi melindungi akun, API, dan data; Komputasi Tersebar dan Paralel membantu menangani beban kerja besar; Proyek Perangkat Lunak mengatur proses tim; Sistem Informasi menilai manfaatnya untuk organisasi; dan Kewirausahaan membahas apakah produk tersebut memiliki pelanggan serta model pendapatan yang masuk akal.

**Catatan kurikulum:** pengelompokan semester di rangkuman ini mengikuti folder Kurikulum 2020 yang digunakan repositori. Dokumen sumber menyebut sejumlah mata kuliah sebagai mata kuliah Semester 5 untuk Kurikulum 2020 maupun Kurikulum 2024, tetapi susunan kurikulum dan kode mata kuliah dapat berbeda. Gunakan silabus resmi angkatan sebagai acuan administratif.

---

# 1. KEAMANAN DAN JAMINAN INFORMASI

Sumber: [Rangkuman Materi Keamanan dan Jaminan Informasi](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/Keamanan_dan_Jaminan_Informasi/RANGKUMAN_MATERI.md)

## 1.1. Tujuan keamanan informasi

Keamanan informasi adalah upaya melindungi informasi dan sistem yang memprosesnya terhadap akses, penggunaan, pengungkapan, perubahan, gangguan, atau penghancuran yang tidak sah. Keamanan bukan hanya memasang antivirus. Perlindungan yang baik mencakup teknologi, manusia, prosedur, kebijakan, fasilitas fisik, dan manajemen risiko.

Aset yang perlu dilindungi dapat berupa data pelanggan, kredensial login, kode sumber, server, jaringan, perangkat pengguna, layanan bisnis, ataupun reputasi organisasi. Ancaman merupakan sesuatu yang berpotensi menimbulkan kerugian; kerentanan adalah kelemahan yang dapat dieksploitasi; risiko menghubungkan kemungkinan terjadinya insiden dengan dampaknya.

### CIA Triad

| Prinsip | Makna | Contoh pelanggaran | Kontrol umum |
|---|---|---|---|
| Confidentiality (kerahasiaan) | Informasi hanya dapat diakses pihak yang berwenang | Data pribadi dibaca penyerang | Enkripsi, otorisasi, least privilege |
| Integrity (integritas) | Informasi tetap akurat, lengkap, dan tidak diubah tanpa izin | Nilai transaksi diubah secara ilegal | Hash, MAC, tanda tangan digital, audit log |
| Availability (ketersediaan) | Sistem dan data tersedia saat dibutuhkan pengguna sah | Situs lumpuh akibat DDoS | Redundansi, backup, mitigasi DDoS, failover |

Pelanggaran CIA sering dijelaskan dengan DAD: **Disclosure** merusak kerahasiaan, **Alteration** merusak integritas, dan **Destruction/Denial** merusak ketersediaan. Parkerian Hexad memperluas CIA dengan **possession/control** (penguasaan data), **authenticity** (keaslian), dan **utility** (kegunaan data). Sebagai contoh, file terenkripsi yang kuncinya hilang mungkin tetap rahasia dan tidak berubah, tetapi tidak lagi berguna bagi pemiliknya.

### Ancaman, kerentanan, dan serangan

- **Malware:** perangkat lunak berbahaya, seperti virus, worm, trojan, spyware, dan ransomware.
- **Phishing/social engineering:** memanipulasi manusia agar menyerahkan kredensial atau menjalankan tindakan berbahaya.
- **DoS/DDoS:** menghabiskan sumber daya sistem atau jaringan agar layanan tidak tersedia.
- **Man-in-the-Middle (MitM):** penyerang berada di jalur komunikasi untuk menyadap atau mengubah pesan.
- **Insider threat:** ancaman dari orang yang telah memiliki akses sah, baik disengaja maupun tidak disengaja.
- **Password attack:** menebak kata sandi, menggunakan kredensial yang bocor, atau mencoba banyak kemungkinan.
- **Eksploitasi kerentanan:** memanfaatkan kesalahan konfigurasi, kelemahan perangkat lunak, atau kontrol akses yang tidak memadai.

Perbedaan istilah penting: **ancaman tidak sama dengan kerentanan**. Penyerang adalah salah satu sumber ancaman; celah pada aplikasi merupakan kerentanan; kemungkinan dan dampak eksploitasi celah itulah yang dinilai sebagai risiko. Kontrol keamanan dapat bersifat **preventif** (mencegah), **detektif** (menemukan), atau **korektif/pemulihan** (memperbaiki dampak).

## 1.2. Tata kelola keamanan dan manajemen risiko

Keamanan perlu dijalankan sebagai proses berulang: identifikasi aset, penilaian ancaman dan kerentanan, analisis risiko, pemilihan kontrol, penerapan kebijakan, pemantauan, audit, dan perbaikan. ISO/IEC 27001 berhubungan dengan penerapan **Information Security Management System (ISMS)**: organisasi mengelola risiko keamanan secara sistematis dan berkelanjutan. Kerangka NIST Cybersecurity Framework juga membantu mengorganisasi aktivitas keamanan ke dalam fungsi seperti Govern, Identify, Protect, Detect, Respond, dan Recover.

Dokumen tata kelola yang umum adalah kebijakan tingkat organisasi, standar teknis, prosedur operasional, dan pedoman. Kebijakan menjelaskan arah dan aturan yang wajib dipatuhi; standar mendefinisikan persyaratan minimum; prosedur menjelaskan langkah kerja; pedoman memberi rekomendasi praktik.

### Rumus risiko kuantitatif

Misalkan sebuah server bernilai Rp100.000.000 dan insiden diperkirakan menyebabkan kerusakan 30% dari nilai aset.

\[
SLE = AV \times EF
\]

- **AV (Asset Value):** nilai aset.
- **EF (Exposure Factor):** proporsi nilai aset yang hilang atau terkena dampak dalam satu kejadian.
- **SLE (Single Loss Expectancy):** kerugian moneter per kejadian.

\[
SLE = Rp100.000.000 \times 0{,}30 = Rp30.000.000
\]

Jika insiden rata-rata terjadi dua kali per tahun, maka **ARO (Annualized Rate of Occurrence) = 2**.

\[
ALE = SLE \times ARO
\]

\[
ALE = Rp30.000.000 \times 2 = Rp60.000.000/tahun
\]

**ALE (Annualized Loss Expectancy)** adalah perkiraan kerugian tahunan. Angka tersebut merupakan estimasi untuk pengambilan keputusan, bukan jaminan bahwa kerugian aktual persis sama.

Untuk menilai manfaat kontrol, gunakan:

\[
Manfaat\ Bersih = ALE_{sebelum}-ALE_{sesudah}-Biaya\ Kontrol
\]

Jika ALE sebelum kontrol Rp60 juta, setelah kontrol Rp10 juta, dan biaya kontrol tahunan Rp20 juta, manfaat bersih yang diperkirakan ialah Rp30 juta per tahun. Selain nilai finansial, keputusan juga harus mempertimbangkan kewajiban hukum, dampak reputasi, keselamatan, dan toleransi risiko organisasi.

## 1.3. Model kendali akses

Kendali akses menentukan **siapa** boleh melakukan **aksi apa** terhadap **objek yang mana**. Autentikasi memeriksa identitas (misalnya kata sandi dan MFA); otorisasi memeriksa izin setelah identitas diketahui; accounting/auditing mencatat aktivitas untuk penelusuran.

| Model | Prinsip | Kekuatan | Risiko/keterbatasan |
|---|---|---|---|
| DAC (Discretionary Access Control) | Pemilik objek dapat mengatur izin pengguna lain | Fleksibel dan mudah diterapkan | Kesalahan pemilik dapat memperluas akses |
| MAC (Mandatory Access Control) | Akses mengikuti label klasifikasi dan clearance terpusat | Cocok untuk kebutuhan klasifikasi ketat | Lebih kaku dan administrasinya kompleks |
| RBAC (Role-Based Access Control) | Izin diberikan kepada peran/jabatan, lalu pengguna memperoleh peran | Efektif untuk organisasi besar | Peran yang terlalu banyak atau terlalu luas sulit dikelola |
| ABAC (Attribute-Based Access Control) | Keputusan akses berdasarkan atribut pengguna, objek, tindakan, dan konteks | Granular dan kontekstual | Kebijakan dan evaluasinya lebih kompleks |

**Bell–LaPadula** menekankan kerahasiaan. Aturan ringkasnya: **no read up**—subjek tidak membaca data dengan klasifikasi lebih tinggi; dan **no write down**—subjek tidak menulis informasi berklasifikasi lebih tinggi ke tingkat lebih rendah. Model ini mencegah kebocoran informasi dari tingkat rahasia menuju tingkat yang lebih rendah.

**Biba** menekankan integritas. Aturan ringkasnya: **no read down** dan **no write up** dalam interpretasi klasik, agar data berintegritas rendah tidak mencemari proses atau objek berintegritas tinggi. Jangan tertukar: Bell–LaPadula berfokus pada confidentiality, sedangkan Biba berfokus pada integrity.

Prinsip pendukung kendali akses:
- **Least privilege:** setiap akun menerima izin minimum yang diperlukan.
- **Need-to-know:** akses data diberikan hanya ketika diperlukan untuk tugas.
- **Separation of duties:** tugas kritis dibagi ke beberapa pihak untuk mengurangi penyalahgunaan.
- **MFA (Multi-Factor Authentication):** menggabungkan faktor yang berbeda, misalnya sesuatu yang diketahui, dimiliki, atau merupakan karakteristik biologis pengguna.
- **Zero Trust:** jangan otomatis mempercayai akses hanya karena berasal dari jaringan internal; verifikasi identitas, perangkat, konteks, dan hak akses secara berkelanjutan.

## 1.4. Kriptografi simetris dan asimetris

Kriptografi mengubah informasi agar hanya pihak yang memiliki kemampuan atau kunci yang tepat dapat membacanya. Istilah dasar:
- **Plaintext:** pesan sebelum enkripsi.
- **Ciphertext:** hasil enkripsi.
- **Encryption:** mengubah plaintext menjadi ciphertext.
- **Decryption:** mengembalikan ciphertext menjadi plaintext menggunakan kunci yang sesuai.

### Kunci simetris

Enkripsi dan dekripsi memakai kunci rahasia yang sama:

\[
C=E_K(P), \qquad P=D_K(C)
\]

AES adalah algoritma kunci simetris modern yang umum digunakan, dengan panjang kunci 128, 192, atau 256 bit. Algoritma ini efisien untuk mengenkripsi data dalam jumlah besar. Tantangan utama simetris adalah distribusi dan penyimpanan kunci: kedua pihak harus memperoleh kunci yang sama tanpa membiarkan penyerang mendapatkannya.

Mode operasi memengaruhi cara cipher blok digunakan. CBC memerlukan IV yang memenuhi persyaratan keamanan dan biasanya dipadukan dengan mekanisme autentikasi yang benar. GCM merupakan mode authenticated encryption yang memberikan kerahasiaan sekaligus autentikasi/integritas ciphertext dan data terkait, asalkan nonce tidak digunakan ulang secara melanggar aturan.

### Kunci asimetris

Kriptografi asimetris memakai pasangan **public key** dan **private key**. Keduanya berkaitan secara matematis tetapi private key harus dijaga rahasia.

- Untuk menjaga kerahasiaan kepada penerima: pengirim mengenkripsi menggunakan public key penerima; penerima mendekripsi menggunakan private key miliknya.
- Untuk membuat tanda tangan digital: pemilik menandatangani pesan atau hash-nya menggunakan private key; penerima memverifikasi tanda tangan memakai public key penanda tangan.

Tanda tangan digital bukan sekadar “mengenkripsi pesan dengan private key”. Mekanisme tanda tangan memiliki algoritma dan aturan khusus, umumnya bekerja atas hash pesan. Tanda tangan membantu menguji integritas, autentisitas asal, dan mendukung non-repudiation, tetapi tidak dengan sendirinya membuat isi pesan rahasia.

| Teknologi | Kegunaan umum | Hal yang harus diingat |
|---|---|---|
| AES | Enkripsi data | Simetris dan cepat |
| RSA | Enkripsi/pembungkus kunci atau tanda tangan, bergantung skema | Asimetris; keamanan terkait masalah matematika tertentu dan parameter yang tepat |
| Diffie–Hellman | Menyepakati rahasia bersama melalui kanal yang dapat disadap | Pertukaran kunci saja tidak mengautentikasi pihak lawan; perlu autentikasi agar tahan MitM |
| ECC | Kriptografi berbasis kurva eliptik | Dapat mencapai tingkat keamanan tertentu dengan kunci relatif ringkas |

Dalam sistem modern, kriptografi sering digunakan secara hibrida: kriptografi asimetris atau protokol pertukaran kunci membantu membuat rahasia sesi, lalu algoritma simetris yang efisien mengenkripsi lalu lintas data.

## 1.5. Hash, MAC, tanda tangan digital, dan PKI

Fungsi hash memetakan masukan dengan panjang beragam menjadi digest dengan panjang tetap. Hash kriptografik yang baik bersifat deterministik, tahan pre-image, tahan second pre-image, dan tahan collision. **Avalanche effect** berarti perubahan kecil pada input seharusnya mengubah output secara signifikan.

SHA-256 dan SHA-3 merupakan contoh keluarga hash modern. MD5 dan SHA-1 tidak layak dipilih untuk tujuan yang membutuhkan collision resistance. Hash biasa tidak membuktikan siapa yang membuat data, sebab siapa pun dapat menghitung hash. Untuk autentikasi pesan diperlukan mekanisme tambahan.

- **Hash:** mendeteksi perubahan bila digest pembanding dapat dipercaya.
- **MAC/HMAC:** menggunakan kunci rahasia bersama untuk memeriksa integritas sekaligus autentisitas pesan terhadap pihak yang memiliki kunci.
- **Tanda tangan digital:** menggunakan private key penanda tangan dan diverifikasi dengan public key; berguna untuk integritas dan autentikasi asal.
- **Enkripsi:** terutama menjaga kerahasiaan, bukan otomatis menjamin integritas jika algoritma/mode yang dipakai tidak memberikan autentikasi.

### Public Key Infrastructure (PKI)

PKI membantu menghubungkan identitas dengan public key melalui sertifikat digital. **Certificate Authority (CA)** menandatangani sertifikat yang mengikat identitas/entitas tertentu dengan kunci publik. Sertifikat X.509 dapat memuat identitas subjek, public key, issuer, masa berlaku, nomor seri, penggunaan kunci, dan tanda tangan CA.

Pemeriksaan sertifikat mencakup rantai ke CA tepercaya, masa berlaku, nama domain atau identitas yang sesuai, penggunaan sertifikat, serta status pencabutan jika relevan. TLS pada HTTPS menggunakan sertifikat dan protokol kriptografi untuk membantu membangun kanal yang aman. Ikon gembok tidak berarti situs tersebut otomatis jujur; sertifikat terutama membantu memastikan identitas koneksi dan perlindungan kanal sesuai proses validasinya.

## 1.6. Pertahanan jaringan, keamanan fisik, dan respons insiden

- **Firewall:** mengizinkan atau memblokir lalu lintas berdasarkan kebijakan. Firewall tradisional berfokus pada aturan jaringan/transport; sistem lebih canggih dapat memeriksa aplikasi.
- **IDS (Intrusion Detection System):** mendeteksi aktivitas mencurigakan dan memberi peringatan.
- **IPS (Intrusion Prevention System):** berada pada jalur atau memiliki kemampuan untuk otomatis memblokir aktivitas yang terdeteksi.
- **VPN:** membangun kanal komunikasi terlindungi melalui jaringan lain; keamanan akhirnya bergantung pada konfigurasi dan endpoint.
- **Kerberos:** protokol autentikasi berbasis tiket yang menggunakan layanan tepercaya untuk membantu autentikasi di jaringan.
- **Backup dan pemulihan:** cadangan harus teruji, terpisah dari sistem produksi, dan dilindungi dari penghapusan oleh penyerang.
- **Keamanan fisik:** pengendalian akses ruangan, pengelolaan perangkat, daya, pendingin, kebakaran, bencana, dan pembuangan media penyimpanan.

Siklus respons insiden umumnya mencakup persiapan, deteksi dan analisis, containment/pembatasan dampak, eradication/pembersihan, recovery/pemulihan, serta lessons learned. Jangan menghapus bukti secara sembarangan; log, waktu kejadian, dan chain of custody dapat penting untuk investigasi.

### Target penguasaan KJI
Anda seharusnya dapat membedakan ancaman–kerentanan–risiko, menerapkan CIA pada skenario, menghitung SLE/ARO/ALE, membandingkan DAC/MAC/RBAC/ABAC, menjelaskan Bell–LaPadula versus Biba, memilih penggunaan kriptografi yang tepat, dan menjelaskan peran hash, HMAC, tanda tangan digital, sertifikat, firewall, IDS, dan IPS.

---

# 2. KEWIRAUSAHAAN / TECHNOPRENEURSHIP

Sumber: [Rangkuman Materi Kewirausahaan](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/Kewirausahaan/RANGKUMAN_MATERI.md)

## 2.1. Pola pikir kewirausahaan dan inovasi

Kewirausahaan merupakan proses mengenali peluang, menghimpun sumber daya, menciptakan nilai, dan mengelola risiko untuk menghasilkan usaha yang berkelanjutan. Dalam konteks informatika, technopreneurship menggunakan perangkat lunak, data, otomasi, atau teknologi digital sebagai komponen utama nilai bisnis.

Joseph Schumpeter menghubungkan kewirausahaan dengan **creative destruction**: inovasi produk, proses, pasar, sumber pasokan, atau bentuk organisasi baru dapat mengubah industri yang telah ada. Wirausahawan bukan semata-mata orang yang memiliki ide; ia perlu membuktikan bahwa ada kebutuhan pelanggan dan bahwa solusi dapat dibuat serta dipertahankan secara ekonomis.

Karakteristik wirausaha yang relevan:
- Mengambil **risiko terukur**, bukan bertindak tanpa perhitungan.
- Mencari peluang dari masalah nyata pengguna.
- Memiliki daya tahan, belajar dari kegagalan, dan mengubah strategi berdasarkan bukti.
- Mengembangkan kemampuan bernegosiasi, berkomunikasi, dan membangun tim.
- Menjaga etika, kualitas layanan, kepercayaan, dan kepatuhan hukum.

### Design Thinking dan Lean Startup

Design Thinking membantu memahami masalah dari sudut pandang pengguna. Alur yang sering digunakan adalah **Empathize → Define → Ideate → Prototype → Test**. Tahapan ini tidak selalu linear: hasil uji prototipe dapat mengharuskan tim kembali mendefinisikan masalah.

Lean Startup menekankan eksperimen cepat dengan siklus **Build → Measure → Learn**:
1. Buat Minimum Viable Product (MVP) yang cukup untuk menguji asumsi penting.
2. Ukur respons menggunakan metrik yang relevan.
3. Pelajari apakah hipotesis didukung bukti.
4. Putuskan apakah melanjutkan arah yang sama (*persevere*) atau mengubah arah secara mendasar (*pivot*).

MVP bukan produk ceroboh dengan semua fitur dihilangkan. MVP adalah eksperimen minimum yang memungkinkan asumsi bisnis utama diuji dengan biaya dan waktu yang masuk akal.

Teknik ideasi seperti SCAMPER dapat memicu alternatif: Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, dan Reverse/Rearrange. Namun, banyaknya ide bukan ukuran keberhasilan; ide harus divalidasi melalui bukti masalah, kesediaan pengguna mencoba atau membayar, dan kemampuan penyampaian solusi.

## 2.2. Bentuk badan usaha dan aspek legal

| Bentuk | Ciri | Kelebihan | Hal yang perlu dipertimbangkan |
|---|---|---|---|
| Usaha perseorangan | Dimiliki satu individu | Pendirian relatif sederhana dan kendali langsung | Tanggung jawab pemilik umumnya tidak terpisah dari usaha |
| Firma | Persekutuan beberapa orang yang menjalankan usaha bersama | Menggabungkan keahlian dan modal | Sekutu dapat menanggung tanggung jawab pribadi sesuai ketentuan hukum |
| CV | Memiliki sekutu aktif dan sekutu komanditer/pasif | Memungkinkan pemisahan peran pengelola dan penyetor modal | Sekutu aktif menanggung risiko tanggung jawab yang lebih luas |
| PT | Badan hukum terpisah, modal berbentuk saham | Pemisahan entitas dan tanggung jawab pemegang saham sesuai hukum | Formalitas, pelaporan, dan tata kelola lebih kompleks |
| Koperasi | Berorientasi pada manfaat anggota | Partisipasi dan prinsip demokratis anggota | Harus mematuhi prinsip dan tata kelola koperasi |

Pemilihan bentuk usaha dipengaruhi struktur kepemilikan, risiko, kebutuhan investasi, jumlah pendiri, model pendapatan, rencana ekspansi, dan ketentuan hukum yang berlaku. Rangkuman ini menjelaskan konsep umum; pengambilan keputusan legal harus merujuk aturan Indonesia yang berlaku pada saat pendirian.

Etika bisnis mencakup transparansi informasi, perlakuan adil terhadap konsumen dan karyawan, perlindungan data, tidak membuat klaim palsu, serta menangani konflik kepentingan. Hak kekayaan intelektual penting bagi bisnis teknologi:
- **Hak cipta** melindungi ekspresi karya seperti kode sumber dan dokumentasi, bukan ide abstrak semata.
- **Merek** membedakan identitas barang atau jasa.
- **Paten** melindungi invensi yang memenuhi persyaratan hukum; kode program murni dan invensi yang menerapkan komputer memiliki ketentuan yang spesifik.
- **Rahasia dagang** melindungi informasi bisnis yang bernilai karena dirahasiakan dan dijaga secara wajar.

Periksa lisensi kode, font, gambar, dataset, dan pustaka pihak ketiga sebelum dipakai dalam produk komersial. Menggunakan proyek open-source tidak berarti tidak ada kewajiban; lisensi permissive seperti MIT/Apache dan copyleft seperti GPL memiliki persyaratan yang berbeda.

## 2.3. Business Model Canvas (BMC)

Business Model Canvas merangkum cara perusahaan menciptakan, menyampaikan, dan menangkap nilai melalui sembilan blok yang saling berkaitan.

| Blok BMC | Pertanyaan panduan | Contoh produk digital |
|---|---|---|
| Customer Segments | Siapa pengguna/pelanggan utama? | UMKM, mahasiswa, perusahaan |
| Value Propositions | Masalah apa yang diselesaikan dan mengapa solusi ini bernilai? | Pencatatan stok lebih mudah |
| Channels | Melalui saluran apa pengguna menemukan dan memakai produk? | Website, aplikasi, marketplace |
| Customer Relationships | Bagaimana pelanggan diperoleh dan dipertahankan? | Self-service, komunitas, dukungan |
| Revenue Streams | Dari mana pendapatan berasal? | Langganan, komisi, lisensi |
| Key Resources | Sumber daya apa yang wajib tersedia? | Kode, data, tim, cloud |
| Key Activities | Aktivitas apa yang harus dilakukan dengan baik? | Pengembangan, dukungan, pemasaran |
| Key Partnerships | Siapa mitra kunci? | Payment gateway, cloud, logistik |
| Cost Structure | Biaya apa yang dominan? | Gaji, server, pemasaran, transaksi |

BMC berguna untuk melihat hubungan antarkomponen. Misalnya, segmen pelanggan B2B mungkin memerlukan kanal penjualan langsung, onboarding, dukungan teknis, dan siklus penjualan yang lebih panjang dibandingkan aplikasi konsumen yang mengandalkan unduhan mandiri. Perubahan value proposition dapat memengaruhi sumber pendapatan, aktivitas, mitra, serta biaya.

## 2.4. Strategi pemasaran: STP, 4P, dan 7P

**Segmentation** membagi pasar ke kelompok yang relatif serupa berdasarkan aspek geografis, demografis, psikografis, atau perilaku. **Targeting** memilih segmen yang akan dilayani berdasarkan ukuran, pertumbuhan, aksesibilitas, persaingan, dan kecocokan dengan sumber daya tim. **Positioning** membangun persepsi yang jelas dibanding pesaing. Ketiganya disebut STP.

Bauran pemasaran **4P**:
- **Product:** manfaat, fitur, kualitas, desain, layanan, dan pengalaman.
- **Price:** harga, paket, diskon, strategi penetration atau skimming.
- **Place:** bagaimana produk disediakan dan didistribusikan.
- **Promotion:** komunikasi nilai melalui iklan, konten, hubungan publik, atau promosi penjualan.

Untuk layanan jasa, model **7P** menambahkan **People** (orang yang memberikan layanan), **Process** (alur pelayanan), dan **Physical Evidence** (bukti yang membangun kepercayaan seperti antarmuka, ulasan, sertifikasi, dan laporan).

Pemasaran digital dapat menggunakan awareness → consideration → conversion → retention. Metrik harus sesuai tujuan:
- **Conversion rate:** proporsi pengunjung atau calon pelanggan yang melakukan tindakan sasaran.
- **CAC (Customer Acquisition Cost):** biaya untuk memperoleh pelanggan baru.
- **LTV (Lifetime Value):** estimasi kontribusi nilai pelanggan selama hubungan bisnis.
- **Churn rate:** proporsi pelanggan yang berhenti dalam periode tertentu.
- **Retention rate:** proporsi pelanggan yang tetap aktif.

CAC dan LTV harus dihitung dengan basis yang konsisten. Pendapatan seumur hidup bukan selalu laba seumur hidup; untuk keputusan yang lebih sehat, gunakan margin kontribusi dan perhitungkan biaya layanan, pembayaran, dukungan, serta churn.

## 2.5. Keuangan usaha, BEP, ROI, dan pendanaan

Biaya dapat dibedakan menjadi:
- **Fixed Cost (FC):** biaya yang relatif tetap terhadap volume pada rentang dan periode tertentu, misalnya sewa atau gaji tetap.
- **Variable Cost (VC):** biaya yang berubah mengikuti unit/transaksi, misalnya biaya per transaksi payment gateway.
- **Harga per unit (P)** dan **biaya variabel per unit (VCu)** digunakan untuk menghitung kontribusi tiap penjualan.

\[
BEP_{unit}=\frac{FC}{P-VC_u}
\]

Penyebut adalah **contribution margin per unit**, yaitu bagian harga jual setelah biaya variabel. Rumus ini mengasumsikan harga, biaya variabel per unit, dan biaya tetap cukup stabil di rentang analisis.

Contoh: biaya tetap Rp12.000.000 per bulan, harga jual Rp100.000 per unit, dan biaya variabel Rp40.000 per unit.

\[
BEP=\frac{12.000.000}{100.000-40.000}=200\ unit
\]

Artinya, usaha perlu menjual sekitar 200 unit per bulan untuk mencapai titik impas operasional dalam asumsi tersebut. BEP rupiah dapat dihitung dari unit impas dikali harga per unit, atau dengan rasio margin kontribusi jika asumsi penjualan beragam sesuai model yang digunakan.

\[
ROI=\frac{Manfaat\ Bersih}{Biaya\ Investasi}\times100\%
\]

ROI memberi rasio manfaat bersih terhadap biaya investasi untuk periode analisis yang ditetapkan. Jangan mengabaikan periode waktu, risiko, arus kas, dan biaya peluang ketika membandingkan investasi.

**Laporan keuangan dasar:**
- **Laporan laba rugi:** pendapatan dan beban selama periode tertentu, menghasilkan laba atau rugi.
- **Laporan arus kas:** penerimaan dan pengeluaran kas; usaha dapat mencatat laba tetapi tetap kehabisan kas.
- **Neraca/laporan posisi keuangan:** aset, liabilitas, dan ekuitas pada suatu tanggal.

Pendanaan usaha dapat berasal dari modal sendiri (**bootstrapping**), pendapatan pelanggan, pinjaman, angel investor, atau venture capital. Investor umumnya memperhatikan masalah dan ukuran pasar, produk, traction, tim, keunggulan kompetitif, model pendapatan, unit economics, risiko, serta penggunaan dana. Pitch deck harus menyampaikan cerita bisnis dengan bukti, bukan sekadar daftar fitur.

### Target penguasaan Kewirausahaan
Anda seharusnya mampu mengubah masalah pengguna menjadi hipotesis produk, menjelaskan tahapan Design Thinking dan Lean Startup, membandingkan bentuk usaha, mengisi sembilan blok BMC, memilih STP dan bauran pemasaran yang sesuai, serta menghitung BEP dan menafsirkan CAC/LTV, ROI, dan arus kas.

---

# 3. KOMPUTASI TERSEBAR DAN PARALEL

Sumber: [Rangkuman Materi Komputasi Tersebar dan Paralel](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/Komputasi_Tersebar_dan_Paralel/RANGKUMAN_MATERI.md)

## 3.1. Sistem terdistribusi versus komputasi paralel

**Sistem terdistribusi** terdiri atas beberapa komputer independen yang berkomunikasi melalui jaringan, tetapi dirancang untuk tampak sebagai satu layanan yang koheren. Fokus utama: koordinasi antarmesin, komunikasi, konsistensi, kegagalan parsial, dan transparansi.

**Komputasi paralel** membagi pekerjaan ke beberapa unit pemrosesan yang bekerja bersamaan demi mempercepat satu komputasi. Paralelisme dapat berjalan di multi-core satu mesin, GPU, atau cluster. Sistem terdistribusi dapat melakukan komputasi paralel, tetapi kedua istilah tidak identik.

Karakteristik penting sistem terdistribusi:
1. Banyak proses berjalan konkuren pada mesin yang berbeda.
2. Tidak ada jam fisik global sempurna yang diketahui semua mesin.
3. Komponen dapat gagal secara independen; satu node gagal belum tentu membuat semua node gagal.
4. Komunikasi jaringan memiliki latensi, kemungkinan kehilangan paket, dan partisi jaringan.

### Transparansi distribusi

Transparansi menyembunyikan detail distribusi dari pengguna atau aplikasi, misalnya:
- **Access:** cara mengakses sumber daya seragam.
- **Location:** pengguna tidak perlu mengetahui lokasi fisik sumber daya.
- **Migration/Relocation:** sumber daya bisa berpindah, termasuk saat sedang digunakan.
- **Replication:** terdapat salinan data/layanan tanpa harus diketahui pengguna.
- **Concurrency:** akses bersamaan dikelola dengan benar.
- **Failure:** sistem mendeteksi, membatasi, atau memulihkan kegagalan sejauh mungkin.
- **Performance:** sistem dapat menyesuaikan konfigurasi untuk mempertahankan kinerja.
- **Scaling:** sistem dapat berkembang tanpa perubahan besar terhadap cara penggunaan.

Arsitektur umum meliputi client-server, N-tier, peer-to-peer, serta service/microservice. Middleware menyederhanakan komunikasi dan menyamarkan perbedaan platform. RPC (Remote Procedure Call) membuat operasi jarak jauh menyerupai pemanggilan prosedur; RMI merupakan gagasan serupa untuk objek. Meski tampak seperti pemanggilan lokal, komunikasi jarak jauh dapat gagal, lambat, atau menghasilkan timeout. Karena itu, desain perlu menangani retry, idempotensi, timeouts, dan duplikasi pesan.

## 3.2. Sinkronisasi waktu fisik

Jam setiap mesin memiliki perbedaan (*clock skew*) dan perubahan laju (*clock drift*) akibat ketidaksempurnaan osilator serta kondisi perangkat. Timestamp fisik dapat membantu penjadwalan dan pencatatan, tetapi tidak selalu cukup untuk menentukan urutan kausal kejadian.

- **Cristian:** klien meminta waktu dari time server dan memperkirakan delay bolak-balik. Dalam asumsi delay simetris, estimasi sederhananya:

\[
T_{klien}\approx T_{server}+\frac{T_1-T_0}{2}
\]

  dengan \(T_0\) waktu pengiriman request dan \(T_1\) waktu diterimanya balasan. Rumus ini mengabaikan sejumlah komponen dan mengandalkan pendekatan delay simetris.
- **Berkeley:** koordinator mengumpulkan waktu dari node, menghitung perkiraan waktu bersama, dan mengirimkan offset agar node menyesuaikan jam.
- **NTP (Network Time Protocol):** menggunakan sistem server waktu bertingkat (stratum) serta pertukaran timestamp untuk menyelaraskan jam melalui jaringan.

Sinkronisasi tidak selalu berarti semua jam identik sempurna. Tujuannya adalah mengendalikan ketidakpastian waktu sesuai kebutuhan aplikasi.

## 3.3. Jam logika Lamport dan Vector Clock

Lamport mengutamakan hubungan kausal dibanding waktu dinding. Relasi **happens-before**, ditulis \(a \rightarrow b\), berlaku ketika:
1. a dan b berada dalam proses yang sama dan a terjadi terlebih dahulu;
2. a adalah pengiriman pesan dan b adalah penerimaan pesan itu;
3. jika \(a\rightarrow b\) dan \(b\rightarrow c\), maka \(a\rightarrow c\) (transitivitas).

Setiap proses menyimpan penghitung \(L_i\). Proses menambah jam sebelum peristiwa lokal. Pesan dikirim dengan timestamp. Saat menerima timestamp \(t\), penerima memperbarui:

\[
L_j=\max(L_j,t)+1
\]

Jam Lamport menjamin bahwa jika \(a\rightarrow b\), timestamp a lebih kecil dari b, tetapi kebalikannya tidak selalu benar. Dua kejadian dengan timestamp berurutan belum tentu saling memengaruhi.

**Vector clock** menyimpan vektor penghitung per proses. Vector clock lebih mampu membedakan kejadian kausal dan konkuren:
- Jika semua komponen vector A kurang dari atau sama dengan B dan setidaknya satu lebih kecil, A mendahului B.
- Jika tidak ada vektor yang komponen-komponennya semuanya lebih kecil atau sama, kedua kejadian dapat bersifat konkuren.

## 3.4. Mutual exclusion dan pemilihan pemimpin

**Mutual exclusion terdistribusi** memastikan hanya satu proses memasuki critical section untuk sumber daya tertentu pada satu waktu.

- **Token Ring:** sebuah token beredar di lingkaran logis; proses hanya boleh masuk critical section saat memegang token. Perlu strategi untuk menangani token hilang atau node gagal.
- **Ricart–Agrawala:** proses meminta izin dari proses lain dengan timestamp; proses lain menunda jawaban apabila ia memiliki prioritas lebih tinggi untuk masuk critical section. Skema dasar memerlukan \(2(N-1)\) pesan untuk permintaan dan balasan kepada \(N-1\) node.
- **Maekawa:** menggunakan voting/quorum untuk mengurangi jumlah pesan, tetapi desain perlu menangani deadlock atau starvation sesuai protokolnya.

Algoritma **Bully** memilih koordinator berdasarkan ID. Ketika proses mendeteksi leader tidak merespons, ia menghubungi proses ber-ID lebih tinggi. Jika tidak ada respons yang lebih tinggi, ia dapat mengumumkan diri sebagai koordinator; apabila ada yang merespons, proses yang lebih tinggi dapat melanjutkan pemilihan. Asumsi ID unik dan kemampuan mendeteksi kegagalan harus jelas.

## 3.5. Konsistensi, CAP, dan konsensus

Teorema CAP relevan **ketika terjadi network partition**:
- **Consistency (C):** secara umum, operasi baca melihat keadaan yang konsisten sesuai model consistency yang dibahas, bukan data lama yang melanggar jaminan sistem.
- **Availability (A):** permintaan yang diterima oleh node yang tidak gagal mendapat respons.
- **Partition Tolerance (P):** sistem tetap beroperasi meskipun komunikasi antarbagian jaringan terputus.

Saat partition terjadi, sistem tidak dapat sekaligus mempertahankan strong consistency dan availability dalam pengertian CAP klasik. Sistem harus menentukan apakah operasi tertentu ditolak/ditunda agar konsistensi terjaga (pendekatan CP), atau tetap melayani request dengan kemungkinan data sementara berbeda (pendekatan AP). CAP bukan pernyataan bahwa sistem selalu hanya bisa memilih dua sifat tanpa konteks; perdebatan ini terutama tentang perilaku ketika partition terjadi.

**Two-Phase Commit (2PC)** mengkoordinasikan transaksi terdistribusi:
1. **Prepare/Vote:** coordinator meminta peserta mempersiapkan commit dan memberi keputusan siap/tidak.
2. **Commit/Abort:** jika seluruh peserta siap, coordinator mengirim commit; jika tidak, mengirim abort.
Keterbatasan penting: coordinator/komunikasi yang gagal pada kondisi tertentu dapat membuat peserta menunggu keputusan, sehingga 2PC adalah protokol atomic commit, bukan otomatis solusi konsensus fault-tolerant yang selalu tersedia.

**Paxos** dan **Raft** adalah protokol konsensus yang dirancang agar node sepakat pada urutan nilai/log meskipun sebagian node gagal, dengan asumsi dan batas tertentu (misalnya mayoritas/quorum berkomunikasi). Raft memisahkan ide leader election, log replication, dan safety rules agar lebih mudah dipahami.

## 3.6. Arsitektur paralel, Amdahl, Gustafson, dan MapReduce

Taksonomi Flynn mengklasifikasikan arsitektur berdasarkan aliran instruksi dan data:
- **SISD:** satu aliran instruksi dan satu aliran data.
- **SIMD:** satu instruksi mengolah banyak elemen data, misalnya operasi vektor dan sebagian pekerjaan GPU.
- **MISD:** beberapa aliran instruksi terhadap aliran data yang sama; jarang digunakan dalam bentuk umum.
- **MIMD:** banyak prosesor menjalankan instruksi berbeda pada data berbeda, misalnya multi-core dan cluster.

Pada **shared memory**, thread berbagi ruang memori, misalnya dengan OpenMP. Pendekatan ini memudahkan berbagi data tetapi rentan race condition, deadlock, dan masalah sinkronisasi. Pada **distributed memory**, proses memiliki memori terpisah dan berkomunikasi lewat pesan, misalnya MPI; pendekatan ini lebih eksplisit dan dapat berkembang ke banyak node, tetapi membutuhkan komunikasi serta pembagian data yang tepat.

### Hukum Amdahl

Jika proporsi pekerjaan yang bisa diparalelkan adalah \(P\) dan sisanya serial, speedup teoretis dengan \(N\) prosesor adalah:

\[
S(N)=\frac{1}{(1-P)+\frac{P}{N}}
\]

Contoh: 80% program bisa diparalelkan (\(P=0{,}8\)) dan digunakan 4 prosesor.

\[
S(4)=\frac{1}{0{,}2+\frac{0{,}8}{4}}
=\frac{1}{0{,}4}=2{,}5
\]

Walaupun empat prosesor tersedia, percepatan idealnya hanya 2,5 kali karena masih ada bagian serial. Biaya komunikasi dan sinkronisasi dapat membuat hasil aktual lebih rendah.

### Hukum Gustafson

Hukum Gustafson mempertimbangkan bahwa ukuran masalah dapat diperbesar ketika jumlah prosesor bertambah:

\[
S_G(N)=N-\alpha(N-1)
\]

dengan \(\alpha\) sebagai proporsi bagian serial pada skala kerja yang dipertimbangkan. Amdahl berguna ketika ukuran pekerjaan tetap; Gustafson berguna saat kapasitas paralel memungkinkan masalah yang lebih besar diselesaikan dalam waktu sebanding.

### MapReduce

MapReduce membagi pemrosesan data:
1. **Map:** memproses record masukan dan menghasilkan pasangan key-value perantara.
2. **Shuffle/Sort:** mengelompokkan keluaran berdasarkan key.
3. **Reduce:** menggabungkan nilai-nilai untuk masing-masing key.

Contoh menghitung jumlah kata: Map menghasilkan pasangan (kata, 1); shuffle mengelompokkan kata yang sama; Reduce menjumlahkan semua angka untuk masing-masing kata. Kualitas rancangan bergantung pada pembagian data, distribusi key, biaya shuffle, dan penanganan kegagalan.

### Target penguasaan KTP
Anda perlu membedakan sistem terdistribusi dan paralel, menjelaskan transparansi dan kegagalan parsial, menghitung timestamp Lamport, memahami Vector Clock, membandingkan mutual exclusion, menjelaskan CAP/2PC/Raft secara tepat, mengklasifikasikan Flynn, menghitung speedup Amdahl/Gustafson, serta menelusuri MapReduce.

---

# 4. PEMBELAJARAN MESIN

Sumber: [Rangkuman Materi Pembelajaran Mesin](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/Pembelajaran_Mesin/RANGKUMAN_MATERI.md)

## 4.1. Konsep dasar dan tipe pembelajaran

Machine Learning (ML) membangun model yang mempelajari pola dari data untuk melakukan prediksi atau pengambilan keputusan. Dalam rumusan klasik, program dikatakan belajar dari pengalaman \(E\) untuk tugas \(T\) dengan ukuran kinerja \(P\) apabila kinerjanya pada T yang diukur oleh P meningkat seiring pengalaman E.

- **Supervised learning:** data memiliki label/target. Digunakan untuk klasifikasi (kelas diskrit) dan regresi (nilai numerik).
- **Unsupervised learning:** data tidak memiliki label target yang diketahui; model mencari struktur seperti klaster atau representasi.
- **Reinforcement learning:** agen belajar melalui interaksi dengan lingkungan dan sinyal reward.

Tahapan eksperimen ML umumnya mencakup definisi target, pengumpulan data, eksplorasi, pembersihan dan prapemrosesan, pembagian data, pelatihan, tuning, evaluasi, lalu deployment dan monitoring. Prapemrosesan dan pelatihan harus dipelajari dari training set saja bila parameter itu dapat membocorkan informasi; setelah itu transformasi yang sama diterapkan pada validation/test set.

### Train, validation, dan test

- **Training set:** digunakan untuk menyesuaikan parameter model.
- **Validation set:** digunakan untuk memilih hiperparameter, ambang keputusan, atau konfigurasi.
- **Test set:** digunakan untuk estimasi akhir setelah pilihan model diselesaikan.

**Data leakage** terjadi ketika informasi yang seharusnya tidak tersedia pada saat prediksi memengaruhi proses pelatihan atau pemilihan model. Contoh: melakukan normalisasi seluruh dataset sebelum pembagian, menggunakan informasi label test untuk memilih fitur, atau membiarkan data yang hampir duplikat tersebar ke train dan test. Leakage membuat hasil tampak terlalu bagus dan tidak mencerminkan performa saat digunakan.

## 4.2. K-Nearest Neighbors (k-NN)

k-NN adalah algoritma berbasis instance dan sering disebut lazy learner karena tidak membangun model parametrik yang kompleks pada fase training. Saat data baru masuk, algoritma menghitung jarak ke titik training, mengambil \(k\) tetangga terdekat, lalu melakukan voting kelas atau agregasi nilai.

Jarak Euclidean:

\[
d(x,y)=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
\]

Jarak Manhattan:

\[
d(x,y)=\sum_{i=1}^{n}|x_i-y_i|
\]

Jarak Minkowski menggeneralisasi beberapa metrik jarak. Pemilihan metrik perlu sesuai tipe fitur dan interpretasi data.

Normalisasi penting karena fitur dengan skala lebih besar dapat mendominasi jarak. **Min-Max scaling** memetakan nilai ke rentang tertentu; **standardization** menggunakan rata-rata dan simpangan baku:

\[
z=\frac{x-\mu}{\sigma}
\]

Nilai \(k\) kecil dapat menghasilkan batas keputusan rumit dan sensitif terhadap noise (variance tinggi), sedangkan \(k\) besar menghasilkan keputusan lebih halus namun dapat mengabaikan pola lokal (bias tinggi). Nilai \(k\) dipilih berdasarkan validasi, bukan karena ada satu angka yang selalu paling baik. k-NN mudah dipahami tetapi prediksi bisa mahal pada dataset besar, peka terhadap skala dan dimensi, dan membutuhkan penyimpanan data pelatihan.

## 4.3. Decision Tree: Entropy, Information Gain, dan Gain Ratio

Decision tree membagi data secara bertahap menurut fitur yang dipilih agar kelas di tiap simpul semakin homogen. Pohon dapat digunakan untuk klasifikasi atau regresi.

Entropi Shannon mengukur ketidakmurnian kelas pada himpunan \(S\):

\[
H(S)=-\sum_{i=1}^{c}p_i\log_2(p_i)
\]

Jika semua contoh berasal dari satu kelas, entropi 0. Untuk dua kelas seimbang, entropi maksimum 1 bit.

Information Gain untuk atribut \(A\):

\[
IG(S,A)=H(S)-\sum_{v\in Values(A)}
\frac{|S_v|}{|S|}H(S_v)
\]

Atribut dengan gain yang tinggi menghasilkan pengurangan entropi lebih besar. ID3 cenderung menyukai atribut dengan banyak nilai unik. C4.5 menggunakan **Gain Ratio** untuk mengimbangi kecenderungan ini:

\[
GainRatio(S,A)=\frac{IG(S,A)}{SplitInfo(S,A)}
\]

\[
SplitInfo(S,A)=-\sum_v\frac{|S_v|}{|S|}\log_2\frac{|S_v|}{|S|}
\]

Decision tree mudah dijelaskan dan dapat menangkap hubungan nonlinier tanpa normalisasi fitur numerik yang wajib. Namun, pohon yang terlalu dalam dapat overfit; kendalikan dengan pruning, batas kedalaman, minimum sampel per daun, atau validasi.

## 4.4. Naive Bayes

Teorema Bayes:

\[
P(C\mid X)=\frac{P(X\mid C)P(C)}{P(X)}
\]

Untuk klasifikasi, model membandingkan probabilitas posterior kelas \(C\) setelah melihat fitur \(X\). Naive Bayes menggunakan asumsi bahwa fitur-fitur saling bebas secara kondisional ketika kelas diketahui:

\[
P(X\mid C)=\prod_{i=1}^{n}P(x_i\mid C)
\]

Asumsi itu sering tidak sepenuhnya benar, tetapi model masih bisa bekerja baik dan efisien. Jenis Naive Bayes disesuaikan dengan data: Gaussian untuk fitur numerik berasumsi distribusi normal per kelas; Multinomial lazim untuk frekuensi/count fitur seperti teks; Bernoulli cocok untuk fitur biner.

**Laplace smoothing** mencegah probabilitas nol untuk kategori yang tidak pernah diamati:

\[
P(x_i\mid C_k)=\frac{N_{ik}+\alpha}{N_k+\alpha V}
\]

\(N_{ik}\) adalah hitungan kategori pada kelas, \(N_k\) jumlah observasi/total hitungan yang sesuai dengan formulasi, \(V\) jumlah kategori, dan \(\alpha\) parameter smoothing (sering 1). Pastikan definisi hitungan menyesuaikan tipe Naive Bayes. Dalam implementasi Multinomial, penyebut biasanya menggunakan total seluruh feature counts pada kelas ditambah \(\alpha V\).

Kelebihan Naive Bayes ialah cepat, sederhana, dan dapat efektif untuk teks berdimensi tinggi. Kekurangannya adalah asumsi independensi dapat terlalu kuat, dan probabilitas yang dihasilkan belum tentu terkalibrasi dengan baik.

## 4.5. Support Vector Machine (SVM)

SVM mencari hyperplane pemisah dengan margin maksimum. **Support vectors** adalah titik pelatihan kritis yang menentukan posisi batas tersebut. Margin lebih besar dapat membantu generalisasi.

Untuk data yang tidak dapat dipisahkan linear, kernel trick memungkinkan model menghitung kemiripan di ruang fitur yang lebih kaya tanpa secara eksplisit membentuk semua dimensinya.
- **Linear kernel:** cocok jika batas keputusan dapat didekati dengan garis/bidang linear.
- **Polynomial kernel:** dapat menangkap hubungan polinomial.
- **RBF/Gaussian kernel:** fleksibel menangkap pola nonlinier.

Bentuk umum kernel RBF:

\[
K(x,x')=\exp(-\gamma\|x-x'\|^2)
\]

Parameter \(C\) mengatur kompromi antara margin dan penalti kesalahan; \(\gamma\) mengatur seberapa lokal pengaruh titik untuk RBF. Nilai hiperparameter perlu ditentukan menggunakan validasi atau cross-validation. SVM peka terhadap skala fitur dan memerlukan perhatian pada encoding fitur kategoris serta penanganan imbalance.

## 4.6. Clustering: K-Means, Hierarchical, dan DBSCAN

Clustering mengelompokkan data tanpa label berdasarkan kemiripan. Hasil klaster perlu ditafsirkan; algoritma tidak otomatis mengetahui arti bisnis setiap kelompok.

### K-Means
K-Means menentukan \(K\) centroid, mengalokasikan setiap data ke centroid terdekat, lalu memperbarui centroid sebagai rata-rata anggota klaster. Langkah assignment dan update diulang hingga konvergen atau batas iterasi tercapai. Tujuannya meminimalkan within-cluster sum of squares (inertia/WCSS):

\[
WCSS=\sum_{k=1}^{K}\sum_{x_i\in C_k}\|x_i-\mu_k\|^2
\]

- Perlu menentukan K di awal.
- Peka terhadap inisialisasi, skala fitur, dan outlier.
- Cenderung cocok untuk klaster yang relatif kompak.
- Elbow method mencari titik penurunan WCSS mulai melambat; ini petunjuk, bukan aturan matematis yang selalu memberi satu K pasti.
- K-Means++ membantu memilih centroid awal yang lebih tersebar.

### Hierarchical clustering
Agglomerative clustering dimulai dari klaster tunggal dan menggabungkan pasangan secara bertahap. Dendrogram menunjukkan urutan penggabungan dan dapat dipotong untuk memperoleh jumlah klaster tertentu.
- **Single linkage:** jarak minimum antartitik dua klaster; dapat menghasilkan chaining.
- **Complete linkage:** jarak maksimum antartitik; mendorong klaster yang lebih kompak.
- **Average linkage:** menggunakan rata-rata jarak antaranggota dua klaster.

### DBSCAN
DBSCAN membentuk klaster berdasarkan kepadatan:
- **Epsilon (\(\varepsilon\))**: radius lingkungan.
- **MinPts**: ambang jumlah titik minimum untuk menyebut daerah padat.
- **Core point** memiliki jumlah tetangga yang memenuhi syarat.
- **Border point** berada dekat core point tetapi kepadatan lokalnya sendiri tidak cukup.
- **Noise/outlier** tidak termasuk klaster berdasarkan parameter yang dipilih.

DBSCAN tidak harus menentukan K dan dapat menemukan bentuk klaster yang tidak bulat; kekurangannya sensitif terhadap skala serta sulit pada data dengan kepadatan sangat berbeda.

## 4.7. Evaluasi klasifikasi dan validasi

Confusion matrix menghubungkan label aktual dan prediksi:

| | Prediksi positif | Prediksi negatif |
|---|---:|---:|
| Aktual positif | TP | FN |
| Aktual negatif | FP | TN |

- **Accuracy:** proporsi seluruh prediksi yang benar.
- **Precision:** proporsi prediksi positif yang benar.
- **Recall:** proporsi aktual positif yang berhasil ditemukan.
- **F1-score:** rata-rata harmonik precision dan recall.

\[
Accuracy=\frac{TP+TN}{TP+TN+FP+FN}
\]

\[
Precision=\frac{TP}{TP+FP}, \qquad Recall=\frac{TP}{TP+FN}
\]

\[
F1=2\frac{Precision\times Recall}{Precision+Recall}
\]

Accuracy dapat tampak tinggi pada data tidak seimbang. Jika kelas positif jarang dan penting ditemukan, recall, precision, F1, PR curve, dan biaya false positive/false negative mungkin lebih informatif. ROC-AUC mengukur kemampuan pemeringkatan kelas di berbagai threshold; untuk kelas positif sangat jarang, PR-AUC sering memberikan perspektif tambahan.

**K-Fold Cross-Validation:** dataset dibagi ke \(K\) fold. Pada setiap putaran, satu fold menjadi validasi dan sisanya untuk pelatihan; skor digabungkan. Pada classification imbalance, stratified K-fold membantu mempertahankan proporsi kelas. Semua langkah pemrosesan yang belajar parameter harus berada di dalam pipeline fold untuk menghindari leakage.

### Bias–variance, overfitting, dan regularisasi

\[
Error \approx Bias^2 + Variance + Irreducible\ Error
\]

- **High bias/underfitting:** model terlalu sederhana; kinerja buruk di training dan test.
- **High variance/overfitting:** model terlalu menyesuaikan training; kinerja training bagus tetapi generalisasi buruk.
- **Regularisasi:** membatasi kompleksitas atau besarnya parameter untuk meningkatkan generalisasi.

L1 cenderung menghasilkan parameter sparse (sebagian bobot menjadi nol); L2 menghukum kuadrat besarnya parameter dan biasanya mengecilkan bobot. Kekuatan regularisasi harus disetel berdasarkan validasi.

### Target penguasaan Pembelajaran Mesin
Anda harus mampu memilih algoritma sesuai jenis masalah dan data, menghitung jarak k-NN, entropi dan information gain, menerapkan Teorema Bayes dan smoothing, menjelaskan margin serta kernel SVM, menelusuri K-Means/DBSCAN, menghitung metrik dari confusion matrix, dan merancang eksperimen yang bebas data leakage.

---

# 5. PENGEMBANGAN BERBASIS PLATFORM

Sumber: [Rangkuman Materi Pengembangan Berbasis Platform](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/Pengembangan_Berbasis_Platform/RANGKUMAN_MATERI.md)

## 5.1. Arsitektur web klien-server

Pada platform web, browser menjadi klien yang merender antarmuka dan mengirim request. Server memproses request, menjalankan logika bisnis, berinteraksi dengan database bila diperlukan, lalu mengirim response. Pemisahan ini memudahkan pengembangan, tetapi menuntut validasi, kontrol akses, dan penanganan kegagalan pada sisi yang tepat.

### Frontend

- **HTML5 semantik** memberi struktur bermakna melalui elemen seperti header, nav, main, article, section, dan footer. Struktur yang jelas membantu aksesibilitas, pemeliharaan, dan pemahaman dokumen.
- **CSS box model** terdiri dari content, padding, border, dan margin. Flexbox terutama mengatur tata letak satu dimensi, sedangkan Grid mengatur baris dan kolom dua dimensi.
- **JavaScript dan DOM** memungkinkan program membaca dan memodifikasi struktur serta perilaku halaman. Event listener menangani interaksi pengguna.
- Validasi sisi klien membantu kenyamanan pengguna, tetapi tidak dapat menjadi satu-satunya penjaga keamanan karena request bisa dibuat di luar browser.

### AJAX, Fetch, dan pemrograman asinkron

AJAX adalah pola komunikasi untuk memperbarui sebagian halaman tanpa reload penuh. Teknologi modern sering memakai Fetch API dan Promise; async/await menyediakan sintaks yang lebih mudah dibaca untuk operasi asinkron.

Contoh alur (bukan kode lengkap): event klik memanggil fungsi asinkron; fungsi menjalankan fetch ke API; response diperiksa; data JSON dibaca; UI diperbarui; error jaringan atau status response ditangani. Fetch tidak otomatis melempar exception untuk semua HTTP 4xx/5xx, sehingga kode perlu memeriksa response.ok atau status.

Request harus menangani loading, state kosong, kegagalan jaringan, autentikasi habis, dan hasil yang datang terlambat. Jangan mempercayai data dari API tanpa validasi bentuk data dan encoding output sesuai konteks tampilan.

## 5.2. Backend PHP, request HTTP, dan keamanan database

Pada HTTP, **GET** lazim digunakan untuk membaca sumber daya atau melakukan pencarian; parameter sering terlihat pada URL dan dapat tercatat di riwayat/log. **POST** mengirim data dalam body untuk membuat atau memproses sesuatu. HTTPS melindungi data saat transit, tetapi tidak berarti semua metode atau payload otomatis aman.

Backend memvalidasi input, memeriksa autentikasi/otorisasi, menjalankan aturan bisnis, melakukan akses data, dan mengembalikan response yang tepat. Keamanan harus diterapkan di server, bukan hanya di formulir browser.

### SQL Injection dan prepared statements

SQL injection terjadi ketika input tak tepercaya disisipkan ke string SQL sehingga mengubah struktur/niat query. Pencegahan utama adalah query berparameter atau **prepared statements** (misalnya melalui PDO), bukan sekadar menghapus tanda petik atau mengganti beberapa karakter.

Praktik tambahan:
- Gunakan akun database dengan hak minimum.
- Validasi tipe, format, rentang, serta aturan bisnis.
- Jangan membangun nama tabel/kolom dari input bebas; identifier dinamis membutuhkan allowlist karena parameter query biasanya hanya untuk nilai.
- Simpan kredensial di environment/configuration yang tidak ikut di-commit.
- Jangan memaparkan detail stack trace dan kredensial pada response produksi.

Pola **Model–View–Controller (MVC)** memisahkan Model (data dan aturan domain), View (presentasi), dan Controller (mengatur alur request). Pemisahan membantu keterujian dan pemeliharaan, tetapi tidak otomatis membuat aplikasi aman atau arsitekturnya baik; batas tanggung jawab harus tetap jelas.

## 5.3. Cookies dan sessions

HTTP secara default **stateless**: server tidak otomatis mengingat request sebelumnya. Login biasanya membutuhkan mekanisme status.

- **Cookie** disimpan browser dan dapat dikirim kembali dalam request. Isinya perlu dibatasi dan diatur aman.
- **Session** menyimpan data sesi di server; klien umumnya menyimpan session identifier, bukan seluruh data sesi.

Cookie yang membawa session ID idealnya menggunakan atribut **Secure** (hanya melalui HTTPS), **HttpOnly** (tidak dapat diakses JavaScript biasa), dan **SameSite** sesuai alur situs. Session ID perlu diganti setelah autentikasi atau perubahan hak akses penting untuk mengurangi session fixation. Token sesi dan cookie tetap harus dilindungi dari pencurian serta penggunaan ulang.

Perbedaan konsep: autentikasi membuktikan siapa pengguna, session mempertahankan konteks antar-request, sedangkan otorisasi memutuskan tindakan yang boleh dilakukan pengguna. Session tidak boleh dianggap sebagai pengganti pemeriksaan otorisasi pada setiap operasi penting.

## 5.4. RESTful API, JSON, JWT, dan HTTP status

REST adalah gaya arsitektur untuk sistem berbasis sumber daya. Resource diidentifikasi menggunakan URI, dan operasi biasanya memakai semantik metode HTTP yang konsisten.

| Metode | Tujuan umum | Catatan |
|---|---|---|
| GET | Membaca resource | Safe dan idempotent secara semantik |
| POST | Membuat resource atau memproses operasi | Tidak otomatis idempotent |
| PUT | Mengganti representasi resource secara menyeluruh | Idempotent jika dirancang sesuai semantik |
| PATCH | Memodifikasi sebagian resource | Idempotensi tergantung rancangan patch |
| DELETE | Menghapus resource | Semestinya idempotent dari sudut hasil keadaan, meskipun response dapat berbeda |

Status response yang sering ditemui:
- **200 OK:** request berhasil.
- **201 Created:** resource berhasil dibuat.
- **204 No Content:** berhasil tanpa body response.
- **400 Bad Request:** request tidak dapat diproses karena bentuk/input salah.
- **401 Unauthorized:** autentikasi tidak tersedia/tidak valid.
- **403 Forbidden:** identitas telah diketahui atau request dipahami, tetapi tindakan tidak diizinkan.
- **404 Not Found:** resource tidak ditemukan atau sengaja tidak diungkap keberadaannya.
- **409 Conflict:** konflik dengan keadaan resource.
- **422 Unprocessable Content:** request terbentuk benar tetapi gagal validasi semantik, jika digunakan oleh API.
- **500 Internal Server Error:** kegagalan server yang tidak semestinya dibebankan pada kesalahan pengguna.

JSON adalah format pertukaran data yang ringan dan umum digunakan. API perlu menetapkan kontrak data, validasi, versi, pagination, error structure, autentikasi, otorisasi, dan pembatasan request.

### JSON Web Token (JWT)

JWT sering berformat tiga bagian yang dipisahkan titik: **Header.Payload.Signature**. Payload berisi claims; base64url encoding bukan enkripsi. Siapa pun yang memegang token dapat membaca payload biasa, jadi rahasia tidak boleh disimpan di dalamnya hanya karena token ditandatangani.

Server harus memverifikasi signature dengan algoritma dan key yang diharapkan, memeriksa issuer/audience/expiry bila relevan, serta menentukan otorisasi setiap permintaan. Token bearer dapat digunakan siapa pun yang berhasil mencurinya sampai kedaluwarsa atau dicabut melalui strategi sistem. JWT tidak otomatis lebih aman daripada session; pilihan bergantung pada kebutuhan pencabutan, skala, arsitektur, dan threat model.

## 5.5. Platform Android

Android membangun aplikasi melalui komponen, manifest, resource, build tooling seperti Gradle, dan runtime Android. Aplikasi mobile harus menangani perubahan lifecycle, rotasi, pemulihan state, penggunaan baterai, lifecycle proses, dan izin sistem.

### Empat komponen utama

1. **Activity:** komponen yang berinteraksi langsung dengan pengguna dan biasanya merepresentasikan layar.
2. **Service:** komponen untuk pekerjaan yang tidak memiliki UI; batasan background execution Android modern perlu diperhatikan.
3. **Broadcast Receiver:** menerima broadcast dari sistem atau aplikasi sesuai aturan.
4. **Content Provider:** menyediakan akses data terstruktur untuk berbagi data antar aplikasi dengan kontrol izin.

### Activity lifecycle

Urutan yang umum dipelajari:
- **onCreate():** membuat Activity dan menginisialisasi komponen UI/state awal.
- **onStart():** Activity mulai terlihat.
- **onResume():** Activity berada di foreground dan dapat menerima interaksi.
- **onPause():** kehilangan fokus; tugas ringan yang perlu dilakukan segera dapat ditangani di sini.
- **onStop():** tidak terlihat.
- **onDestroy():** Activity sedang dihancurkan; tidak dijamin selalu dipanggil pada setiap terminasi proses.

Lifecycle tidak selalu berupa rangkaian tunggal tanpa perubahan. Sistem dapat menghentikan proses saat berada di background; simpan state yang perlu dipertahankan dan jangan mengandalkan objek dalam memori untuk data permanen.

### Intent dan izin

- **Explicit Intent:** target komponen disebut secara spesifik, misalnya berpindah ke Activity detail di aplikasi sendiri.
- **Implicit Intent:** menyatakan aksi umum, misalnya membuka URL atau membagikan teks, lalu sistem memilih aplikasi yang dapat menangani permintaan.
- **Permissions:** akses ke lokasi, kamera, kontak, dan data sensitif harus mengikuti izin sistem dan prinsip least privilege. Minta izin pada konteks yang dapat dipahami pengguna dan tangani penolakan.

### Penyimpanan data dan location-based services

- **SharedPreferences/DataStore:** preferensi sederhana dan pengaturan; jangan simpan rahasia sensitif secara plaintext.
- **SQLite:** basis data relasional lokal.
- **Room:** lapisan abstraksi di atas SQLite dengan entity, DAO, dan database untuk membantu validasi serta pemeliharaan.
- **RecyclerView:** menampilkan daftar data besar secara efisien dengan menggunakan ulang View.
- **Location-Based Services (LBS):** memanfaatkan sumber lokasi seperti GPS dan jaringan. Akurasi, konsumsi baterai, izin lokasi foreground/background, serta tujuan pengumpulan data harus dipertimbangkan.

### Target penguasaan PBP
Anda harus dapat menjelaskan alur request–response, DOM dan Fetch/AJAX, GET versus POST, penggunaan prepared statements, cookies versus session, MVC, REST dan status code, mekanisme JWT, komponen/lifecycle Android, intent eksplisit versus implisit, penyimpanan lokal, serta izin dan penggunaan lokasi yang aman.

---

# 6. PROYEK PERANGKAT LUNAK

Sumber: [Rangkuman Materi Proyek Perangkat Lunak](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/Proyek_Perangkat_Lunak/RANGKUMAN_MATERI.md)

## 6.1. Tujuan capstone dan cara kerja Agile

Proyek Perangkat Lunak mengintegrasikan analisis kebutuhan, desain, implementasi, basis data, pengujian, kolaborasi tim, dan deployment untuk menghasilkan produk yang dapat digunakan. Fokusnya bukan hanya banyaknya kode, tetapi nilai bagi pengguna, kualitas teknis, proses kolaborasi, kemampuan mengelola perubahan, dan bukti bahwa produk memenuhi kebutuhan.

Agile cocok untuk konteks ketika kebutuhan dapat berkembang dan umpan balik harus diperoleh secara berkala. Scrum merupakan kerangka kerja empiris yang menggunakan transparansi, inspeksi, dan adaptasi. Iterasi tidak menghapus kebutuhan akan perencanaan; perencanaan dilakukan bertahap dan diperbarui ketika ada bukti baru.

### Peran Scrum

- **Product Owner:** memaksimalkan nilai produk, mengelola urutan Product Backlog, menjelaskan tujuan, dan membantu memastikan item backlog dipahami.
- **Scrum Master:** membantu tim memahami dan menjalankan Scrum, memfasilitasi perbaikan, serta menangani hambatan proses.
- **Developers:** tim lintas keahlian yang menghasilkan increment sesuai Definition of Done. QA, frontend, backend, database, dan desain merupakan kompetensi yang dapat ada di tim; bukan berarti Scrum selalu mengharuskan jabatan QA terpisah.

### Artefak dan event

| Elemen | Isi/fungsi |
|---|---|
| Product Backlog | Daftar pekerjaan/fitur/peningkatan produk yang diurutkan menurut nilai dan kebutuhan |
| Sprint Backlog | Sprint Goal, item terpilih, dan rencana kerja tim untuk Sprint |
| Increment | Hasil kerja yang memenuhi Definition of Done dan dapat digunakan |
| Sprint Planning | Menentukan mengapa Sprint bernilai, apa yang bisa dilakukan, dan bagaimana pekerjaan dikerjakan |
| Daily Scrum | Inspeksi kemajuan menuju Sprint Goal dan adaptasi rencana harian |
| Sprint Review | Menginspeksi hasil dengan stakeholder dan membahas adaptasi berikutnya |
| Sprint Retrospective | Menilai kualitas dan efektivitas cara kerja tim untuk perbaikan |

## 6.2. User story, INVEST, dan acceptance criteria

Format sederhana user story:

**Sebagai [peran], saya ingin [fitur/aksi], sehingga [manfaat].**

Contoh: “Sebagai pengelola stok, saya ingin menerima peringatan ketika persediaan di bawah batas minimum, sehingga saya dapat melakukan pengadaan sebelum stok habis.”

INVEST adalah panduan kualitas:
- **Independent:** sebisa mungkin tidak terikat pada story lain.
- **Negotiable:** detailnya bisa dibahas, bukan spesifikasi kontrak yang kaku sejak awal.
- **Valuable:** memberikan nilai bagi pengguna/stakeholder.
- **Estimable:** cukup dipahami untuk diperkirakan.
- **Small:** cukup kecil untuk ditangani dalam satu Sprint.
- **Testable:** memenuhi kriteria yang dapat diverifikasi.

Acceptance criteria memperjelas kondisi yang harus dipenuhi. Format Gherkin:

~~~gherkin
GIVEN stok produk berada di bawah batas minimum
WHEN pengelola membuka dashboard persediaan
THEN sistem menampilkan peringatan untuk produk tersebut
~~~

Acceptance criteria berfokus pada perilaku/hasil yang dapat diperiksa. **Definition of Done** lebih luas: standar mutu yang harus dipenuhi sebuah increment, misalnya review kode selesai, pengujian lulus, dokumentasi diperbarui, dan tidak ada rahasia yang ikut di-commit.

## 6.3. Estimasi, prioritas, dan pemantauan

**Story point** merupakan estimasi relatif atas kompleksitas, usaha, ketidakpastian, dan risiko, bukan satuan jam yang universal. Planning Poker menggunakan diskusi dan kartu estimasi (sering mengikuti nilai Fibonacci seperti 1, 2, 3, 5, 8, 13) untuk mengungkap perbedaan pemahaman. Angka story point antar-tim tidak selalu dapat dibandingkan.

Prioritas backlog dapat mempertimbangkan nilai pengguna, urgensi, risiko teknis, ketergantungan, dan biaya penundaan. **Velocity** adalah jumlah story point yang diselesaikan tim per Sprint menurut aturan Done mereka sendiri; ia membantu perencanaan, bukan metrik produktivitas personal.

Burndown chart menunjukkan pekerjaan tersisa terhadap waktu. Bila grafik berbeda dari garis ideal, tim perlu menyelidiki penyebab—misalnya scope berubah, item terlalu besar, atau hambatan eksternal—bukan mengejar bentuk grafik dengan menurunkan kualitas.

## 6.4. Git, branching, pull request, dan code review

Git mengelola riwayat perubahan dan mendukung kerja paralel. Strategi branching bergantung pada ukuran tim dan proses rilis. Gitflow klasik dapat menggunakan:
- **main/master:** riwayat rilis produksi yang stabil.
- **develop:** integrasi pengembangan.
- **feature/**: perubahan fitur terisolasi.
- **release/**: stabilisasi rilis jika model tersebut dipakai.
- **hotfix/**: perbaikan darurat terhadap rilis.

Tidak semua tim perlu menerapkan Gitflow secara kaku; trunk-based development dapat lebih sesuai untuk rilis sering dan integrasi berkelanjutan. Yang penting adalah aturan branch dan proses merge dipahami serta konsisten.

Pull Request/Merge Request menjadi tempat meninjau perubahan sebelum digabungkan. Review seharusnya memeriksa kebenaran, keamanan, keterbacaan, dampak arsitektur, penanganan error, dan test coverage. Review bukan hanya mencari gaya penulisan. Hindari commit besar yang mencampur perubahan tidak terkait, tulis pesan commit yang jelas, dan jangan mengunggah secret, kredensial, file build, atau data pribadi ke repo.

## 6.5. Clean architecture, CI/CD, dan Docker

Pemisahan tanggung jawab menjaga agar perubahan pada UI atau database tidak merambat ke seluruh sistem tanpa alasan. Salah satu alur lapisan umum:

**Presentation/Controller → Service/Use Case → Repository/Data Access → Database atau layanan eksternal.**

Detail implementasi dapat bervariasi. Controller sebaiknya mengatur request dan response, service menjalankan aturan bisnis, dan repository mengisolasi akses data. Tidak setiap proyek memerlukan banyak lapisan; arsitektur harus sebanding dengan kompleksitas dan risiko.

### Continuous Integration (CI)

Pipeline CI biasanya berjalan ketika ada push atau pull request:
1. Memasang dependency dengan versi yang terkunci.
2. Menjalankan formatter/linter dan static analysis.
3. Menjalankan unit test serta pengujian lain yang relevan.
4. Melakukan build dan memeriksa artefak.
5. Melaporkan status sehingga perubahan gagal tidak langsung digabungkan ke branch rilis.

**Continuous Delivery** memastikan perubahan berada dalam keadaan siap dirilis; **Continuous Deployment** dapat merilis otomatis ke produksi setelah seluruh gerbang terpenuhi. CI bukan sekadar menjalankan build, dan deployment otomatis tetap membutuhkan strategi secret management, approval yang tepat, observability, backup, serta rollback.

### Docker

**Dockerfile** mendefinisikan bagaimana image dibangun. **Image** adalah templat immutable yang berisi sistem file dan metadata aplikasi; **container** merupakan instance berjalan dari image. **Docker Compose** membantu mendefinisikan beberapa service, jaringan, volume, dan konfigurasi dalam satu proyek, misalnya backend, database, dan reverse proxy.

Kontainerisasi membantu konsistensi lingkungan tetapi bukan otomatis menjamin keamanan. Gunakan image yang tepercaya dan diperbarui, jalankan dengan hak minimum, hindari memasukkan secret ke image, batasi port, perhatikan volume persisten, serta tetapkan konfigurasi development dan production dengan benar.

## 6.6. Pengujian penerimaan dan rilis

- **Unit test:** memeriksa unit kecil dengan dependensi minimal.
- **Integration test:** memeriksa kerja sama modul atau sistem eksternal.
- **System test:** menguji sistem terintegrasi terhadap spesifikasi.
- **User Acceptance Testing (UAT):** pengguna atau wakil bisnis menguji apakah alur nyata memenuhi kebutuhan yang disepakati.

UAT tidak menggantikan pengujian teknis. Tim tetap perlu menguji validasi, otorisasi, error handling, performa yang relevan, kompatibilitas, dan pemulihan. Umpan balik pengguna dicatat sebagai backlog baru atau revisi yang disepakati, bukan langsung diubah tanpa memperhitungkan dampak.

Dokumentasi penutupan dapat mencakup user manual, API collection/specification, arsitektur, skema data, deployment guide, daftar keterbatasan, known issues, serta rencana pemeliharaan.

### Target penguasaan PPL
Anda harus mampu memetakan peran/artefak/event Scrum, menulis user story dan acceptance criteria yang dapat diuji, menjelaskan story point/velocity, memilih workflow Git, mengulas PR secara bermutu, merancang pipeline CI, membedakan image dan container, serta menjelaskan peran UAT dalam proses rilis.

---

# 7. SISTEM INFORMASI

Sumber: [Rangkuman Materi Sistem Informasi](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/Sistem_Informasi/RANGKUMAN_MATERI.md)

## 7.1. Sistem informasi sebagai sistem sosio-teknis

Sistem Informasi bukan sekadar aplikasi atau database. Ia menggabungkan **people, process, dan technology** untuk mengumpulkan, memproses, menyimpan, dan menyebarkan informasi dalam organisasi. Sistem yang teknisnya baik tetap dapat gagal jika proses kerja tidak cocok, pelatihan buruk, data tidak dipercaya, atau pengguna tidak memperoleh manfaat.

### Hierarki DIKW

- **Data:** fakta mentah, angka, atau simbol belum ditafsirkan.
- **Information:** data yang diproses dan diberi konteks sehingga menjawab pertanyaan tertentu.
- **Knowledge:** pemahaman dan aturan yang terbentuk dengan menghubungkan informasi serta pengalaman.
- **Wisdom:** pertimbangan untuk menggunakan pengetahuan saat mengambil keputusan yang tepat dan bertanggung jawab.

Contoh: angka suhu 40 adalah data; “suhu rak server berada pada 40°C pukul 14.00” adalah informasi; “suhu yang terus naik dapat menandakan masalah pendinginan” merupakan pengetahuan; memutuskan memindahkan beban kerja dan memanggil teknisi berdasarkan risiko adalah penerapan kebijaksanaan.

DIKW adalah alat bantu konseptual; informasi tidak selalu otomatis menjadi pengetahuan atau kebijaksanaan. Konteks, validitas data, pengalaman, nilai, dan penilaian manusia tetap diperlukan.

## 7.2. Sistem informasi menurut tingkat manajemen

| Sistem | Pengguna/tingkat | Tujuan dan karakteristik | Contoh |
|---|---|---|---|
| TPS (Transaction Processing System) | Operasional | Menangani transaksi rutin berjumlah besar dengan akurat | POS, transaksi bank, absensi |
| MIS (Management Information System) | Manajemen menengah | Mengolah data transaksi menjadi laporan periodik dan ringkasan | Rekap penjualan bulanan |
| DSS (Decision Support System) | Analis/manajer | Mendukung masalah semi-terstruktur melalui data dan model | Simulasi skenario anggaran |
| EIS/ESS (Executive Information/Support System) | Eksekutif | Menyajikan indikator strategis dan tren internal/eksternal | Dashboard KPI direksi |

Perbedaan utama bukan hanya tampilan dashboard, melainkan tingkat keputusan yang didukung dan struktur masalahnya. TPS mendukung kegiatan rutin, MIS membuat ringkasan operasional, DSS menyediakan analisis/model untuk alternatif keputusan, sementara ESS/EIS memberi gambaran strategis tingkat tinggi. Kategori sistem tidak selalu eksklusif; sistem modern dapat menggabungkan kemampuan beberapa kategori.

Sistem pendukung keputusan dapat mencakup **what-if analysis** (bagaimana hasil berubah jika asumsi berubah), **sensitivity analysis** (seberapa besar keluaran terpengaruh oleh perubahan suatu variabel), dan **goal seeking** (nilai input apa yang dibutuhkan untuk mencapai target).

## 7.3. Keunggulan kompetitif: Porter’s Five Forces dan Value Chain

**Porter’s Five Forces** menganalisis tekanan industri:
1. Rivalitas antar pesaing saat ini.
2. Ancaman pendatang baru dan hambatan masuk pasar.
3. Daya tawar pembeli.
4. Daya tawar pemasok.
5. Ancaman produk/jasa pengganti.

Analisis ini membantu menjelaskan mengapa teknologi tertentu mungkin memperkuat atau mengurangi posisi perusahaan. Misalnya, platform digital dapat mengurangi hambatan distribusi bagi pendatang baru sekaligus memungkinkan perusahaan mapan menjangkau pelanggan lebih luas; dampak akhirnya bergantung pada efek jaringan, data, biaya berpindah, kepercayaan, dan struktur pasar.

**Porter’s Value Chain** membagi aktivitas menjadi:
- **Primary activities:** inbound logistics, operations, outbound logistics, marketing & sales, dan service.
- **Support activities:** infrastruktur perusahaan, manajemen SDM, pengembangan teknologi, dan procurement/pengadaan.

Sistem informasi dapat meningkatkan efisiensi di beberapa titik rantai nilai, seperti persediaan terintegrasi, otomatisasi produksi, pengiriman yang dapat dilacak, CRM, atau portal pemasok. Manfaat baru muncul jika proses dan kualitas data juga dirancang dengan baik.

## 7.4. Enterprise systems: ERP, SCM, CRM

### ERP (Enterprise Resource Planning)
ERP mengintegrasikan proses inti—misalnya keuangan, SDM, pengadaan, inventori, manufaktur, dan penjualan—melalui data serta proses yang saling terhubung. Integrasi mengurangi information silos, duplikasi, dan inkonsistensi, tetapi proyek ERP berisiko tinggi karena melibatkan migrasi data, perubahan proses, integrasi sistem lama, biaya lisensi, pelatihan, dan manajemen perubahan.

**Business Process Reengineering (BPR)** adalah pemikiran ulang dan perancangan ulang proses bisnis secara mendasar. Organisasi perlu memutuskan kapan menyesuaikan proses dengan praktik baku ERP dan kapan kebutuhan unik memang membenarkan kustomisasi.

### SCM (Supply Chain Management)
SCM mengoordinasikan aliran material, informasi, dan keuangan dari pemasok hulu hingga operasi internal dan pelanggan hilir. **Bullwhip effect** adalah amplifikasi fluktuasi permintaan saat informasi bergerak mundur melalui rantai pasok. Variasi kecil di penjualan ritel dapat menimbulkan perubahan pesanan yang besar di distributor dan pabrik akibat batching, keterlambatan, promosi, dan perkiraan permintaan yang berbeda.

Pengurangan bullwhip membutuhkan visibilitas data yang lebih baik, perkiraan kolaboratif, lead time yang lebih pendek, serta koordinasi kebijakan inventori dan pemesanan.

### CRM (Customer Relationship Management)
- **Operational CRM:** mengotomatisasi interaksi dan operasi pelanggan seperti penjualan, layanan, dan pemasaran.
- **Analytical CRM:** menganalisis data pelanggan untuk segmentasi, churn, personalisasi, atau prediksi nilai pelanggan.
- **Collaborative CRM:** berbagi informasi pelanggan lintas kanal/tim dengan kontrol akses yang tepat.

Data pelanggan harus dikelola sesuai tujuan, dasar pemrosesan, keamanan, dan hak pengguna. CRM yang agresif tanpa transparansi dapat merusak kepercayaan meskipun sistem analitiknya akurat.

## 7.5. Knowledge Management dan model SECI

Manajemen pengetahuan merupakan proses memperoleh, membagikan, menyimpan, dan menggunakan pengetahuan organisasi.

- **Tacit knowledge:** melekat pada pengalaman atau keterampilan pribadi dan sukar diformalkan.
- **Explicit knowledge:** dapat didokumentasikan, seperti SOP, manual, diagram, laporan, atau basis pengetahuan.

Model **SECI** menjelaskan perputaran konversi pengetahuan:
1. **Socialization (tacit → tacit):** belajar melalui observasi dan pengalaman bersama.
2. **Externalization (tacit → explicit):** mengungkapkan pengalaman menjadi dokumen atau model.
3. **Combination (explicit → explicit):** menggabungkan dokumen dan data menjadi pengetahuan terstruktur baru.
4. **Internalization (explicit → tacit):** menerapkan panduan sehingga menjadi kompetensi dan kebiasaan.

Repositori dokumen saja belum menjamin manajemen pengetahuan yang berhasil. Organisasi memerlukan konteks, pembaruan, pencarian yang efektif, insentif berbagi, dan kepercayaan bahwa pengetahuan akan digunakan secara tepat.

## 7.6. Bisnis digital, e-commerce, etika, dan privasi

Model bisnis e-commerce dapat berupa **B2C** (perusahaan ke konsumen), **B2B** (perusahaan ke perusahaan), **C2C** (konsumen ke konsumen), dan bentuk lain. Model pendapatan dapat berasal dari penjualan langsung, langganan, komisi/marketplace, iklan, freemium, atau lisensi. Pilihan model berpengaruh pada strategi akuisisi pengguna, biaya layanan, kebutuhan kepercayaan, dan desain sistem.

Isu etika sistem informasi antara lain privasi, akurasi data, kepemilikan informasi, akses yang adil, transparansi algoritma, pengawasan pekerja, bias, dan keamanan. Organisasi perlu membatasi pengumpulan data, membatasi akses, menjelaskan penggunaan yang relevan, mengamankan data, dan memiliki prosedur untuk insiden.

### Target penguasaan Sistem Informasi
Anda seharusnya mampu menjelaskan people–process–technology dan DIKW, mengklasifikasikan TPS/MIS/DSS/ESS, menerapkan Five Forces dan Value Chain pada kasus bisnis, membedakan ERP/SCM/CRM/KMS, menjelaskan bullwhip effect dan SECI, serta menilai dampak etika dari penggunaan data dan teknologi.

---

# 8. SINTESIS SEMESTER 5

Tujuh mata kuliah dapat dipahami melalui satu alur pengembangan layanan digital:

1. **Temukan masalah dan pelanggan:** Kewirausahaan membantu memvalidasi kebutuhan, target pasar, value proposition, dan model pendapatan.
2. **Tentukan manfaat organisasi:** Sistem Informasi menilai bagaimana produk membantu proses bisnis, keputusan, dan daya saing.
3. **Rancang serta bangun produk:** Pengembangan Berbasis Platform menyediakan komponen web/API/mobile, sementara Proyek Perangkat Lunak mengelola backlog dan kolaborasi.
4. **Tambahkan kemampuan prediktif bila diperlukan:** Pembelajaran Mesin memproses data untuk klasifikasi, prediksi, atau clustering.
5. **Skalakan komputasi dengan tepat:** Komputasi Tersebar dan Paralel membantu koordinasi banyak proses dan pengolahan skala besar.
6. **Lindungi sistem dan data:** Keamanan dan Jaminan Informasi menetapkan kontrol akses, kriptografi, deteksi, respons insiden, dan pengelolaan risiko.
7. **Uji, rilis, dan evaluasi:** proses CI, pengujian, UAT, monitoring, serta umpan balik memungkinkan perbaikan berulang.

Keputusan teknis semestinya mengikuti kebutuhan dan risiko. Model ML dengan F1 tinggi tidak cukup bila datanya bocor atau digunakan tanpa persetujuan yang tepat. REST API yang berjalan bukan berarti aman bila otorisasi tidak diperiksa. Container tidak menghilangkan kebutuhan konfigurasi dan monitoring. BMC yang rapi juga bukan bukti produk akan laku tanpa validasi pelanggan.

## 9. RUMUS DAN KONSEP KUNCI YANG WAJIB DIINGAT

| Konsep | Rumus atau aturan ringkas |
|---|---|
| SLE | \(SLE=AV\times EF\) |
| ALE | \(ALE=SLE\times ARO\) |
| Manfaat bersih kontrol keamanan | \(ALE_{sebelum}-ALE_{sesudah}-Biaya\ Kontrol\) |
| BEP unit | \(BEP=FC/(P-VC_u)\) |
| ROI | \((Manfaat\ Bersih/Biaya\ Investasi)\times100\%\) |
| Lamport saat menerima pesan | \(L_j=\max(L_j,t)+1\) |
| Amdahl | \(S(N)=1/((1-P)+P/N)\) |
| Gustafson | \(S_G(N)=N-\alpha(N-1)\) |
| Euclidean distance | \(d(x,y)=\sqrt{\sum_i(x_i-y_i)^2}\) |
| Entropy | \(H(S)=-\sum_i p_i\log_2p_i\) |
| Information Gain | Entropy sebelum split dikurangi entropy rata-rata setelah split |
| Naive Bayes | \(P(C\mid X)=P(X\mid C)P(C)/P(X)\) |
| F1 | \(2PR/(P+R)\) |

## 10. CHECKLIST SEBELUM UJIAN

Pastikan Anda bisa menjawab tanpa hanya menghafal definisi:

- [ ] Menjelaskan contoh pelanggaran confidentiality, integrity, dan availability.
- [ ] Menghitung SLE dan ALE, lalu menilai manfaat finansial kontrol keamanan.
- [ ] Membedakan DAC, MAC, RBAC, ABAC, Bell–LaPadula, dan Biba.
- [ ] Memilih kapan enkripsi simetris, kriptografi asimetris, hash, HMAC, dan tanda tangan digital digunakan.
- [ ] Menyusun BMC dari contoh usaha aplikasi dan menjelaskan kaitan STP dengan 4P/7P.
- [ ] Menghitung BEP dan menginterpretasikan perbedaan laba, arus kas, CAC, dan LTV.
- [ ] Menjelaskan clock Lamport, vector clock, CAP ketika terjadi partition, dan peran 2PC/Raft.
- [ ] Menghitung speedup menggunakan Hukum Amdahl dan menjelaskan kapan Gustafson relevan.
- [ ] Menghitung jarak k-NN, entropy/information gain, probabilitas Naive Bayes, dan metrik klasifikasi.
- [ ] Menjelaskan overfitting, data leakage, cross-validation, serta perbedaan K-Means dan DBSCAN.
- [ ] Menjelaskan alur web client-server, Fetch/AJAX, prepared statements, session, REST, JWT, dan lifecycle Android.
- [ ] Menulis user story serta acceptance criteria, membedakan event Scrum, dan memahami dasar CI/CD serta Docker.
- [ ] Menerapkan DIKW, TPS/MIS/DSS/ESS, Porter’s Five Forces, Value Chain, ERP/SCM/CRM, serta model SECI pada studi kasus.

**Strategi belajar:** untuk setiap topik, berlatihlah dalam tiga bentuk: definisi konsep dengan kalimat sendiri, contoh kasus penerapan, dan perhitungan/penelusuran langkah bila topiknya matematis. Pada ujian komprehensif, jawaban yang kuat tidak hanya menyebut istilah, tetapi menunjukkan kapan konsep tepat digunakan, asumsi apa yang berlaku, dan keterbatasan apa yang harus diperhatikan.
