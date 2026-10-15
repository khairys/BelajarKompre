# RANGKUMAN LENGKAP SEMESTER 4
## Persiapan Ujian Komprehensif S1 Informatika — Universitas Diponegoro

# GAMBARAN UMUM SEMESTER 4

Semester 4 mempertemukan fondasi pemrograman, matematika, struktur data, basis data, dan sistem operasi yang telah Anda pelajari sebelumnya dengan pengembangan aplikasi dan teknik komputasi yang lebih kompleks.

Pada tahap ini, Anda mulai mendalami bagaimana komputer menghasilkan visual, bagaimana komputer saling berkomunikasi dalam jaringan, bagaimana DBMS menjaga performa dan konsistensi data, bagaimana program dirancang menggunakan paradigma objek, bagaimana perangkat lunak dikembangkan secara sistematis, dan bagaimana kecerdasan buatan menyelesaikan masalah.

Enam mata kuliahnya adalah:

| Mata kuliah | Fokus pembelajaran |
|---|---|
| Grafika dan Komputasi Visual | Membentuk, mentransformasikan, dan menganalisis objek visual |
| Jaringan Komputer | Mengirimkan data antarkomputer dengan protokol dan mekanisme yang sesuai |
| Manajemen Basis Data | Mengoptimalkan query, mengelola transaksi, dan memulihkan basis data |
| Pemrograman Berorientasi Objek | Merancang perangkat lunak modular menggunakan kelas dan objek |
| Rekayasa Perangkat Lunak | Mengelola kebutuhan, desain, pengembangan, serta pengujian perangkat lunak |
| Sistem Cerdas | Menyelesaikan masalah melalui pencarian, penalaran, dan pembelajaran |

Hubungan antarmata kuliah ini sangat penting. Aplikasi berbasis jaringan dapat menggunakan OOP sebagai pendekatan pemrograman, RPL sebagai proses pengembangannya, Manajemen Basis Data untuk menjaga data, dan Sistem Cerdas untuk menghasilkan keputusan otomatis. Grafika dan Komputasi Visual dapat digunakan untuk menampilkan hasilnya secara visual.

---

# 1. GRAFIKA DAN KOMPUTASI VISUAL

Sumber: [Rangkuman Grafika dan Komputasi Visual](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/Grafika_dan_Komputasi_Visual/RANGKUMAN_MATERI.md)

Grafika dan Komputasi Visual mempelajari dua bidang yang berkaitan.

**Computer Graphics** berfokus pada pembentukan gambar dari model matematis dan representasi objek. Contohnya, game engine mengubah model tiga dimensi menjadi gambar pada layar.

**Digital Image Processing** berfokus pada pengolahan citra yang sudah tersedia, misalnya meningkatkan kontras, mengurangi noise, dan mendeteksi tepi objek.

Dengan demikian, computer graphics umumnya membentuk gambar dari model, sedangkan pengolahan citra memproses atau menganalisis gambar.

## 1.1. Representasi citra digital dan warna

Citra digital dapat direpresentasikan sebagai matriks piksel. Setiap piksel menyimpan informasi intensitas atau warna.

Pada citra grayscale 8-bit, intensitas umumnya direpresentasikan dari 0 sampai 255:

- 0 menunjukkan hitam.
- 255 menunjukkan putih.
- Nilai di antaranya menunjukkan tingkat keabuan.

Citra berwarna RGB menyimpan komponen merah, hijau, dan biru. Setiap kombinasi intensitas ketiganya menghasilkan warna yang berbeda.

Contohnya, pada representasi RGB 8-bit per kanal:

- `(255, 0, 0)` menunjukkan merah.
- `(0, 255, 0)` menunjukkan hijau.
- `(0, 0, 255)` menunjukkan biru.
- `(255, 255, 255)` menunjukkan putih.
- `(0, 0, 0)` menunjukkan hitam.

Model warna yang perlu dikenali:

**RGB** digunakan secara luas pada layar digital karena warna dibentuk melalui penambahan cahaya.

**CMYK** digunakan dalam banyak proses pencetakan berbasis tinta.

**HSL** merepresentasikan warna melalui hue, saturation, dan lightness, sehingga pengaturan warna tertentu dapat terasa lebih intuitif bagi manusia.

## 1.2. Algoritma pembentukan garis DDA

Komputer menampilkan objek grafis sebagai kumpulan piksel. Karena garis matematis dapat melewati posisi di antara piksel, algoritma rasterisasi menentukan piksel mana yang paling sesuai untuk membentuk garis.

Digital Differential Analyzer (DDA) menghitung perubahan koordinat secara bertahap.

Untuk garis yang menghubungkan \((x_1,y_1)\) dan \((x_2,y_2)\):

\[
\Delta x=x_2-x_1
\]

\[
\Delta y=y_2-y_1
\]

Tentukan jumlah langkah:

\[
steps=\max(|\Delta x|,|\Delta y|)
\]

Kemudian:

\[
x_{inc}=\frac{\Delta x}{steps},
\qquad
y_{inc}=\frac{\Delta y}{steps}
\]

Koordinat diperbarui berulang kali menggunakan kedua increment tersebut, lalu dibulatkan ke posisi piksel terdekat.

**Contoh:**

Garis dari \((1,1)\) ke \((5,3)\).

\[
\Delta x=4,\qquad \Delta y=2
\]

\[
steps=4
\]

Sehingga:

\[
x_{inc}=1,\qquad y_{inc}=0.5
\]

Koordinat perkiraannya:

- `(1, 1)`
- `(2, 1.5)`
- `(3, 2)`
- `(4, 2.5)`
- `(5, 3)`

Koordinat pecahan dibulatkan sesuai kebijakan rasterisasi yang digunakan.

Kelebihan DDA adalah konsepnya sederhana. Kekurangannya, perhitungan pecahan dan pembulatan berulang dapat menambah biaya komputasi.

## 1.3. Algoritma Bresenham

Bresenham membuat garis dengan memanfaatkan aritmetika bilangan bulat sehingga efisien untuk rasterisasi.

Untuk kasus dasar ketika \(0\leq m<1\), dengan garis bergerak dari kiri ke kanan:

\[
\Delta x=x_2-x_1,\qquad
\Delta y=y_2-y_1
\]

Parameter keputusan awal:

\[
p_0=2\Delta y-\Delta x
\]

Pada setiap langkah, algoritma menentukan apakah piksel berikutnya tetap pada baris yang sama atau bergerak satu baris ke atas.

Jika \(p_k<0\):

\[
p_{k+1}=p_k+2\Delta y
\]

Jika \(p_k\geq0\):

\[
p_{k+1}=p_k+2\Delta y-2\Delta x
\]

Rumus tersebut berlaku untuk kasus kemiringan dasar di atas. Garis dengan kemiringan lain memerlukan penyesuaian terhadap arah sumbu dan tanda perubahan koordinat.

Perbedaan utama DDA dan Bresenham:

| Aspek | DDA | Bresenham |
|---|---|---|
| Perhitungan utama | Increment koordinat pecahan | Parameter keputusan integer |
| Pembulatan | Dilakukan selama iterasi | Tidak memerlukan operasi pecahan pada algoritma dasar |
| Efisiensi | Sederhana, tetapi floating-point dapat menambah biaya | Umumnya lebih efisien untuk rasterisasi |
| Konsep penting | Perubahan koordinat bertahap | Pemilihan piksel berdasarkan keputusan |

## 1.4. Algoritma lingkaran midpoint

Algoritma midpoint membentuk lingkaran menggunakan persamaan:

\[
x^2+y^2=R^2
\]

Kuncinya adalah memanfaatkan simetri delapan arah. Cukup hitung titik pada satu bagian lingkaran, kemudian hasilnya dicerminkan ke bagian lain.

Parameter keputusan awal yang umum digunakan:

\[
p_0=1-R
\]

Berdasarkan nilai parameter tersebut, algoritma memilih piksel berikutnya dan memperbarui parameter keputusan.

Algoritma ini mengurangi perhitungan berulang karena tidak perlu menghitung seluruh keliling lingkaran secara terpisah.

## 1.5. Transformasi geometri 2D

Transformasi geometri mengubah posisi, ukuran, dan orientasi objek.

### Translasi

Translasi menggeser objek sejauh \(t_x\) dan \(t_y\).

\[
x'=x+t_x
\]

\[
y'=y+t_y
\]

### Penskalaan (*scaling*)

Penskalaan mengubah ukuran objek:

\[
x'=s_xx,\qquad y'=s_yy
\]

Jika \(s_x=s_y\), pembesaran dilakukan secara seragam. Jika faktor berbeda, objek mengalami perubahan proporsi.

### Rotasi

Rotasi sebesar sudut \(\theta\) terhadap titik asal, dengan konvensi koordinat Kartesius dan sudut positif berlawanan arah jarum jam:

\[
x'=x\cos\theta-y\sin\theta
\]

\[
y'=x\sin\theta+y\cos\theta
\]

Matriks rotasinya:

\[
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
\]

### Koordinat homogen

Translasi dapat digabungkan dengan transformasi lain melalui koordinat homogen.

Titik \((x,y)\) diubah menjadi:

\[
\mathbf{p}=
\begin{bmatrix}
x\\y\\1
\end{bmatrix}
\]

Matriks translasi:

\[
T(t_x,t_y)=
\begin{bmatrix}
1&0&t_x\\
0&1&t_y\\
0&0&1
\end{bmatrix}
\]

Matriks penskalaan:

\[
S=
\begin{bmatrix}
s_x&0&0\\
0&s_y&0\\
0&0&1
\end{bmatrix}
\]

Matriks rotasi:

\[
R=
\begin{bmatrix}
\cos\theta&-\sin\theta&0\\
\sin\theta&\cos\theta&0\\
0&0&1
\end{bmatrix}
\]

Untuk vektor kolom, transformasi dilakukan dengan perkalian matriks terhadap vektor koordinat.

**Urutan transformasi penting.** Perkalian matriks umumnya tidak komutatif, sehingga melakukan translasi lalu rotasi dapat menghasilkan posisi akhir yang berbeda dari rotasi lalu translasi.

Rotasi terhadap pusat sembarang \((x_p,y_p)\) dapat dibangun melalui:

\[
M=T(x_p,y_p)R(\theta)T(-x_p,-y_p)
\]

Artinya, geser pusat rotasi ke titik asal, lakukan rotasi, lalu kembalikan ke posisi semula.

## 1.6. Line clipping menggunakan Cohen–Sutherland

Clipping adalah proses memotong bagian objek grafis yang berada di luar jendela tampilan.

Cohen–Sutherland menggunakan kode wilayah atau *outcode* empat bit untuk menandai posisi endpoint terhadap jendela kliping:

- Top: di atas batas.
- Bottom: di bawah batas.
- Right: di kanan batas.
- Left: di kiri batas.

Bit dapat digabungkan untuk menunjukkan beberapa kondisi sekaligus.

Misalkan jendela tampilan ditentukan oleh:

\[
[x_{\min},x_{\max}]\times[y_{\min},y_{\max}]
\]

Ada tiga kondisi utama.

**Trivial accept:** kedua endpoint memiliki outcode `0000`. Seluruh garis berada di dalam jendela.

**Trivial reject:** operasi bitwise AND atas kedua outcode tidak sama dengan nol. Kedua endpoint berada di luar pada sisi yang sama sehingga garis tidak memotong jendela.

**Clipping diperlukan:** garis perlu diperiksa lebih lanjut terhadap batas-batas jendela.

Perhatikan perbedaan kondisi terakhir: jika bitwise AND bernilai nol, garis belum tentu sepenuhnya berada di dalam jendela. Titik potong masih perlu dihitung apabila kedua outcode tidak sama-sama nol.

Algoritma Sutherland–Hodgman juga perlu dikenali. Algoritma ini digunakan untuk clipping poligon terhadap batas jendela kliping.

## 1.7. Proyeksi 3D

Proyeksi memetakan objek tiga dimensi ke bidang dua dimensi agar dapat ditampilkan pada layar.

### Proyeksi paralel atau ortografik

Garis proyeksi sejajar satu sama lain. Ukuran objek tidak berubah hanya karena jarak dari kamera.

Penggunaannya antara lain gambar teknik dan CAD.

### Proyeksi perspektif

Garis proyeksi bertemu pada pusat proyeksi. Objek yang lebih jauh tampak lebih kecil dan garis yang sejajar dapat terlihat menuju titik hilang.

Proyeksi perspektif lebih mendekati cara manusia melihat kedalaman.

Perbedaan utamanya terletak pada cara kedalaman memengaruhi ukuran visual objek.

## 1.8. Hidden surface removal

Dalam objek 3D, beberapa permukaan dapat berada di belakang permukaan lain. Tidak semua permukaan tersebut seharusnya terlihat dari sudut pandang kamera.

### Z-buffer

