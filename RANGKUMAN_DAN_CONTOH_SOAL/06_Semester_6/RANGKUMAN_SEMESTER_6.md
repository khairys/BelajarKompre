# RANGKUMAN LENGKAP SEMESTER 6
## Persiapan Ujian Komprehensif S1 Informatika — Universitas Diponegoro

Semester 6 menggabungkan tiga kemampuan utama lulusan Informatika: merancang algoritma yang efisien, mengelola proyek secara terukur, serta memastikan perangkat lunak memenuhi kebutuhan dan memiliki kualitas yang dapat diuji. Di samping itu, mahasiswa mempelajari tanggung jawab sosial dan etika profesi, lalu menerapkan kompetensi tersebut dalam lingkungan kerja nyata melalui Praktik Kerja Lapangan (PKL).

Rangkuman ini mengikuti susunan lima mata kuliah pada folder Semester 6 di repositori BelajarKompre. Setiap bagian mencakup pengertian, cara kerja, perbandingan penting, rumus utama, contoh interpretasi, dan target penguasaan.

## Gambaran Umum Semester 6

| Mata kuliah | Fokus utama |
|---|---|
| Analisis dan Strategi Algoritma | Kompleksitas, divide and conquer, greedy, dynamic programming, backtracking, branch and bound |
| Manajemen Proyek Teknologi Informasi | Seleksi proyek, lingkup, penjadwalan, anggaran, Earned Value, mutu, dan risiko |
| Masyarakat dan Etika Profesi | Teori moral, kode etik, HKI, lisensi perangkat lunak, cybercrime, dan privasi |
| Praktik Kerja Lapangan | Penerapan kompetensi Informatika, tata kelola magang, logbook, laporan, dan seminar |
| Uji Perangkat Lunak | Desain kasus uji, black-box/white-box, coverage, regresi, mutasi, otomasi, dan kinerja |

Kelima mata kuliah saling melengkapi. Analisis Algoritma membantu menentukan apakah suatu solusi layak secara komputasi. Uji Perangkat Lunak memeriksa kebenaran implementasi dan kesesuaiannya terhadap kebutuhan. Manajemen Proyek mengatur scope, waktu, biaya, tim, dan risiko. Etika Profesi membantu memastikan keputusan teknis bertanggung jawab, sedangkan PKL menjadi konteks penerapan kompetensi tersebut di dunia kerja.

**Catatan kurikulum:** urutan di sini mengikuti folder Semester 6 pada repositori. Untuk syarat administrasi PKL, bobot penilaian, maupun aturan akademik yang dapat berubah, tetap gunakan pedoman resmi yang berlaku untuk angkatan Anda.

---

# 1. ANALISIS DAN STRATEGI ALGORITMA

Sumber: [Rangkuman Materi Analisis dan Strategi Algoritma](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/06_Semester_6/Analisis_dan_Strategi_Algoritma/RANGKUMAN_MATERI.md)

## 1.1. Mengapa algoritma dianalisis?

Algoritma adalah prosedur terhingga untuk menyelesaikan masalah. Dua algoritma dapat menghasilkan keluaran yang sama tetapi berbeda dalam kebutuhan waktu dan memori. Analisis algoritma memperkirakan pertumbuhan penggunaan sumber daya ketika ukuran input \(n\) meningkat tanpa bergantung langsung pada kecepatan komputer atau bahasa pemrograman tertentu.

Hal yang biasa dianalisis:
- **Time complexity:** jumlah operasi atau pertumbuhan waktu eksekusi sebagai fungsi ukuran input.
- **Space complexity:** kebutuhan memori, termasuk memori tambahan yang digunakan algoritma.
- **Best case:** perilaku pada input yang paling menguntungkan.
- **Average case:** perilaku rata-rata menurut model distribusi input yang didefinisikan.
- **Worst case:** batas biaya pada input terburuk untuk ukuran yang dipertimbangkan.

Best, average, dan worst case adalah skenario analisis; Big-O, Big-Omega, dan Big-Theta adalah notasi pertumbuhan fungsi. Keduanya berkaitan, tetapi bukan sinonim.

## 1.2. Notasi asimptotik

**Big-O, \(O(g(n))\)** menyatakan batas atas asimptotik. Secara formal, terdapat konstanta \(c>0\) dan \(n_0\) sehingga \(f(n)\le c g(n)\) untuk setiap \(n\ge n_0\).

**Big-Omega, \(\Omega(g(n))\)** menyatakan batas bawah asimptotik. Terdapat \(c>0\) dan \(n_0\) sehingga \(f(n)\ge c g(n)\) untuk setiap \(n\ge n_0\).

**Big-Theta, \(\Theta(g(n))\)** menyatakan batas ketat asimptotik. Terdapat konstanta positif \(c_1,c_2\) dan \(n_0\) sehingga:

\[
c_1g(n)\le f(n)\le c_2g(n), \quad n\ge n_0
\]

Urutan pertumbuhan yang sering digunakan:

\[
O(1)<O(\log n)<O(n)<O(n\log n)<O(n^2)<O(n^3)<O(2^n)<O(n!)
\]

Untuk input yang sangat besar, orde dominan menentukan skalabilitas. Misalnya, algoritma \(O(n\log n)\) cenderung lebih baik untuk ukuran besar daripada \(O(n^2)\), meskipun faktor konstanta, implementasi, hardware, dan ukuran input kecil dapat membuat algoritma yang secara asimptotik lebih buruk tetap cepat pada kondisi tertentu.

**Kesalahan ujian yang harus dihindari:** Big-O tidak secara definisi berarti worst-case, Big-Omega bukan selalu best-case, dan Big-Theta bukan selalu average-case. Kita dapat menyebut worst-case suatu algoritma memiliki kompleksitas \(O(n^2)\), tetapi makna worst-case berasal dari skenario yang dianalisis, bukan dari simbol \(O\) itu sendiri.

### Cara menilai kompleksitas kode

- Sekelompok operasi yang tetap jumlahnya: \(O(1)\).
- Satu loop yang berulang sebanding dengan n: \(O(n)\).
- Dua loop bersarang yang masing-masing berjalan sampai n: umumnya \(O(n^2)\).
- Setiap iterasi membagi ruang pencarian menjadi dua: \(O(\log n)\).
- Memproses n elemen di setiap tingkat pembagian dengan log n tingkat: \(O(n\log n)\).
- Dua bagian yang dijalankan berurutan dijumlahkan; suku dengan laju pertumbuhan tertinggi biasanya mendominasi.
- Loop bersarang tidak otomatis \(O(n^2)\). Batas loop dan perubahan variabel harus dianalisis secara tepat.

Kompleksitas ruang sama pentingnya. Algoritma dapat menghemat waktu dengan menyimpan hasil antara, tetapi konsumsi memori tambahannya dapat meningkat.

## 1.3. Relasi rekurensi dan Teorema Master

Algoritma rekursif dapat dianalisis melalui relasi rekurensi. Bentuk yang umum pada divide and conquer:

\[
T(n)=aT(n/b)+f(n)
\]

dengan:
- \(a\): jumlah submasalah rekursif;
- \(n/b\): ukuran setiap submasalah;
- \(f(n)\): biaya pembagian, penggabungan, atau pekerjaan lain di luar pemanggilan rekursif.

Untuk bentuk sederhana \(f(n)=\Theta(n^d)\), bandingkan \(d\) dengan \(\log_b a\):

1. Jika \(d<\log_b a\), maka \(T(n)=\Theta(n^{\log_b a})\).
2. Jika \(d=\log_b a\), maka \(T(n)=\Theta(n^d\log n)\).
3. Jika \(d>\log_b a\), dan syarat regularitas yang relevan terpenuhi, maka \(T(n)=\Theta(n^d)\).

Teorema Master tidak berlaku langsung untuk setiap rekurensi. Jika ukuran submasalah berbeda, jumlah suku rekursif berubah, atau fungsi biaya tidak sesuai bentuk standar, gunakan metode lain seperti recursion tree, expansion, atau substitution.

**Contoh: Merge Sort**

\[
T(n)=2T(n/2)+\Theta(n)
\]

Terdapat dua submasalah (\(a=2\)), masing-masing setengah ukuran input (\(b=2\)), dan penggabungan memerlukan waktu linear. Karena \(\log_2 2=1\) dan biaya penggabungan juga berorde n, diperoleh:

\[
T(n)=\Theta(n\log n)
\]

## 1.4. Brute force dan algoritma dasar

