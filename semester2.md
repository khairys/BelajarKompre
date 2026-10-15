# RANGKUMAN LENGKAP SEMESTER 2
## S1 Informatika — Universitas Diponegoro

## Gambaran Umum Semester 2

Semester 2 membangun fondasi penting yang akan digunakan kembali pada semester-semester berikutnya. Jika sebelumnya Anda mempelajari pengantar komputer dan pemrograman dasar, sekarang Anda mulai mendalami cara merancang program, memodelkan persoalan menggunakan matematika, memahami eksekusi program oleh CPU, dan menghubungkan perangkat komputasi dengan lingkungan fisik.

Ada tujuh mata kuliah yang dibahas:

1. Algoritma dan Pemrograman.
2. Aljabar Linier.
3. Bahasa Indonesia.
4. Internet of Things.
5. Matematika II.
6. Organisasi dan Arsitektur Komputer.
7. Pendidikan Agama.

Hubungan antarmata kuliah tersebut cukup penting. Algoritma dan Pemrograman mengajarkan cara membuat instruksi. Aljabar Linier dan Matematika II memberikan perangkat matematis untuk menyelesaikan persoalan komputasi. Organisasi dan Arsitektur Komputer menjelaskan bagaimana instruksi dieksekusi. IoT menerapkan komputasi untuk berinteraksi dengan perangkat fisik. Bahasa Indonesia mendukung komunikasi akademik, sedangkan Pendidikan Agama membahas nilai moral dan tanggung jawab.

---

# 1. ALGORITMA DAN PEMROGRAMAN

Sumber: [Rangkuman Algoritma dan Pemrograman](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/Algoritma_dan_Pemrograman/RANGKUMAN_MATERI.md)

## 1.1. Konsep dasar pemrograman prosedural

Algoritma adalah urutan langkah yang terstruktur untuk menyelesaikan suatu masalah. Program adalah implementasi algoritma menggunakan bahasa pemrograman agar dapat dijalankan oleh komputer.

Sebuah algoritma yang baik harus memiliki tujuan jelas, menerima masukan yang sesuai, menghasilkan keluaran yang benar, dan menyelesaikan proses dalam langkah-langkah yang terdefinisi.

Sebagai contoh, untuk menentukan rata-rata tiga nilai, algoritmanya adalah:

1. Membaca tiga nilai.
2. Menjumlahkan ketiga nilai.
3. Membagi jumlah tersebut dengan tiga.
4. Menampilkan hasil.

Dalam paradigma prosedural atau imperatif, program terdiri atas instruksi yang dieksekusi secara berurutan. Variabel menyimpan keadaan yang dapat berubah selama program berjalan.

Berbeda dari paradigma fungsional murni yang mungkin Anda pelajari sebelumnya, C memungkinkan penggunaan perulangan eksplisit, perubahan variabel, pointer, dan pengelolaan memori secara langsung.

## 1.2. Struktur program C

Program C umumnya memiliki fungsi `main()` sebagai titik masuk eksekusi.

```c
#include <stdio.h>

int main(void) {
    int angka = 10;

    printf("%d\n", angka);

    return 0;
}
```

Penjelasan:

- `#include <stdio.h>` menyediakan deklarasi fungsi input/output standar.
- `int main(void)` mendefinisikan fungsi utama.
- `int angka = 10` mendeklarasikan variabel bertipe integer.
- `printf()` menampilkan nilai.
- `return 0` menandakan program selesai secara normal.

Tipe data yang perlu dipahami:

| Tipe data | Fungsi | Contoh |
|---|---|---|
| `int` | Bilangan bulat | `10` |
| `float` | Bilangan pecahan presisi tunggal | `3.14f` |
| `double` | Bilangan pecahan presisi lebih tinggi | `3.141592` |
| `char` | Karakter | `'A'` |

Ukuran tipe tertentu bergantung pada implementasi dan platform. Jangan menganggap semua sistem selalu menggunakan ukuran yang sama.

C juga memanfaatkan operator aritmetika (`+`, `-`, `*`, `/`, `%`), operator perbandingan (`==`, `!=`, `<`, `>`), dan operator logika (`&&`, `||`, `!`).

Perhatikan perbedaan `=` dan `==`. Operator `=` memberikan nilai kepada variabel, sedangkan `==` membandingkan dua nilai.

## 1.3. Percabangan

Percabangan memungkinkan program memilih instruksi berdasarkan suatu kondisi.

Contoh:

```c
if (nilai >= 60) {
    printf("Lulus\n");
} else {
    printf("Tidak lulus\n");
}
```

Struktur yang perlu dikuasai adalah `if`, `if-else`, `if-else if-else`, dan `switch-case`.

`if-else` sesuai untuk kondisi logis dan rentang nilai. `switch-case` sesuai ketika sebuah nilai dibandingkan dengan sejumlah pilihan diskrit.

Contoh lain: apabila nilai lebih dari atau sama dengan 85, mahasiswa mendapat predikat A; jika nilai minimal 75, predikat B; selebihnya mengikuti aturan yang ditentukan.

Urutan kondisi perlu diperhatikan. Jika kondisi umum diperiksa sebelum kondisi yang lebih spesifik, suatu cabang mungkin tidak pernah dijalankan.

Pada `switch-case`, pahami fungsi `break`. Tanpanya, eksekusi bisa berlanjut ke `case` berikutnya (*fall-through*).

## 1.4. Perulangan

Perulangan digunakan untuk mengeksekusi sekumpulan instruksi berulang kali.

| Struktur | Cara kerja | Penggunaan umum |
|---|---|---|
| `for` | Inisialisasi, pemeriksaan kondisi, pembaruan | Iterasi dengan penghitung |
| `while` | Memeriksa kondisi sebelum badan perulangan | Jumlah iterasi belum tentu diketahui |
| `do-while` | Menjalankan badan, kemudian memeriksa kondisi | Badan harus dijalankan minimal sekali |

Contoh:

```c
int total = 0;

for (int i = 1; i <= 5; i++) {
    total += i;
}

printf("%d\n", total);
```

Hasilnya adalah 15 karena program menghitung 1 + 2 + 3 + 4 + 5.

Dua instruksi penting:

- `break` menghentikan perulangan atau keluar dari struktur `switch` yang berlaku.
- `continue` melewati sisa badan iterasi saat ini dan melanjutkan ke iterasi berikutnya.

Kesalahan yang sering muncul adalah *off-by-one error*, yaitu jumlah iterasi berbeda satu langkah dari yang diinginkan. Contohnya, penggunaan `i < 5` berbeda dari `i <= 5`.

## 1.5. Fungsi, prosedur, dan parameter

Fungsi memisahkan tugas program menjadi unit-unit yang lebih kecil sehingga kode lebih mudah dibaca, diuji, dan digunakan kembali.

```c
int tambah(int a, int b) {
    return a + b;
}
```

Fungsi tersebut menerima dua parameter dan mengembalikan hasil penjumlahan.

Di C, subprogram yang tidak mengembalikan nilai biasanya menggunakan tipe `void`.

```c
void tampilkanPesan(void) {
    printf("Halo!\n");
}
```

Hal-hal penting:
- Parameter adalah variabel yang dideklarasikan dalam fungsi.
- Argumen adalah nilai yang dikirim saat fungsi dipanggil.
- Variabel lokal hanya berlaku pada cakupan tempat variabel tersebut dideklarasikan.
- `return` mengembalikan hasil sekaligus mengakhiri eksekusi fungsi terkait.

**Pass-by-value** berarti nilai argumen disalin ke parameter fungsi. Perubahan parameter tersebut tidak mengubah variabel asli pemanggil.

C tidak memiliki pass-by-reference secara langsung seperti pada beberapa bahasa lain. Agar fungsi dapat mengubah variabel asli, alamatnya dapat dikirim menggunakan pointer.

```c
void tambahSatu(int *x) {
    (*x)++;
}
```

Pemanggilan `tambahSatu(&angka)` memungkinkan fungsi mengubah nilai `angka` milik pemanggil.