Z-buffer menyimpan informasi kedalaman untuk setiap posisi piksel.

Secara konseptual:
1. Sistem menentukan warna dan kedalaman calon piksel.
2. Kedalaman calon piksel dibandingkan dengan nilai Z-buffer yang tersimpan.
3. Jika calon piksel lebih dekat menurut konvensi kedalaman yang digunakan, nilai kedalaman dan warna diperbarui.

Dalam konfigurasi umum dengan nilai \(z\) lebih kecil berarti lebih dekat ke kamera, pembaruan dilakukan jika:

\[
z_{\text{baru}}<z_{\text{buffer}}(x,y)
\]

Z-buffer digunakan bersama frame buffer, yang menyimpan informasi warna piksel.

### Back-face culling

Back-face culling mengabaikan poligon yang menghadap menjauhi kamera sesuai orientasi permukaan dan konvensi sistem.

Teknik ini mengurangi pekerjaan rendering untuk permukaan yang tidak perlu ditampilkan pada model tertutup tertentu.

Namun, teknik ini tidak menggantikan depth testing. Dua poligon yang sama-sama menghadap kamera masih dapat saling menutupi.

## 1.9. Pencahayaan dan shading

Shading menentukan bagaimana permukaan objek tampak ketika menerima cahaya.

Model pencahayaan Phong menggabungkan komponen ambient, diffuse, dan specular:

\[
I=I_ak_a+I_dk_d(\mathbf{N}\cdot\mathbf{L})
+I_sk_s(\mathbf{R}\cdot\mathbf{V})^n
\]

Dalam penerapan praktis, dot product dan faktor pencahayaan biasanya dibatasi sesuai kebutuhan agar intensitas tidak negatif.

Komponennya:

- **Ambient:** pencahayaan dasar yang mewakili cahaya lingkungan.
- **Diffuse:** pantulan menyebar yang dipengaruhi arah datang cahaya dan orientasi permukaan.
- **Specular:** highlight yang menunjukkan pantulan lebih mengilap.

### Flat, Gouraud, dan Phong shading

**Flat shading:** menghitung satu intensitas atau warna untuk setiap poligon. Relatif murah, tetapi permukaan dapat terlihat bersudut.

**Gouraud shading:** menghitung pencahayaan pada vertex, kemudian menginterpolasi warnanya di sepanjang poligon.

**Phong shading:** menginterpolasi normal permukaan dan menghitung pencahayaan pada setiap piksel atau fragmen.

Perbedaan yang sering ditanyakan adalah bahwa Gouraud menginterpolasi warna atau intensitas, sedangkan Phong shading menginterpolasi normal sebelum menghitung pencahayaan per piksel.

## 1.10. Pengolahan citra digital

Pengolahan citra memanipulasi intensitas piksel berdasarkan tujuan tertentu.

### Histogram equalization

Histogram menggambarkan distribusi intensitas piksel.

Histogram equalization menggunakan distribusi kumulatif untuk memetakan ulang intensitas sehingga rentang kontras dapat dimanfaatkan lebih efektif.

Tujuannya memperbaiki citra dengan kontras kurang baik, tetapi metode ini tidak selalu memperindah setiap gambar dan dapat memperkuat noise pada kondisi tertentu.

### Konvolusi spasial

Filter konvolusi menggunakan matriks kecil bernama kernel yang diterapkan pada lingkungan piksel.

\[
g(x,y)=\sum_s\sum_tK(s,t)f(x+s,y+t)
\]

Dalam rumus tersebut, \(f\) merupakan citra masukan, \(K\) adalah kernel, dan \(g\) hasil pengolahan.

### Low-pass dan high-pass filter

**Low-pass filter** mengurangi perubahan intensitas yang cepat. Filter rata-rata dan Gaussian sering digunakan untuk mengurangi noise atau menghasilkan efek smoothing.

**High-pass filter** menonjolkan perubahan intensitas yang tajam, misalnya untuk sharpening.

### Deteksi tepi

Tepi muncul pada wilayah yang memiliki perubahan intensitas besar. Operator Sobel memperkirakan gradien intensitas pada arah horizontal dan vertikal.

Kernel Sobel yang umum:

\[
G_x=
\begin{bmatrix}
-1&0&1\\
-2&0&2\\
-1&0&1
\end{bmatrix}
\]

\[
G_y=
\begin{bmatrix}
-1&-2&-1\\
0&0&0\\
1&2&1
\end{bmatrix}
\]

Magnitudo gradien sering diperkirakan dengan:

\[
G=\sqrt{G_x^2+G_y^2}
\]

Nilai yang besar menunjukkan kemungkinan adanya perubahan intensitas yang kuat.

## 1.11. Morfologi citra

Morfologi merupakan operasi yang memproses bentuk objek, terutama pada citra biner.

**Dilasi** cenderung memperbesar atau menebalkan bagian objek.

**Erosi** cenderung mengecilkan objek dan menghilangkan bagian kecil sesuai struktur elemen yang digunakan.

**Opening** merupakan erosi diikuti dilasi dan dapat menghilangkan komponen kecil.

**Closing** merupakan dilasi diikuti erosi dan dapat menutup celah sempit atau lubang kecil.

Efek aktual bergantung pada bentuk struktur elemen (*structuring element*) serta bentuk objek.

### Target penguasaan Grafika dan Komputasi Visual

Anda perlu mampu:
1. Menjalankan algoritma Bresenham pada kasus garis sederhana.
2. Menghitung transformasi translasi, rotasi, dan penskalaan.
3. Menjelaskan koordinat homogen serta urutan perkalian matriks.
4. Menentukan hasil clipping garis.
5. Membedakan proyeksi paralel dan perspektif.
6. Menjelaskan Z-buffer dan tiga model shading.
7. Menghitung konvolusi sederhana serta membedakan operasi morfologi.

---

# 2. JARINGAN KOMPUTER

Sumber: [Rangkuman Jaringan Komputer](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/Jaringan_Komputer/RANGKUMAN_MATERI.md)

Jaringan Komputer mempelajari bagaimana data ditransmisikan dari satu perangkat ke perangkat lain melalui media komunikasi, menggunakan protokol dan mekanisme pengalamatan yang sesuai.

Ketika Anda membuka sebuah situs web, perangkat harus mengetahui alamat tujuan, membagi komunikasi sesuai protokol, mengirimkan paket melalui jaringan, dan memproses respons yang diterima.

## 2.1. Model OSI dan TCP/IP

Model lapisan membagi komunikasi jaringan menjadi beberapa fungsi agar desain dan troubleshooting lebih terstruktur.

### Model OSI tujuh lapisan

| Lapisan | Nama | Fungsi utama |
|---|---|---|
| 7 | Application | Layanan jaringan yang digunakan aplikasi |
| 6 | Presentation | Representasi, transformasi, dan format data |
| 5 | Session | Pengelolaan sesi komunikasi |
| 4 | Transport | Komunikasi antaraplikasi, segmentasi, keandalan |
| 3 | Network | Pengalamatan IP dan routing |
| 2 | Data Link | Frame, MAC address, dan akses media |
| 1 | Physical | Transmisi bit melalui media fisik |

Model TCP/IP praktis sering digambarkan sebagai lima lapisan:

1. Application.
2. Transport.
3. Network.
4. Data Link.
5. Physical.

Model empat lapisan juga sering digunakan dengan menggabungkan Data Link dan Physical menjadi satu lapisan Network Access.

Perbedaan model tidak berarti fungsi dasarnya hilang; pengelompokan lapisannya yang berbeda.

### Enkapsulasi dan dekapsulasi

Ketika aplikasi mengirimkan data, setiap lapisan menambahkan informasi kontrol sesuai tugasnya.

Alur sederhananya:

**Data aplikasi → Segmen transport → Paket IP → Frame → Bit**

Pada sisi penerima, proses dekapsulasi melepaskan informasi kontrol per lapisan sebelum data diberikan ke aplikasi.

PDU yang sering dipakai dalam soal:

- Application: message atau data.
- Transport: segment untuk TCP dan istilah datagram untuk UDP.
- Network: packet.
- Data Link: frame.
- Physical: bit.

## 2.2. Lapisan fisik dan kapasitas kanal

Media fisik bisa berupa kabel tembaga, serat optik, atau gelombang radio.

Kapasitas kanal dipengaruhi bandwidth, karakteristik sinyal, serta noise.

### Teorema Nyquist

Untuk model kanal ideal bebas noise dengan bandwidth \(B\) dan \(M\) level sinyal:

\[
C=2B\log_2M
\]

\(C\) adalah batas laju simbol-data dalam bit per detik pada kondisi model tersebut.

### Teorema Shannon–Hartley

Untuk kanal dengan noise aditif dalam model yang sesuai:

\[
C=B\log_2\left(1+\frac SN\right)
\]

Keterangan:
- \(B\) adalah bandwidth dalam Hz.
- \(S/N\) adalah rasio daya sinyal terhadap daya noise dalam bentuk linier.

Jika rasio diberikan dalam desibel:

\[
SNR_{\mathrm{dB}}=10\log_{10}(S/N)
\]

Kedua rumus tersebut tidak boleh dipertukarkan begitu saja. Nyquist menggunakan jumlah level sinyal dalam model kanal bebas derau, sedangkan Shannon memperhitungkan rasio sinyal terhadap noise.

## 2.3. Data Link Layer

Data Link mengelompokkan bit menjadi frame serta menangani pengalamatan fisik dan deteksi kesalahan sesuai teknologinya.

### MAC address

MAC address digunakan dalam komunikasi pada lapisan Data Link, khususnya untuk pengiriman frame pada jaringan lokal.

Alamat MAC bukan pengganti alamat IP. IP menyediakan pengalamatan logis dan routing antarjaringan, sedangkan MAC digunakan dalam pengiriman frame pada suatu lingkup link.

### Error detection dengan CRC

Cyclic Redundancy Check (CRC) mendeteksi perubahan bit menggunakan pembagian polinomial biner modulo-2.

Proses dasarnya:
1. Pengirim memilih generator polinomial.
2. Data ditambahkan bit nol sesuai derajat generator.
3. Operasi pembagian modulo-2 dilakukan menggunakan XOR.
4. Sisa pembagian dijadikan nilai pemeriksaan atau FCS.
5. Penerima melakukan pemeriksaan sesuai generator yang sama.

CRC dapat mendeteksi banyak pola kesalahan, tetapi tidak otomatis memperbaiki semua kesalahan dan tidak merupakan mekanisme autentikasi kriptografis.

### CSMA/CD dan CSMA/CA

**CSMA/CD** mendeteksi collision pada metode Ethernet half-duplex klasik. Perangkat memeriksa media, melakukan transmisi ketika sesuai, dan menangani tabrakan dengan mekanisme backoff. Mekanisme ini bukan prosedur normal pada Ethernet switched full-duplex modern.

**CSMA/CA** berusaha menghindari collision dalam jaringan nirkabel melalui mekanisme akses kanal dan penundaan yang sesuai. Masalah hidden terminal dapat membuat dua perangkat mengirim tanpa mengetahui bahwa transmisi perangkat lain berpotensi bertabrakan di penerima.

## 2.4. Pengalamatan IPv4

IPv4 menggunakan alamat 32-bit yang biasanya ditulis sebagai empat oktet desimal.

Contoh:

`192.168.1.10`

Alamat dibagi menjadi bagian network dan host sesuai prefix atau subnet mask.

CIDR menggunakan notasi `/n` untuk menunjukkan jumlah bit network.

Contoh:

`192.168.1.10/24`

Prefix `/24` berarti 24 bit untuk bagian network dan 8 bit untuk bagian host.

### Menghitung jumlah host

Untuk subnet IPv4 konvensional yang menggunakan alamat network dan broadcast terpisah:

\[
\text{Jumlah host usable}=2^{32-n}-2
\]

Contoh untuk `/24`:

\[
2^{32-24}-2=2^8-2=254
\]

Pengecualian seperti `/31` untuk link point-to-point dan `/32` untuk satu alamat perlu dipahami dalam konteks penggunaannya.

### Network dan broadcast address

Network address diperoleh dengan melakukan operasi AND antara alamat IP dan subnet mask.

Broadcast address IPv4 konvensional memiliki semua bit host bernilai 1.

Pada subnet `192.168.1.0/24`:
- Network address: `192.168.1.0`.
- Alamat host usable: `192.168.1.1` hingga `192.168.1.254`.
- Broadcast address: `192.168.1.255`.

## 2.5. Subnetting dan VLSM

Subnetting membagi sebuah blok jaringan menjadi subnet yang lebih kecil.

VLSM (*Variable Length Subnet Masking*) memungkinkan tiap subnet memakai prefix berbeda sesuai kebutuhan jumlah host. Dengan demikian, pembagian alamat dapat lebih efisien daripada memberikan ukuran subnet yang sama untuk semua bagian.