**Brute force** memakai cara langsung untuk memeriksa kandidat atau memecahkan masalah, tanpa banyak pemangkasan atau optimasi khusus. Keuntungannya adalah sederhana dan dapat menjadi baseline yang baik. Keterbatasannya adalah biaya yang dapat tumbuh sangat cepat.

- **Linear search:** memeriksa elemen satu per satu sampai ditemukan atau seluruh elemen diperiksa. Worst-case \(O(n)\).
- **Bubble sort:** membandingkan elemen bersebelahan dan menukarnya ketika urutan salah. Worst-case \(O(n^2)\); implementasi dengan early termination dapat lebih cepat untuk input yang sudah terurut.
- **Naive string matching:** mencocokkan pola di setiap posisi teks. Untuk teks n dan pola m, worst-case dapat \(O(nm)\).
- **Exhaustive search:** memeriksa seluruh kandidat yang mungkin. Pendekatan ini layak saat ruang pencarian kecil, tetapi kombinasi dapat tumbuh eksponensial atau faktorial.

Jangan menganggap brute force selalu salah. Ia dapat dipilih untuk problem kecil, implementasi referensi, atau pengujian hasil algoritma yang lebih rumit.

## 1.5. Divide and Conquer dan Decrease and Conquer

Divide and conquer mempunyai tiga langkah:
1. **Divide:** pecah problem menjadi submasalah yang lebih kecil.
2. **Conquer:** selesaikan submasalah, biasanya secara rekursif.
3. **Combine:** gabungkan solusi menjadi jawaban untuk problem awal.

### Merge Sort

Merge Sort membagi array menjadi dua bagian sampai setiap bagian berisi satu elemen, lalu menggabungkan bagian-bagian tersebut secara terurut. Kompleksitas waktu standar best, average, dan worst case adalah \(\Theta(n\log n)\), dengan memori tambahan umumnya \(O(n)\). Merge Sort dapat bersifat stabil apabila prosedur merge mempertahankan urutan relatif elemen yang memiliki kunci sama.

### Quick Sort

Quick Sort memilih pivot, mempartisi elemen menjadi sisi yang relatif lebih kecil dan lebih besar, lalu memproses partisi secara rekursif.
- Rata-rata: \(O(n\log n)\).
- Worst-case: \(O(n^2)\) jika partisi berulang kali sangat tidak seimbang.
- Pemilihan pivot secara acak atau median-of-three dapat mengurangi kemungkinan partisi buruk, namun tidak mengubah kemungkinan worst-case pada semua implementasi.

Kelebihan Quick Sort adalah dapat berjalan dengan memori tambahan yang relatif kecil dalam implementasi in-place; kelemahan utamanya adalah performa sangat dipengaruhi strategi pivot dan pola data.

### Binary Search

Binary Search bekerja pada data yang telah terurut. Target dibandingkan dengan elemen tengah, lalu setengah rentang yang tidak mungkin mengandung target dibuang. Waktu pencarian \(O(\log n)\), asalkan mengakses elemen tengah membutuhkan waktu \(O(1)\), seperti pada array.

Binary Search tidak dapat diterapkan dengan benar pada data tak terurut tanpa proses pengurutan atau strategi lain. Pada linked list, akses ke elemen tengah tidak konstan sehingga keunggulan kompleksitas waktunya tidak sama.

**Decrease and conquer** menyelesaikan satu subproblem yang lebih kecil dan membangun solusi bertahap. Contohnya termasuk binary search dan insertion sort. Perbedaannya dengan divide and conquer klasik ialah jumlah submasalah: decrease and conquer biasanya meneruskan satu submasalah utama, sedangkan divide and conquer menyelesaikan beberapa submasalah lalu menggabungkannya.

## 1.6. Strategi Greedy

Greedy membangun solusi dengan memilih opsi yang paling menguntungkan saat ini atau **optimal lokal**. Strategi ini hanya menjamin optimum global pada masalah yang memiliki sifat yang sesuai, seperti greedy-choice property dan optimal substructure. “Memilih yang termurah dahulu” bukan pembuktian bahwa suatu algoritma optimal.

### Fractional Knapsack

Setiap item memiliki nilai \(v_i\) dan berat \(w_i\), sedangkan kapasitas tas adalah W. Item boleh diambil seluruhnya atau sebagian. Pilih berdasarkan rasio nilai per satuan berat:

\[
density_i=\frac{v_i}{w_i}
\]

Urutkan rasio dari terbesar, lalu ambil item terbaik sampai kapasitas habis. Greedy optimal untuk fractional knapsack karena sebagian item dapat diambil. Untuk 0/1 knapsack, item tidak dapat dipotong sehingga keputusan greedy berdasarkan rasio tidak selalu optimal.

### Huffman Coding

Huffman membuat kode prefix-free berdasarkan frekuensi simbol. Langkah umumnya: pilih dua node berfrekuensi terkecil, gabungkan menjadi node baru dengan frekuensi gabungan, lalu ulangi hingga terbentuk pohon. Simbol yang sering muncul cenderung mendapatkan kode yang lebih pendek.

Kode **prefix-free** berarti tidak ada kode suatu simbol yang menjadi awalan kode simbol lain. Ini membuat decoding dapat dilakukan tanpa delimiter tambahan di antara setiap kode simbol, selama bitstream dan pohon/aturan kodenya diketahui.

### Minimum Spanning Tree (MST)

MST pada graf tak berarah, berbobot, dan terhubung menghubungkan semua simpul dengan total bobot edge minimum tanpa siklus.

- **Kruskal:** urutkan edge dari bobot terkecil, lalu tambahkan edge selama tidak membentuk siklus. Disjoint Set Union/Union-Find membantu memeriksa apakah dua simpul sudah berada di komponen yang sama.
- **Prim:** mulai dari suatu simpul, lalu perluas pohon dengan memilih edge termurah yang menghubungkan pohon saat ini ke simpul di luar pohon.

Kruskal berorientasi pada pemilihan edge; Prim mengembangkan satu pohon dari node awal. Keduanya benar karena menggunakan sifat-sifat MST, bukan hanya karena mengambil edge yang tampak murah.

## 1.7. Dynamic Programming (DP)

Dynamic Programming cocok ketika:
1. **Optimal substructure:** solusi optimal problem dapat dibangun dari solusi optimal subproblem.
2. **Overlapping subproblems:** subproblem yang sama muncul berkali-kali.

DP menyimpan hasil subproblem agar tidak dihitung ulang. **Memoization** umumnya pendekatan top-down dengan cache; **tabulation** umumnya menyelesaikan subproblem dari basis ke ukuran yang lebih besar.

### 0/1 Knapsack

Terdapat n barang dengan nilai \(v_i\), berat \(w_i\), dan kapasitas tas W. Barang hanya dapat diambil atau ditinggalkan. Definisikan \(K[i,w]\) sebagai nilai maksimum dengan menggunakan i barang pertama dan kapasitas w.

\[
K[i,w]=
\begin{cases}
0 & i=0 \text{ atau } w=0\\
K[i-1,w] & w_i>w\\
\max(K[i-1,w],v_i+K[i-1,w-w_i]) & w_i\le w
\end{cases}
\]

Jika barang terlalu berat, barang itu tidak dapat dipilih. Jika muat, bandingkan dua keputusan: tidak mengambil barang atau mengambilnya dan menambah nilai terbaik yang masih muat.

Waktu dan memori tabel dasar \(O(nW)\). Kompleksitas ini disebut **pseudo-polynomial**, karena bergantung pada nilai numerik W, bukan hanya panjang representasi biner W.

### Longest Common Subsequence (LCS)

LCS mencari urutan elemen terpanjang yang terdapat pada dua sekuens dalam urutan yang sama, tetapi elemen tidak harus bersebelahan.

Misalkan \(L[i,j]\) adalah panjang LCS dari prefix pertama sepanjang i dan prefix kedua sepanjang j:
- Jika karakter terakhir sama, \(L[i,j]=L[i-1,j-1]+1\).
- Jika berbeda, \(L[i,j]=\max(L[i-1,j],L[i,j-1])\).
- Basis berupa baris dan kolom bernilai nol.

Algoritma tabel dasar membutuhkan waktu \(O(mn)\) dan memori \(O(mn)\). Dengan menelusuri kembali tabel, kita dapat merekonstruksi subsekuens yang menghasilkan panjang tersebut.

### Contoh perbedaan rekursi naif dan DP

Perhitungan Fibonacci rekursif naif berulang kali menghitung nilai yang sama, sehingga waktunya tumbuh eksponensial. Memoization atau tabulation menghitung setiap nilai yang diperlukan satu kali, sehingga waktu menjadi \(O(n)\). Ini memperlihatkan keuntungan utama DP: eliminasi perhitungan berulang.