## 1.6. Tipe data bentukan: `struct`

`struct` menggabungkan beberapa atribut, termasuk yang bertipe berbeda, menjadi satu tipe data.

```c
typedef struct {
    char nim[15];
    char nama[50];
    float ipk;
} Mahasiswa;
```

Satu objek `Mahasiswa` memiliki NIM, nama, dan IPK. Atributnya dapat diakses menggunakan operator titik, misalnya `mhs.ipk`.

Konsep ini berguna untuk merepresentasikan entitas nyata, seperti mahasiswa, produk, transaksi, dan perangkat IoT.

## 1.7. Array dan string

Array menyimpan sejumlah elemen dengan tipe yang sama. Pada C, indeks array dimulai dari nol.

```c
int nilai[4] = {80, 75, 90, 85};
```

Elemen pertama adalah `nilai[0]`, sedangkan elemen terakhir adalah `nilai[3]`.

Array dua dimensi dapat merepresentasikan matriks:

```c
int matriks[2][3];
```

Pengaksesannya biasanya memakai perulangan bersarang: satu untuk baris dan satu untuk kolom.

String pada C direpresentasikan sebagai array karakter yang diakhiri oleh null terminator `'\0'`. Misalnya, string `"Halo"` membutuhkan lima posisi karakter termasuk terminatornya.

Fungsi dari pustaka `<string.h>` yang perlu dikenali antara lain:

- `strlen()` untuk menghitung panjang string sebelum terminator.
- `strcpy()` untuk menyalin string.
- `strcmp()` untuk membandingkan string secara leksikografis.
- `strcat()` untuk menggabungkan string.

Fungsi-fungsi tersebut mensyaratkan penggunaan buffer yang memadai dan string yang valid. Kesalahan pengelolaan ukuran dapat menimbulkan buffer overflow.

## 1.8. Pointer dan memori dinamis

Pointer merupakan variabel yang menyimpan alamat memori.

Dua operator utamanya adalah `&` dan `*`.

```c
int angka = 10;
int *p = &angka;

*p = 25;
```

Setelah kode tersebut dijalankan, `angka` bernilai 25 karena `p` menunjuk ke lokasi memori milik `angka`.

Memori dinamis dialokasikan saat program berjalan, biasanya pada *heap*. Fungsi pentingnya:

| Fungsi | Tujuan |
|---|---|
| `malloc()` | Mengalokasikan blok memori |
| `calloc()` | Mengalokasikan blok dan mengisi byte dengan nol |
| `realloc()` | Mengubah ukuran alokasi |
| `free()` | Membebaskan memori yang dialokasikan secara dinamis |

Contoh:

```c
#include <stdlib.h>

int *data = malloc(5 * sizeof(int));

if (data != NULL) {
    data[0] = 100;
    free(data);
    data = NULL;
}
```

Kesalahan yang wajib dikenali adalah:

- **Memory leak:** memori dialokasikan tetapi tidak dilepaskan ketika sudah tidak dibutuhkan.
- **Dangling pointer:** pointer masih menyimpan alamat memori yang masa pakainya sudah berakhir.
- **Null dereference:** program mencoba mengakses memori melalui pointer null.
- **Out-of-bounds access:** program membaca atau menulis di luar batas alokasi.

## 1.9. Algoritma pencarian

Linear Search memeriksa elemen dari awal satu per satu hingga nilai ditemukan atau data habis.

Kompleksitas waktunya:
- Kasus terbaik: O(1).
- Kasus terburuk: O(n).

Binary Search memeriksa elemen tengah, kemudian membuang setengah ruang pencarian berdasarkan hasil perbandingan.

Kompleksitas waktunya:
- Kasus terbaik: O(1).
- Kasus terburuk: O(log n).

**Syarat utama Binary Search adalah data sudah terurut.** Tanpa kondisi tersebut, keputusan membuang setengah data tidak dapat diandalkan.

Contoh: untuk mencari angka 17 pada daftar yang terurut, Binary Search memeriksa nilai tengah. Jika nilai tengah lebih kecil daripada 17, pencarian dilanjutkan pada separuh kanan; jika lebih besar, pencarian dilanjutkan pada separuh kiri.

## 1.10. Algoritma pengurutan

| Algoritma | Mekanisme | Kompleksitas waktu |
|---|---|---|
| Bubble Sort | Menukar elemen bersebelahan yang urutannya salah | Umumnya O(n²) |
| Selection Sort | Memilih nilai minimum dari bagian yang belum terurut | O(n²) |
| Insertion Sort | Menyisipkan nilai ke bagian yang sudah terurut | Terburuk O(n²) |
| Merge Sort | Membagi array, mengurutkan bagian, lalu menggabungkan | O(n log n) |
| Quick Sort | Mempartisi elemen relatif terhadap pivot | Rata-rata O(n log n), terburuk O(n²) |

Merge Sort biasanya membutuhkan memori tambahan O(n). Quick Sort dapat efisien dalam praktik, tetapi kinerja sangat dipengaruhi cara memilih pivot.

Untuk ujian, jangan hanya menghafal kompleksitas. Anda perlu bisa menjalankan satu atau dua langkah algoritma pada array tertentu dan menunjukkan hasil setiap tahap.

## 1.11. Pemrosesan file

Pemrosesan file memungkinkan data tetap tersedia setelah program selesai.

Fungsi penting:
- `fopen()` membuka file.
- `fclose()` menutup file.
- `fprintf()` menulis teks terformat.
- `fscanf()` membaca data terformat.
- `fgets()` membaca baris atau bagian teks.

Mode umum:
- `r`: membaca file yang ada.
- `w`: menulis; membuat file baru atau menimpa isi file.
- `a`: menambahkan data ke akhir file.

Selalu periksa apakah file berhasil dibuka. File harus ditutup dengan benar setelah digunakan.

### Target penguasaan Algoritma dan Pemrograman

Anda perlu mampu menulis program C sederhana hingga menengah; menggunakan fungsi, array, `struct`, dan pointer; menjelaskan alur kontrol; melakukan pencarian dan pengurutan; serta membaca atau menulis file dengan aman.

---

# 2. ALJABAR LINIER

Sumber: [Rangkuman Aljabar Linier](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/Aljabar_Linier/RANGKUMAN_MATERI.md)

Aljabar Linier mempelajari vektor dan matriks, sistem persamaan linier, ruang vektor, serta transformasi linier. Materi ini digunakan dalam machine learning, grafika komputer, analisis data, kriptografi, dan pemrosesan citra.

## 2.1. Vektor

Vektor dapat dipandang sebagai susunan komponen yang merepresentasikan besaran atau titik dalam ruang berdimensi tertentu.

Misalnya:

\[
\mathbf{u}=(2,3),\qquad \mathbf{v}=(4,1)
\]

Penjumlahan dilakukan berdasarkan komponen:

\[
\mathbf{u}+\mathbf{v}=(6,4)
\]

Perkalian skalar juga dilakukan terhadap setiap komponen:

\[
3\mathbf{u}=(6,9)
\]

### Norma atau panjang vektor

Untuk vektor \(\mathbf{v}=(v_1,\ldots,v_n)\):

\[
\|\mathbf{v}\|=\sqrt{v_1^2+\cdots+v_n^2}
\]

Jika \(\mathbf{v}=(3,4)\), panjang vektornya adalah 5.

### Dot product

\[
\mathbf{u}\cdot\mathbf{v}
=\sum_{i=1}^{n}u_i v_i
=\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta
\]

Dot product menghasilkan bilangan skalar. Untuk dua vektor nonnol, dot product bernilai nol jika keduanya ortogonal.

Contoh:

\[
(1,2)\cdot(2,-1)=2-2=0
\]

Jadi, kedua vektor tersebut saling tegak lurus.

### Proyeksi dan cross product

Proyeksi ortogonal \(\mathbf{u}\) pada \(\mathbf{a}\) adalah:

\[
\operatorname{proj}_{\mathbf{a}}\mathbf{u}
=\frac{\mathbf{u}\cdot\mathbf{a}}
{\|\mathbf{a}\|^2}\mathbf{a}
\]