Contoh: jika sebuah organisasi memerlukan subnet untuk 100, 50, dan 20 host, kebutuhan tersebut tidak harus diberi alokasi prefix yang sama.

Prinsip pengerjaan:
1. Tentukan jumlah host yang dibutuhkan pada setiap subnet.
2. Cari jumlah bit host minimum yang memenuhi kebutuhan.
3. Tentukan prefix yang sesuai.
4. Alokasikan blok terbesar terlebih dahulu dan pastikan setiap blok tidak tumpang tindih.
5. Periksa network, rentang host, dan broadcast address.

## 2.6. Routing

Routing menentukan jalur paket dari jaringan asal menuju jaringan tujuan.

### RIP

RIP termasuk protokol distance-vector yang menggunakan hop count sebagai metrik. Batas jarak 15 hop yang valid membuat RIP tidak cocok untuk jaringan yang membutuhkan skala routing besar.

RIP memiliki risiko *count-to-infinity*. Teknik seperti split horizon dan poison reverse dapat membantu mengurangi masalah routing loop tertentu.

### OSPF

OSPF merupakan protokol link-state. Router menyebarkan informasi mengenai topologi yang relevan, membentuk representasi graf jaringan, lalu menghitung rute terpendek menggunakan algoritma Dijkstra.

Metrik OSPF menggunakan cost, yang dalam banyak implementasi terkait dengan bandwidth berdasarkan aturan konfigurasi.

### BGP

BGP digunakan untuk routing antar-autonomous system pada internet. BGP termasuk path-vector dan mempertimbangkan kebijakan routing serta atribut jalur, bukan hanya mencari jalur fisik terpendek.

Perbedaan utama ketiganya:

| Protokol | Keluarga | Konteks penggunaan |
|---|---|---|
| RIP | Distance-vector | Jaringan relatif kecil dan sederhana |
| OSPF | Link-state | Routing internal yang membutuhkan perhitungan jalur berdasarkan topologi |
| BGP | Path-vector | Routing antar-autonomous system |

## 2.7. TCP dan UDP

Lapisan Transport menyediakan komunikasi antaraplikasi melalui port.

### TCP

TCP berorientasi koneksi dan menyediakan:
- Sequence number.
- Acknowledgment.
- Retransmisi untuk penanganan kehilangan data.
- Penyusunan ulang data.
- Flow control.
- Congestion control.

TCP digunakan ketika urutan data dan keandalan pengiriman menjadi penting.

### UDP

UDP mengirimkan datagram tanpa membangun koneksi TCP. UDP tidak memberikan jaminan pengiriman, urutan, ataupun retransmisi sebagaimana layanan TCP.

UDP cocok ketika aplikasi memerlukan overhead rendah atau ingin mengelola keandalan sendiri, contohnya aplikasi media real-time dan sejumlah protokol query.

| Aspek | TCP | UDP |
|---|---|---|
| Koneksi | Berorientasi koneksi | Connectionless |
| Reliabilitas transport | Ada mekanisme ACK dan retransmisi | Tidak menyediakan jaminan tersebut |
| Urutan | Menyediakan aliran data terurut | Tidak menjamin urutan datagram |
| Flow control | Ada | Tidak disediakan oleh UDP |
| Congestion control | Ada mekanisme pada TCP | Harus ditangani sesuai kebutuhan protokol/aplikasi |
| Header minimum | 20 byte | 8 byte |

## 2.8. TCP three-way handshake

TCP membangun koneksi melalui pertukaran tiga segmen dasar:

1. Client mengirim `SYN` dengan sequence number \(x\).
2. Server merespons `SYN-ACK` dengan sequence number \(y\) dan acknowledgment \(x+1\).
3. Client mengirim `ACK` untuk mengonfirmasi sequence number server, yaitu \(y+1\).

Handshake menyinkronkan parameter awal komunikasi dan mengonfirmasi bahwa kedua ujung dapat bertukar segmen dalam koneksi.

Penutupan TCP biasa melibatkan FIN dan ACK di kedua arah sesuai keadaan koneksi. Karena dua arah aliran data dapat ditutup secara terpisah, proses penutupan sering digambarkan sebagai four-way teardown.

## 2.9. Flow control dan congestion control

**Flow control** menjaga agar pengirim tidak membanjiri penerima dengan data yang melebihi kapasitas buffer penerima.

**Congestion control** berusaha mencegah kemacetan jaringan akibat terlalu banyak data yang dikirim ke jaringan.

Pada TCP, dua mekanisme ini berbeda.

Dalam algoritma congestion control AIMD, pengirim meningkatkan congestion window secara bertahap ketika kondisi jaringan memungkinkan dan menguranginya ketika terdapat tanda kemacetan.

Pada model TCP Reno sederhana:
- Slow Start meningkatkan congestion window secara eksponensial per RTT hingga mencapai ambang atau mendeteksi congestion.
- Congestion Avoidance melakukan peningkatan lebih lambat, secara aditif.
- Multiplicative decrease mengurangi congestion window saat terjadi tanda kemacetan.

Detail respons terhadap loss bergantung pada varian TCP. Jangan menganggap seluruh implementasi modern mengikuti satu perilaku yang persis sama.

## 2.10. Delay jaringan

Total delay end-to-end dapat diuraikan menjadi:

\[
d_{\text{total}}
=d_{\text{trans}}
+d_{\text{prop}}
+d_{\text{proc}}
+d_{\text{queue}}
\]

**Transmission delay:**

\[
d_{\text{trans}}=\frac LR
\]

dengan \(L\) adalah panjang paket dalam bit dan \(R\) adalah laju transmisi dalam bit per detik.

**Propagation delay:**

\[
d_{\text{prop}}=\frac ds
\]

dengan \(d\) adalah jarak dan \(s\) adalah kecepatan rambat sinyal dalam media.

Processing delay muncul ketika perangkat memproses paket. Queueing delay muncul saat paket menunggu untuk dikirim.

Contoh: paket 12.000 bit dikirim melalui link berkapasitas 6 Mbps.

\[
d_{\text{trans}}=
\frac{12.000}{6.000.000}
=0{,}002\text{ detik}
\]

Jadi transmission delay-nya adalah 2 milidetik. Hasil tersebut belum memasukkan propagation, processing, atau queueing delay.

## 2.11. Protokol lapisan aplikasi

### DNS

DNS menerjemahkan nama domain ke informasi jaringan, termasuk alamat IP.

Jenis record yang perlu dikenali:
- `A`: alamat IPv4.
- `AAAA`: alamat IPv6.
- `CNAME`: nama alias.
- `MX`: server penerima email domain.
- `NS`: name server untuk zona DNS.

Resolusi DNS dapat melibatkan cache, resolver rekursif, root server, server TLD, dan authoritative server.

### HTTP

HTTP adalah protokol komunikasi aplikasi yang banyak digunakan dalam web.

- HTTP/1.1 mendukung koneksi persisten.
- HTTP/2 mendukung multiplexing beberapa stream melalui satu koneksi TCP.
- HTTP/3 menggunakan QUIC di atas UDP dan mengurangi masalah head-of-line blocking pada lapisan transport yang dapat terjadi pada multiplexing HTTP/2 di atas TCP.

Untuk ujian, pahami fungsi setiap versi dan perbedaan mekanisme transportnya, bukan hanya nomor versinya.

## 2.12. Socket programming

Socket menyediakan antarmuka bagi program untuk melakukan komunikasi jaringan.

Pada TCP server, alur umum ialah:

`socket()` → `bind()` → `listen()` → `accept()` → `send()/recv()` → `close()`

Pada TCP client:

`socket()` → `connect()` → `send()/recv()` → `close()`

Untuk UDP, komunikasi lazim menggunakan `sendto()` dan `recvfrom()` tanpa urutan `listen()` dan `accept()` sebagaimana server TCP.

Alamat IP dan port bersama-sama mengidentifikasi endpoint komunikasi tertentu.

## 2.13. Dasar keamanan jaringan

Keamanan jaringan mencakup kerahasiaan, integritas, autentikasi, serta pengendalian akses.

Konsep penting:
- **TLS:** melindungi komunikasi menggunakan mekanisme kriptografi.
- **Firewall:** menyaring lalu lintas berdasarkan aturan kebijakan.
- **NAT:** menerjemahkan alamat jaringan antarruang pengalamatan.
- **VPN:** membentuk koneksi logis yang terlindungi melalui infrastruktur lain.

NAT bukan pengganti firewall, sedangkan VPN tidak otomatis menjamin keamanan seluruh aplikasi pada perangkat pengguna.

### Target penguasaan Jaringan Komputer

Anda perlu mampu:
1. Menjelaskan fungsi tujuh layer OSI.
2. Menghitung subnet, network address, dan broadcast address.
3. Membedakan RIP, OSPF, dan BGP.
4. Menjelaskan TCP, UDP, handshake, flow control, dan congestion control.
5. Menghitung komponen delay.
6. Menjelaskan DNS, HTTP, socket, TLS, firewall, NAT, dan VPN.

---

# 3. MANAJEMEN BASIS DATA

Sumber: [Rangkuman Manajemen Basis Data](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/Manajemen_Basis_Data/RANGKUMAN_MATERI.md)

Pada Semester 3, Basis Data membahas model relasional, ERD, SQL, normalisasi, serta dasar transaksi. Manajemen Basis Data memperluasnya dengan mempelajari mekanisme internal DBMS untuk mengoptimalkan query, mengatur transaksi konkuren, mengelola indeks, dan memulihkan data setelah kegagalan.

Mata kuliah ini penting untuk memahami mengapa query yang hasilnya sama dapat memiliki waktu eksekusi sangat berbeda, serta bagaimana data tetap konsisten ketika banyak pengguna mengaksesnya bersamaan.

## 3.1. Stored procedure dan user-defined function

Stored procedure adalah kumpulan instruksi yang disimpan dalam server basis data dan dapat dipanggil oleh aplikasi atau proses lain.

User-defined function (UDF) adalah fungsi yang didefinisikan pengguna dan dapat dipakai sebagai bagian dari ekspresi SQL sesuai kemampuan DBMS yang digunakan.

Perbedaan umum:

| Aspek | Stored procedure | Function |
|---|---|---|
| Tujuan | Melaksanakan rangkaian operasi | Menghasilkan nilai atau hasil fungsi |
| Pemanggilan | Melalui mekanisme procedure, misalnya `CALL` pada DBMS yang mendukungnya | Dapat digunakan sebagai bagian ekspresi SQL sesuai DBMS |
| Output | Dapat menggunakan parameter output atau result set sesuai DBMS | Jenis nilai balik mengikuti deklarasinya |
| Penggunaan | Operasi bisnis dan proses database | Perhitungan atau transformasi data |

Kelebihan keduanya mencakup pemusatan logika, penggunaan kembali, dan potensi pengurangan jumlah komunikasi klien–server.

Namun, menyimpan logika di database bukan otomatis jaminan bebas SQL injection. Pencegahan tetap membutuhkan parameterisasi, hak akses yang tepat, dan desain yang aman.

## 3.2. Database trigger

Trigger adalah prosedur yang otomatis dijalankan ketika kejadian tertentu terjadi pada tabel atau objek database.

Pemicu yang umum:
- `INSERT`.
- `UPDATE`.
- `DELETE`.

Trigger dapat dijalankan sebelum atau sesudah operasi, tergantung jenis trigger yang didukung DBMS.

**BEFORE trigger** dapat digunakan untuk validasi atau transformasi nilai sebelum perubahan diterapkan.

**AFTER trigger** dapat digunakan untuk pencatatan audit atau operasi lanjutan setelah perubahan.

Pada banyak DBMS, `OLD` merujuk ke nilai sebelum operasi dan `NEW` merujuk ke nilai baru. Detail penggunaan bergantung pada jenis operasi dan DBMS.

Trigger perlu dirancang dengan hati-hati karena logika tersembunyi di sisi database bisa menyulitkan debugging dan memengaruhi kinerja transaksi.

## 3.3. Penyimpanan fisik dan buffer manager

DBMS biasanya memindahkan data antara media penyimpanan sekunder dan RAM melalui blok atau halaman yang disebut *page*.

Buffer manager mengelola halaman database yang berada di memori dan menentukan halaman yang dipertahankan atau diganti ketika ruang buffer terbatas.

Kebijakan penggantian yang perlu dikenali:
- **LRU:** mengutamakan penggantian halaman yang paling lama tidak diakses.
- **Clock:** menggunakan struktur penanda dan pengulangan penelusuran halaman untuk memperkirakan kebutuhan penggantian secara efisien.

Kinerja database sangat dipengaruhi biaya I/O. Query yang memerlukan banyak pembacaan disk dapat jauh lebih lambat daripada query yang kebutuhan datanya sudah tersedia di buffer.

## 3.4. Indeks B+ Tree