## 1.8. Backtracking dan Branch and Bound

Kedua strategi menjelajahi **state-space tree**, tetapi cara pemangkasan dan tujuan umumnya berbeda.

### Backtracking

Backtracking mencari solusi yang memenuhi kendala, atau seluruh solusi yang valid. Algoritma menambahkan keputusan secara bertahap, memeriksa kelayakan solusi parsial, dan kembali ke keputusan sebelumnya ketika cabang tidak dapat menghasilkan solusi valid. Penelusuran sering menggunakan Depth-First Search (DFS).

**Contoh N-Queens:** tempatkan N ratu pada papan \(N\times N\) sehingga tidak ada dua ratu yang menyerang satu sama lain. Tempatkan satu ratu per baris dan periksa apakah kolom atau diagonalnya konflik. Bila konflik terjadi, jangan lanjutkan cabang tersebut.

Contoh lain mencakup pewarnaan graf, subset sum, dan pencarian labirin. Backtracking memangkas berdasarkan kendala; ia tidak otomatis membuat problem kombinatorial menjadi polynomial.

### Branch and Bound

Branch and Bound (B&B) umumnya ditujukan untuk masalah optimasi. Setiap node merepresentasikan solusi parsial, sedangkan **bound** memperkirakan hasil terbaik yang mungkin dicapai pada cabang itu. Jika batas tersebut tidak dapat mengalahkan solusi terbaik yang sudah ditemukan, cabang dapat dipangkas.

Pemilihan node dapat menggunakan DFS, BFS, atau best-first berdasarkan bound. Contoh aplikasi termasuk Traveling Salesperson Problem (TSP), knapsack optimasi, dan 15-puzzle. B&B dapat mempercepat pencarian secara praktis, tetapi untuk masalah kombinatorial umum worst-case tetap dapat sangat besar.

| Aspek | Backtracking | Branch and Bound |
|---|---|---|
| Tujuan umum | Menemukan satu atau semua solusi valid | Menemukan solusi optimum |
| Dasar pemangkasan | Kendala tidak terpenuhi atau solusi parsial tidak layak | Bound tidak dapat mengalahkan solusi terbaik yang ada |
| Penelusuran | Sering DFS | DFS, BFS, atau best-first |
| Contoh | N-Queens, graph coloring | TSP, optimasi knapsack |

## 1.9. P, NP, NP-hard, dan NP-complete

Istilah ini membahas tingkat kesulitan masalah, khususnya masalah keputusan.

- **P:** masalah keputusan yang dapat diselesaikan dalam waktu polynomial pada mesin deterministik.
- **NP:** masalah keputusan yang sertifikat jawaban “ya”-nya dapat diverifikasi dalam waktu polynomial. NP tidak berarti “non-polynomial”.
- **NP-hard:** masalah yang setidaknya sesulit setiap masalah di NP menurut reduksi polynomial yang sesuai. NP-hard tidak harus berupa masalah keputusan dan tidak harus berada di NP.
- **NP-complete:** masalah yang termasuk NP sekaligus NP-hard.

Jika satu masalah NP-complete memiliki algoritma polynomial untuk seluruh input, maka \(P=NP\). Sampai sekarang belum diketahui apakah \(P=NP\). Reduksi polynomial dipakai untuk membuktikan bahwa masalah baru setidaknya sekeras masalah yang sudah diketahui sulit; arah reduksi harus tepat.

### Target penguasaan Analisis dan Strategi Algoritma

Anda seharusnya dapat menjelaskan arti formal O, Ω, dan Θ; menghitung kompleksitas kode; menyelesaikan rekurensi sederhana; membandingkan Merge Sort, Quick Sort, dan Binary Search; menjelaskan kapan greedy optimal; menyusun tabel DP knapsack atau LCS; membedakan backtracking dan B&B; serta mendefinisikan P, NP, NP-hard, dan NP-complete.

---

# 2. MANAJEMEN PROYEK TEKNOLOGI INFORMASI

Sumber: [Rangkuman Materi Manajemen Proyek](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/06_Semester_6/Manajemen_Proyek/RANGKUMAN_MATERI.md)

## 2.1. Proyek, operasi, dan kendala utama

**Proyek** adalah usaha sementara untuk menghasilkan produk, layanan, atau hasil yang unik. Operasi bersifat berulang dan berkelanjutan. Contoh proyek TI adalah mengembangkan aplikasi akademik, migrasi database, menerapkan ERP, atau membangun pusat data baru.

Manajemen proyek mengatur ruang lingkup, jadwal, biaya, kualitas, risiko, komunikasi, sumber daya, stakeholder, serta pengadaan. **Triple constraint** klasik mencakup scope, time, dan cost; mutu dipengaruhi cara ketiganya diseimbangkan. Penambahan fitur dapat memperpanjang jadwal, menaikkan biaya, atau menurunkan mutu jika waktu dan sumber daya tidak disesuaikan.

### Lima process groups

1. **Initiating:** mengotorisasi proyek dan membangun kesepahaman awal.
2. **Planning:** merinci scope, jadwal, biaya, risiko, mutu, komunikasi, dan kebutuhan sumber daya.
3. **Executing:** melaksanakan pekerjaan dan mengelola tim.
4. **Monitoring and Controlling:** membandingkan realisasi dengan baseline serta melakukan tindakan korektif.
5. **Closing:** memperoleh penerimaan formal, menyerahkan hasil, mengarsipkan artefak, dan mencatat lessons learned.

Kelima kelompok ini tidak selalu berjalan satu kali secara linear. Dalam proyek nyata, perencanaan, pelaksanaan, dan pengendalian dapat berulang ketika informasi baru muncul.

### Struktur organisasi proyek

- **Functional:** anggota berada di departemen fungsional; manajer fungsional dominan dan kewenangan project manager dapat rendah.
- **Matrix:** kewenangan dibagi antara manajer fungsional dan project manager. Bentuknya dapat weak, balanced, atau strong matrix.
- **Projectized:** sumber daya diorganisasi menurut proyek dan project manager memiliki kewenangan relatif tinggi.

Struktur berpengaruh pada pengambilan keputusan, ketersediaan ahli, potensi konflik prioritas, dan biaya koordinasi.

## 2.2. Seleksi proyek secara finansial

Organisasi perlu menilai manfaat, biaya, risiko, kesesuaian strategis, kelayakan teknis, kapasitas tim, dan dampak operasional sebelum memilih proyek.

### Net Present Value (NPV)

\[
NPV=\sum_{t=1}^{n}\frac{R_t}{(1+r)^t}-I_0
\]

\(R_t\) adalah arus kas bersih periode t, r tingkat diskonto, dan \(I_0\) investasi awal. Dalam model konvensional, NPV positif menunjukkan nilai kini arus kas yang diperkirakan melebihi investasi awal pada asumsi model. Perbandingan antarkandidat hanya masuk akal bila periode, risiko, dan asumsi diskonto ditangani dengan konsisten.

### Return on Investment (ROI)

\[
ROI=\frac{Total\ Manfaat-Total\ Biaya}{Total\ Biaya}\times100\%
\]

ROI menunjukkan manfaat bersih relatif terhadap total biaya pada periode analisis. Namun, ROI sederhana tidak secara langsung memperhitungkan pola waktu uang seperti NPV. Definisi manfaat, biaya, dan periode perlu dinyatakan sebelum hasil dibandingkan.

### Payback Period

Payback period adalah waktu yang diperlukan agar arus kas bersih kumulatif menutup investasi awal. Jika arus kas bersih per tahun konstan, pendekatan sederhana:

\[
Payback\ Period=\frac{Investasi\ Awal}{Arus\ Kas\ Bersih\ Tahunan}
\]

Payback mudah dipahami, tetapi versi sederhananya dapat mengabaikan nilai waktu uang dan arus kas setelah titik impas. Karena itu, metode ini tidak sebaiknya menjadi satu-satunya dasar keputusan.

## 2.3. Project Charter, stakeholder, scope, dan WBS

**Project Charter** memberikan otorisasi formal terhadap proyek, merangkum alasan bisnis, tujuan tingkat tinggi, batasan awal, risiko utama, dan otoritas manajer proyek. **Stakeholder register** mengidentifikasi pihak yang dapat memengaruhi atau terpengaruh proyek beserta kepentingan, pengaruh, kebutuhan informasi, dan strategi pelibatannya.