Cross product digunakan pada vektor tiga dimensi dan menghasilkan vektor yang tegak lurus terhadap kedua vektor masukan.

## 2.2. Sistem persamaan linier

Sistem persamaan linier dapat dinyatakan dalam bentuk:

\[
A\mathbf{x}=\mathbf{b}
\]

- \(A\) adalah matriks koefisien.
- \(\mathbf{x}\) adalah vektor variabel.
- \(\mathbf{b}\) adalah vektor konstanta.

Sistem ini dapat ditulis sebagai matriks augmented \([A\mid\mathbf{b}]\).

Penyelesaian dapat dilakukan dengan operasi baris elementer:
1. Menukar dua baris.
2. Mengalikan satu baris dengan konstanta bukan nol.
3. Menambahkan kelipatan satu baris ke baris lain.

**Eliminasi Gauss** mengubah matriks menjadi bentuk eselon baris, kemudian menggunakan substitusi balik.

**Eliminasi Gauss–Jordan** melanjutkan eliminasi hingga bentuk eselon baris tereduksi.

Tiga kemungkinan solusi:
- Solusi tunggal.
- Tidak ada solusi, misalnya muncul persamaan \(0=5\).
- Tak hingga banyak solusi, misalnya satu persamaan merupakan kelipatan persamaan lainnya dan sistem konsisten.

## 2.3. Matriks, determinan, dan invers

Matriks merepresentasikan data atau transformasi dalam susunan baris dan kolom.

Jika \(A\) berukuran \(m\times p\), dan \(B\) berukuran \(p\times n\), perkalian \(AB\) menghasilkan matriks berukuran \(m\times n\).

Perkalian matriks umumnya tidak komutatif:

\[
AB\neq BA
\]

Determinan didefinisikan untuk matriks persegi. Untuk matriks 2 × 2:

\[
A=
\begin{bmatrix}
a&b\\c&d
\end{bmatrix}
\]

\[
\det(A)=ad-bc
\]

Matriks memiliki invers jika determinannya tidak nol:

\[
A^{-1}A=AA^{-1}=I
\]

Invers dapat dicari menggunakan Gauss–Jordan dengan:

\[
[A\mid I]\longrightarrow[I\mid A^{-1}]
\]

Jika \(\det(A)=0\), matriks tersebut singular dan tidak memiliki invers.

## 2.4. Ruang vektor dan subruang

Ruang vektor adalah himpunan objek yang mendukung operasi penjumlahan dan perkalian skalar sesuai aksioma tertentu.

Subruang adalah bagian dari ruang vektor yang tetap menjadi ruang vektor dengan operasi yang diwariskan.

Uji subruang yang praktis mencakup:
- Memuat vektor nol.
- Tertutup terhadap penjumlahan.
- Tertutup terhadap perkalian skalar.

Ketiga kondisi ini perlu dipenuhi untuk subruang vektor.

## 2.5. Kombinasi linier, span, dan independensi

Kombinasi linier dari vektor dapat ditulis sebagai:

\[
\mathbf{v}=c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k
\]

Span adalah himpunan seluruh kombinasi linier yang dapat dibentuk dari suatu himpunan vektor.

Untuk menguji kebebasan linier, periksa:

\[
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k=\mathbf{0}
\]

Jika satu-satunya solusi adalah \(c_1=\cdots=c_k=0\), himpunan tersebut bebas linier. Jika terdapat solusi nontrivial, himpunannya bergantung linier.

## 2.6. Basis, dimensi, rank, dan nullity

Basis adalah himpunan vektor yang:
1. Bebas linier.
2. Merentang ruang vektor yang sedang dibahas.

Dimensi adalah jumlah vektor pada suatu basis.

Bagi matriks \(A\) yang berukuran \(m\times n\), rank adalah dimensi ruang baris maupun ruang kolom. Nullity adalah dimensi ruang solusi \(A\mathbf{x}=\mathbf{0}\).

Teorema rank-nullity menyatakan:

\[
\operatorname{rank}(A)+
\operatorname{nullity}(A)=n
\]

dengan \(n\) sebagai jumlah kolom matriks.

## 2.7. Eigenvalue, eigenvector, dan transformasi linier

Eigenvalue \(\lambda\) dan eigenvector tak nol \(\mathbf{v}\) memenuhi:

\[
A\mathbf{v}=\lambda\mathbf{v}
\]

Persamaan karakteristik untuk mendapatkan eigenvalue adalah:

\[
\det(A-\lambda I)=0
\]

Setelah memperoleh eigenvalue, cari eigenvector dengan menyelesaikan:

\[
(A-\lambda I)\mathbf{v}=\mathbf{0}
\]

Konsep eigen digunakan dalam PCA untuk reduksi dimensi, grafika komputer, analisis jaringan, dan sejumlah metode komputasi lainnya.

Transformasi linier adalah pemetaan yang mempertahankan struktur penjumlahan dan perkalian skalar. Kernel merupakan himpunan masukan yang dipetakan ke vektor nol, sedangkan range merupakan himpunan hasil yang dapat dicapai.

### Target penguasaan Aljabar Linier

Anda harus dapat melakukan operasi vektor dan matriks, menyelesaikan SPL, menghitung determinan dan invers, menguji independensi linier, mencari basis dan dimensi, serta menyelesaikan persoalan eigenvalue sederhana.

---

# 3. BAHASA INDONESIA

Sumber: [Rangkuman Bahasa Indonesia](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/Bahasa_Indonesia/RANGKUMAN_MATERI.md)

Mata kuliah ini membangun kemampuan berbahasa akademik. Bagi mahasiswa Informatika, keterampilan tersebut digunakan ketika menulis laporan praktikum, spesifikasi sistem, laporan penelitian, artikel ilmiah, dan skripsi.

## 3.1. Kedudukan dan fungsi Bahasa Indonesia

Bahasa Indonesia berfungsi sebagai bahasa nasional dan bahasa negara.

Sebagai bahasa nasional, Bahasa Indonesia berperan sebagai identitas dan pemersatu bangsa serta sarana komunikasi antardaerah.

Sebagai bahasa negara, Bahasa Indonesia digunakan dalam urusan resmi kenegaraan dan pendidikan sesuai ketentuan yang berlaku.

## 3.2. Bahasa yang baik dan benar

Kedua konsep ini berkaitan, tetapi berbeda.

**Bahasa yang baik** menyesuaikan penggunaan bahasa dengan konteks, tujuan, dan lawan bicara.

**Bahasa yang benar** mematuhi kaidah bahasa baku, termasuk tata bahasa dan ejaan.

Dalam skripsi, laporan teknis, atau seminar ilmiah, penulis perlu memilih ragam formal dan mengikuti kaidah bahasa baku.

## 3.3. Ejaan dan penulisan kata

Hal-hal yang perlu dikuasai:
- Huruf kapital untuk awal kalimat, nama diri, dan penggunaan lain sesuai kaidah.
- Tanda baca, khususnya koma dan titik.
- Kata depan `di`, `ke`, dan `dari` ditulis terpisah apabila menunjukkan tempat atau arah.
- Awalan `di-` ditulis serangkai dengan kata kerja pasif.

Contoh:

- Benar: *Data disimpan di server.*
- Benar: *Aplikasi dijalankan di komputer laboratorium.*

Pada kalimat pertama, `di server` menunjukkan tempat, sedangkan `disimpan` merupakan kata kerja pasif.

## 3.4. Kalimat efektif

Kalimat efektif menyampaikan gagasan secara tepat, jelas, logis, dan tidak berlebihan.

Ciri pentingnya:
1. Kesepadanan struktur, termasuk kejelasan subjek dan predikat.
2. Kesejajaran bentuk atau paralelisme.
3. Kehematan kata.
4. Ketepatan makna.
5. Kelogisan.
6. Tidak menimbulkan ambiguitas.

Contoh tidak efektif:

"Tahapan penelitian meliputi pengumpulan data, menganalisis algoritma, dan pengujian sistem."