B+ Tree merupakan indeks berbentuk pohon seimbang yang banyak digunakan untuk query dengan kondisi kesetaraan maupun rentang.

Karakteristik utama:
- Simpul internal menyimpan kunci pemisah dan penunjuk ke subtree.
- Nilai indeks serta penunjuk record atau referensi data berada pada leaf node.
- Leaf node terhubung dalam urutan nilai sehingga range scan dapat berlangsung efisien.
- Pohon dipertahankan agar tingginya relatif kecil dibandingkan jumlah entri.

Misalnya, query:

```sql
SELECT *
FROM Pegawai
WHERE gaji BETWEEN 5000000 AND 10000000;
```

Indeks B+ Tree pada kolom `gaji` dapat membantu menemukan posisi awal rentang, lalu menelusuri entri terkait pada leaf node.

Pencarian awal dapat diperkirakan O(log n), sementara penelusuran hasil rentang memerlukan waktu tambahan sesuai banyaknya entri yang ditemukan. Pada model sederhana, pencarian rentang dapat dijelaskan sebagai O(log n + k), dengan \(k\) sebagai jumlah entri hasil.

### Penyisipan dan split

Jika node penuh ketika kunci baru dimasukkan, node dapat dibagi menjadi beberapa bagian dan informasi pemisah diteruskan ke parent. Jika parent juga penuh, split dapat berlanjut hingga tingkat akar.

Hal ini menjaga keseimbangan tinggi pohon.

## 3.5. Hash index dan hashing dinamis

Indeks hash menggunakan fungsi hash untuk memetakan kunci ke lokasi penyimpanan.

Hashing sangat sesuai untuk pencarian berbasis kesetaraan, tetapi umumnya tidak seefektif B+ Tree untuk pencarian rentang yang terurut.

Materi ini juga mencakup:
- Static hashing.
- Extendible hashing.
- Linear hashing.

Static hashing menggunakan struktur dan ruang bucket yang relatif tetap, sedangkan extendible dan linear hashing menyediakan metode pengembangan struktur ketika kebutuhan data bertambah.

Perlu dipahami bahwa collision atau overflow bucket dapat memengaruhi kinerja. Hash index juga tidak otomatis mempercepat seluruh query, karena manfaatnya bergantung pada kondisi pencarian dan rencana eksekusi.

## 3.6. Query optimization

DBMS dapat mengubah strategi eksekusi query tanpa mengubah hasil logisnya.

Query optimizer memperkirakan biaya berbagai rencana berdasarkan informasi seperti ukuran tabel, statistik distribusi, indeks yang tersedia, dan jumlah baris hasil perantara.

### Push selection down

Operator seleksi \(\sigma\) didorong sedekat mungkin ke tabel sumber sehingga baris yang tidak relevan dibuang sebelum operasi yang lebih mahal.

### Push projection down

Operator proyeksi \(\pi\) membatasi kolom yang dipertahankan sehingga ukuran data perantara dapat dikurangi.

### Reordering joins

Urutan join dapat diatur agar intermediate result yang dihasilkan lebih kecil atau operasi berikutnya lebih efisien.

Tiga strategi optimasi query ini bertujuan mengurangi jumlah data yang perlu diproses dan dipindahkan.

## 3.7. Algoritma join

Misalkan terdapat dua tabel dengan masing-masing \(M\) dan \(N\) baris.

### Nested Loop Join

Memeriksa pasangan baris dari dua relasi dengan mekanisme loop bersarang.

Kompleksitas perbandingan sederhana dapat mencapai:

\[
O(MN)
\]

Nested Loop Join dapat efektif jika tabel luar kecil atau tersedia indeks yang sesuai pada tabel bagian dalam.

### Block Nested Loop Join

Membaca tabel luar dalam blok untuk menggunakan buffer dengan lebih efisien dan mengurangi frekuensi akses I/O.

### Sort-Merge Join

Mengurutkan kedua relasi berdasarkan atribut join, kemudian menelusuri hasil pengurutan untuk mencari pasangan yang sesuai.

Jika diperlukan pengurutan penuh, biaya dapat diperkirakan:

\[
O(M\log M+N\log N)
\]

dengan biaya tambahan untuk membaca kedua relasi dan menangani hasil join.

### Hash Join

Membangun struktur hash dari salah satu input lalu mencari pasangan yang sesuai dari input lain.

Pada asumsi hash yang baik, ukuran data yang sesuai, dan jumlah operasi I/O yang dapat dikelola, biaya komputasinya dapat mendekati:

\[
O(M+N)
\]

Biaya aktual tetap dipengaruhi memori, distribusi data, dan kebutuhan partisi jika tabel tidak muat seluruhnya di RAM.

## 3.8. Transaksi dan ACID

Empat properti ACID:

**Atomicity** memastikan operasi transaksi berhasil seluruhnya atau dibatalkan sebagai unit.

**Consistency** menjaga agar transaksi memindahkan database dari keadaan valid ke keadaan valid sesuai aturan integritas.

**Isolation** mengendalikan pengaruh transaksi yang berjalan bersamaan.

**Durability** memastikan perubahan yang telah di-commit tetap bertahan sesuai jaminan pemulihan DBMS.

Contoh: pemindahan saldo harus mempertahankan aturan bahwa total saldo tidak berubah akibat transfer yang berhasil, jika tidak ada biaya atau operasi lain yang memengaruhinya.

Jika sistem mengalami kegagalan di tengah transfer, mekanisme recovery memastikan tidak ada transaksi setengah selesai yang merusak konsistensi.

## 3.9. Anomali konkurensi

Ketika transaksi berjalan bersamaan, beberapa masalah dapat terjadi.

**Dirty read:** transaksi membaca perubahan transaksi lain yang belum di-commit, kemudian perubahan tersebut dibatalkan.

**Non-repeatable read:** pembacaan ulang terhadap baris yang sama memberikan nilai berbeda karena transaksi lain telah mengubahnya.

**Phantom read:** query yang sama atas suatu rentang baris menghasilkan himpunan baris berbeda karena ada transaksi lain yang menambah atau menghapus baris yang cocok.

Tingkat isolasi transaksi mengatur fenomena apa yang dapat terjadi sesuai jaminan implementasi DBMS.

## 3.10. Conflict serializability dan precedence graph

Dua operasi dari transaksi berbeda berkonflik jika mengakses item data yang sama dan setidaknya salah satunya merupakan operasi write.

Pasangan konflik meliputi:
- Read–Write.
- Write–Read.
- Write–Write.

Read–Read tidak berkonflik dalam pengujian conflict serializability klasik karena keduanya tidak mengubah nilai item tersebut.

Precedence graph dibangun dengan:
- Satu simpul untuk setiap transaksi.
- Sisi \(T_i\rightarrow T_j\) ketika operasi transaksi \(T_i\) mendahului operasi berkonflik milik \(T_j\).

Teorema penting:

**Suatu jadwal conflict-serializable jika dan hanya jika precedence graph-nya tidak mempunyai siklus.**

Contoh: jika graf memiliki hubungan \(T_1\rightarrow T_2\) dan \(T_2\rightarrow T_1\), graf mempunyai siklus. Jadwal tersebut tidak conflict-serializable.

## 3.11. Two-Phase Locking (2PL)

2PL mengatur perolehan dan pelepasan lock dalam dua fase:

**Growing phase:** transaksi dapat memperoleh lock baru, tetapi tidak melepaskan lock yang sudah diperoleh.

**Shrinking phase:** transaksi melepaskan lock, tetapi tidak memperoleh lock baru.

Strict 2PL mempertahankan lock eksklusif sampai transaksi commit atau abort. Pendekatan ini membantu menghindari cascading rollback akibat transaksi lain membaca perubahan yang belum commit.

Namun, locking dapat menyebabkan deadlock apabila transaksi saling menunggu lock yang dipegang satu sama lain.

## 3.12. Deadlock handling

Wait-for graph menggambarkan hubungan tunggu ant ar transaksi.

- Simpul merepresentasikan transaksi.
- Sisi \(T_i\rightarrow T_j\) menunjukkan \(T_i\) menunggu sumber daya yang dipegang \(T_j\).

Dalam model wait-for graph untuk lock database, siklus menunjukkan adanya deadlock.

Dua protokol pencegahan yang perlu dibedakan:

**Wait-die:** transaksi yang lebih tua boleh menunggu transaksi lebih muda, sedangkan transaksi lebih muda yang meminta lock milik transaksi lebih tua dibatalkan.

**Wound-wait:** transaksi lebih tua dapat membatalkan transaksi lebih muda yang menghalangi permintaannya; transaksi lebih muda dapat menunggu transaksi lebih tua.

Keduanya memakai timestamp untuk menentukan urutan usia transaksi.

## 3.13. MVCC dan recovery

**Multi-Version Concurrency Control (MVCC)** memungkinkan DBMS mempertahankan beberapa versi data agar pembacaan dapat menggunakan versi yang sesuai dengan snapshot transaksi. Implementasinya berbeda antar-DBMS dan tidak berarti semua konflik penulisan otomatis hilang.

### Write-Ahead Logging (WAL)

Prinsip utama WAL adalah log perubahan harus disimpan secara persisten sesuai urutan yang diwajibkan sebelum halaman data terkait ditulis ke media penyimpanan.

Log juga harus memenuhi ketentuan durability sebelum commit dianggap berhasil.

### ARIES

ARIES adalah algoritma recovery yang menggunakan log dan pendekatan pemulihan terstruktur.

Tiga tahap utama:

**1. Analysis:** menentukan transaksi aktif dan halaman kotor berdasarkan log serta checkpoint.

**2. Redo:** mengulang perubahan yang diperlukan agar keadaan database kembali ke kondisi yang mencerminkan riwayat log sebelum kegagalan.

**3. Undo:** membatalkan perubahan transaksi yang tidak commit.

ARIES menggunakan compensation log records untuk mencatat pekerjaan undo dan mendukung pemulihan yang benar apabila terjadi kegagalan lagi.

### Target penguasaan Manajemen Basis Data

Anda perlu mampu:
1. Menjelaskan procedure, function, dan trigger.
2. Membedakan B+ Tree dengan hash index.
3. Membandingkan algoritma join.
4. Menjelaskan strategi query optimization.
5. Memeriksa conflict serializability menggunakan precedence graph.
6. Memahami 2PL, Strict 2PL, dan deadlock handling.
7. Menjelaskan MVCC, WAL, dan fase recovery ARIES.

---

# 4. PEMROGRAMAN BERORIENTASI OBJEK (PBO)

Sumber: [Rangkuman Pemrograman Berorientasi Objek](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/Pemrograman_Berorientasi_Objek/RANGKUMAN_MATERI.md)

Pemrograman Berorientasi Objek mengorganisasi program menjadi kelas dan objek yang menggabungkan atribut serta perilaku.

Repo Anda menggunakan Java sebagai bahasa implementasi utama untuk materi ini.

Misalnya, sistem akademik mempunyai objek Mahasiswa. Objek tersebut memiliki keadaan berupa NIM, nama, dan IPK, serta perilaku seperti memperbarui data atau menghitung informasi tertentu.

## 4.1. Class dan object

**Class** adalah definisi atau cetak biru yang mendeskripsikan atribut dan metode.

**Object** merupakan instans dari sebuah class.

Tiga karakteristik objek:

**State:** nilai atribut yang menggambarkan kondisi objek.

**Behavior:** tindakan yang dapat dilakukan objek melalui metode.

**Identity:** identitas yang membedakan satu objek dengan objek lain, bahkan ketika nilai atributnya sama.

Contoh Java:

```java
class Mahasiswa {
    String nama;
    double ipk;

    void tampilkanData() {
        System.out.println(nama + " - " + ipk);
    }
}
```

Penggunaan:

```java
Mahasiswa m = new Mahasiswa();
m.nama = "Andi";
m.ipk = 3.75;
m.tampilkanData();
```

Contoh tersebut masih memungkinkan akses langsung ke atribut; desain yang lebih baik untuk banyak kasus menggunakan enkapsulasi.

## 4.2. Enkapsulasi

Enkapsulasi membatasi akses langsung terhadap detail internal objek.

Atribut yang sensitif biasanya dibuat `private`, lalu akses diberikan melalui metode yang diperlukan.

```java
class Rekening {
    private double saldo;

    public double getSaldo() {
        return saldo;
    }

    public void setor(double jumlah) {
        if (jumlah > 0) {
            saldo += jumlah;
        }
    }
}
```

Dengan desain ini, program di luar class tidak dapat langsung mengatur saldo melalui assignment sembarangan. Nilai saldo diubah melalui operasi yang menerapkan validasi.

Access modifier Java yang perlu diingat:

| Modifier | Akses umum |
|---|---|
| `private` | Di dalam class terkait |
| Package-private | Dalam package yang sama |
| `protected` | Dalam package dan subclass sesuai aturan Java |
| `public` | Dapat diakses dari konteks luar yang memenuhi aturan akses |

Tujuan enkapsulasi bukan sekadar membuat getter dan setter, melainkan menjaga validitas keadaan objek serta mengendalikan cara data dimodifikasi.

## 4.3. Relasi antarobjek

PBO dan UML mengenal beberapa bentuk hubungan antarkelas.

**Dependency** adalah ketergantungan penggunaan, misalnya objek memanggil layanan objek lain untuk suatu operasi.

**Association** merupakan hubungan struktural antara dua kelas yang saling berinteraksi.

**Aggregation** menggambarkan hubungan whole–part yang relatif longgar. Bagian tetap dapat memiliki siklus hidup mandiri meskipun objek keseluruhannya tidak ada.

**Composition** menggambarkan hubungan whole–part yang lebih kuat. Dalam model tersebut, siklus hidup bagian terikat pada objek pemilik.

**Inheritance** menunjukkan hubungan *is-a* antara subclass dan superclass.

Contoh:
- Dosen menggunakan Printer merupakan contoh dependency.
- Mahasiswa mengikuti MataKuliah dapat dimodelkan sebagai association.
- Departemen mempunyai Dosen dapat dimodelkan sebagai aggregation jika dosen tetap ada secara mandiri.
- Rumah tersusun atas Ruangan dapat dimodelkan sebagai composition sesuai asumsi model.
- Lingkaran merupakan Bentuk merupakan inheritance.

Pemilihan relasi bergantung pada makna domain, bukan hanya pada kemudahan menulis kode.

## 4.4. Inheritance

Inheritance memungkinkan subclass mewarisi atribut dan metode superclass.

Di Java, pewarisan kelas menggunakan `extends`.

```java
class Bentuk {
    void gambar() {
        System.out.println("Menggambar bentuk");
    }
}

class Lingkaran extends Bentuk {
    @Override
    void gambar() {
        System.out.println("Menggambar lingkaran");
    }
}
```

Subclass dapat menambahkan perilaku atau mengganti implementasi metode warisan sesuai aturan overriding.

Java tidak mendukung pewarisan multiple inheritance antar-class. Namun, sebuah class dapat mengimplementasikan beberapa interface.

Konstruktor superclass dapat dipanggil melalui `super(...)`. Dalam aturan Java, explicit constructor invocation seperti `super(...)` atau `this(...)` harus berada di posisi awal konstruktor. Jika tidak dituliskan, Java biasanya menyisipkan pemanggilan konstruktor tanpa argumen superclass apabila tersedia.

## 4.5. Abstract class dan interface

Keduanya membantu mendeskripsikan kontrak dan abstraksi.

**Abstract class** dapat memiliki atribut instance, constructor, metode konkret, dan metode abstrak. Class ini tidak dapat dibuat menjadi objek secara langsung.

**Interface** terutama mendefinisikan kontrak kemampuan atau operasi yang dapat diimplementasikan oleh berbagai class.

Perbandingan:

| Aspek | Abstract class | Interface |
|---|---|---|
| Tujuan umum | Berbagi keadaan dan implementasi dalam satu hierarki | Mendefinisikan kontrak kemampuan |
| Constructor | Ada | Tidak ada |
| Atribut instance | Dapat memiliki | Tidak memiliki instance field biasa; field yang dideklarasikan adalah konstanta `public static final` |
| Implementasi metode | Metode konkret dan abstrak | Metode abstrak serta metode `default` atau `static` sesuai fitur Java |
| Hubungan pewarisan | Class hanya memiliki satu superclass langsung | Class dapat mengimplementasikan beberapa interface |

Gunakan abstract class ketika subclass perlu mewarisi perilaku atau keadaan yang berhubungan erat. Gunakan interface ketika Anda ingin menyatakan kemampuan yang dapat dimiliki berbagai tipe objek.

## 4.6. Polimorfisme

Polimorfisme memungkinkan satu nama operasi digunakan pada konteks atau objek berbeda.

### Method overloading

Beberapa metode memiliki nama yang sama tetapi daftar parameter berbeda.

```java
int tambah(int a, int b) {
    return a + b;
}

double tambah(double a, double b) {
    return a + b;
}
```

Keduanya mempunyai nama `tambah`, tetapi tanda tangan parameternya berbeda.

Perbedaan return type saja tidak cukup untuk membuat overloading.

### Method overriding

Subclass mengganti implementasi metode yang diwarisi dengan signature yang sesuai.

```java
Bentuk b = new Lingkaran();
b.gambar();
```

Jika `gambar()` dioverride dan objek sebenarnya adalah `Lingkaran`, implementasi `Lingkaran` yang dipanggil melalui dynamic dispatch.

Konsep ini mendukung desain fleksibel: fungsi yang bekerja dengan tipe umum `Bentuk` dapat menerima berbagai subclass tanpa perlu mengetahui seluruh detail implementasinya.

## 4.7. Upcasting dan downcasting

**Upcasting** mengubah referensi subclass menjadi referensi superclass. Ini umumnya dilakukan secara otomatis.

**Downcasting** mencoba mengubah referensi superclass ke tipe subclass yang lebih spesifik. Operasi ini harus sesuai dengan jenis objek sebenarnya.

```java
if (b instanceof Lingkaran) {
    Lingkaran l = (Lingkaran) b;
}
```

Pemeriksaan `instanceof` membantu menghindari `ClassCastException` saat objek tidak cocok dengan tipe tujuan.

## 4.8. Exception handling

Exception handling memungkinkan program menangani kondisi abnormal tanpa langsung menghentikan keseluruhan alur secara tak terkendali.

Struktur umumnya:

```java
try {
    // Operasi yang dapat menghasilkan exception
} catch (Exception e) {
    // Penanganan kondisi
} finally {
    // Pekerjaan pembersihan jika diperlukan
}
```

`try` menampung operasi yang berpotensi gagal, `catch` menangani jenis exception tertentu, sedangkan `finally` digunakan untuk pekerjaan yang perlu dilakukan setelah alur try/catch selesai dalam keadaan normal maupun exception, dengan memperhatikan pengecualian pada terminasi proses.

### Checked dan unchecked exception

**Checked exception** harus ditangani atau dideklarasikan melalui `throws` sesuai aturan compiler.

**Unchecked exception** merupakan exception dalam keluarga `RuntimeException` dan turunannya, yang tidak diwajibkan oleh compiler untuk ditangani menggunakan `try-catch`.

Contoh:
- `IOException` adalah checked exception.
- `NullPointerException` dan `ArrayIndexOutOfBoundsException` adalah unchecked exception.

`Error`, seperti kegagalan sumber daya internal tertentu pada JVM, berbeda dari exception biasa dan umumnya tidak ditangani oleh logika aplikasi rutin.

### Assertion

Assertion dapat digunakan untuk memeriksa asumsi internal programmer saat pengujian.

Contoh:

```java
assert umur >= 0 : "Umur tidak boleh negatif";
```

Assertion Java biasanya perlu diaktifkan dengan opsi `-ea`. Assertion bukan pengganti validasi input pengguna yang harus tetap aktif dalam produksi.

## 4.9. Generics dan Java Collections

Generics memberikan parameter tipe sehingga struktur data dapat digunakan kembali dengan pemeriksaan tipe yang lebih kuat saat kompilasi.

Contoh:

```java
List<String> nama = new ArrayList<>();
nama.add("Rina");
```

Dengan `List<String>`, daftar tersebut dimaksudkan untuk menampung String sehingga kesalahan tipe dapat dicegah lebih awal.

Java Collections Framework menyediakan beberapa tipe penting.

### List

List mempertahankan urutan dan dapat menyimpan elemen duplikat.

- `ArrayList`: akses berdasarkan indeks umumnya O(1); penambahan di akhir diamortisasi O(1).
- `LinkedList`: mendukung operasi pada ujung list secara efisien; akses berdasarkan indeks membutuhkan traversal.

### Set

Set tidak mengizinkan elemen duplikat menurut aturan kesetaraan yang digunakan.

- `HashSet`: pencarian dan penambahan rata-rata O(1) pada kondisi hash yang baik.
- `TreeSet`: mempertahankan elemen dalam urutan yang ditentukan, dengan operasi umum O(log n).

### Map

Map menyimpan pemetaan key–value dengan kunci unik.

- `HashMap`: akses rata-rata mendekati O(1) pada kondisi hash yang baik.
- `TreeMap`: mengurutkan kunci dan biasanya mempunyai operasi dasar O(log n).

Klaim kompleksitas tersebut merupakan karakteristik umum, bukan jaminan untuk seluruh kondisi implementasi atau input.

## 4.10. Serialisasi dan persistensi objek

Serialisasi mengubah keadaan atau graf objek menjadi representasi yang dapat disimpan atau dikirim, misalnya byte stream.

Dalam serialisasi Java klasik, kelas biasanya mengimplementasikan `Serializable`.

Kata kunci `transient` menandai field yang tidak diserialisasikan melalui mekanisme default Java serialization.

`serialVersionUID` membantu memeriksa kompatibilitas versi kelas saat deserialisasi.

Serialisasi perlu diterapkan dengan hati-hati. Data yang disimpan harus dikendalikan, dan deserialisasi sumber tidak tepercaya bisa menimbulkan risiko keamanan.

## 4.11. Prinsip desain SOLID

SOLID merupakan lima prinsip desain untuk membantu membangun perangkat lunak yang modular dan mudah dipelihara.

**S — Single Responsibility Principle (SRP)**

Satu class sebaiknya memiliki satu tanggung jawab utama atau satu alasan utama untuk berubah.

Contoh: pemrosesan pembayaran sebaiknya tidak digabung begitu saja dengan pembuatan laporan dan pengiriman email dalam satu class yang besar.

**O — Open/Closed Principle (OCP)**

Komponen dirancang agar dapat diperluas tanpa harus terus-menerus mengubah kode inti yang sudah stabil.

Penerapan polymorphism dan interface dapat membantu tujuan ini.

**L — Liskov Substitution Principle (LSP)**

Objek subclass harus dapat menggantikan superclass tanpa melanggar kontrak atau menyebabkan perilaku program yang tidak benar.

**I — Interface Segregation Principle (ISP)**

Klien tidak seharusnya dipaksa bergantung pada operasi yang tidak digunakannya. Beberapa interface kecil sering lebih baik daripada satu interface besar yang tidak cocok untuk seluruh implementasi.

**D — Dependency Inversion Principle (DIP)**

Modul tingkat tinggi dan tingkat rendah sebaiknya bergantung pada abstraksi, bukan saling terikat langsung secara berlebihan.

Contohnya, layanan pembayaran dapat bergantung pada interface `PaymentGateway`, bukan secara langsung bergantung pada satu kelas penyedia pembayaran tertentu.

### Target penguasaan PBO

Anda perlu mampu:
1. Membuat dan menggunakan class serta object.
2. Menjelaskan enkapsulasi, inheritance, abstraction, dan polymorphism.
3. Membedakan association, aggregation, dan composition.
4. Menulis kode overriding, overloading, interface, serta abstract class.
5. Menjelaskan checked dan unchecked exception.
6. Memilih `List`, `Set`, atau `Map` sesuai kebutuhan.
7. Mengidentifikasi pelanggaran SOLID dan mengusulkan perbaikannya.

---

# 5. REKAYASA PERANGKAT LUNAK (RPL)

Sumber: [Rangkuman Rekayasa Perangkat Lunak](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/Rekayasa_Perangkat_Lunak/RANGKUMAN_MATERI.md)

Rekayasa Perangkat Lunak adalah disiplin teknik untuk mengembangkan perangkat lunak secara sistematis. Tujuannya bukan sekadar membuat program berjalan, melainkan memastikan hasilnya sesuai kebutuhan, dapat diuji, dapat dipelihara, dan dapat dikembangkan sesuai perubahan kebutuhan.

## 5.1. Software Development Life Cycle (SDLC)

SDLC menjelaskan tahapan pengembangan perangkat lunak dari perumusan kebutuhan hingga pemeliharaan.

Tahapan yang umum:
1. Memahami kebutuhan.
2. Menganalisis dan merencanakan sistem.
3. Mendesain arsitektur dan komponen.
4. Mengimplementasikan kode.
5. Menguji kualitas.
6. Melakukan deployment.
7. Memelihara dan memperbaiki perangkat lunak.

Urutan dan pembagian tahap bergantung model SDLC yang digunakan.

## 5.2. Waterfall

Waterfall menggunakan pendekatan yang relatif berurutan. Setiap fase diselesaikan dan disetujui sebelum melanjutkan ke fase berikutnya.

Kelebihan:
- Tahapan dan dokumentasi jelas.
- Kemajuan mudah dipantau melalui deliverable formal.
- Cocok ketika kebutuhan relatif stabil dan dapat dipahami sejak awal.