Manajemen scope mengumpulkan kebutuhan, menentukan batas pekerjaan, membuat WBS, memvalidasi deliverable, dan mengendalikan perubahan.

### Work Breakdown Structure (WBS)

WBS adalah dekomposisi hierarkis berorientasi deliverable atas seluruh ruang lingkup pekerjaan. Unit di level terendah yang dapat diestimasi dan ditugaskan disebut **work package**.

**Aturan 100%:** WBS harus mencakup 100% ruang lingkup pekerjaan yang didefinisikan, tidak boleh ada pekerjaan yang terlewat dan tidak boleh menambahkan pekerjaan tak berhubungan di luar scope. WBS bukan hanya daftar aktivitas acak; ia menjadi dasar untuk menentukan aktivitas, durasi, biaya, penanggung jawab, dan sumber daya.

**Scope creep** adalah pertumbuhan lingkup yang tidak dikendalikan. Perubahan bukan otomatis buruk, tetapi perlu melalui penilaian dampak dan mekanisme persetujuan yang ditetapkan.

## 2.4. Penjadwalan: CPM dan PERT

Aktivitas proyek saling bergantung. Relasi yang umum:
- **Finish-to-Start (FS):** aktivitas B dimulai setelah A selesai.
- **Start-to-Start (SS):** B dapat mulai setelah A dimulai sesuai hubungan yang disepakati.
- **Finish-to-Finish (FF):** penyelesaian B bergantung pada penyelesaian A.
- **Start-to-Finish (SF):** B tidak dapat selesai sebelum A mulai; hubungan ini relatif jarang.

### Critical Path Method (CPM)

Critical path merupakan jalur dengan total durasi terpanjang pada network diagram yang menentukan durasi tercepat proyek dapat selesai menurut durasi dan ketergantungan yang dimodelkan. Dalam model CPM klasik, aktivitas pada jalur kritis memiliki total float/slack nol. Keterlambatan aktivitas kritis cenderung menunda tanggal akhir, kecuali dapat dikompensasi lewat tindakan lain.

Forward pass menghitung:
- **ES (Early Start):** mulai paling awal.
- **EF (Early Finish):** selesai paling awal.

Backward pass menghitung:
- **LS (Late Start):** mulai paling akhir agar target akhir tidak tertunda.
- **LF (Late Finish):** selesai paling akhir agar target akhir tidak tertunda.

Dalam konvensi durasi kontinu, \(EF=ES+Durasi\) dan \(LS=LF-Durasi\). Sebagian soal menghitung hari secara inklusif sehingga memakai \(EF=ES+Durasi-1\). Ikuti satu konvensi yang konsisten dan jangan mencampur keduanya.

\[
Float=LS-ES=LF-EF
\]

Float positif berarti aktivitas memiliki kelonggaran waktu sebelum mulai memengaruhi tanggal selesai proyek pada model yang digunakan.

### PERT

PERT memperkirakan durasi saat ketidakpastian tinggi dengan tiga estimasi:
- \(a\): optimistis.
- \(m\): paling mungkin.
- \(b\): pesimistis.

\[
t_e=\frac{a+4m+b}{6}
\]

\[
Variance=\left(\frac{b-a}{6}\right)^2
\]

Expected duration digunakan untuk estimasi jadwal; varians menggambarkan ketidakpastian menurut asumsi PERT. Varians jalur bisa dihitung dengan menjumlahkan varians aktivitas pada jalur jika asumsi independensi yang sesuai berlaku. PERT tidak menjamin tanggal selesai karena realisasi tetap dipengaruhi perubahan lingkup, sumber daya, dependency, dan risiko.

Gantt chart menunjukkan aktivitas terhadap waktu; network diagram lebih berguna untuk menganalisis ketergantungan dan critical path. Keduanya memiliki tujuan visual yang saling melengkapi.

## 2.5. Estimasi biaya dan cost baseline

Metode estimasi umum:
- **Analogous estimating:** memakai proyek serupa sebagai pembanding; cepat, tetapi bergantung pada kesesuaian data historis.
- **Parametric estimating:** menggunakan hubungan statistik, misalnya biaya per unit fungsi atau jumlah server.
- **Bottom-up estimating:** mengestimasi work package lalu menjumlahkannya; detail tetapi memerlukan waktu.
- **Three-point estimating:** memakai skenario optimistis, paling mungkin, dan pesimistis.

**Cost baseline** adalah anggaran yang disetujui sebagai pembanding kinerja biaya. Cadangan kontingensi menangani risiko yang telah diidentifikasi, sedangkan management reserve biasanya diperlakukan terpisah untuk pekerjaan tak terduga dalam konteks tata kelola organisasi.

## 2.6. Earned Value Management (EVM)

EVM menghubungkan lingkup yang telah selesai dengan jadwal dan biaya. Definisi dasar:
- **PV (Planned Value):** nilai anggaran pekerjaan yang direncanakan selesai sampai tanggal status.
- **EV (Earned Value):** nilai anggaran untuk pekerjaan yang benar-benar telah diselesaikan.
- **AC (Actual Cost):** biaya aktual dari pekerjaan yang dilaksanakan.
- **BAC (Budget at Completion):** total anggaran baseline.

Varians jadwal dan biaya:

\[
SV=EV-PV
\]

\[
CV=EV-AC
\]

Indeks kinerja:

\[
SPI=\frac{EV}{PV}, \qquad CPI=\frac{EV}{AC}
\]

Interpretasi:
- SV positif: nilai anggaran pekerjaan yang selesai lebih besar daripada nilai pekerjaan yang direncanakan hingga tanggal status.
- CV positif: nilai yang diperoleh lebih besar daripada biaya aktual.
- SPI di bawah 1: progres berdasarkan nilai pekerjaan berada di belakang rencana.
- CPI di bawah 1: biaya aktual lebih tinggi daripada nilai hasil kerja.

Contoh: \(PV=100\), \(EV=80\), \(AC=90\). Maka \(SV=-20\), \(CV=-10\), \(SPI=0{,}8\), dan \(CPI\approx0{,}89\). Proyek tertinggal dari rencana dan biaya yang digunakan relatif tidak efisien menurut metrik EVM.

Perkiraan biaya akhir dapat dihitung melalui rumus berbeda bergantung pada asumsi:

\[
EAC\approx\frac{BAC}{CPI}
\]

Rumus ini cocok ketika efisiensi biaya sampai sekarang diperkirakan berlanjut. Jika varians dianggap hanya terjadi satu kali, atau pekerjaan tersisa dipengaruhi faktor yang berbeda, perhitungan EAC dapat berubah.

\[
ETC=EAC-AC
\]

\[
VAC=BAC-EAC
\]

- **EAC:** Estimate at Completion, perkiraan total biaya pada saat proyek selesai.
- **ETC:** Estimate to Complete, perkiraan biaya tambahan yang masih diperlukan.
- **VAC:** Variance at Completion, selisih baseline dengan perkiraan biaya akhir. Nilai negatif berarti proyek diperkirakan melampaui anggaran.

EVM mengukur kemajuan menggunakan nilai anggaran pekerjaan yang selesai, bukan sekadar jumlah task atau persentase waktu yang berlalu.

## 2.7. Mutu, risiko, komunikasi, dan penutupan

**Quality Assurance (QA)** berfokus pada proses dan praktik yang membangun keyakinan bahwa kualitas dapat tercapai. **Quality Control (QC)** memeriksa hasil/output untuk menemukan ketidaksesuaian. Pengujian produk adalah bagian dari kontrol kualitas, tetapi tidak menggantikan tata kelola proses.

Alat bantu kualitas:
- **Pareto chart:** membantu melihat kategori penyebab yang paling banyak berkontribusi menurut data.
- **Fishbone/Ishikawa diagram:** mengelompokkan dugaan penyebab berdasarkan faktor seperti people, process, technology, measurement, materials, dan environment.
- Checklist, inspeksi, audit, serta analisis tren.

Manajemen risiko berjalan melalui identifikasi, analisis probabilitas dan dampak, perencanaan respons, penetapan pemilik risiko, serta pemantauan pemicu. **Risk register** dapat memuat deskripsi, penyebab, kemungkinan, dampak, prioritas, pemilik, strategi respons, dan status.

\[
EMV=Probabilitas\ Terjadi\times Dampak\ Moneter
\]

Jika probabilitas 20% dan dampak kerugian Rp50 juta, EMV kerugian adalah Rp10 juta. EMV adalah nilai ekspektasian; bukan prediksi bahwa kerugian aktual pasti tepat Rp10 juta.

