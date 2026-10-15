# Rangkuman Belajar Ujian Komprehensif Informatika — Semester 1

Semester 1 adalah fondasi untuk memahami ilmu komputer. Di semester ini, kamu mulai mempelajari bagaimana program bekerja, bagaimana komputer merepresentasikan dan memproses informasi, bagaimana masalah dibuktikan secara matematis, serta bagaimana berpikir secara logis.

Saya menyusun rangkuman ini berdasarkan delapan dokumen mata kuliah yang tersedia di repository [BelajarKompre](https://github.com/khairys/BelajarKompre). Materi di bawah mengikuti urutan konsep yang tercantum dalam dokumen-dokumen tersebut, dengan penjelasan menggunakan bahasa yang lebih sederhana.

## Peta besar semester 1

1\. Dasar Pemrograman

Bagaimana memberikan instruksi kepada komputer untuk menyelesaikan masalah.

2\. Dasar Sistem

Bagaimana komputer merepresentasikan data dan membangun rangkaian logika digital.

3\. Logika Informatika

Bagaimana memeriksa kebenaran pernyataan dan menarik kesimpulan secara formal.

4\. Struktur Diskrit

Bagaimana memahami himpunan, kombinasi, graf, pohon, dan struktur matematis yang digunakan dalam komputasi.

5\. Matematika I

Bagaimana memahami perubahan, limit, turunan, dan integral.

6\. Bahasa Inggris

Bagaimana memahami bacaan akademik, tata bahasa, dan teks teknis Informatika.

7\. Pancasila dan Kewarganegaraan

Bagaimana memahami nilai kebangsaan, konstitusi, hak warga negara, dan etika dalam penggunaan teknologi.

8\. Olah Raga

Pengembangan kebugaran fisik, kesehatan, dan kebiasaan hidup aktif.

Kita akan membahas masing-masing mata kuliah dari konsep paling dasar hingga tujuan akhir pembelajarannya.

# 1. Dasar Pemrograman

Dokumen repo: [Rangkuman Dasar Pemrograman](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Dasar_Pemrograman/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Dasar Pemrograman mengajarkan cara mengubah masalah menjadi langkah-langkah yang dapat dijalankan oleh komputer. Dalam dokumen repo ini, fokus utamanya adalah paradigma pemrograman fungsional dan rekursi.

Paradigma fungsional perlu kamu perhatikan karena penekanannya berbeda dari pemrograman prosedural yang biasanya menggunakan banyak perulangan dan perubahan nilai variabel.

### Urutan materi

A. Memahami masalah dan algoritma

Sebelum menulis program, kamu perlu mampu memahami masalah, memecahnya menjadi bagian-bagian kecil, mengenali pola, dan menyusun algoritma penyelesaiannya.

Contoh: jika ingin menghitung rata-rata lima nilai mahasiswa, kamu harus menentukan nilai yang masuk, cara menjumlahkan, dan cara membaginya dengan jumlah data.

B. Tipe data dan operator

Komputer mengolah data menggunakan tipe dan operasi yang sesuai.

- Integer: bilangan bulat, seperti `10`.
- Real: bilangan pecahan, seperti `3.5`.
- Boolean: nilai benar atau salah.
- Character: satu karakter.
- Operator aritmetika: tambah, kurang, kali, dan bagi.
- Operator logika: AND, OR, dan NOT.

C. Tipe data bentukan atau Abstract Data Type (ADT)

Data kompleks dapat dibentuk dari beberapa nilai sederhana.

Misalnya, objek `Point` menyimpan koordinat \\(x\\) dan \\(y\\). Kamu memerlukan konstruktor untuk membentuk objek dan selektor untuk mengambil komponennya.

Intinya, kamu belajar mengorganisasi data berdasarkan makna dan operasi yang dapat dilakukan terhadapnya.

D. Ekspresi kondisional

Program harus bisa menentukan hasil berdasarkan kondisi tertentu.

Contohnya, sebuah fungsi mengembalikan nilai lulus ketika nilai mahasiswa memenuhi batas kelulusan. Kamu perlu memahami kondisi, operator perbandingan, dan percabangan logis.

E. Rekursi

Rekursi terjadi ketika sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan masalah yang lebih kecil.

Contohnya, faktorial:

\\[ n!=n\times(n-1)! \\]

dengan kondisi dasar \\(0!=1\\).

Ada dua komponen utama yang wajib dipahami:

- Basis: kondisi saat rekursi berhenti.
- Rekurens: cara menyelesaikan masalah dengan memanggil fungsi untuk masalah yang lebih kecil.

Tanpa basis yang benar, rekursi dapat berjalan tanpa akhir.

F. List dan pengolahan kumpulan data

Kamu mempelajari cara menyimpan sekumpulan elemen dalam list fungsional.

Operasi yang perlu dikenal antara lain `Konso` untuk menambahkan elemen di awal, `Konsi` untuk menambahkan elemen di akhir, `FirstElmt` untuk mengambil elemen pertama, dan `Tail` untuk mengambil sisa list.

Dari sini, kamu belajar menghitung panjang list, menjumlahkan elemen, mencari nilai maksimum, serta membalik urutan list secara rekursif.

G. Himpunan, list of list, dan pohon biner

Materi berkembang menjadi struktur data yang lebih kompleks.

- Himpunan atau set: koleksi elemen tanpa duplikasi.
- List of list: list yang elemen-elemennya juga berupa list, misalnya untuk merepresentasikan matriks.
- Pohon biner: struktur data yang setiap simpulnya memiliki paling banyak dua anak.
- Lambda dan higher-order functions: fungsi tanpa nama dan fungsi yang dapat menerima atau menghasilkan fungsi lain, seperti `map` dan `filter`.

### Target setelah mempelajari Dasar Pemrograman

Kamu seharusnya mampu membaca suatu masalah, menentukan struktur datanya, menulis fungsi, menjelaskan basis dan rekurens, serta menelusuri hasil pemanggilan fungsi.

Pertanyaan komprehensif yang harus bisa kamu jawab: Apa perbedaan paradigma fungsional dan prosedural? Mengapa rekursi membutuhkan basis? Bagaimana memproses list tanpa menggunakan perulangan biasa?

# 2. Dasar Sistem

Dokumen repo: [Rangkuman Dasar Sistem](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Dasar_Sistem/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Dasar Sistem menjelaskan fondasi perangkat keras digital: bagaimana informasi direpresentasikan dalam bentuk biner dan bagaimana rangkaian elektronik melakukan operasi logika.

Bayangkan komputer sebagai kumpulan rangkaian yang memproses sinyal. Mata kuliah ini membahas prinsip matematis dan logika di balik rangkaian tersebut.

### Urutan materi

A. Sistem bilangan dan representasi data

Komputer menggunakan biner, yaitu bilangan berbasis 2. Selain itu, kamu perlu memahami desimal berbasis 10, oktal berbasis 8, dan heksadesimal berbasis 16.

Contoh:

\\[ 13\_{10}=1101_2 \\]

Kamu belajar konversi antarbasis, operasi aritmetika biner, dan representasi bilangan bertanda.

B. Gerbang logika

Gerbang logika menerima satu atau beberapa input lalu menghasilkan output berdasarkan aturan tertentu.

| Gerbang      | Fungsi                                                                                       |
| ------------ | -------------------------------------------------------------------------------------------- |
| AND          | Bernilai 1 jika semua input bernilai 1                                                       |
| OR           | Bernilai 1 jika minimal satu input bernilai 1                                                |
| NOT          | Membalik nilai input                                                                         |
| XOR          | Bernilai 1 jika kedua input berbeda                                                          |
| NAND dan NOR | Kebalikan dari AND dan OR; keduanya dapat digunakan untuk membangun rangkaian logika lainnya |

Kamu harus bisa membaca tabel kebenaran (truth table) dan menentukan output dari kombinasi input.

C. Aljabar Boolean

Aljabar Boolean merupakan matematika yang digunakan untuk menyederhanakan ekspresi logika.

Misalnya, kamu mempelajari hukum identitas, komplemen, distributif, serta hukum De Morgan.

Tujuannya adalah menghasilkan rangkaian yang lebih sederhana tanpa mengubah fungsi logikanya.

D. Karnaugh Map (K-Map)

K-Map membantu menyederhanakan fungsi Boolean secara visual melalui pengelompokan sel bernilai 1 atau 0.

Kemampuan pentingnya bukan sekadar menggambar peta, tetapi menentukan kelompok dengan benar dan menghasilkan persamaan Boolean yang lebih sederhana.

E. Rangkaian kombinasional

Rangkaian kombinasional menghasilkan output berdasarkan input saat ini saja, tanpa menyimpan keadaan sebelumnya.

Contohnya:

- Half adder dan full adder untuk penjumlahan biner.
- Comparator untuk membandingkan dua bilangan.
- Decoder dan encoder untuk menerjemahkan representasi data.
- Multiplexer untuk memilih salah satu dari beberapa input.

F. Rangkaian sekuensial dan flip-flop

Berbeda dari rangkaian kombinasional, rangkaian sekuensial memiliki keadaan atau state yang disimpan.

Kamu akan mempelajari SR latch serta SR, D, JK, dan T flip-flop. Elemen-elemen ini menjadi dasar penyimpanan satu bit dan perubahan keadaan berdasarkan sinyal clock.

G. Counter, register, dan memori

Materi berlanjut pada rangkaian yang menyimpan dan mengelola data:

- Counter: menghitung urutan keadaan atau pulsa.
- Register: menyimpan sekumpulan bit.
- Shift register: menggeser posisi bit.
- SRAM dan DRAM: jenis memori dengan karakteristik penyimpanan berbeda.
- ROM dan flash memory: penyimpanan nonvolatil yang mempertahankan data ketika daya dimatikan.

### Target setelah mempelajari Dasar Sistem

Kamu seharusnya mampu mengonversi bilangan, membaca tabel kebenaran, menyederhanakan persamaan Boolean, membedakan rangkaian kombinasional dan sekuensial, serta menjelaskan cara flip-flop menyimpan bit.

Pertanyaan komprehensif yang perlu dikuasai: Mengapa komputer menggunakan biner? Apa perbedaan rangkaian kombinasional dan sekuensial? Mengapa D flip-flop dapat digunakan untuk menyimpan data?

# 3. Logika Informatika

Dokumen repo: [Rangkuman Logika Informatika](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Logika_Informatika/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Logika Informatika mengajarkan cara menentukan apakah suatu pernyataan benar, apakah sebuah kesimpulan mengikuti premisnya, dan bagaimana kebenaran tersebut dapat dibuktikan secara formal.

Perbedaan utamanya dari Struktur Diskrit adalah penekanannya pada sistem logika dan penalaran formal.

### Urutan materi

A. Proposisi dan operator logika

Proposisi adalah pernyataan yang bernilai benar atau salah.

Misalnya:

- \\(p\\): Komputer sedang menyala.
- \\(q\\): Sistem operasi sedang berjalan.

Dari dua proposisi tersebut, kamu mempelajari operator:

\\[ \neg p,\quad p\land q,\quad p\lor q,\quad p\to q \\]

Artinya secara berurutan: NOT, AND, OR, dan implikasi.

Kamu juga mempelajari tabel kebenaran, tautologi, kontradiksi, dan kontingensi.

B. Ekuivalensi logis

Dua ekspresi disebut ekuivalen secara logis apabila memiliki nilai kebenaran yang sama untuk semua kemungkinan input.

Contoh hukum De Morgan:

\\[ \neg(p\land q)\equiv\neg p\lor\neg q \\]

Kemampuan ini penting ketika menyederhanakan kondisi program atau membuktikan suatu pernyataan.

C. Aturan inferensi

Inferensi adalah cara menarik kesimpulan dari premis.

Contoh Modus Ponens:

1. Jika hujan, jalan menjadi basah.
2. Hujan sedang turun.
3. Kesimpulan: jalan menjadi basah.

Dalam logika simbolik:

\\[ p\to q,\ p\ \therefore q \\]

Kamu mempelajari aturan inferensi lainnya seperti Modus Tollens dan silogisme hipotetis.

D. Semantic Tableaux

Metode pohon semantik digunakan untuk menguji konsistensi atau validitas argumen.

Kamu menguraikan ekspresi logika menjadi cabang-cabang sesuai aturan. Cabang yang mengandung proposisi dan negasinya sekaligus dapat ditutup karena kontradiktif.

E. Bentuk normal CNF dan DNF

Ekspresi logika dapat diubah ke format standar.

- CNF: konjungsi dari klausa-klausa disjungtif.
- DNF: disjungsi dari bagian-bagian konjungtif.

Contohnya, \\((p\lor q)\land r\\) merupakan CNF, sedangkan \\((p\land q)\lor r\\) merupakan DNF.

Kamu perlu memahami bagaimana mengubah ekspresi dari satu bentuk ke bentuk lainnya.

F. Resolusi dan pembuktian melalui kontradiksi

Resolusi digunakan untuk memperoleh klausa baru dari klausa-klausa yang memiliki literal komplementer.

Untuk menguji validitas argumen melalui resolution refutation, kamu mengambil premis, menegasikan kesimpulan, lalu mencoba memperoleh kontradiksi.

G. Logika predikat orde pertama (First-Order Logic/FOL)

Logika berkembang dari pernyataan sederhana menjadi pernyataan mengenai objek, sifat, dan relasi.

Kamu mempelajari:

- Predikat, seperti `Mahasiswa(x)`.
- Kuantor universal \\(\forall\\), yang berarti untuk semua.
- Kuantor eksistensial \\(\exists\\), yang berarti terdapat setidaknya satu.
- Negasi kuantor, substitusi, unifikasi, dan resolusi FOL.

Contoh:

\\[ \forall x,\ Mahasiswa(x)\to Belajar(x) \\]

Artinya, setiap individu yang merupakan mahasiswa memenuhi pernyataan bahwa ia belajar.

### Target setelah mempelajari Logika Informatika

Kamu seharusnya mampu menghitung tabel kebenaran, membedakan tautologi dan kontradiksi, menerapkan aturan inferensi, mengubah ekspresi ke CNF/DNF, serta menerjemahkan pernyataan bahasa sehari-hari menjadi logika predikat.

Pertanyaan penting: Apa perbedaan implikasi dan ekuivalensi? Mengapa argumen yang kesimpulannya benar belum tentu valid? Apa fungsi kuantor universal dan eksistensial?

# 4. Struktur Diskrit

Dokumen repo: [Rangkuman Struktur Diskrit](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Struktur_Diskrit/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Struktur Diskrit mempelajari struktur matematika yang terdiri atas elemen-elemen terpisah atau dapat dihitung. Bidang ini sangat penting untuk algoritma, struktur data, basis data, jaringan, dan kriptografi.

### Urutan materi

A. Himpunan

Himpunan adalah kumpulan objek yang terdefinisi dengan jelas.

Jika \\(A=\\{1,2,3\\}\\) dan \\(B=\\{3,4,5\\}\\), maka:

\\[ A\cup B=\\{1,2,3,4,5\\} \\]

\\[ A\cap B=\\{3\\} \\]

Kamu juga mempelajari selisih himpunan, komplemen, subset, dan himpunan kuasa.

B. Relasi

Relasi menjelaskan hubungan antara elemen-elemen suatu himpunan.

Misalnya, hubungan “lebih besar dari”, “sama dengan”, atau “merupakan teman dari”.

Sifat relasi yang perlu dipahami mencakup refleksif, simetris, antisimetris, dan transitif. Kombinasi sifat tertentu menghasilkan relasi ekuivalensi atau partial order.

C. Fungsi

Fungsi memetakan setiap elemen domain ke tepat satu elemen kodomain.

Kamu mempelajari domain, kodomain, range, serta jenis pemetaan seperti injektif, surjektif, dan bijektif.

Konsep ini menjadi dasar pemahaman fungsi dalam pemrograman dan matematika.

D. Prinsip sarang merpati (Pigeonhole Principle)

Jika jumlah objek lebih banyak daripada jumlah wadah, maka minimal satu wadah harus berisi lebih dari satu objek.

Misalnya, jika enam orang ditempatkan ke dalam lima kelompok, setidaknya ada satu kelompok yang berisi dua orang atau lebih.

Prinsip ini digunakan untuk membuktikan keberadaan suatu kondisi tanpa harus memeriksa seluruh kemungkinan satu per satu.

E. Induksi matematika

Induksi digunakan untuk membuktikan pernyataan yang berlaku untuk bilangan bulat dalam suatu rentang.

Prosesnya memiliki tiga bagian:

1. Membuktikan kasus dasar.
2. Mengasumsikan pernyataan benar untuk \\(k\\).
3. Membuktikan bahwa pernyataan juga benar untuk \\(k+1\\).

Induksi banyak digunakan untuk membuktikan rumus penjumlahan, sifat struktur data, dan kebenaran algoritma.

F. Kombinatorika dan pencacahan

Kombinatorika membahas cara menghitung banyaknya kemungkinan.

Kamu harus membedakan:

- Permutasi: urutan diperhatikan.
- Kombinasi: urutan tidak diperhatikan.

Untuk \\(n\\) objek yang dipilih \\(r\\) objek sekaligus tanpa pengulangan:

\\[ P(n,r)=\frac{n!}{(n-r)!} \\]

\\[ C(n,r)=\frac{n!}{r!(n-r)!} \\]

Kombinatorika digunakan dalam analisis kompleksitas, probabilitas diskrit, dan perhitungan kemungkinan konfigurasi.

G. Relasi rekurens

Relasi rekurens mendefinisikan suatu urutan berdasarkan nilai sebelumnya.

Contohnya, barisan Fibonacci:

\\[ F_n=F\_{n-1}+F\_{n-2} \\]

dengan nilai awal yang ditentukan.

Kamu mempelajari bagaimana memodelkan urutan tersebut dan mencari rumus atau solusi relasinya.

H. Teori bilangan dan aritmetika modular

Materinya meliputi keterbagian, FPB, algoritma Euclid, kongruensi, invers modulo, serta teorema bilangan yang mendukung kriptografi.

Contoh:

\\[ 17\bmod 5=2 \\]

Artinya, sisa pembagian 17 dengan 5 adalah 2.

I. Graf dan pohon

Graf terdiri dari simpul (vertex) dan sisi (edge) yang menggambarkan hubungan.

Kamu mempelajari derajat simpul, lintasan, sirkuit, graf planar, pewarnaan graf, pohon, dan spanning tree.

Contoh penerapan: komputer dapat merepresentasikan jaringan sebagai graf, lalu menggunakan algoritma pencarian lintasan untuk menemukan rute.

J. Dasar kriptografi RSA

Pada bagian akhir, materi menghubungkan teori bilangan dengan keamanan informasi.

RSA menggunakan dua kunci yang berkaitan secara matematis: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Pemahaman dasarnya melibatkan bilangan prima, modulo, dan invers modular.

### Target setelah mempelajari Struktur Diskrit

Kamu seharusnya dapat melakukan operasi himpunan, memeriksa sifat relasi, membedakan permutasi dan kombinasi, membuktikan pernyataan menggunakan induksi, menyelesaikan soal graf dan pohon, serta memahami mengapa aritmetika modular menjadi dasar kriptografi.

Pertanyaan penting: Apa perbedaan relasi dan fungsi? Mengapa jumlah sisi pohon dengan \\(n\\) simpul adalah \\(n-1\\)? Kapan menggunakan permutasi dan kapan menggunakan kombinasi?

# 5. Matematika I

Dokumen repo: [Rangkuman Matematika I](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Matematika_I/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Matematika I berfokus pada kalkulus. Kamu mempelajari fungsi, perubahan nilai, laju perubahan, dan akumulasi.

Secara sederhana, turunan menjelaskan bagaimana suatu nilai berubah, sedangkan integral menjelaskan akumulasi nilai dalam suatu rentang.

### Urutan materi

A. Bilangan real dan pertidaksamaan

Kamu mulai dengan sifat bilangan real, interval, pertidaksamaan, dan nilai mutlak.

Hal pentingnya adalah menentukan rentang nilai \\(x\\) yang memenuhi suatu kondisi, termasuk ketika ada pecahan aljabar atau nilai mutlak.

B. Fungsi

Fungsi menggambarkan hubungan antara input dan output.

Kamu mempelajari domain, range, grafik fungsi, simetri, komposisi fungsi, serta karakteristik fungsi aljabar dan trigonometri yang diperlukan untuk kalkulus.

C. Limit dan kekontinuan

Limit membahas nilai yang didekati suatu fungsi ketika input mendekati titik tertentu.

Contoh:

\\[ \lim\_{x\to 2}(x+3)=5 \\]

Kamu belajar menghitung limit menggunakan manipulasi aljabar, mempelajari limit sepihak, serta memahami kapan fungsi kontinu dan kapan terdapat diskontinuitas.

D. Turunan

Turunan menyatakan laju perubahan sesaat suatu fungsi terhadap variabelnya.

Contohnya:

\\[ f(x)=x^2 \quad\Rightarrow\quad f'(x)=2x \\]

Kamu mempelajari definisi turunan, aturan pangkat, aturan hasil kali dan hasil bagi, aturan rantai, serta turunan fungsi implisit.

E. Aplikasi turunan

Turunan digunakan untuk menyelesaikan persoalan nyata, bukan hanya manipulasi rumus.

Topiknya meliputi:

- Menentukan apakah fungsi naik atau turun.
- Mencari nilai maksimum dan minimum.
- Menganalisis kecekungan dan titik belok.
- Menyelesaikan masalah optimasi, misalnya menentukan ukuran yang meminimalkan biaya.

F. Integral

Integral membahas antiturunan dan akumulasi.

Kamu mempelajari integral fungsi aljabar dan transenden serta teknik penyelesaiannya, antara lain substitusi, integral parsial, pecahan parsial, dan substitusi trigonometri.

G. Integral tentu dan Teorema Dasar Kalkulus

Integral tentu menghitung akumulasi fungsi pada suatu interval.

\\[ \int_a^b f(x)\\,dx=F(b)-F(a) \\]

dengan \\(F'(x)=f(x)\\).

Kamu belajar hubungan integral dan turunan, serta penggunaan integral untuk menghitung luas daerah di antara dua kurva dan volume benda putar.

### Target setelah mempelajari Matematika I

Kamu seharusnya mampu menyelesaikan limit, melakukan diferensiasi dan integrasi, menjelaskan makna geometris turunan dan integral, serta memilih metode yang sesuai untuk persoalan kalkulus.

Pertanyaan penting: Apa perbedaan limit, turunan, dan integral? Bagaimana mencari titik maksimum atau minimum? Kapan menggunakan substitusi dan kapan menggunakan integral parsial?

# 6. Bahasa Inggris

Dokumen repo: [Rangkuman Bahasa Inggris](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Bahasa_Inggris/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Bahasa Inggris di semester ini diarahkan pada kemampuan memahami bacaan akademik dan teknis, termasuk teks yang berkaitan dengan teknologi dan ilmu komputer.

Tujuannya bukan hanya menghafal tata bahasa, tetapi juga memahami informasi dan menyampaikan penjelasan teknis secara tepat.

### Urutan materi

A. Stative verbs dan dynamic verbs

Dynamic verbs menunjukkan tindakan atau proses, seperti run, write, dan process. Stative verbs menggambarkan keadaan atau persepsi, seperti know, believe, dan belong.

Perbedaan ini memengaruhi penggunaan bentuk kalimat, terutama bentuk continuous.

B. Tenses utama

Kamu mempelajari fungsi waktu dalam kalimat.

- Simple Present: fakta dan kebiasaan. “The system processes data.”
- Simple Past: kejadian yang sudah selesai. “The system processed the data.”
- Present Perfect: kejadian atau perkembangan yang memiliki hubungan dengan keadaan saat ini. “The system has processed the data.”

C. Passive voice

Kalimat pasif menekankan objek atau proses yang dikenai tindakan.

Contoh:

Active: “The program processes the data.”

Passive: “The data is processed by the program.”

Bentuk ini sering digunakan dalam penjelasan teknis, laporan eksperimen, dan dokumentasi.

D. Conditional sentences

Kalimat pengandaian digunakan untuk menjelaskan hubungan kondisi dan akibat.

- Zero conditional: fakta umum.
- First conditional: kemungkinan realistis di masa depan.
- Second conditional: situasi hipotetis.
- Third conditional: situasi hipotetis yang berkaitan dengan masa lalu.

E. Relative clauses

Relative clauses menambahkan informasi tentang orang, objek, atau konsep. Kamu perlu mengenali kata penghubung seperti who, which, that, dan whose serta perbedaan klausa pembatas dan klausa tambahan.

F. Subject-verb agreement

Subjek dan kata kerja harus cocok dalam jumlah dan bentuknya.

Contoh:

- “The algorithm works.”
- “The algorithms work.”

Materi ini juga mencakup ketepatan struktur kalimat dan pengenalan kesalahan gramatika.

G. Membaca teks ilmiah dan teknis

Pada bagian akhir, kamu menerapkan tata bahasa untuk memahami artikel tentang teknologi, membaca gagasan utama dan detail pendukung, menyimpulkan informasi, serta mengenali kesalahan penulisan.

### Target setelah mempelajari Bahasa Inggris

Kamu seharusnya mampu membaca penjelasan teknis sederhana, mengenali struktur kalimat, memahami informasi utama sebuah artikel, dan menjelaskan konsep Informatika dengan kalimat Inggris yang tepat.

Pertanyaan penting: Kapan menggunakan passive voice? Apa perbedaan simple past dan present perfect? Bagaimana menemukan ide utama sebuah teks teknis?

# 7. Pancasila dan Kewarganegaraan

Dokumen repo: [Rangkuman Pancasila dan Kewarganegaraan](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Pancasila_dan_Kewarganegaraan/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Mata kuliah ini membahas nilai dasar kehidupan berbangsa dan bernegara, termasuk tanggung jawab warga negara serta penerapan etika dalam perkembangan teknologi.

Dalam repository, materinya menggabungkan tema Pendidikan Pancasila dan Pendidikan Kewarganegaraan.

### Urutan materi

A. Sejarah dan perumusan Pancasila

Kamu mempelajari latar belakang historis lahirnya Pancasila, proses perumusan dasar negara, dan kedudukannya dalam kehidupan bangsa Indonesia.

B. Pancasila sebagai sistem filsafat

Pancasila dipelajari melalui dasar pemikiran tentang hakikat manusia, sumber pengetahuan mengenai nilai-nilai bangsa, serta tujuan dan makna nilai tersebut.

Lima sila juga perlu dipahami sebagai kesatuan nilai yang saling berkaitan.

C. Pancasila sebagai ideologi terbuka

Kamu mempelajari Pancasila sebagai dasar yang tetap, tetapi nilai-nilainya dapat diterapkan untuk menghadapi perkembangan masyarakat dan perubahan zaman.

D. Pancasila sebagai sistem etika dan dasar pengembangan ilmu pengetahuan

Bagian ini membahas hubungan antara nilai moral dan kemajuan teknologi.

Dalam Informatika, penerapannya dapat berupa pertanyaan tentang privasi data, keadilan algoritma, penyalahgunaan kecerdasan buatan, keamanan informasi, dan tanggung jawab pengembang perangkat lunak.

E. Identitas nasional

Kamu mempelajari unsur pembentuk identitas bangsa, seperti sejarah, bahasa, kebudayaan, pengalaman sosial, dan simbol kebangsaan.

F. Negara, konstitusi, dan sistem hukum

Kamu mempelajari unsur negara, fungsi konstitusi, serta kedudukan UUD 1945 sebagai hukum dasar negara.

G. Demokrasi, HAM, dan negara hukum

Materinya mencakup kedaulatan rakyat, demokrasi Pancasila, hak asasi manusia, kewajiban warga negara, dan prinsip bahwa penyelenggaraan negara harus berdasarkan hukum.

H. Wawasan Nusantara dan Ketahanan Nasional

Wawasan Nusantara memandang Indonesia sebagai satu kesatuan wilayah dan bangsa. Ketahanan nasional membahas kemampuan bangsa untuk mempertahankan keberlangsungan dan menghadapi berbagai ancaman serta tantangan.

### Target setelah mempelajari mata kuliah ini

Kamu seharusnya mampu menjelaskan kedudukan Pancasila, hubungan antara warga negara dan konstitusi, prinsip dasar demokrasi dan HAM, serta bagaimana nilai Pancasila digunakan untuk menilai dampak perkembangan teknologi.

Pertanyaan penting: Apa fungsi Pancasila sebagai dasar negara? Bagaimana etika Pancasila diterapkan pada AI? Apa perbedaan hak dan kewajiban warga negara?

# 8. Olah Raga

Dokumen repo: [Rangkuman Olah Raga](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/Olah_Raga/RANGKUMAN_MATERI.md)

## Apa yang dipelajari?

Mata kuliah ini merupakan bagian dari pengembangan kebugaran fisik dan kebiasaan hidup sehat. Berbeda dengan mata kuliah teknis, orientasinya lebih banyak pada aktivitas fisik dan praktik.

Secara umum, tujuan pembelajarannya adalah:

A. Kebugaran jasmani

Memahami dan mengembangkan kemampuan tubuh untuk menjalankan aktivitas sehari-hari, termasuk daya tahan, kekuatan, dan kelenturan sesuai dengan kegiatan yang dilakukan.

B. Aktivitas fisik yang teratur

Membangun kebiasaan bergerak secara teratur dan memahami pentingnya menjaga kondisi tubuh selama menjalani kegiatan akademik.

C. Disiplin dan kerja sama

Aktivitas olahraga juga dapat melatih kedisiplinan, mengikuti aturan, menghargai orang lain, serta bekerja sama dalam aktivitas kelompok.

### Target pembelajaran

Memahami pentingnya kebugaran, menjaga kebiasaan hidup aktif, dan mengikuti kegiatan olahraga dengan disiplin. Dokumen repo untuk mata kuliah ini tidak memiliki arsip materi mentah yang tercatat, sehingga detail silabus dan bentuk penilaiannya perlu dicocokkan dengan ketentuan perkuliahanmu.

# 9. Hubungan antara delapan mata kuliah

Meskipun terlihat berbeda, materi semester 1 saling mendukung.

Struktur Diskrit + Logika Informatika + Matematika I

Fondasi penalaran dan matematika

Dasar Pemrograman

Mengubah masalah menjadi algoritma dan fungsi

Dasar Sistem

Memahami bagaimana logika dan data direpresentasikan secara digital

Bahasa Inggris mendukung pembacaan dokumentasi teknis. Pancasila dan Kewarganegaraan membangun pemahaman tanggung jawab sosial dan etika. Olah Raga mendukung kebugaran dan aktivitas fisik.

Contoh hubungan lintas mata kuliah: Struktur Diskrit membantumu memahami graf dan pohon, Dasar Pemrograman mengajarkan cara mengolah struktur tersebut dengan algoritma, Logika Informatika membantumu memeriksa kebenaran kondisi program, dan Dasar Sistem menjelaskan logika digital pada tingkat perangkat keras.

Hubungan seperti ini sangat penting untuk ujian komprehensif karena penguji dapat meminta kamu menjelaskan tidak hanya definisi sebuah konsep, tetapi juga penggunaannya dan hubungannya dengan konsep lain.

# 10. Apa yang harus dikuasai sebelum melanjutkan ke semester 2?

Gunakan daftar periksa ini sebagai target belajar. Tandai suatu materi hanya setelah kamu benar-benar bisa menjelaskannya tanpa bergantung pada rangkuman.

## Checklist penguasaan semester 1

0/20

Dasar Pemrograman

Menjelaskan paradigma fungsional dan prosedural

Menulis fungsi rekursif dengan basis dan rekurens

Mengolah list, himpunan, dan pohon biner

Dasar Sistem

Mengonversi bilangan desimal dan biner

Menggunakan gerbang logika dan tabel kebenaran

Menyederhanakan Boolean dan membedakan rangkaian kombinasional/sekuensial

Logika Informatika

Menghitung tabel kebenaran dan mengenali tautologi

Menerapkan aturan inferensi

Memahami CNF/DNF serta kuantor FOL

Struktur Diskrit

Melakukan operasi himpunan dan memahami relasi/fungsi

Membedakan permutasi dan kombinasi

Memahami induksi, graf, pohon, relasi rekurens, dan modulo

Matematika I

Menghitung limit dan turunan

Menyelesaikan persoalan maksimum/minimum

Menghitung integral dasar dan memahami aplikasinya

Bahasa Inggris

Mengenali tenses, passive voice, dan conditional sentences

Memahami ide utama teks teknis bahasa Inggris

Pancasila dan Kewarganegaraan

Menjelaskan kedudukan Pancasila dan konstitusi

Menghubungkan demokrasi, HAM, dan etika teknologi

Olah Raga

Memahami pentingnya kebugaran dan aktivitas fisik teratur

Reset checklist

## Cara menggunakan rangkuman ini

Saran saya, jangan menghafal seluruh isi sekaligus. Gunakan dokumen ini sebagai peta besar. Pelajari satu mata kuliah pada satu waktu, baca rangkuman asli di repo, kemudian kerjakan contoh soal tanpa melihat pembahasan.

Untuk mata kuliah teknis, prioritaskan latihan menyelesaikan masalah dan menjelaskan setiap langkah. Untuk mata kuliah konseptual, prioritaskan pemahaman definisi, alasan, contoh penerapan, dan hubungan antarkonsep.

Kita mulai dari Dasar Pemrograman terlebih dahulu, karena materi ini membantu membangun cara berpikir algoritmik yang akan digunakan kembali dalam banyak mata kuliah berikutnya. Setelah peta semester 1 ini dipahami, langkah selanjutnya adalah membedah Dasar Pemrograman secara lebih mendalam, dari tipe data sampai rekursi dan pohon biner, disertai contoh dan latihan soal.