Kekurangan:
- Perubahan kebutuhan dapat mahal ketika fase berikutnya sudah berjalan.
- Kesalahan dalam memahami kebutuhan sejak awal bisa berdampak hingga akhir proyek.
- Umpan balik produk akhir datang relatif terlambat jika tidak disertai prototipe atau validasi dini.

## 5.3. Agile dan Scrum

Agile merupakan pendekatan pengembangan adaptif yang mengutamakan kolaborasi, umpan balik, dan pengiriman perangkat lunak yang berfungsi.

Scrum adalah salah satu kerangka kerja yang menerapkan prinsip tersebut melalui pekerjaan iteratif.

Peran utama:
- **Product Owner:** memaksimalkan nilai produk dan mengelola prioritas Product Backlog.
- **Scrum Master:** membantu tim menjalankan Scrum, memfasilitasi kolaborasi, dan membantu mengatasi hambatan.
- **Developers:** membangun increment yang memenuhi kriteria kualitas.

Aktivitas penting:
- Sprint Planning.
- Daily Scrum.
- Sprint Review.
- Sprint Retrospective.

Artefak penting:
- Product Backlog.
- Sprint Backlog.
- Increment.

Durasi sprint biasanya konsisten dan tidak lebih dari satu bulan menurut Scrum Guide modern. Scrum tidak identik dengan metode tanpa dokumentasi; dokumentasi tetap diperlukan selama mendukung produk, pengambilan keputusan, dan pemeliharaan.

## 5.4. V-Model dan Spiral

**V-Model** menghubungkan fase spesifikasi dan desain dengan tingkat pengujian yang sesuai.

Contoh pemetaan:
- Kebutuhan pengguna berkaitan dengan acceptance testing.
- Spesifikasi sistem berkaitan dengan system testing.
- Desain arsitektur berkaitan dengan integration testing.
- Desain modul berkaitan dengan unit testing.

Ide utamanya adalah perencanaan pengujian dipertimbangkan sejak fase pengembangan, bukan hanya setelah implementasi selesai.

**Spiral Model** mengembangkan perangkat lunak melalui putaran berulang dengan perhatian khusus terhadap identifikasi serta pengelolaan risiko. Model ini berguna untuk proyek yang ketidakpastian atau risikonya tinggi.

## 5.5. Requirements Engineering

Requirements Engineering mengumpulkan, menganalisis, mendokumentasikan, dan memvalidasi kebutuhan sistem.

Tahapan yang umum meliputi:
- Inception: memahami konteks dan masalah.
- Elicitation: menggali kebutuhan dari stakeholder.
- Elaboration: menganalisis dan memperjelas kebutuhan.
- Specification: menuliskan kebutuhan.
- Validation: memeriksa apakah kebutuhan sudah benar dan dipahami bersama.
- Requirements management: mengelola perubahan kebutuhan.

Metode elicitation dapat meliputi wawancara, observasi, survei, workshop, dan analisis dokumen.

## 5.6. Functional requirement dan non-functional requirement

**Functional requirement (FR)** menjelaskan fungsi yang harus disediakan sistem.

Contoh: “Sistem harus memungkinkan pengguna mengatur ulang kata sandi melalui email verifikasi.”

**Non-functional requirement (NFR)** menjelaskan batasan dan atribut kualitas sistem.

Contoh:
- Waktu respons maksimal dalam kondisi beban tertentu.
- Ketersediaan layanan.
- Keamanan.
- Kemudahan penggunaan.
- Kemudahan pemeliharaan.
- Portabilitas.

Salah satu kerangka yang digunakan dalam materi adalah FURPS+:

- **F — Functionality**
- **U — Usability**
- **R — Reliability**
- **P — Performance**
- **S — Supportability**
- **+ — batasan tambahan**, misalnya antarmuka, desain, atau kebutuhan implementasi.

Persyaratan harus cukup spesifik agar dapat diverifikasi. “Sistem harus cepat” terlalu ambigu. Sebaliknya, target waktu respons dapat diukur jika beban, lingkungan, dan kondisi pengukurannya didefinisikan.

## 5.7. UML dan use case diagram

UML merupakan bahasa pemodelan untuk mendeskripsikan struktur dan perilaku sistem.

Use case diagram menampilkan:
- Aktor.
- Use case.
- Batas sistem.
- Hubungan aktor dan use case.
- Relasi antarpenggunaan ketika diperlukan.

**`<<include>>`** menunjukkan bahwa use case sumber memasukkan perilaku use case tujuan sebagai bagian wajib dari alurnya.

**`<<extend>>`** menunjukkan perilaku tambahan yang diterapkan pada kondisi tertentu terhadap use case dasar.

Contoh:
- Proses transfer uang dapat `include` autentikasi.
- Pembelian dapat `extend` penggunaan kupon jika pengguna memilih opsi tersebut.

Hubungan tersebut bukan sekadar simbol untuk menghubungkan dua aktivitas. Gunakan `include` atau `extend` sesuai makna perilaku sistem.

## 5.8. Activity diagram

Activity diagram memodelkan aliran aktivitas dalam sebuah proses.

Komponen yang perlu dikenali:
- Initial node.
- Action atau activity.
- Control flow.
- Decision dan merge node.
- Fork dan join.
- Final node.
- Swimlane.

**Decision node** memilih aliran berdasarkan kondisi.

**Merge node** menggabungkan kembali alternatif aliran.

**Fork node** membagi aliran menjadi aktivitas yang dapat berlangsung paralel.

**Join node** menyelaraskan kembali aliran paralel.

Swimlane digunakan untuk menunjukkan aktor, peran, atau bagian organisasi yang bertanggung jawab atas aktivitas.

## 5.9. Sequence diagram

Sequence diagram menjelaskan interaksi antaraktor dan objek berdasarkan urutan waktu.

Elemen utamanya:
- Lifeline.
- Activation bar.
- Message.
- Return message.
- Combined fragments seperti `alt`, `opt`, dan `loop`.

Contoh login aplikasi:
1. Pengguna mengirim permintaan login.
2. UI meneruskan kredensial ke layanan autentikasi.
3. Layanan autentikasi memeriksa data pengguna melalui repository.
4. Repository mengakses database.
5. Hasil dikirim kembali ke layanan dan UI.

Sequence diagram memperlihatkan objek mana yang saling berkomunikasi dan urutan pesan yang terjadi.

## 5.10. Class diagram

Class diagram memodelkan struktur statis sebuah sistem.

Notasi kelas biasanya berisi:
- Nama class.
- Atribut.
- Operasi atau metode.

Visibilitas UML:
- `+`: public.
- `-`: private.
- `#`: protected.
- `~`: package.

Relasi penting:
- Association.
- Aggregation.
- Composition.
- Generalization atau inheritance.
- Dependency.

Multiplicity menunjukkan jumlah instance yang diperbolehkan dalam hubungan.

Contoh:
- `1`: tepat satu.
- `0..1`: nol atau satu.
- `0..*`: nol atau banyak.
- `1..*`: minimal satu.

Class diagram perlu mencerminkan kebutuhan domain dan tidak harus menampilkan seluruh detail kode.

## 5.11. Kohesi dan kopling

Prinsip umum desain yang baik adalah **high cohesion dan loose coupling**.

**Cohesion** adalah tingkat keterkaitan elemen-elemen di dalam satu modul. Kohesi tinggi berarti elemen tersebut bekerja sama untuk menjalankan tugas yang jelas.

**Coupling** adalah tingkat ketergantungan antarmodul. Kopling yang longgar mempermudah perubahan pada satu modul tanpa memaksa banyak modul lain berubah.

Contoh desain buruk adalah sebuah class besar yang menangani autentikasi, pembayaran, laporan, akses database, dan pengiriman email tanpa pemisahan tanggung jawab.

Contoh desain lebih baik adalah memisahkan komponen berdasarkan tanggung jawab dan berkomunikasi melalui kontrak yang terdefinisi.

## 5.12. Arsitektur perangkat lunak

### Monolitik

Aplikasi dibangun sebagai satu unit deployment utama.

Kelebihannya adalah struktur awal dapat lebih sederhana. Namun, proyek yang berkembang besar membutuhkan pemisahan internal yang baik agar pemeliharaan tidak menjadi sulit.

### Layered architecture

Aplikasi dipisahkan menjadi lapisan menurut tanggung jawab.

Contoh:
- Presentation.
- Application atau service.
- Domain/business logic.
- Data access.

### Model–View–Controller (MVC)

- **Model:** data dan aturan domain yang relevan.
- **View:** penyajian antarmuka.
- **Controller:** menerima input dan mengoordinasikan alur aplikasi.

MVC membantu memisahkan tanggung jawab antarmuka, kontrol alur, serta data atau logika domain sesuai implementasinya.

## 5.13. Verifikasi dan validasi

Dua pertanyaan yang sering diingat:

**Verifikasi:** “Are we building the product right?” Apakah hasil dikembangkan sesuai spesifikasi dan rancangan?

**Validasi:** “Are we building the right product?” Apakah sistem yang dibuat benar-benar menjawab kebutuhan pengguna?

Keduanya penting, tetapi berbeda. Sistem dapat sesuai dokumen teknis namun tetap tidak cocok untuk kebutuhan pengguna jika dokumen atau kebutuhan awalnya salah.

## 5.14. Black-box testing

Black-box testing menguji perilaku sistem berdasarkan input dan output tanpa harus memeriksa detail implementasi internal.

### Equivalence Partitioning

Domain input dibagi menjadi kelas yang diperkirakan memberikan perilaku serupa. Test case dipilih dari kelas-kelas tersebut.

Contoh: kolom umur menerima integer dari 18 hingga 60.

Kelas dapat berupa:
- Kurang dari 18: tidak valid.
- 18 sampai 60: valid.
- Lebih dari 60: tidak valid.

### Boundary Value Analysis

Kesalahan kerap muncul di sekitar batas rentang. Nilai yang diuji dapat mencakup:

\[
\min-1,\min,\min+1,\max-1,\max,\max+1
\]

Untuk rentang valid 18 sampai 60, kandidat uji mencakup 17, 18, 19, 59, 60, dan 61.

### Decision table

Decision table memetakan kombinasi kondisi dengan tindakan yang diharapkan. Teknik ini berguna untuk aturan bisnis yang melibatkan banyak kondisi.

## 5.15. White-box testing dan cyclomatic complexity

White-box testing memeriksa struktur internal kode, seperti cabang dan jalur eksekusi.

Control Flow Graph (CFG) memodelkan instruksi sebagai node dan perpindahan alur sebagai edge.

Cyclomatic complexity mengukur kompleksitas jalur independen dalam CFG:

\[
V(G)=E-N+2P
\]

dengan:
- \(E\): jumlah edge.
- \(N\): jumlah node.
- \(P\): jumlah komponen graf yang terpisah.

Untuk satu CFG terhubung, \(P=1\), sehingga:

\[
V(G)=E-N+2
\]

Pada CFG sederhana, hasilnya juga dapat dihitung sebagai jumlah node keputusan atau predikat ditambah satu.

Contoh: kode berisi satu `if` dengan dua cabang, tanpa kondisi lain. Cyclomatic complexity dasarnya adalah 2.

Nilai tersebut membantu menentukan jumlah basis path yang diperlukan untuk pengujian struktural, tetapi tidak berarti dua test case saja selalu cukup untuk menguji seluruh persyaratan bisnis.

### Target penguasaan RPL

Anda perlu mampu:
1. Memilih model SDLC sesuai kondisi proyek.
2. Membedakan FR dan NFR.
3. Menyusun kebutuhan sistem yang terukur.
4. Membaca dan menyusun use case, activity, sequence, dan class diagram.
5. Menjelaskan kohesi, kopling, layered architecture, dan MVC.
6. Membedakan verifikasi dan validasi.
7. Membuat test case dengan equivalence partitioning dan boundary value analysis.
8. Menghitung cyclomatic complexity dari CFG sederhana.

---

# 6. SISTEM CERDAS / KECERDASAN BUATAN

Sumber: [Rangkuman Sistem Cerdas](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/Sistem_Cerdas/RANGKUMAN_MATERI.md)

Sistem Cerdas mempelajari bagaimana komputer mengambil keputusan, mencari solusi, merepresentasikan pengetahuan, melakukan penalaran dalam ketidakpastian, dan mempelajari pola dari data.

Pada semester ini, fokusnya lebih luas daripada machine learning saja. Materi juga mencakup pencarian ruang keadaan, logika simbolik, sistem pakar, fuzzy logic, dan jaringan syaraf tiruan.

## 6.1. Agen cerdas dan rational agent

Agen cerdas menerima informasi dari lingkungan melalui sensor dan menghasilkan tindakan melalui aktuator.