Strategi respons terhadap ancaman:
- **Avoid:** mengubah rencana agar ancaman dihindari.
- **Mitigate:** menurunkan probabilitas dan/atau dampak.
- **Transfer:** mengalihkan sebagian konsekuensi melalui mekanisme seperti asuransi atau kontrak.
- **Accept:** menerima risiko dengan sadar, biasanya dengan rencana kontingensi yang sesuai.

Komunikasi perlu menetapkan siapa yang memerlukan informasi apa, kapan, melalui kanal apa, dan siapa yang bertanggung jawab mengirimkannya. Penutupan proyek mencakup penerimaan formal deliverable, serah terima, penyelesaian kontrak, dokumentasi, pengarsipan, serta lessons learned.

### Target penguasaan Manajemen Proyek

Anda seharusnya mampu membedakan proyek dan operasi, menghitung NPV/ROI/payback dengan asumsi jelas, membuat WBS sesuai aturan 100%, menghitung CPM/PERT, menafsirkan PV/EV/AC dan indikator EVM, serta menyusun respons risiko yang dapat dipertanggungjawabkan.

---

# 3. MASYARAKAT DAN ETIKA PROFESI

Sumber: [Rangkuman Materi Masyarakat dan Etika Profesi](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/06_Semester_6/Masyarakat_dan_Etika_Profesi/RANGKUMAN_MATERI.md)

## 3.1. Etika, moral, hukum, dan profesionalisme

Etika adalah kajian sistematis tentang alasan tindakan dinilai benar atau salah; moral merupakan nilai dan praktik yang dianut oleh individu atau masyarakat; hukum adalah aturan yang diberlakukan melalui lembaga berwenang. Ketiganya berhubungan tetapi tidak sama. Tindakan yang legal belum tentu etis, dan tindakan tidak etis tidak selalu memenuhi unsur pelanggaran hukum.

Profesional Informatika perlu mempertimbangkan keselamatan, privasi, keamanan, aksesibilitas, keadilan, kepercayaan, dan dampak teknologi terhadap masyarakat. Keahlian teknis tidak menghapus kewajiban menyampaikan keterbatasan sistem, menghindari klaim palsu, serta menangani cacat atau kerentanan secara bertanggung jawab.

### Utilitarianisme

Utilitarianisme menilai tindakan melalui konsekuensinya dan mempertimbangkan manfaat serta kerugian untuk pihak yang terdampak. Prinsip yang sering diingat adalah memilih tindakan yang menghasilkan kebaikan terbesar bagi jumlah orang terbanyak.

Kelemahannya jika diterapkan secara dangkal adalah manfaat agregat dapat dipakai untuk membenarkan pelanggaran hak kelompok kecil. Analisis tetap harus menilai distribusi dampak, risiko, hak, dan ketidakpastian.

### Deontologi Kantian

Deontologi berfokus pada kewajiban serta prinsip moral. Manusia tidak boleh diperlakukan hanya sebagai sarana untuk mencapai tujuan pihak lain. Dalam TI, keuntungan komersial tidak otomatis membenarkan kebohongan, manipulasi pengguna, atau pelanggaran privasi.

### Virtue Ethics

Etika kebajikan menekankan karakter dan kebiasaan moral seperti kejujuran, keadilan, keberanian moral, tanggung jawab, dan kebijaksanaan praktis. Pertanyaannya bukan sekadar “aturan apa yang berlaku?”, melainkan juga “bagaimana seorang profesional berintegritas seharusnya bertindak?”

Saat menjawab studi kasus etika, susun jawaban secara sistematis: fakta dan ketidakpastian → pihak terdampak → nilai/kewajiban yang berkonflik → alternatif tindakan → konsekuensi → prinsip/kode etik relevan → keputusan dan mitigasi.

## 3.2. Kode etik profesi komputer

Kode etik ACM/IEEE-CS menguraikan tanggung jawab penting insinyur perangkat lunak:
1. **Public:** mengutamakan keselamatan dan kepentingan umum.
2. **Client and Employer:** melayani klien/atasan dengan jujur, selama tidak bertentangan dengan kepentingan publik.
3. **Product:** memastikan kualitas produk setinggi yang wajar dicapai secara profesional.
4. **Judgment:** menjaga integritas dan independensi pertimbangan.
5. **Management:** mempromosikan manajemen proyek serta produk yang etis.
6. **Profession:** menjaga integritas dan reputasi profesi.
7. **Colleagues:** menghormati, bersikap adil, dan membantu rekan sejawat.
8. **Self:** mengembangkan kompetensi dan praktik etis sepanjang karier.

Kode etik tidak otomatis menjawab setiap dilema. Kode tersebut menjadi landasan menilai permintaan fitur yang membahayakan, tekanan tenggat yang mendorong pemotongan pengujian, konflik kepentingan, penggunaan data yang tidak pantas, dan temuan keamanan yang perlu dilaporkan.

## 3.3. Hak Kekayaan Intelektual (HKI/HAKI)

Hak kekayaan intelektual membentuk hak atas karya, identitas dagang, invensi, atau informasi rahasia. Beberapa kategori utama:

- **Hak cipta:** melindungi ekspresi nyata karya seperti kode sumber, dokumentasi, dan materi kreatif; bukan monopoli atas ide abstrak semata.
- **Paten:** melindungi invensi yang memenuhi persyaratan hukum seperti kebaruan, langkah inventif, dan dapat diterapkan dalam industri. Aturan untuk invensi yang diimplementasikan dengan komputer bergantung pada yurisdiksi serta substansi teknis.
- **Merek:** membedakan barang/jasa sebuah pihak dalam perdagangan.
- **Rahasia dagang:** melindungi informasi bernilai ekonomi yang dirahasiakan dan dijaga dengan upaya yang wajar.

Satu produk dapat memiliki kode yang dilindungi hak cipta, merek dagang, serta invensi teknis yang mungkin memenuhi syarat perlindungan paten. Hak-hak ini tidak saling menggantikan.

### Lisensi perangkat lunak

- **Proprietary/closed source:** penggunaan, redistribusi, dan modifikasi dibatasi oleh pemilik hak dan ketentuan lisensi.
- **Permissive**, seperti MIT atau Apache-2.0: umumnya mengizinkan penggunaan dan redistribusi yang fleksibel, dengan kewajiban sesuai teks lisensi. Apache-2.0 juga memiliki ketentuan paten serta NOTICE tertentu.
- **Copyleft**, seperti GPL: distribusi karya turunan dalam kondisi tertentu membawa kewajiban terkait lisensi dan penyediaan kode sumber sesuai ketentuan.

“Open-source” bukan berarti tidak memiliki hak cipta atau tidak memiliki kewajiban. Kewajiban bergantung pada lisensi, hubungan kode, cara distribusi, dan penggunaan. Untuk produk nyata, tinjau lisensi komponen, font, gambar, dataset, dan pustaka; konsultasikan ahli hukum bila dampaknya penting.

## 3.4. Cybercrime dan tanggung jawab keamanan

Kejahatan siber dapat menggunakan sistem atau data elektronik sebagai objek, alat, atau target tindakan melawan hukum. Contohnya antara lain akses ilegal, intersepsi, manipulasi/perusakan data, gangguan sistem, penipuan digital, pencurian identitas, ransomware, dan serangan terhadap ketersediaan.

Bedakan aktivitas berikut:
- **Riset kerentanan yang sah:** dilakukan dengan izin, ruang lingkup yang disetujui, dan praktik pelaporan yang bertanggung jawab.
- **Penetration testing:** memiliki otorisasi tertulis dan batas pengujian yang jelas.
- **Akses tanpa izin:** mengakses sistem atau data melampaui otorisasi, meskipun pelaku mengklaim hanya “menguji keamanan”.

Respons yang bertanggung jawab mencakup membatasi dampak, menjaga bukti dan log, melapor melalui jalur yang sah, tidak mengambil data lebih banyak daripada yang diperlukan, dan berkoordinasi untuk pengungkapan kerentanan bila dibutuhkan.

UU ITE dan ketentuan lain di Indonesia mengatur aspek informasi dan transaksi elektronik. Penentuan pasal, unsur tindak pidana, dan sanksi harus merujuk naskah peraturan resmi yang berlaku pada saat analisis karena ketentuan dapat berubah dan penerapannya bergantung pada fakta. Rangkuman ini adalah materi akademik, bukan nasihat hukum.

## 3.5. Perlindungan data pribadi dan privasi