Bentuk yang lebih sejajar:

"Tahapan penelitian meliputi pengumpulan data, analisis algoritma, dan pengujian sistem."

Ketiga unsur tersebut mengikuti bentuk yang sepadan.

## 3.5. Paragraf dan argumentasi

Paragraf idealnya memiliki satu gagasan utama yang didukung kalimat-kalimat penjelas.

Paragraf deduktif menyampaikan gagasan utama pada awal paragraf, sedangkan paragraf induktif membangun penjelasan terlebih dahulu dan menyampaikan simpulan di akhir.

Dua istilah penting:
- **Kohesi:** keterpaduan bentuk bahasa, misalnya penggunaan kata rujukan dan kata penghubung.
- **Koherensi:** keterkaitan makna dan logika antargagasan.

Penulisan ilmiah harus didukung argumen yang relevan, data yang memadai, dan penalaran yang dapat diperiksa.

## 3.6. Membaca kritis dengan SQ3R

SQ3R adalah metode membaca sistematis:

1. **Survey:** memindai judul, abstrak, subjudul, dan kesimpulan.
2. **Question:** menyusun pertanyaan tentang informasi yang perlu ditemukan.
3. **Read:** membaca secara aktif untuk menjawab pertanyaan.
4. **Recite:** menjelaskan kembali isi dengan kata-kata sendiri.
5. **Review:** meninjau ulang gagasan penting dan memeriksa pemahaman.

Metode ini berguna ketika membaca banyak artikel ilmiah, terutama saat mencari research gap atau membandingkan penelitian terdahulu.

## 3.7. Sistematika karya ilmiah

Struktur umum skripsi yang dijelaskan dalam materi mencakup:

**Bab I — Pendahuluan:** latar belakang, rumusan masalah, batasan masalah, tujuan, dan manfaat.

**Bab II — Tinjauan Pustaka:** penelitian terdahulu serta teori yang mendukung penelitian.

**Bab III — Metodologi:** rancangan eksperimen atau metode pengembangan, dataset, tahapan penelitian, serta teknik evaluasi.

**Bab IV — Hasil dan Pembahasan:** hasil pengujian, analisis data, interpretasi, dan hubungan hasil dengan tujuan penelitian.

**Bab V — Penutup:** kesimpulan dan saran.

Kesimpulan harus menjawab rumusan masalah berdasarkan hasil yang diperoleh, bukan menambahkan klaim baru yang belum dibahas.

## 3.8. Kutipan dan integritas akademik

Kutipan langsung menggunakan kata-kata sumber, sedangkan kutipan tidak langsung atau parafrasa menyampaikan kembali gagasan sumber dengan struktur dan redaksi sendiri.

Keduanya tetap memerlukan atribusi yang benar.

Gaya sitasi yang disebut dalam materi antara lain:
- IEEE, lazim menggunakan nomor seperti `[1]`.
- APA, menggunakan pola penulis dan tahun.

Referensi harus konsisten dengan kutipan dalam teks. Menyalin ide atau tulisan orang lain tanpa mengakui sumber dapat menjadi pelanggaran integritas akademik.

Materi juga membahas metode pidato dan presentasi, seperti membaca naskah, menghafal, berbicara spontan, atau berbicara menggunakan kerangka.

### Target penguasaan Bahasa Indonesia

Anda harus mampu memperbaiki kalimat tidak efektif, menyusun paragraf yang logis, menjelaskan struktur laporan ilmiah, menggunakan sitasi yang konsisten, dan merangkum artikel tanpa kehilangan makna utama.

---

# 4. INTERNET OF THINGS (IoT)

Sumber: [Rangkuman Internet of Things](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/Internet_of_Things/RANGKUMAN_MATERI.md)

Internet of Things adalah pendekatan yang menghubungkan objek fisik dengan sistem komputasi melalui sensor, mikrokontroler, jaringan, dan aplikasi.

Contohnya sistem penyiraman tanaman otomatis. Sensor mengukur kelembapan tanah, mikrokontroler membaca hasil pengukuran, kemudian sistem menyalakan pompa jika kondisi memenuhi aturan tertentu.

## 4.1. Arsitektur IoT

Arsitektur empat lapisan yang digunakan dalam rangkuman repo adalah:

**1. Perception/Sensing Layer**

Berinteraksi dengan dunia fisik menggunakan sensor, aktuator, RFID, atau kamera.

**2. Network/Transmission Layer**

Mengirimkan data melalui jaringan seperti Wi-Fi, Bluetooth Low Energy, Zigbee, LoRaWAN, atau jaringan seluler.

**3. Middleware/Data Processing Layer**

Mengolah, menyimpan, mengatur, dan meneruskan data. Lapisan ini dapat mencakup layanan backend, broker pesan, database, serta komputasi cloud.

**4. Application Layer**

Menyediakan antarmuka dan fungsi untuk pengguna, seperti dashboard, notifikasi, laporan, atau kendali perangkat.

Implementasi nyata dapat menggabungkan beberapa fungsi dalam satu layanan atau menggunakan arsitektur dengan jumlah lapisan berbeda. Model empat lapisan tersebut berfungsi sebagai kerangka konseptual.

## 4.2. Mikrokontroler dan ESP32

ESP32 adalah keluarga sistem pada chip yang banyak digunakan dalam proyek IoT karena menyediakan kemampuan pemrosesan dan konektivitas, termasuk Wi-Fi dan Bluetooth pada varian yang sesuai.

Antarmuka perangkat keras yang penting:

| Antarmuka | Fungsi |
|---|---|
| GPIO | Input/output digital |
| ADC | Mengubah sinyal analog menjadi nilai digital |
| DAC | Menghasilkan keluaran analog pada perangkat yang mendukungnya |
| PWM | Mengatur keluaran melalui duty cycle |
| UART | Komunikasi serial asinkron |
| I2C | Komunikasi menggunakan jalur SDA dan SCL |
| SPI | Komunikasi serial sinkron berkecepatan tinggi |

Pada ADC 12-bit, terdapat \(2^{12}=4096\) kode digital, yaitu 0 hingga 4095.

PWM lazim digunakan untuk mengendalikan kecerahan LED dan kecepatan motor pada rangkaian yang sesuai. Duty cycle adalah proporsi periode sinyal ketika sinyal berada pada keadaan aktif.

I2C menggunakan jalur data SDA dan clock SCL, sementara SPI lazim menggunakan MOSI, MISO, SCK, dan jalur pemilih chip seperti CS/SS.

## 4.3. Sensor dan aktuator

**Sensor** mengukur keadaan lingkungan. Contohnya:
- DHT11/DHT22 untuk suhu dan kelembapan.
- BME280 untuk pengukuran lingkungan melalui antarmuka digital.
- HC-SR04 untuk pengukuran jarak ultrasonik.
- PIR untuk mendeteksi perubahan radiasi inframerah akibat pergerakan.
- LDR untuk mendeteksi intensitas cahaya.

Untuk sensor ultrasonik, jarak diperkirakan dari waktu tempuh suara pulang-pergi:

\[
\text{Jarak (cm)}
\approx
\frac{\text{Waktu (mikrodetik)}\times0{,}0343}{2}
\]

Pembagian dua diperlukan karena suara bergerak dari sensor ke objek, kemudian kembali ke sensor.

**Aktuator** menghasilkan tindakan fisik. Contohnya relay, motor servo, dan pompa.

Perangkat bertegangan rendah tidak boleh langsung dihubungkan ke beban bertegangan tinggi tanpa rangkaian pengendali dan perlindungan yang sesuai.

## 4.4. MQTT dan HTTP

HTTP menggunakan model request–response. Klien mengirim permintaan, kemudian server mengembalikan respons.

MQTT menggunakan model publish–subscribe:
- **Publisher** mengirim pesan.
- **Broker** menerima dan meneruskan pesan.
- **Subscriber** menerima pesan dari topic yang dilanggani.
- **Topic** mengidentifikasi kategori atau jalur pesan.

Contoh topic: `kampus/lab/suhu`.

Tiga tingkat QoS MQTT:

- **QoS 0 — At most once:** pesan dikirim tanpa konfirmasi penerimaan pada tingkat protokol MQTT tersebut; overhead rendah, tetapi pesan dapat hilang.
- **QoS 1 — At least once:** pengiriman menggunakan konfirmasi; pesan dapat diterima lebih dari sekali.
- **QoS 2 — Exactly once:** menggunakan pertukaran pesan tambahan untuk menjamin pengiriman tepat sekali dalam konteks protokolnya, dengan overhead paling besar.

Pilihan QoS bergantung pada kebutuhan keandalan dan biaya komunikasi.

| Aspek | HTTP | MQTT |
|---|---|---|
| Pola komunikasi | Request–response | Publish–subscribe |
| Perantara | Biasanya server layanan | Broker pesan |
| Penggunaan umum | API web dan permintaan data | Telemetri serta komunikasi perangkat |
| Kelebihan | Model sederhana dan luas penggunaannya | Efisien untuk pesan kecil dan banyak klien |

Protokol lainnya:
- **CoAP:** protokol untuk perangkat terbatas yang menggunakan model REST dan biasanya berjalan di atas UDP.
- **WebSocket:** memungkinkan komunikasi dua arah melalui koneksi persisten.

## 4.5. Cloud dan data sensor

Data sensor biasanya mempunyai cap waktu (*timestamp*), sehingga dapat diperlakukan sebagai data deret waktu atau *time-series*.

Contohnya:
- Suhu setiap detik.
- Kelembapan setiap menit.
- Konsumsi energi setiap jam.

Sistem dapat menyimpan data tersebut untuk visualisasi, analisis tren, deteksi anomali, dan pemicu notifikasi.

Contoh teknologi yang dicantumkan repo antara lain InfluxDB, TimescaleDB, ThingsBoard, Grafana, dan broker MQTT. Setiap teknologi mempunyai fungsi berbeda; tidak semuanya merupakan jenis komponen yang sama.

## 4.6. Keamanan IoT

Risiko IoT meliputi:
- Kata sandi bawaan yang tidak diganti.
- Komunikasi tanpa enkripsi.
- Kebocoran token atau kredensial.
- Firmware rentan dan pembaruan yang tidak aman.
- Akses perangkat oleh pihak yang tidak berwenang.
- Pengambilalihan perangkat untuk dijadikan bagian botnet.

Mitigasi mencakup penggunaan kredensial unik, autentikasi, otorisasi, enkripsi TLS saat sesuai, pembaruan firmware yang aman, dan pembatasan akses jaringan.

### Target penguasaan IoT

Anda harus mampu menjelaskan aliran data dari sensor hingga aplikasi, membedakan fungsi mikrokontroler dan server, memilih protokol komunikasi, menghitung jarak pada contoh sensor ultrasonik, serta menjelaskan keamanan perangkat.

---

# 5. MATEMATIKA II — KALKULUS PEUBAH BANYAK

Sumber: [Rangkuman Matematika II](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/Matematika_II/RANGKUMAN_MATERI.md)

Matematika II memperluas kalkulus satu variabel ke fungsi dengan beberapa variabel. Konsep ini sangat penting untuk optimasi, machine learning, analisis citra, dan grafika komputer.

## 5.1. Geometri ruang tiga dimensi

Sebuah vektor di ruang tiga dimensi dapat dituliskan sebagai:

\[
\mathbf{v}=(a,b,c)
\]

Garis yang melalui titik \(P_0=(x_0,y_0,z_0)\) dan memiliki vektor arah \((a,b,c)\) dapat ditulis secara parametrik:

\[
\begin{aligned}
x&=x_0+at\\
y&=y_0+bt\\
z&=z_0+ct
\end{aligned}
\]

Bidang dengan vektor normal \((a,b,c)\) yang melalui titik \(P_0\) mempunyai persamaan:

\[
a(x-x_0)+b(y-y_0)+c(z-z_0)=0
\]

Vektor normal menunjukkan arah yang tegak lurus terhadap bidang. Konsep ini mendukung analisis posisi, geometri 3D, dan pencahayaan dalam grafika komputer.

## 5.2. Fungsi peubah banyak dan turunan parsial

Fungsi dua variabel mempunyai bentuk:

\[
z=f(x,y)
\]

Turunan parsial terhadap \(x\) menghitung perubahan fungsi terhadap \(x\) dengan memperlakukan variabel lain sebagai konstanta.

Contoh:

\[
f(x,y)=x^2y+3y^2
\]

Turunan parsialnya:

\[
\frac{\partial f}{\partial x}=2xy
\]

\[
\frac{\partial f}{\partial y}=x^2+6y
\]

Prinsipnya sama seperti turunan biasa, tetapi variabel yang tidak sedang diturunkan diperlakukan sebagai konstanta.

Turunan parsial campuran dapat berupa \(f_{xy}\) dan \(f_{yx}\). Untuk fungsi yang cukup mulus di sekitar titik yang dibahas, kedua turunan campuran tersebut sama menurut teorema Clairaut/Schwarz.

## 5.3. Gradien dan turunan berarah

Gradien fungsi dua variabel didefinisikan sebagai:

\[
\nabla f=
\left\langle
\frac{\partial f}{\partial x},
\frac{\partial f}{\partial y}
\right\rangle
\]

Untuk contoh sebelumnya:

\[
\nabla f=\langle2xy,x^2+6y\rangle
\]

Gradien menunjukkan arah kenaikan lokal tercepat suatu fungsi yang terdiferensialkan. Besar gradien menunjukkan laju kenaikan maksimum pada titik tersebut.

Jika \(\mathbf{u}\) merupakan vektor satuan, turunan arah fungsi adalah:

\[
D_{\mathbf{u}}f=\nabla f\cdot\mathbf{u}
\]

Penting: arah untuk turunan berarah perlu menggunakan vektor satuan. Jika vektor arah awal belum memiliki panjang satu, normalkan terlebih dahulu.

Konsep ini menjadi fondasi gradient descent, yaitu prosedur optimasi yang memperbarui parameter ke arah penurunan fungsi kerugian.

## 5.4. Bidang singgung dan garis normal

Untuk permukaan implisit:

\[
F(x,y,z)=c
\]

gradien \(\nabla F\) pada titik yang sesuai berperan sebagai vektor normal permukaan.

Persamaan bidang singgung pada titik \((x_0,y_0,z_0)\) adalah:

\[
F_x(x_0,y_0,z_0)(x-x_0)
+F_y(x_0,y_0,z_0)(y-y_0)
+F_z(x_0,y_0,z_0)(z-z_0)=0
\]

Rumus tersebut digunakan ketika permukaan dinyatakan secara implisit dan gradien tidak nol pada titik yang dibahas.

## 5.5. Optimasi fungsi dua variabel

Titik kritis fungsi terdiferensialkan dapat dicari dengan menyelesaikan:

\[
f_x=0,\qquad f_y=0
\]

Setelah titik kritis didapat, gunakan turunan kedua:

\[
D=f_{xx}f_{yy}-(f_{xy})^2
\]

Interpretasinya:

- \(D>0\) dan \(f_{xx}>0\): minimum lokal.
- \(D>0\) dan \(f_{xx}<0\): maksimum lokal.
- \(D<0\): saddle point atau titik pelana.
- \(D=0\): uji tidak memberikan kesimpulan; dibutuhkan analisis tambahan.

Contoh:

\[
f(x,y)=x^2+y^2
\]

Gradiennya nol pada \((0,0)\). Karena \(f_{xx}=2\), \(f_{yy}=2\), dan \(f_{xy}=0\), diperoleh \(D=4>0\). Karena \(f_{xx}>0\), titik tersebut adalah minimum lokal, sekaligus minimum global untuk fungsi ini.

## 5.6. Optimasi berkendala dengan pengali Lagrange

Pengali Lagrange digunakan ketika nilai fungsi hendak dimaksimalkan atau diminimalkan dengan kendala tertentu.

Untuk fungsi objektif \(f(x,y,z)\) dengan kendala \(g(x,y,z)=c\), persamaan yang dicari adalah:

\[
\nabla f=\lambda\nabla g
\]

bersama dengan:

\[
g(x,y,z)=c
\]

Nilai \(\lambda\) adalah pengali Lagrange.

Secara intuitif, pada kandidat ekstrem berkendala yang memenuhi syarat kehalusan, gradien fungsi objektif sejajar dengan gradien fungsi kendala.

Metode ini banyak digunakan dalam persoalan optimasi sumber daya, geometri, dan machine learning.

## 5.7. Integral lipat dua

Integral lipat dua:

\[
\iint_R f(x,y)\,dA
\]

mengakumulasi nilai fungsi pada daerah dua dimensi \(R\). Jika \(f(x,y)\geq0\), integral tersebut dapat ditafsirkan sebagai volume di bawah permukaan \(z=f(x,y)\) di atas daerah \(R\).

Untuk daerah persegi panjang, Teorema Fubini memungkinkan integral dihitung secara bertahap:

\[
\iint_R f(x,y)\,dA
=
\int_a^b\int_c^d f(x,y)\,dy\,dx
\]

dengan batas sesuai daerah integrasi.

Pada daerah umum, Anda perlu menentukan batas integral berdasarkan bentuk geometris wilayah tersebut.

## 5.8. Koordinat polar

Transformasi koordinat polar:

\[
x=r\cos\theta,\qquad y=r\sin\theta
\]

Elemen luasnya adalah:

\[
dA=r\,dr\,d\theta
\]

Faktor \(r\) merupakan faktor Jacobian dan tidak boleh dihilangkan.

Koordinat polar sangat berguna untuk daerah berbentuk lingkaran atau bagian lingkaran.

Sebagai contoh, luas lingkaran berjari-jari \(R\) dapat dihitung dengan:

\[
A=\int_0^{2\pi}\int_0^R r\,dr\,d\theta
=\pi R^2
\]

## 5.9. Aplikasi integral lipat

Integral lipat dapat menghitung:
- Luas daerah, dengan mengintegralkan fungsi 1.
- Volume di bawah permukaan.
- Massa pelat tipis jika distribusi rapat massanya diketahui.
- Pusat massa melalui integral momen yang sesuai.

Untuk rapat massa \(\rho(x,y)\), massa total adalah:

\[
m=\iint_R\rho(x,y)\,dA
\]

Koordinat pusat massa diperoleh dengan membagi momen terhadap masing-masing sumbu dengan massa total, jika massa positif dan integralnya terdefinisi.

### Target penguasaan Matematika II

Anda perlu mahir menurunkan fungsi multivariabel, menghitung gradien, menentukan titik kritis, menggunakan uji turunan kedua, menerapkan pengali Lagrange, serta menghitung integral lipat pada daerah yang tepat.

---

# 6. ORGANISASI DAN ARSITEKTUR KOMPUTER

Sumber: [Rangkuman Organisasi dan Arsitektur Komputer](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/Organisasi_dan_Arsitektur_Komputer/RANGKUMAN_MATERI.md)

Mata kuliah ini menjelaskan hubungan antara perangkat lunak dan perangkat keras. Program yang Anda tulis akhirnya diterjemahkan menjadi instruksi mesin, kemudian diproses oleh CPU dan berinteraksi dengan memori serta perangkat I/O.

## 6.1. Perbedaan arsitektur dan organisasi komputer

**Arsitektur komputer** mengacu pada karakteristik yang terlihat oleh pemrogram pada tingkat instruksi, seperti instruction set, tipe data, dan mode pengalamatan.

**Organisasi komputer** menjelaskan bagaimana fitur tersebut direalisasikan melalui komponen perangkat keras, sirkuit, jalur data, unit kontrol, serta struktur memori.

Keduanya berkaitan, tetapi tidak identik. Dua prosesor dengan arsitektur instruksi yang sama masih dapat mempunyai organisasi internal dan kinerja yang berbeda.

## 6.2. Arsitektur Von Neumann

Model Von Neumann menggunakan konsep stored-program, yaitu instruksi program dan data disimpan dalam memori yang sama.

CPU terdiri atas:
- **ALU:** menjalankan operasi aritmetika dan logika.
- **Control Unit:** mengendalikan operasi serta aliran instruksi.
- **Register:** menyimpan operand, alamat, dan informasi yang diperlukan selama eksekusi.

Register penting:
- **PC (Program Counter):** menyimpan alamat instruksi berikutnya.
- **IR (Instruction Register):** menyimpan instruksi yang sedang diproses.
- **MAR (Memory Address Register):** menyimpan alamat memori yang hendak diakses.
- **MDR/MBR (Memory Data/Buffer Register):** menampung data yang dibaca dari atau ditulis ke memori.

## 6.3. Siklus instruksi

Siklus dasar instruksi terdiri dari:

1. **Fetch:** CPU mengambil instruksi dari memori.
2. **Decode:** unit kontrol menafsirkan instruksi.
3. **Execute:** CPU menjalankan operasi.
4. **Interrupt handling:** jika ada interupsi yang perlu dilayani, CPU melakukan penanganan sesuai mekanisme sistem.

Contoh: instruksi penjumlahan mengambil nilai operand yang diperlukan, menjalankan operasi melalui unit aritmetika, kemudian menyimpan hasil ke lokasi tujuan.

Interupsi memungkinkan perangkat atau kejadian tertentu meminta perhatian CPU tanpa harus menunggu CPU memeriksa perangkat terus-menerus.

## 6.4. Mengukur kinerja CPU

Rumus waktu eksekusi CPU:

\[
\text{CPU Time}
=\frac{\text{Instruction Count}\times\text{CPI}}
{\text{Clock Rate}}
\]

Keterangan:
- **Instruction Count (IC):** jumlah instruksi yang dijalankan.
- **CPI:** rata-rata siklus clock per instruksi.
- **Clock Rate:** frekuensi clock prosesor.

Kinerja tidak ditentukan oleh frekuensi clock saja. Jumlah instruksi, CPI, arsitektur, dan perilaku memori ikut memengaruhi waktu eksekusi.

### Hukum Amdahl

Hukum Amdahl menjelaskan batas percepatan jika hanya sebagian pekerjaan dapat dipercepat:

\[
S=\frac{1}{(1-f)+f/k}
\]

\(f\) adalah proporsi pekerjaan yang dipercepat, sedangkan \(k\) adalah faktor percepatan pada bagian tersebut. Bagian yang tidak dipercepat tetap membatasi kinerja keseluruhan.

## 6.5. Hirarki memori dan lokalitas

Susunan umum memori dari yang paling dekat dengan CPU hingga penyimpanan sekunder adalah:

**Register → Cache → RAM → SSD/HDD.**

Secara umum, tingkat yang lebih dekat dengan CPU lebih cepat, berkapasitas lebih kecil, dan lebih mahal per satuan penyimpanan.

Cache bekerja efektif karena adanya dua prinsip lokalitas:

- **Lokalitas temporal:** data atau instruksi yang baru diakses kemungkinan akan diakses kembali.
- **Lokalitas spasial:** lokasi memori di sekitar alamat yang diakses berpotensi segera dibutuhkan.

Contohnya, perulangan yang berulang kali menggunakan variabel dan array berurutan cenderung memperlihatkan kedua jenis lokalitas tersebut.

## 6.6. Cache memory

Cache menyimpan salinan blok memori utama agar akses berikutnya dapat dilakukan lebih cepat.

- **Hit:** data ditemukan di cache.
- **Miss:** data tidak ditemukan dan perlu diambil dari tingkat memori berikutnya.
- **Hit rate:** proporsi akses yang menghasilkan hit.
- **Miss rate:** proporsi akses yang menghasilkan miss.
- **Miss penalty:** biaya tambahan akibat miss.

Average Memory Access Time:

\[
\text{AMAT}
=\text{Hit Time}
+(\text{Miss Rate}\times\text{Miss Penalty})
\]

Tiga metode pemetaan cache:

**Direct mapping:** sebuah blok memori utama hanya dapat dipetakan ke satu lokasi cache tertentu.

\[
\text{Line Number}
=\text{Block Address}
\bmod \text{Number of Lines}
\]

**Fully associative:** blok dapat ditempatkan pada line mana saja yang tersedia.

**Set-associative:** blok ditentukan ke satu set tertentu, tetapi dapat ditempatkan pada salah satu line di set itu.

Metode tersebut memiliki trade-off antara kompleksitas perangkat keras, fleksibilitas penempatan, dan potensi conflict miss.

Kebijakan penggantian mencakup LRU dan FIFO. Pada kebijakan penulisan:
- **Write-through:** pembaruan cache diteruskan langsung ke memori utama.
- **Write-back:** pembaruan ditahan di cache hingga blok perlu ditulis kembali, biasanya dengan bantuan dirty bit.

## 6.7. ISA dan mode pengalamatan

Instruction Set Architecture (ISA) mendefinisikan operasi yang dapat dijalankan prosesor.

Instruksi biasanya mencakup opcode, yaitu kode operasi, serta informasi operand sumber atau tujuan.

Mode pengalamatan utama:

- **Immediate:** nilai operand tercantum langsung pada instruksi.
- **Direct:** alamat operand diberikan langsung.
- **Indirect:** instruksi merujuk lokasi yang menyimpan alamat operand sebenarnya.
- **Register:** operand tersimpan di register.
- **Register indirect:** register menyimpan alamat operand.
- **Base/displacement:** alamat efektif dihitung dari isi register dan offset.

Mode pengalamatan menentukan bagaimana CPU menemukan operand yang dibutuhkan instruksi.

## 6.8. RISC dan CISC

RISC (*Reduced Instruction Set Computer*) menekankan instruksi yang relatif sederhana dan mendukung desain pipeline yang efisien.

CISC (*Complex Instruction Set Computer*) menyediakan instruksi yang lebih kaya dan dapat memiliki panjang atau kompleksitas yang bervariasi.

Contoh arsitektur yang sering digunakan untuk pembahasan RISC adalah ARM, MIPS, dan RISC-V. x86 merupakan contoh keluarga ISA CISC.

Perbedaan tersebut menjelaskan pendekatan desain; kinerja prosesor modern tidak dapat disimpulkan hanya dari label RISC atau CISC.

## 6.9. Pipeline dan hazards

Pipeline membagi eksekusi instruksi menjadi tahap-tahap yang dapat berjalan tumpang tindih.

Model lima tahap yang umum:

1. **IF:** Instruction Fetch.
2. **ID:** Instruction Decode dan pembacaan register.
3. **EX:** Eksekusi atau perhitungan alamat.
4. **MEM:** Akses memori data.
5. **WB:** Write Back hasil ke register.

Pipeline meningkatkan throughput ketika tahapan bekerja dengan baik, tetapi tidak otomatis membuat setiap instruksi individu selesai lima kali lebih cepat.

Hambatan pipeline:

- **Structural hazard:** dua operasi memperebutkan sumber daya perangkat keras yang sama.
- **Data hazard:** suatu instruksi membutuhkan hasil instruksi sebelumnya yang belum tersedia.
- **Control hazard:** percabangan membuat aliran instruksi berikutnya belum pasti.

Penanganan dapat berupa forwarding, stall, dan branch prediction sesuai penyebab hambatannya.

## 6.10. Transfer input/output

Tiga teknik penting:

**Programmed I/O:** CPU memeriksa status perangkat dan mengelola transfer melalui program, yang dapat membuang waktu saat menunggu.

**Interrupt-driven I/O:** perangkat memberi sinyal interupsi saat perlu dilayani sehingga CPU tidak harus melakukan polling terus-menerus.

**Direct Memory Access (DMA):** pengendali DMA dapat memindahkan blok data antara perangkat I/O dan memori tanpa CPU mengelola setiap unit data secara individual.

### Target penguasaan Organisasi dan Arsitektur Komputer

Anda harus mampu menjelaskan siklus instruksi, fungsi register, menghitung CPU time dan AMAT, membandingkan metode cache, membedakan RISC dengan CISC, serta menjelaskan pipeline, hazards, interrupt, dan DMA.

---

# 7. PENDIDIKAN AGAMA