Agen rasional memilih tindakan yang diharapkan memberikan hasil terbaik berdasarkan ukuran kinerja, informasi yang tersedia, dan karakteristik lingkungannya.

Rasionalitas tidak selalu berarti mengetahui hasil masa depan dengan sempurna. Agen dapat mengambil keputusan rasional meskipun informasi terbatas.

## 6.2. Kerangka PEAS

PEAS membantu mendeskripsikan tugas suatu agen.

- **P — Performance Measure:** ukuran keberhasilan.
- **E — Environment:** lingkungan tempat agen beroperasi.
- **A — Actuators:** perangkat atau mekanisme untuk bertindak.
- **S — Sensors:** mekanisme untuk mengamati lingkungan.

Contoh mobil otonom:

**Performance:** keselamatan, efisiensi waktu, dan kepatuhan lalu lintas.

**Environment:** jalan, kendaraan lain, pejalan kaki, dan cuaca.

**Actuators:** kemudi, rem, dan akselerator.

**Sensors:** kamera, radar, lidar, dan GPS.

Kerangka PEAS membantu mengidentifikasi kebutuhan input dan output sebelum arsitektur agen dirancang.

## 6.3. Karakteristik lingkungan

Lingkungan AI dapat diklasifikasikan melalui beberapa pasangan konsep.

**Fully observable vs partially observable:** apakah agen memiliki informasi keadaan yang diperlukan atau hanya pengamatan parsial.

**Deterministic vs stochastic:** apakah hasil tindakan dapat diprediksi dengan pasti atau dipengaruhi ketidakpastian.

**Episodic vs sequential:** apakah keputusan tiap episode berdiri sendiri atau memengaruhi keputusan berikutnya.

**Static vs dynamic:** apakah lingkungan berubah ketika agen berpikir.

**Discrete vs continuous:** apakah keadaan dan tindakan berupa pilihan diskrit atau variabel kontinu.

**Single-agent vs multi-agent:** apakah satu agen atau banyak agen berinteraksi.

Karakteristik tersebut membantu menentukan algoritma dan representasi yang sesuai.

## 6.4. State space search

State space search memandang masalah sebagai kumpulan keadaan yang terhubung oleh tindakan.

Komponen dasarnya:
- Initial state.
- Successor function atau tindakan yang mungkin.
- Goal test.
- Path cost.
- Goal state.

Contohnya, pencarian rute dari kota asal menuju kota tujuan. Node mewakili kota, edge mewakili jalur, dan biaya edge dapat merepresentasikan jarak atau waktu.

## 6.5. Breadth-First Search (BFS)

BFS mengembangkan simpul secara melebar per tingkat.

BFS menggunakan queue dengan prinsip FIFO.

Karakteristiknya:
- Complete pada ruang keadaan dengan branching factor terbatas dan kondisi penelusuran yang sesuai.
- Optimal jika semua langkah memiliki biaya yang sama.
- Memerlukan memori yang besar; dalam analisis pencarian pohon, kebutuhan dapat tumbuh secara eksponensial terhadap kedalaman solusi.

BFS cocok untuk mencari lintasan dengan jumlah langkah minimum pada graf yang tidak berbobot.

## 6.6. Depth-First Search (DFS)

DFS menelusuri satu cabang sedalam mungkin sebelum melakukan backtracking.

DFS menggunakan stack atau struktur rekursi yang berperilaku seperti stack.

Kelebihan:
- Kebutuhan memori dapat lebih kecil daripada BFS pada model pohon tertentu.
- Dapat menemukan solusi tanpa mengeksplorasi semua simpul pada tingkat yang sama terlebih dahulu.

Kekurangan:
- Tidak menjamin solusi dengan biaya minimum.
- Pada graf dengan siklus atau jalur tak terbatas, strategi tanpa penanganan yang tepat dapat gagal mencapai solusi lain yang tersedia.

Perbedaan penting: BFS mengutamakan kedalaman terkecil, sedangkan DFS mengutamakan penelusuran cabang sedalam mungkin.

## 6.7. Uniform Cost Search (UCS)

UCS memperluas simpul dengan biaya lintasan kumulatif terkecil.

Fungsi prioritas:

\[
g(n)=\text{biaya dari awal sampai simpul }n
\]

UCS menggunakan priority queue.

Dalam kondisi biaya langkah positif atau nonnegatif dengan implementasi yang sesuai, UCS dapat menemukan solusi biaya minimum. Untuk graf berbobot nonnegatif, konsepnya berhubungan erat dengan algoritma Dijkstra.

## 6.8. Greedy Best-First Search

Greedy Best-First Search menggunakan heuristik untuk memperkirakan kedekatan simpul terhadap tujuan.

Fungsi evaluasi:

\[
f(n)=h(n)
\]

\(h(n)\) merupakan perkiraan biaya dari simpul saat ini ke tujuan.

Metode ini dapat menemukan solusi dengan cepat pada kasus yang sesuai, tetapi tidak selalu optimal karena mengabaikan biaya yang sudah dikeluarkan.

## 6.9. A* Search

A* menggabungkan biaya yang sudah dikeluarkan dengan perkiraan biaya menuju tujuan.

\[
f(n)=g(n)+h(n)
\]

- \(g(n)\): biaya dari initial state ke \(n\).
- \(h(n)\): perkiraan biaya dari \(n\) ke tujuan.
- \(f(n)\): estimasi total biaya melalui \(n\).

A* mengembangkan node dengan nilai \(f(n)\) terendah.

### Admissible heuristic

Heuristik admissible tidak pernah melebih-lebihkan biaya optimal sebenarnya untuk menuju tujuan.

\[
h(n)\leq h^*(n)
\]

dengan \(h^*(n)\) sebagai biaya optimal sejati dari \(n\) ke goal.

### Consistent heuristic

Heuristik konsisten memenuhi:

\[
h(n)\leq c(n,a,n')+h(n')
\]

untuk transisi dari \(n\) ke \(n'\) melalui aksi \(a\).

Dalam kerangka kondisi standar, admissibility mendukung optimalitas A* pada tree search, sementara consistency penting untuk sifat optimal A* graph search tanpa perlu membuka kembali node yang telah ditutup. Implementasi dan asumsi tetap perlu diperhatikan.

## 6.10. Minimax dan alpha-beta pruning

Minimax digunakan untuk permainan dengan dua pemain yang bergantian mengambil keputusan dalam model yang sesuai, seperti permainan zero-sum deterministik.

Pemain MAX berusaha memaksimalkan nilai evaluasi, sedangkan MIN berusaha meminimalkannya.

Pada setiap node:
- Node MAX memilih nilai anak terbesar.
- Node MIN memilih nilai anak terkecil.

Alpha-beta pruning mengurangi jumlah cabang yang perlu dievaluasi tanpa mengubah hasil minimax pada kondisi pencarian yang sesuai.

- \(\alpha\): nilai terbaik yang diketahui untuk MAX.
- \(\beta\): nilai terbaik yang diketahui untuk MIN.

Cabang dapat dipangkas ketika:

\[
\alpha\geq\beta
\]

Pemangkasan tersebut penting karena pohon permainan dapat tumbuh sangat cepat ketika kedalaman pencarian meningkat.

## 6.11. Representasi pengetahuan dan logika

Sistem simbolik merepresentasikan pengetahuan melalui fakta, aturan, dan hubungan logis.

Sebagai contoh:

- Jika jalan basah, maka mungkin baru terjadi hujan atau ada penyiraman.
- Jika sistem menerima bukti tambahan, sistem dapat memperbarui kesimpulan yang didukung bukti.

Dalam logika proposisional, pernyataan dapat dinyatakan sebagai simbol dan dihubungkan melalui operator seperti AND, OR, NOT, serta implikasi.

### Resolution

Resolusi digunakan untuk membuktikan entailment dalam logika dengan pendekatan refutasi.

Langkah konseptual:
1. Ambil basis pengetahuan \(KB\).
2. Tambahkan negasi dari tujuan yang ingin dibuktikan.
3. Ubah pernyataan ke Conjunctive Normal Form (CNF).
4. Terapkan aturan resolusi.
5. Jika menghasilkan klausa kosong, ditemukan kontradiksi sehingga tujuan terbukti dari basis pengetahuan menurut kerangka logika tersebut.

## 6.12. Sistem pakar

Sistem pakar meniru proses pengambilan keputusan berbasis pengetahuan yang dikumpulkan dari ahli bidang tertentu.

Komponen umumnya:
- **Knowledge base:** fakta dan aturan.
- **Working memory:** fakta kasus yang sedang dianalisis.
- **Inference engine:** mekanisme penerapan aturan.
- **Explanation facility:** membantu menjelaskan bagaimana kesimpulan diperoleh.

Aturan dapat ditulis sebagai:

`IF kondisi THEN kesimpulan`

Contoh:

`IF suhu tinggi AND kipas tidak berputar THEN periksa sistem pendingin`

Aturan tersebut merupakan ilustrasi logika sederhana, bukan diagnosis teknis yang pasti.

### Forward chaining

Forward chaining dimulai dari fakta yang tersedia dan menerapkan aturan untuk menghasilkan fakta atau kesimpulan baru.

Pendekatan ini bersifat data-driven.

### Backward chaining

Backward chaining dimulai dari hipotesis yang ingin dibuktikan, lalu mencari fakta dan aturan yang dibutuhkan untuk mendukungnya.

Pendekatan ini bersifat goal-driven.

## 6.13. Certainty Factor (CF)

Sistem berbasis aturan sering harus menghadapi keyakinan yang tidak sepenuhnya pasti.

Certainty Factor merupakan model representasi tingkat keyakinan atau ketidakpercayaan terhadap hipotesis.

\[
CF(H,E)=MB(H,E)-MD(H,E)
\]

dengan:
- \(MB\): ukuran keyakinan terhadap hipotesis.
- \(MD\): ukuran ketidakpercayaan terhadap hipotesis.

Nilai CF biasanya berada pada rentang \([-1,1]\).

Jika aturan memiliki CF dan fakta memiliki bobot keyakinan dalam model yang digunakan, propagasi sederhana dapat dinyatakan sebagai:

\[
CF(H)=CF(E)\times CF(\text{Rule})
\]

Untuk dua bukti positif yang mendukung hipotesis yang sama, salah satu rumus kombinasi yang digunakan pada model CF adalah:

\[
CF_{\text{combine}}
=CF_1+CF_2(1-CF_1)
\]

Rumus kombinasi berbeda untuk kondisi keyakinan positif, negatif, atau berlawanan tanda. Pastikan memilih rumus sesuai skenario, bukan menerapkan satu rumus ke seluruh kasus.

## 6.14. Fuzzy logic

Fuzzy logic digunakan ketika kategori linguistik tidak selalu mempunyai batas tegas.

Dalam logika Boolean, suatu pernyataan biasanya bernilai benar atau salah. Dalam fuzzy logic, tingkat keanggotaan suatu input pada himpunan fuzzy dapat berada di antara 0 dan 1.

Contoh:
- Suhu 24°C dapat memiliki derajat keanggotaan tertentu pada kategori “hangat”.
- Suhu 30°C mungkin memiliki keanggotaan lebih besar pada kategori “panas”.

Nilai keanggotaan bukan otomatis probabilitas; nilainya menyatakan derajat keanggotaan pada himpunan fuzzy.

Tiga tahap sistem inferensi fuzzy:

**Fuzzification:** mengubah input numerik menjadi derajat keanggotaan fuzzy.

**Rule evaluation:** menerapkan aturan linguistik seperti:

`IF suhu panas AND kelembapan tinggi THEN kipas cepat`

**Defuzzification:** mengubah hasil fuzzy menjadi nilai output yang tegas.

Untuk operasi fuzzy dasar:
- AND sering dimodelkan menggunakan minimum.
- OR sering dimodelkan menggunakan maksimum.

Metode yang digunakan dapat bervariasi sesuai sistem fuzzy.

## 6.15. Mamdani dan Sugeno

### Mamdani

Output aturan berupa himpunan fuzzy yang digabungkan sebelum proses defuzzifikasi.

Metode centroid atau Center of Gravity merupakan salah satu cara memperoleh output crisp:

\[
z^*=
\frac{\int z\mu_C(z)\,dz}
{\int\mu_C(z)\,dz}
\]

### Sugeno

Konsekuen aturan biasanya berupa konstanta atau fungsi matematis dari input. Hasil akhir sering dihitung melalui rata-rata berbobot:

\[
z^*=\frac{\sum_i w_i z_i}{\sum_i w_i}
\]

dengan \(w_i\) sebagai kekuatan aktivasi aturan dan \(z_i\) sebagai output konsekuen aturan.

Perbedaan pokoknya: Mamdani menghasilkan himpunan output fuzzy yang kemudian didefuzzifikasi, sedangkan Sugeno menggunakan nilai atau fungsi output yang lebih langsung untuk agregasi berbobot.

## 6.16. Jaringan Syaraf Tiruan (JST)

JST meniru sebagian ide sistem saraf biologis melalui unit komputasi yang terhubung dengan bobot.

Sebuah neuron menerima input \(x_i\), memiliki bobot \(w_i\), dan bias \(b\).

\[
z=\sum_{i=1}^n w_ix_i+b
\]

Keluaran:

\[
y=f(z)
\]

dengan \(f\) sebagai fungsi aktivasi.

### Fungsi aktivasi

**Sigmoid**

\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]