Data pribadi adalah informasi yang dapat mengidentifikasi seseorang secara langsung atau tidak langsung, termasuk jika digabung dengan data lain dalam konteks tertentu. UU Perlindungan Data Pribadi Indonesia (UU No. 27 Tahun 2022) merupakan kerangka penting; detail pemenuhan kewajiban perlu diperiksa pada regulasi pelaksana dan pedoman terbaru.

Prinsip yang perlu dipahami:
- Menetapkan tujuan dan dasar pemrosesan yang sah serta transparan.
- Mengumpulkan data yang relevan dan secukupnya (*data minimization*).
- Menjaga kualitas, keamanan, dan batas penyimpanan.
- Membatasi akses berdasarkan kebutuhan.
- Memberi mekanisme untuk melaksanakan hak subjek data sesuai aturan.
- Menangani insiden dan notifikasi sesuai kewajiban hukum.
- Menilai risiko vendor, transfer lintas negara, profiling, serta pemrosesan data sensitif.

**Pengendali data pribadi** menentukan tujuan dan kendali pemrosesan, sedangkan **prosesor data pribadi** memproses data untuk dan atas instruksi pengendali dalam pengaturan yang relevan. Penentuan peran bergantung pada aktivitas yang benar-benar dilakukan dan hukum yang berlaku.

GDPR Uni Eropa adalah rezim tersendiri. Relevansinya pada suatu organisasi harus dinilai melalui cakupan teritorial dan materiil, bukan diasumsikan otomatis berlaku pada semua organisasi di semua negara.

### Target penguasaan Masyarakat dan Etika Profesi

Anda seharusnya mampu membandingkan utilitarianisme, deontologi, dan etika kebajikan; menerapkan kode etik ACM/IEEE pada dilema TI; membedakan hak cipta, paten, merek, dan rahasia dagang; membaca perbedaan lisensi software; serta menganalisis cybercrime dan privasi tanpa mencampuradukkan etika, kebijakan organisasi, dan hukum.

---

# 4. PRAKTIK KERJA LAPANGAN (PKL)

Sumber: [Panduan dan Rangkuman Materi PKL](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/06_Semester_6/Praktik_Kerja_Lapangan/RANGKUMAN_MATERI.md)

## 4.1. Tujuan PKL

PKL menjadi jembatan antara perkuliahan dan lingkungan kerja nyata. Mahasiswa belajar memahami proses bisnis, budaya organisasi, standar kerja, kolaborasi tim, teknologi yang digunakan, pengelolaan perubahan, dan cara mendokumentasikan kontribusi teknis berdasarkan bukti.

PKL bukan hanya hadir di kantor atau menyelesaikan tugas tanpa refleksi. Kegiatan yang baik memiliki ruang lingkup, tujuan, peran mahasiswa, bukti hasil, dan analisis hubungan antara masalah, metode, implementasi, pengujian, serta hasil.

Kontribusi dapat berupa pengembangan fitur, analisis kebutuhan, desain sistem, perbaikan bug, pengujian otomatis, data engineering, keamanan, dashboard, dokumentasi API, atau dukungan infrastruktur sesuai kebutuhan mitra dan arahan pembimbing.

## 4.2. Alur administrasi dan pelaksanaan

Dokumen sumber di repo merangkum panduan pelaksanaan PKL Departemen Informatika Undip. Di dalamnya dicantumkan syarat seperti minimal 80 SKS, tanpa nilai E, serta lulus mata kuliah prasyarat seperti Rekayasa Perangkat Lunak, Pemrograman Berorientasi Objek, Basis Data, dan Jaringan Komputer. Syarat tersebut adalah informasi dari dokumen sumber; batas SKS, prasyarat, formulir, durasi, dan portal dapat berbeda antarangkatan, sehingga harus diverifikasi melalui panduan resmi terbaru sebelum mendaftar.

Alur umum PKL:
1. Memeriksa syarat akademik dan administrasi.
2. Menentukan mitra dan ruang lingkup pekerjaan.
3. Menyusun proposal yang memuat latar belakang, tujuan, rencana kegiatan, serta lingkup teknis.
4. Mendapatkan pembimbing akademik dan pembimbing lapangan sesuai prosedur.
5. Melaksanakan aktivitas dengan menaati kebijakan organisasi dan batas akses sistem.
6. Memperbarui logbook secara berkala dan memperoleh validasi pembimbing sesuai aturan.
7. Mengumpulkan bukti kontribusi, menyusun laporan, menuntaskan revisi, lalu mengikuti seminar/ujian apabila diwajibkan.

Persiapan juga meliputi perjanjian kerahasiaan, keamanan akun, izin untuk memasukkan cuplikan kode atau gambar ke laporan, serta penyamaran data pelanggan. Artefak perusahaan tidak boleh dianggap bebas dipublikasikan hanya karena mahasiswa yang mengerjakannya.

## 4.3. Logbook dan bukti kerja

Logbook yang baik mencatat tanggal, tujuan, aktivitas spesifik, hasil, kendala, penyelesaian, serta tindak lanjut. Hindari entri umum seperti “mengerjakan aplikasi”. Entri yang lebih baik misalnya: “menambahkan validasi endpoint pembaruan persediaan; menulis pengujian untuk input kosong dan kode produk duplikat; membuat pull request dan menunggu review”.

Bukti kerja yang dapat relevan, sesuai izin mitra:
- Logbook/kartu aktivitas yang disahkan sesuai pedoman.
- Commit atau pull request yang boleh dibagikan.
- Test report, ringkasan issue, atau dokumentasi desain.
- Surat penerimaan dan surat selesai magang.
- Diagram sistem, rekap aktivitas, atau tangkapan layar yang tidak mengungkap informasi rahasia.

Jangan menaruh source code internal, data pelanggan, kredensial, token API, atau dokumen bisnis rahasia di repositori pribadi maupun lampiran laporan tanpa izin yang jelas.

## 4.4. Sistematika laporan PKL

Ikuti format resmi yang berlaku. Struktur yang tercantum pada dokumen repo secara umum meliputi:

### Bagian awal
Sampul, lembar pengesahan, kata pengantar, daftar isi, daftar gambar, daftar tabel, dan daftar lampiran sesuai pedoman.

### BAB I — Pendahuluan
- Latar belakang dan urgensi kegiatan.
- Lingkup dan batasan pekerjaan.
- Tujuan PKL yang spesifik.
- Manfaat kegiatan bagi mahasiswa, mitra, dan institusi.

### BAB II — Tinjauan Umum Instansi
- Profil perusahaan atau instansi.
- Produk, layanan, dan konteks proses bisnis.
- Struktur organisasi dan divisi tempat mahasiswa bekerja.
- Hubungan lingkup kerja dengan kebutuhan organisasi.

### BAB III — Metodologi dan Pelaksanaan Praktik Kerja
- Metode pengembangan atau cara kerja, seperti Scrum, Kanban, atau SDLC.
- Lingkungan teknis: bahasa, framework, database, sistem operasi, deployment, dan tools.
- Analisis kebutuhan dan deskripsi masalah.
- Perancangan sistem: UML, ERD, API, atau arsitektur sesuai proyek.
- Tahapan implementasi dan pembagian tanggung jawab.

### BAB IV — Hasil dan Pembahasan
- Modul atau fitur yang dikerjakan beserta alasan desain.
- Implementasi dan bukti keluaran.
- Metode pengujian dan hasil pengujian.
- Kendala teknis/organisasional, solusi, dan konsekuensi.
- Evaluasi kontribusi terhadap tujuan PKL serta keterbatasan hasil.

### BAB V — Penutup
Kesimpulan harus menjawab tujuan PKL dengan bukti, bukan hanya mengulang daftar kegiatan. Saran harus spesifik, realistis, dan dapat ditindaklanjuti oleh mitra atau pekerjaan lanjutan.

### Bagian akhir
Daftar pustaka sesuai gaya yang ditentukan dan lampiran yang diperbolehkan, seperti logbook, dokumen administratif, hasil uji, atau artefak teknis yang tidak melanggar kerahasiaan.

Laporan yang kuat menjelaskan keputusan, trade-off, dan proses validasi. Jika menampilkan arsitektur atau alur data, diagram harus sesuai sistem sebenarnya dan didukung penjelasan.

## 4.5. Presentasi dan evaluasi PKL

Panduan sumber menjelaskan peran pembimbing lapangan dan dosen penguji dalam penilaian. Persiapan presentasi sebaiknya mencakup:
- Kedisiplinan, komunikasi, kerja tim, dan profesionalisme.
- Pemahaman masalah serta proses bisnis mitra.
- Kontribusi individu yang dibuktikan.
- Pemilihan metode, kualitas implementasi, dan pengujian.
- Kelengkapan laporan dan kemampuan menjawab pertanyaan.