Sumber: [Rangkuman Pendidikan Agama](https://github.com/khairys/BelajarKompre/blob/main/RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/Pendidikan_Agama/RANGKUMAN_MATERI.md)

Catatan: berkas dalam repo secara khusus merangkum Pendidikan Agama Islam. Mahasiswa yang mengikuti pendidikan agama lain mempelajari materi sesuai agama masing-masing.

Mata kuliah ini menekankan pembentukan integritas, tanggung jawab, etika, serta hubungan antara ilmu pengetahuan dan kehidupan bermasyarakat.

## 7.1. Konsep ketuhanan dan tauhid

Dalam materi Islam, tauhid dibahas melalui tiga dimensi:

- **Rububiyah:** meyakini Allah sebagai Pencipta dan Pengatur alam semesta.
- **Uluhiyah:** mengesakan Allah dalam ibadah.
- **Asma wa Sifat:** mengimani nama dan sifat Allah sebagaimana diajarkan dalam sumber ajaran Islam.

Materi ini menjadi bagian dari pembahasan akidah.

## 7.2. Hakikat manusia

Materi membahas unsur jasmani dan rohani manusia serta perannya sebagai hamba Allah dan khalifah di bumi.

Gagasan tersebut menghubungkan tanggung jawab personal dan sosial: manusia tidak hanya dituntut mengembangkan kemampuan, tetapi juga menggunakan kemampuan tersebut secara bertanggung jawab.

## 7.3. Sumber ajaran Islam

Tiga kelompok sumber utama yang dibahas ialah:

1. **Al-Qur'an:** sumber utama ajaran Islam.
2. **Hadis/Sunnah:** perkataan, perbuatan, dan ketetapan Nabi yang menjelaskan atau melengkapi pemahaman terhadap ajaran.
3. **Ijtihad:** upaya penalaran untuk menetapkan hukum pada persoalan yang memerlukan kajian lebih lanjut.

Contoh metode penalaran dalam ijtihad adalah ijma', qiyas, dan maslahah mursalah.

## 7.4. Hukum taklifi

Lima kategori yang perlu dikenal:

| Kategori | Makna umum |
|---|---|
| Wajib | Harus dilaksanakan |
| Sunnah | Dianjurkan untuk dilaksanakan |
| Mubah | Diperbolehkan |
| Makruh | Dianjurkan untuk ditinggalkan |
| Haram | Dilarang |

Dalam kajian Islam, setiap kategori memiliki konsekuensi normatif yang berbeda.

## 7.5. Akhlak, moral, dan etika

Ketiganya berkaitan dengan penilaian dan perilaku, tetapi memiliki penekanan yang berbeda.

Etika mengkaji penalaran mengenai baik dan buruk. Moral berkaitan dengan norma yang berkembang dalam masyarakat. Akhlak dalam materi Islam berkaitan dengan karakter dan perilaku berdasarkan ajaran agama.

Contoh akhlak terpuji mencakup kejujuran, amanah, keadilan, dan kerendahan hati. Perilaku tercela meliputi kebohongan, pengkhianatan, kesombongan, dan iri dengki.

## 7.6. Islam, ilmu pengetahuan, dan teknologi

Penguasaan teknologi dapat diarahkan untuk memberikan manfaat kepada masyarakat.

Dalam konteks Informatika, penerapan nilai moral meliputi:
- Menjaga privasi pengguna.
- Tidak memanipulasi data.
- Tidak menyebarkan hoaks.
- Menjaga kejujuran akademik.
- Menghindari penyalahgunaan AI dan sistem digital.
- Memperhatikan dampak teknologi terhadap orang lain.

Materi juga membahas toleransi antarumat beragama, masyarakat madani, serta kesejahteraan sosial melalui instrumen seperti zakat, infak, sedekah, dan wakaf (ZISWAF).

### Target penguasaan Pendidikan Agama

Anda perlu mampu menjelaskan konsep-konsep utama sesuai silabus agama yang ditempuh, serta menerapkan nilai moral pada kasus kehidupan akademik dan penggunaan teknologi.

---

# 8. SINTESIS SEMESTER 2

Tujuh mata kuliah di Semester 2 membentuk fondasi yang saling melengkapi.

| Bidang | Pertanyaan mendasar yang dijawab |
|---|---|
| Algoritma dan Pemrograman | Bagaimana masalah diselesaikan melalui instruksi? |
| Aljabar Linier | Bagaimana vektor dan matriks memodelkan data dan transformasi? |
| Bahasa Indonesia | Bagaimana gagasan disampaikan secara akurat dan ilmiah? |
| Internet of Things | Bagaimana sistem komputasi berinteraksi dengan dunia fisik? |
| Matematika II | Bagaimana perubahan dan optimasi fungsi multivariabel dianalisis? |
| Organisasi dan Arsitektur Komputer | Bagaimana instruksi dijalankan oleh perangkat keras? |
| Pendidikan Agama | Bagaimana ilmu dan teknologi digunakan secara bertanggung jawab? |

Contoh integrasi antarmata kuliah adalah sistem pemantauan suhu ruangan.

Program C atau perangkat lunak terkait mengatur logika proses. Sensor dan mikrokontroler membaca suhu. Jaringan mengirimkan data ke server. Basis matematis diperlukan jika data hendak dianalisis atau digunakan untuk optimasi. Pengetahuan arsitektur komputer menjelaskan eksekusi instruksi. Data dan hasil pengujian kemudian dilaporkan secara akademik, dengan tetap memperhatikan etika dan tanggung jawab.

Dengan kata lain, Semester 2 tidak hanya mengajarkan cara menulis kode. Semester ini mulai menghubungkan algoritma, matematika, hardware, komunikasi data, dan tanggung jawab penggunaan teknologi.

---

# 9. DAFTAR RUMUS DAN KONSEP YANG WAJIB DIKUASAI

## Algoritma dan Pemrograman

- Linear Search: kasus terburuk O(n).
- Binary Search: kasus terburuk O(log n), dengan syarat data terurut.
- Merge Sort: O(n log n).
- Quick Sort: rata-rata O(n log n), kasus terburuk O(n²).
- Pointer: pahami perbedaan `&` dan `*`, serta aturan masa hidup memori.

## Aljabar Linier

- Norma vektor:

  \[
  \|\mathbf{v}\|=\sqrt{\sum_i v_i^2}
  \]

- Dot product:

  \[
  \mathbf{u}\cdot\mathbf{v}=\sum_i u_i v_i
  \]

- Invers matriks persegi ada jika \(\det(A)\neq0\).
- Persamaan eigen:

  \[
  \det(A-\lambda I)=0
  \]

- Rank-nullity:

  \[
  \operatorname{rank}(A)+\operatorname{nullity}(A)=n
  \]

## Matematika II

- Gradien:

  \[
  \nabla f=\langle f_x,f_y\rangle
  \]

- Turunan arah:

  \[
  D_{\mathbf{u}}f=\nabla f\cdot\mathbf{u}
  \]

- Uji titik kritis:

  \[
  D=f_{xx}f_{yy}-(f_{xy})^2
  \]

- Pengali Lagrange:

  \[
  \nabla f=\lambda\nabla g
  \]

- Koordinat polar:

  \[
  x=r\cos\theta,\quad y=r\sin\theta,\quad dA=r\,dr\,d\theta
  \]

## Organisasi dan Arsitektur Komputer

- Waktu CPU:

  \[
  \text{CPU Time}=
  \frac{IC\times CPI}{\text{Clock Rate}}
  \]

- AMAT:

  \[
  \text{AMAT}=\text{Hit Time}+
  (\text{Miss Rate}\times\text{Miss Penalty})
  \]

- Hukum Amdahl:

  \[
  S=\frac{1}{(1-f)+f/k}
  \]

## Internet of Things

- ADC 12-bit memiliki 4096 tingkat kode digital.
- Jarak HC-SR04, bila waktu diberikan dalam mikrodetik:

  \[
  d\approx\frac{t\times0{,}0343}{2}\text{ cm}
  \]

- MQTT: bedakan publisher, broker, subscriber, topic, dan QoS 0/1/2.

---

# 10. CHECKLIST PERSIAPAN UJIAN SEMESTER 2

Gunakan checklist berikut untuk menilai penguasaan Anda.

### Algoritma dan Pemrograman
- [ ] Saya mampu membaca alur program C dan memprediksi hasilnya.
- [ ] Saya dapat menulis percabangan, perulangan, fungsi, dan `struct`.
- [ ] Saya memahami array, string, pointer, dan memori dinamis.
- [ ] Saya dapat menelusuri linear search, binary search, dan sorting.
- [ ] Saya memahami operasi file dasar.

### Aljabar Linier
- [ ] Saya dapat melakukan operasi vektor dan matriks.
- [ ] Saya dapat menyelesaikan SPL dengan eliminasi Gauss.
- [ ] Saya dapat menentukan determinan dan invers.
- [ ] Saya memahami ruang vektor, span, independensi, basis, dan dimensi.
- [ ] Saya dapat menyelesaikan soal eigenvalue sederhana.

### Bahasa Indonesia
- [ ] Saya mampu membedakan bahasa yang baik dengan bahasa yang benar.
- [ ] Saya dapat memperbaiki kalimat tidak efektif.
- [ ] Saya memahami struktur karya ilmiah.
- [ ] Saya dapat menyusun parafrasa dan sitasi secara benar.
- [ ] Saya memahami metode SQ3R.

### Internet of Things
- [ ] Saya dapat menjelaskan arsitektur IoT empat lapisan.
- [ ] Saya memahami fungsi sensor, aktuator, dan mikrokontroler.
- [ ] Saya dapat membedakan GPIO, ADC, PWM, UART, I2C, dan SPI.
- [ ] Saya memahami MQTT, HTTP, dan QoS MQTT.
- [ ] Saya dapat mengidentifikasi risiko keamanan IoT.

### Matematika II
- [ ] Saya dapat menghitung turunan parsial dan gradien.
- [ ] Saya dapat menghitung turunan arah.
- [ ] Saya dapat menentukan dan mengklasifikasikan titik kritis.
- [ ] Saya dapat menyelesaikan optimasi berkendala dasar.
- [ ] Saya dapat menyusun batas integral lipat dan menggunakan koordinat polar.

### Organisasi dan Arsitektur Komputer
- [ ] Saya memahami siklus fetch–decode–execute.
- [ ] Saya mengetahui fungsi register utama CPU.
- [ ] Saya dapat menghitung waktu CPU dan AMAT.
- [ ] Saya dapat membedakan metode pemetaan cache.
- [ ] Saya memahami RISC, CISC, pipeline, hazards, interrupt, dan DMA.

### Pendidikan Agama
- [ ] Saya memahami materi inti sesuai silabus agama yang saya tempuh.
- [ ] Saya dapat menjelaskan hubungan nilai moral dengan penggunaan teknologi.
- [ ] Saya dapat menganalisis contoh persoalan integritas akademik dan tanggung jawab sosial.

---

## Penutup

Target akhir Semester 2 adalah mampu berpindah dari pemahaman konsep menuju penerapan. Untuk materi pemrograman dan matematika, utamakan latihan penyelesaian masalah secara langsung. Untuk organisasi komputer dan IoT, latih penjelasan alur kerja sistem dari awal hingga akhir. Untuk Bahasa Indonesia dan Pendidikan Agama, pastikan Anda mampu menjelaskan konsep dan menerapkannya dalam situasi nyata.

Rangkuman ini adalah peta belajar menyeluruh. Untuk persiapan ujian yang lebih kuat, cocokkan penguasaan setiap bagian dengan berkas `CONTOH_SOAL_DAN_PEMBAHASAN.md` pada mata kuliah terkait di repo, khususnya latihan hitungan, penelusuran algoritma, dan pembahasan kasus.