Menghasilkan nilai antara 0 dan 1.

**Tanh**

\[
\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
\]

Menghasilkan nilai antara -1 dan 1.

**ReLU**

\[
f(z)=\max(0,z)
\]

Menghasilkan nol untuk input negatif dan nilai input itu sendiri untuk input positif.

### Single-layer perceptron

Perceptron satu lapisan dapat mempelajari pemisahan kelas secara linier dalam kondisi pembelajaran yang sesuai.

Keterbatasan klasiknya adalah tidak mampu merepresentasikan fungsi yang tidak dapat dipisahkan secara linier, seperti XOR, dengan satu perceptron standar.

### Multi-Layer Perceptron (MLP)

MLP menggunakan satu atau lebih hidden layer. Lapisan-lapisan ini memungkinkan pembentukan representasi yang lebih kompleks.

Backpropagation menghitung gradien galat terhadap parameter jaringan menggunakan aturan rantai kalkulus. Gradien kemudian digunakan untuk memperbarui bobot.

Secara umum, pembaruan parameter berbasis gradient descent dapat ditulis:

\[
w_{\text{baru}}=
w_{\text{lama}}-\eta\frac{\partial E}{\partial w}
\]

dengan:
- \(\eta\): learning rate.
- \(E\): fungsi loss.
- \(\partial E/\partial w\): gradien loss terhadap bobot.

Learning rate terlalu besar dapat membuat optimasi tidak stabil, sedangkan nilai terlalu kecil dapat memperlambat pembelajaran.

### Target penguasaan Sistem Cerdas

Anda perlu mampu:
1. Menyusun deskripsi agen dengan PEAS.
2. Menelusuri BFS, DFS, UCS, Greedy, dan A*.
3. Membandingkan completeness, optimality, serta kebutuhan memori.
4. Menjalankan minimax dan menentukan cabang alpha-beta yang dipangkas.
5. Menjelaskan resolusi dan inferensi logika.
6. Membedakan forward chaining dan backward chaining.
7. Menghitung CF sederhana.
8. Menjalankan tahapan inferensi fuzzy Mamdani dan Sugeno.
9. Menghitung keluaran neuron dan menjelaskan backpropagation.

---

# 7. SINTESIS SEMESTER 4

Enam mata kuliah Semester 4 memperluas kemampuan Anda dari implementasi komponen menuju pembangunan sistem yang terstruktur.

| Bidang | Pertanyaan mendasar |
|---|---|
| Grafika dan Komputasi Visual | Bagaimana objek matematis ditampilkan atau citra dianalisis? |
| Jaringan Komputer | Bagaimana dua sistem bertukar data secara benar dan efisien? |
| Manajemen Basis Data | Bagaimana data diakses, dijaga, dan dipulihkan secara efisien? |
| PBO | Bagaimana kode disusun menjadi objek dan komponen yang modular? |
| RPL | Bagaimana sebuah produk perangkat lunak dibangun dan diuji secara sistematis? |
| Sistem Cerdas | Bagaimana komputer mencari solusi dan menghasilkan keputusan? |

## Contoh integrasi: aplikasi pemesanan daring

Bayangkan Anda membangun aplikasi pemesanan.

1. **PBO** digunakan untuk merancang class pelanggan, pesanan, pembayaran, dan produk.
2. **RPL** digunakan untuk mengumpulkan kebutuhan, membuat diagram UML, memilih arsitektur, dan menetapkan strategi pengujian.
3. **Jaringan Komputer** menjelaskan komunikasi browser dengan server melalui HTTP, pemetaan nama domain melalui DNS, serta pengiriman data melalui jaringan.
4. **Manajemen Basis Data** mengatur query, indeks, transaksi pembayaran, konkurensi, dan recovery.
5. **Sistem Cerdas** dapat menambahkan rekomendasi produk, pencarian rute, atau sistem keputusan.
6. **Grafika dan Komputasi Visual** membantu menyajikan gambar produk, visualisasi data, atau fitur pemrosesan citra.

Contoh tersebut memperlihatkan bahwa materi bukan bidang yang terpisah sepenuhnya. Sebuah aplikasi kompleks membutuhkan integrasi pengetahuan dari beberapa mata kuliah sekaligus.

---

# 8. RUMUS DAN KONSEP YANG WAJIB DIINGAT

## Grafika dan Komputasi Visual

- DDA menggunakan increment koordinat dan pembulatan.
- Bresenham menggunakan parameter keputusan bilangan bulat.
- Translasi: \(x'=x+t_x\), \(y'=y+t_y\).
- Rotasi memakai sinus dan kosinus.
- Cohen–Sutherland menggunakan outcode dan bitwise AND.
- Z-buffer membandingkan kedalaman permukaan.
- Gouraud menginterpolasi intensitas atau warna; Phong shading menginterpolasi normal.
- Konvolusi citra menerapkan kernel pada lingkungan piksel.

## Jaringan Komputer

- OSI mempunyai tujuh lapisan.
- TCP/IP lazim dijelaskan melalui model empat atau lima lapisan.
- IPv4 terdiri atas 32 bit.
- Jumlah host konvensional: \(2^{32-n}-2\).
- Nyquist: \(C=2B\log_2M\).
- Shannon–Hartley: \(C=B\log_2(1+S/N)\).
- Transmission delay: \(L/R\).
- Propagation delay: \(d/s\).
- TCP menyediakan mekanisme keandalan transport, sedangkan UDP tidak menjamin pengiriman atau urutan datagram.

## Manajemen Basis Data

- B+ Tree mendukung pencarian dan range scan.
- Hash index umumnya cocok untuk pencarian kesetaraan.
- Query optimizer dapat mendorong seleksi dan proyeksi ke bagian bawah execution tree.
- ACID: Atomicity, Consistency, Isolation, Durability.
- Conflict serializability diuji melalui precedence graph tanpa siklus.
- 2PL mempunyai growing phase dan shrinking phase.
- ARIES menggunakan analysis, redo, dan undo.

## PBO

- Class adalah definisi; object adalah instans.
- Enkapsulasi melindungi keadaan internal.
- Overloading berbeda dari overriding.
- Abstract class dapat mempunyai constructor dan atribut instance.
- Interface mendefinisikan kontrak yang dapat diimplementasikan oleh banyak class.
- List mengizinkan duplikasi; Set tidak mengizinkan duplikasi; Map menyimpan key–value.
- SOLID: SRP, OCP, LSP, ISP, dan DIP.

## RPL

- Waterfall relatif berurutan.
- Agile bersifat iteratif dan adaptif.
- FR menjelaskan fungsi; NFR menjelaskan kualitas atau batasan.
- Include berarti perilaku yang selalu disertakan; extend berarti perilaku tambahan kondisional.
- Prinsip desain umum: high cohesion dan loose coupling.
- Verifikasi berbeda dari validasi.
- Cyclomatic complexity: \(V(G)=E-N+2P\), atau jumlah node keputusan + 1 untuk CFG sederhana yang terhubung.

## Sistem Cerdas

- BFS menggunakan queue; DFS menggunakan stack.
- UCS memilih biaya lintasan terkecil.
- Greedy menggunakan \(h(n)\).
- A* menggunakan \(f(n)=g(n)+h(n)\).
- Alpha-beta pruning terjadi ketika \(\alpha\geq\beta\).
- Forward chaining dimulai dari fakta; backward chaining dimulai dari tujuan.
- Fuzzy logic mengizinkan derajat keanggotaan dalam rentang [0,1].
- Neuron buatan menghitung \(z=\sum w_ix_i+b\).
- Pembaruan bobot gradient descent: \(w_{\text{baru}}=w_{\text{lama}}-\eta\,\partial E/\partial w\).

---

# 9. CHECKLIST PERSIAPAN UJIAN SEMESTER 4

## Grafika dan Komputasi Visual

- [ ] Saya dapat menjalankan Bresenham pada contoh koordinat sederhana.
- [ ] Saya dapat menghitung transformasi translasi, rotasi, dan skala.
- [ ] Saya memahami urutan transformasi matriks.
- [ ] Saya dapat memeriksa kondisi clipping garis.
- [ ] Saya dapat menjelaskan proyeksi 3D dan Z-buffer.
- [ ] Saya membedakan Flat, Gouraud, dan Phong shading.
- [ ] Saya memahami konvolusi, Sobel, dilasi, erosi, opening, dan closing.

## Jaringan Komputer

- [ ] Saya mampu menjelaskan OSI dan TCP/IP.
- [ ] Saya dapat menghitung network address dan broadcast address.
- [ ] Saya mampu merancang pembagian subnet untuk kebutuhan host.
- [ ] Saya membedakan RIP, OSPF, dan BGP.
- [ ] Saya memahami handshake TCP dan perbedaan TCP dengan UDP.
- [ ] Saya dapat menghitung transmission dan propagation delay.
- [ ] Saya memahami DNS, HTTP, socket, TLS, firewall, NAT, dan VPN.

## Manajemen Basis Data

- [ ] Saya memahami stored procedure, function, dan trigger.
- [ ] Saya dapat menjelaskan cara kerja indeks B+ Tree.
- [ ] Saya mampu membandingkan Nested Loop, Sort-Merge, dan Hash Join.
- [ ] Saya dapat mengidentifikasi anomali konkurensi.
- [ ] Saya mampu membuat precedence graph dan menguji siklus.
- [ ] Saya memahami 2PL, Strict 2PL, dan penanganan deadlock.
- [ ] Saya dapat menjelaskan WAL dan tiga fase ARIES.

## Pemrograman Berorientasi Objek

- [ ] Saya dapat membuat class dan object dalam Java.
- [ ] Saya memahami enkapsulasi dan access modifier.
- [ ] Saya dapat menjelaskan inheritance dan polymorphism.
- [ ] Saya dapat membedakan overloading dan overriding.
- [ ] Saya memahami interface, abstract class, dan relasi antarobjek.
- [ ] Saya memahami exception, generics, dan collections.
- [ ] Saya mampu memberikan contoh penerapan SOLID.

## Rekayasa Perangkat Lunak

- [ ] Saya mampu membandingkan Waterfall, V-Model, Spiral, dan Agile.
- [ ] Saya dapat membedakan functional dan non-functional requirements.
- [ ] Saya dapat membaca dan menyusun use case diagram.
- [ ] Saya memahami activity, sequence, dan class diagram.
- [ ] Saya dapat menjelaskan kohesi, kopling, layered architecture, dan MVC.
- [ ] Saya dapat menyusun equivalence partition dan boundary test.
- [ ] Saya dapat menghitung cyclomatic complexity dari CFG sederhana.

## Sistem Cerdas

- [ ] Saya dapat menyusun PEAS untuk suatu agen.
- [ ] Saya mampu menelusuri BFS, DFS, UCS, Greedy, dan A*.
- [ ] Saya memahami admissible dan consistent heuristic.
- [ ] Saya dapat menjalankan minimax dan alpha-beta pruning sederhana.
- [ ] Saya memahami resolusi dan representasi pengetahuan.
- [ ] Saya dapat membedakan forward dan backward chaining.
- [ ] Saya dapat melakukan perhitungan Certainty Factor sederhana.
- [ ] Saya memahami fuzzifikasi, evaluasi aturan, dan defuzzifikasi.
- [ ] Saya dapat menghitung keluaran neuron dan menjelaskan backpropagation.

---

# PENUTUP SEMESTER 4

Semester 4 merupakan tahap ketika Anda perlu mulai berpikir seperti perancang sistem, bukan hanya programmer.

Saat mempelajari setiap mata kuliah, latih dua kemampuan. Pertama, jelaskan konsep, tujuan, dan mekanisme kerjanya. Kedua, terapkan konsep tersebut pada kasus nyata melalui perhitungan, penelusuran algoritma, desain, query, atau analisis skenario.

Untuk melengkapi rangkuman ini, gunakan berkas `CONTOH_SOAL_DAN_PEMBAHASAN.md` yang tersedia pada folder setiap mata kuliah di repo. Utamakan latihan yang meminta Anda menunjukkan langkah penyelesaian, menjelaskan alasan memilih metode, serta membandingkan alternatif solusi.

Target akhirnya adalah mampu menjawab tiga pertanyaan untuk setiap materi: **apa konsepnya, bagaimana cara kerjanya, dan kapan atau mengapa konsep tersebut digunakan.**