Alur presentasi yang jelas: masalah dan konteks → tujuan → peran serta kontribusi → metode/teknologi → hasil dan bukti → kendala dan solusi → keterbatasan → kesimpulan serta rekomendasi. Terangkan dengan jujur mana yang dikerjakan sendiri dan mana hasil kerja tim.

### Target penguasaan PKL

Anda seharusnya mampu menjelaskan proses pengajuan hingga seminar, menyusun logbook yang dapat diverifikasi, menyusun laporan dengan fokus rekayasa, memaparkan kontribusi individu, dan menjaga kerahasiaan artefak mitra.

---

# 5. UJI PERANGKAT LUNAK

Sumber: [Rangkuman Materi Uji Perangkat Lunak](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/06_Semester_6/Uji_Perangkat_Lunak/RANGKUMAN_MATERI.md)

## 5.1. Konsep dan tujuan pengujian

Software testing adalah aktivitas terencana untuk mengevaluasi software, menemukan defect, dan memberikan informasi mengenai kualitas, kesesuaian kebutuhan, serta risiko rilis.

Istilah dasar:
- **Error/mistake:** kesalahan manusia.
- **Defect/bug:** cacat pada artefak software seperti kebutuhan, desain, atau kode.
- **Failure:** perilaku sistem yang tidak sesuai saat software dijalankan.
- **Test case:** kondisi awal, input, langkah, serta hasil yang diharapkan.
- **Test suite:** kumpulan test case.
- **Test oracle:** mekanisme untuk menentukan perilaku/hasil yang benar.
- **Regression testing:** menjalankan kembali tes setelah perubahan untuk menemukan efek samping.
- **Verification:** apakah produk dibangun sesuai spesifikasi?
- **Validation:** apakah produk yang dibangun memenuhi kebutuhan nyata pengguna?

Testing dapat dinamis, yaitu menjalankan program, atau statis, seperti review kode dan analisis artefak tanpa menjalankan program. Pengujian dapat menemukan defect tetapi tidak membuktikan program bebas dari seluruh defect. Karena semua kombinasi masukan biasanya tidak dapat diuji satu per satu, strategi tes harus berorientasi risiko.

## 5.2. Tujuh prinsip ISTQB

1. **Testing shows the presence of defects:** testing menunjukkan keberadaan defect; tidak membuktikan ketiadaan semua defect.
2. **Exhaustive testing is impossible:** pengujian seluruh kombinasi input dan keadaan biasanya tidak praktis.
3. **Early testing saves time and money:** review kebutuhan dan desain sejak awal dapat mencegah biaya perbaikan lebih besar pada tahap akhir.
4. **Defects cluster together:** defect sering terkonsentrasi pada beberapa komponen; histori bisa digunakan untuk memprioritaskan pengujian.
5. **Beware of the pesticide paradox:** tes yang sama terus diulang dapat kehilangan kemampuan menemukan defect baru, sehingga test suite perlu ditinjau.
6. **Testing is context dependent:** strategi untuk sistem kritis berbeda dari strategi untuk aplikasi hiburan.
7. **Absence-of-errors fallacy:** produk dengan sedikit bug tetap gagal jika tidak memecahkan masalah atau memenuhi kebutuhan pengguna.

Pernyataan “80% bug berada di 20% kode” kerap digunakan sebagai ilustrasi Pareto, bukan hukum universal yang pasti berlaku pada setiap proyek.

## 5.3. Test plan, test case, dan defect report

**Test plan** menjelaskan tujuan, scope, strategi, resource, jadwal, lingkungan, risiko, kriteria entry/exit, dan tanggung jawab. **Test case** memuat prasyarat, input, prosedur, serta expected result. **Test report** merangkum apa yang diuji, hasil, cakupan, defect, risiko tersisa, dan rekomendasi.

Defect report yang baik mencakup:
- Judul spesifik dan mudah dicari.
- Versi/build dan lingkungan.
- Langkah reproduksi yang ringkas tetapi lengkap.
- Expected result dan actual result.
- Bukti log/screenshot/trace yang aman.
- Severity dan priority bila dipakai pada alur kerja tim.

**Severity** mengukur tingkat dampak defect, sedangkan **priority** menentukan urgensi penanganan. Keduanya tidak selalu sama: defect dengan dampak teknis terbatas dapat berprioritas tinggi karena menghalangi demo atau rilis, sementara defect yang jarang terjadi mungkin ditangani menurut konteks risiko.

Siklus defect tipikal ialah New → Triaged/Assigned → In Progress → Fixed → Retest → Closed, dengan kemungkinan status Reopened atau Deferred. Status yang tepat bergantung proses tim.

## 5.4. Level pengujian

### Unit testing
Menguji fungsi, metode, kelas, atau komponen kecil secara relatif terisolasi. Mock/stub dapat menggantikan dependensi agar pengujian fokus pada unit.

### Integration testing
Menguji interaksi antarmodul, API, database, atau layanan eksternal.
- **Big-bang integration:** banyak komponen digabung sekaligus, sehingga sumber kegagalan bisa sulit dilacak.
- **Top-down:** mulai dari modul tingkat atas dan memakai **stub** untuk modul bawah yang belum ada.
- **Bottom-up:** mulai dari modul tingkat bawah dan memakai **driver** untuk memanggil modul yang belum mempunyai pengendali atas.
- **Incremental integration:** menggabungkan komponen bertahap agar masalah lebih mudah diisolasi.

### System testing
Menguji sistem terintegrasi penuh terhadap spesifikasi, baik kebutuhan fungsional maupun nonfungsional.

### Acceptance testing
Menilai apakah produk dapat diterima berdasarkan kebutuhan bisnis dan kriteria penerimaan. UAT biasanya dilakukan oleh pengguna atau wakil bisnis. Alpha/beta mengacu pada konteks pengujian internal atau pengguna pada kondisi tertentu, bukan label yang otomatis menjamin kualitas.

## 5.5. Black-box testing

Black-box testing merancang kasus uji berdasarkan spesifikasi dan perilaku yang terlihat, bukan struktur internal kode.

### Equivalence Partitioning (EP)

Domain input dibagi menjadi partisi yang diasumsikan memiliki perilaku serupa. Satu atau lebih perwakilan dipilih dari partisi valid dan invalid.

Misalnya, usia yang diterima adalah integer 18–60:
- Partisi valid: 18 sampai 60.
- Partisi invalid bawah: di bawah 18.
- Partisi invalid atas: di atas 60.
- Partisi invalid format: teks, kosong, null, atau pecahan bila kontrak mengharuskan integer.

### Boundary Value Analysis (BVA)

Kesalahan sering muncul di batas rentang. Untuk usia 18–60 inklusif, uji nilai 17, 18, 19, 59, 60, dan 61. Untuk panjang string, kuota, tanggal, atau pagination, tentukan nilai minimum/maksimum serta apakah batas bersifat inklusif atau eksklusif.

### Decision table

Decision table berguna saat beberapa kondisi membentuk kombinasi aturan bisnis. Tabel memetakan kombinasi kondisi ke tindakan yang diharapkan. Kombinasi yang mustahil atau redundan harus diidentifikasi agar suite ringkas tetapi tetap bermakna.

Contoh: diskon bergantung pada status member dan total belanja. Tes harus meliputi variasi kedua kondisi, bukan hanya memeriksa satu parameter secara terpisah.

### State transition testing

Dipakai untuk sistem yang perilakunya bergantung pada state sebelumnya, seperti proses login, status pemesanan, transaksi pembayaran, atau tiket dukungan. Pengujian memeriksa transisi yang valid serta penolakan transisi tidak sah. Contoh login: setelah jumlah kegagalan tertentu, akun dapat berpindah menjadi temporarily locked; tes memeriksa batas tersebut dan kondisi pembukaan kembali.

**Pairwise testing** mengurangi jumlah kombinasi dengan memastikan pasangan nilai parameter diuji. Teknik ini membantu saat jumlah parameter besar, tetapi tidak menjamin menemukan semua bug yang bergantung pada interaksi tiga faktor atau lebih.

## 5.6. White-box testing dan cyclomatic complexity

White-box testing mempertimbangkan struktur internal program. **Control Flow Graph (CFG)** merepresentasikan instruksi/blok sebagai node dan perpindahan kontrol sebagai edge.

Cyclomatic complexity McCabe mengukur kompleksitas jalur independen dalam CFG:

\[
V(G)=E-N+2P
\]

dengan E jumlah edge, N jumlah node, dan P jumlah komponen terhubung. Untuk satu CFG terhubung, \(P=1\):

\[
V(G)=E-N+2
\]

Pendekatan lain untuk CFG terhubung adalah jumlah simpul keputusan/predikat ditambah satu. Nilai ini menunjukkan jumlah **basis path independen** minimum dalam pendekatan basis path testing, bukan jumlah semua jalur eksekusi.

### Tingkat code coverage

- **Statement coverage:** setiap statement dieksekusi setidaknya sekali.
- **Branch/decision coverage:** setiap cabang keputusan diuji, misalnya true dan false.
- **Condition coverage:** setiap kondisi Boolean atomik menghasilkan true dan false selama pengujian.
- **MC/DC:** setiap kondisi atomik ditunjukkan memiliki pengaruh independen terhadap hasil keputusan; sering digunakan pada sistem yang memerlukan assurance tinggi.

Statement coverage 100% tidak menjamin branch coverage 100%. Branch coverage tidak otomatis membuktikan MC/DC. Coverage adalah ukuran cakupan, bukan bukti bahwa seluruh assertion benar atau semua defect berhasil ditemukan.

## 5.7. Mutation testing dan regression testing

**Mutation testing** sengaja membuat perubahan kecil pada kode, disebut mutant, misalnya mengganti operator < menjadi <=, membalik kondisi, atau mengganti penjumlahan menjadi pengurangan. Mutan dinyatakan terbunuh ketika test suite mendeteksi perubahan melalui perbedaan perilaku atau kegagalan. Mutan yang lolos dapat menunjukkan tes kurang sensitif; sebagian mutan mungkin ekuivalen dengan program awal sehingga tidak dapat dibedakan melalui input-output.

\[
Mutation\ Score=
\frac{Killed\ Mutants}{Non\text{-}equivalent\ Mutants}\times100\%
\]

Regression testing menjalankan ulang tes setelah perubahan kode, konfigurasi, atau dependensi untuk mendeteksi efek samping. Subset regresi dapat dipilih menurut risiko, modul yang berubah, dependensi, dan biaya pengujian.

Tools yang umum dipelajari:
- **JUnit:** pengujian Java.
- **Mockito:** mock dan verifikasi interaksi dependensi.
- **Selenium/Cypress:** otomasi skenario browser end-to-end.
- **Apache JMeter:** pengujian beban dan performa pada protokol yang didukung.

Otomasi cocok untuk tes yang berulang, stabil, dan memiliki oracle jelas. Tidak semua aktivitas tes harus otomatis; pengujian eksploratori, pemeriksaan visual, aksesibilitas, dan penilaian pengalaman pengguna dapat tetap membutuhkan manusia.

## 5.8. Nonfunctional performance testing

- **Load testing:** perilaku pada beban yang diharapkan.
- **Stress testing:** mendorong sistem melewati kapasitas normal untuk melihat titik gagal dan cara pulih.
- **Spike testing:** menguji lonjakan beban mendadak.
- **Endurance/soak testing:** menguji beban dalam waktu lama untuk menemukan kebocoran memori atau degradasi.
- **Scalability testing:** menilai respons ketika beban atau resource ditingkatkan.

Metrik umum termasuk throughput, latency/response time (median dan persentil p95/p99), error rate, penggunaan CPU/memori, dan waktu pemulihan. Laporan harus menyertakan konfigurasi hardware/software, versi, pola request, dataset, serta lingkungan agar hasil dapat diulang. Rata-rata response time saja dapat menyembunyikan tail latency yang dialami oleh sebagian pengguna.

### Target penguasaan Uji Perangkat Lunak

Anda seharusnya dapat membedakan verification dan validation; menentukan level test; membuat kasus uji dengan EP, BVA, decision table, dan state transition; menghitung cyclomatic complexity; menjelaskan statement/branch/condition/MC/DC coverage; serta memahami mutation, regression, dan performance testing.

---

# 6. SINTESIS SEMESTER 6

Tiga skenario memperlihatkan hubungan antarmata kuliah.

**Kasus A — Memperbaiki modul rekomendasi yang lambat.** Analisis Algoritma menilai kompleksitas dan strategi optimasi. Uji Perangkat Lunak menguji kesetaraan hasil, regresi, serta performa setelah perubahan. Manajemen Proyek mengelola risiko, estimasi waktu, scope, dan komunikasi keputusan.

**Kasus B — Menangani insiden pada aplikasi pembayaran.** Etika Profesi memandu tanggung jawab kepada pengguna dan kepentingan umum; Manajemen Proyek mengatur respons serta pemulihan; pengujian memverifikasi perbaikan tanpa menciptakan regresi; dan bukti teknis didokumentasikan dengan menjaga data sensitif.

**Kasus C — Mempertanggungjawabkan hasil PKL.** Logbook serta laporan menunjukkan masalah, metode, kontribusi, implementasi, pengujian, hasil, dan keterbatasan. Konsep manajemen proyek menjelaskan scope, jadwal, dependensi, dan risiko; etika membantu menjaga kerahasiaan serta kejujuran akademik.

## 7. RUMUS KUNCI SEMESTER 6

| Konsep | Rumus atau prinsip |
|---|---|
| Relasi divide and conquer | \(T(n)=aT(n/b)+f(n)\) |
| Fractional knapsack | Prioritas menurut \(v_i/w_i\) |
| 0/1 knapsack DP | Bandingkan nilai tidak mengambil vs mengambil item jika muat |
| NPV | \(\sum_{t=1}^{n}R_t/(1+r)^t-I_0\) |
| ROI | \((Manfaat-Biaya)/Biaya\times100\%\) |
| Expected duration PERT | \((a+4m+b)/6\) |
| Varians PERT | \(((b-a)/6)^2\) |
| Schedule variance | \(SV=EV-PV\) |
| Cost variance | \(CV=EV-AC\) |
| Schedule performance index | \(SPI=EV/PV\) |
| Cost performance index | \(CPI=EV/AC\) |
| EAC jika tren CPI berlanjut | \(EAC\approx BAC/CPI\) |
| Expected Monetary Value | \(EMV=Probabilitas\times Dampak\) |
| Cyclomatic complexity | \(V(G)=E-N+2P\) |
| Mutation score | \(Killed/Non\text{-}equivalent\ mutants\times100\%\) |

## 8. CHECKLIST SEBELUM UJIAN

- [ ] Menjelaskan arti O, Ω, dan Θ tanpa menyamakan notasi dengan best/worst case.
- [ ] Menghitung kompleksitas loop dan menganalisis Merge Sort, Quick Sort, dan Binary Search.
- [ ] Menjelaskan mengapa greedy optimal pada Fractional Knapsack tetapi tidak selalu pada 0/1 Knapsack.
- [ ] Mengisi tabel DP untuk 0/1 Knapsack atau LCS.
- [ ] Membedakan backtracking dan branch-and-bound serta menjelaskan alasan pemangkasan.
- [ ] Mendefinisikan P, NP, NP-hard, dan NP-complete.
- [ ] Menghitung NPV/ROI/payback serta membuat WBS dengan aturan 100%.
- [ ] Menghitung ES, EF, LS, LF, slack, dan jalur kritis dari network diagram.
- [ ] Menghitung expected duration PERT, SV/CV, SPI/CPI dan menafsirkan EAC sesuai asumsi.
- [ ] Menganalisis dilema etika memakai teori moral dan kode etik ACM/IEEE.
- [ ] Membedakan hak cipta, paten, merek, rahasia dagang, dan lisensi perangkat lunak.
- [ ] Menjelaskan batas penggunaan data pribadi dan perlunya memeriksa peraturan terbaru.
- [ ] Menjelaskan proses PKL, menulis logbook dan laporan, serta membuktikan kontribusi individu.
- [ ] Memilih teknik black-box sesuai domain input dan menghitung cyclomatic complexity dari CFG.
- [ ] Membedakan statement, branch, condition, dan MC/DC coverage.
- [ ] Menjelaskan mutation testing, regression testing, serta load/stress/endurance testing.

**Strategi belajar:** pada soal hitungan, tulis definisi variabel dan asumsi dahulu, lalu hitung secara bertahap. Pada soal studi kasus, jelaskan fakta relevan, alternatif, trade-off, bukti, dan keterbatasan. Pada soal pengujian, bedakan kondisi awal, input, langkah, expected result, actual result, dan kesimpulan.

