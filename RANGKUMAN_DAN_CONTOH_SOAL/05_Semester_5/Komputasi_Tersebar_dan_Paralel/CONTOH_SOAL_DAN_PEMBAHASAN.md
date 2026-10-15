# Bank Contoh Soal & Pembahasan: Komputasi Tersebar dan Paralel

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Komputasi Tersebar dan Paralel Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Dr. Retno Kusumaningrum, S.Si., M.Kom., Adhe Setya Pramayuda, S.Kom., M.T., dkk. & Bank Soal HMIF 2019–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (JAM LOGIKA LAMPORT & BULLY ELECTION)

### Soal UTS 1: Perhitungan Jam Logika Lamport pada Diagram Ruang-Waktu (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan 3 buah proses terdistribusi: $P_1, P_2, P_3$ dengan urutan kejadian (*events*) sebagai berikut:
* Pada proses $P_1$:
  * Terjadi event internal $a$.
  * Terjadi event pengiriman pesan $b$ yang mengirim pesan $m_1$ ke proses $P_2$.
  * Terjadi event internal $c$.
* Pada proses $P_2$:
  * Terjadi event pengiriman pesan $d$ yang mengirim pesan $m_2$ ke proses $P_3$.
  * Terjadi event penerimaan pesan $e$ (menerima pesan $m_1$ dari $P_1$).
  * Terjadi event internal $f$.
* Pada proses $P_3$:
  * Terjadi event internal $g$.
  * Terjadi event penerimaan pesan $h$ (menerima pesan $m_2$ dari $P_2$).
  * Terjadi event internal $i$.

Semua jam logika proses diinisialisasi dengan nilai awal $0$.
1. Hitung nilai jam logika Lamport $L(e)$ untuk setiap event: $a, b, c, d, e, f, g, h, i$!
2. Apakah event $a$ mendahului kausal (*happens-before*) event $f$? Buktikan berdasarkan relasi transitif Lamport!
3. Apakah event $c$ dan event $i$ memiliki relasi kausalitas atau bersifat konkuren ($c \parallel i$)? Jelaskan!

**Kunci Pembahasan & Solusi:**
1. **Aturan Jam Logika Lamport:**
   * Aturan 1 (Internal): $L_i = L_i + 1$.
   * Aturan 2 (Kirim): Sebelum kirim, naikkan jam $L_i = L_i + 1$, lalu sertakan nilai tersebut pada pesan $m$.
   * Aturan 3 (Terima): Penerima $j$ memperbarui jam: $L_j = \max(L_j, L_{\text{pesan}}) + 1$.

   *Langkah Perhitungan:*
   * **Proses $P_1$:**
     * Event $a$: Event internal $\implies L(a) = 0 + 1 = \mathbf{1}$.
     * Event $b$: Event kirim pesan $m_1 \implies L(b) = 1 + 1 = \mathbf{2}$. (Pesan $m_1$ membawa timestamp 2).
     * Event $c$: Event internal $\implies L(c) = 2 + 1 = \mathbf{3}$.
   * **Proses $P_2$:**
     * Event $d$: Event kirim pesan $m_2 \implies L(d) = 0 + 1 = \mathbf{1}$. (Pesan $m_2$ membawa timestamp 1).
     * Event $e$: Event terima pesan $m_1$ (timestamp 2) $\implies L(e) = \max(L(d), L(m_1)) + 1 = \max(1, 2) + 1 = \mathbf{3}$.
     * Event $f$: Event internal $\implies L(f) = 3 + 1 = \mathbf{4}$.
   * **Proses $P_3$:**
     * Event $g$: Event internal $\implies L(g) = 0 + 1 = \mathbf{1}$.
     * Event $h$: Event terima pesan $m_2$ (timestamp 1) $\implies L(h) = \max(L(g), L(m_2)) + 1 = \max(1, 1) + 1 = \mathbf{2}$.
     * Event $i$: Event internal $\implies L(i) = 2 + 1 = \mathbf{3}$.

   *Ringkasan Nilai Jam Lamport:*
   * $P_1$: $L(a)=1, L(b)=2, L(c)=3$
   * $P_2$: $L(d)=1, L(e)=3, L(f)=4$
   * $P_3$: $L(g)=1, L(h)=2, L(i)=3$

2. **Pengujian Kausalitas $a \rightarrow f$:**
   * $a$ dan $b$ berada di proses yang sama ($P_1$) dan $a$ sebelum $b \implies a \rightarrow b$.
   * $b$ adalah pengiriman pesan $m_1$ dan $e$ adalah penerimaan pesan $m_1 \implies b \rightarrow e$.
   * $e$ dan $f$ berada di proses yang sama ($P_2$) dan $e$ sebelum $f \implies e \rightarrow f$.
   * Berdasarkan sifat transitif: karena $a \rightarrow b \rightarrow e \rightarrow f$, maka terbukti secara kausal mutlak bahwa $\mathbf{a \rightarrow f}$.

3. **Pengujian Hubungan Event $c$ dan Event $i$:**
   * Nilai $L(c) = 3$ dan $L(i) = 3$.
   * Tidak ada rantai pesan langsung maupun tak langsung yang menghubungkan antara $c$ dan $i$.
   * Informasi dari $c$ tidak dapat mempengaruhi $i$, dan sebaliknya.
   * Kesimpulan: Event $c$ dan event $i$ bersifat **KONKUREN ($c \parallel i$)**.

---

### Soal UTS 2: Algoritma Pemilihan Pemimpin (Bully Leader Election)
**Deskripsi Soal:**
Sebuah cluster sistem terdistribusi terdiri dari 6 buah proses dengan identitas ID: $P_1, P_2, P_3, P_4, P_5, P_6$ di mana $P_6$ sebelumnya bertindak sebagai Koordinator Utama.
Tiba-tiba proses $P_6$ mengalami kecelakaan fisik (*crash / mati*).
Proses $P_3$ menyadari kematian $P_6$ ketika mencoba mengirimkan pesan permintaan dan mengalami timeout.
Jelaskan alur tahapan pelaksanaan **Algoritma Bully** yang diprakarsai oleh $P_3$ hingga terpilih koordinator baru yang sah!

**Kunci Pembahasan & Solusi:**
1. **Tahap 1 (Inisiasi Pemilihan oleh $P_3$):**
   * Karena $P_3$ mendeteksi kegagalan koordinator, $P_3$ memicu pemilihan (*election*) dengan mengirim pesan `ELECTION` ke semua proses yang memiliki **ID lebih tinggi** darinya, yaitu ke $P_4, P_5,$ dan $P_6$.
2. **Tahap 2 (Respon Proses Bertingkat Lebih Tinggi):**
   * Proses $P_6$ sudah mati, sehingga tidak merespon apapun.
   * Proses $P_4$ dan $P_5$ yang masih aktif menerima pesan dari $P_3$.
   * Keduanya mengirim pesan balasan `OK (Answer)` kepada $P_3$ yang menandakan: *"Saya masih hidup dan ID saya lebih tinggi, biar saya yang mengambil alih proses pemilihan"*.
   * Dengan diterimanya pesan `OK`, tugas $P_3$ selesai (ia pasrah menunggu pengumuman hasil).
3. **Tahap 3 (Proses $P_4$ & $P_5$ Memulai Pemilihan Sendiri):**
   * Proses $P_4$ mengirim pesan `ELECTION` ke proses ber-ID lebih tinggi: $P_5$ dan $P_6$.
   * Proses $P_5$ membalas `OK` kepada $P_4$. Maka $P_4$ pasrah.
   * Proses $P_5$ mengirim pesan `ELECTION` ke proses ber-ID lebih tinggi darinya, yaitu $P_6$.
4. **Tahap 4 (Deklarasi Pemimpin Baru oleh $P_5$):**
   * $P_5$ menunggu balasan dari $P_6$ hingga batas waktu (*timeout*).
   * Karena $P_6$ mati, tidak ada pesan balasan yang tiba.
   * Karena tidak ada satupun proses dengan ID lebih tinggi yang merespon, maka **$P_5$ mendeklarasikan dirinya sebagai Koordinator Baru**.
5. **Tahap 5 (Pengumuman Koordinator):**
   * $P_5$ menyiarkan (*broadcast*) pesan `COORDINATOR` ke seluruh proses yang masih hidup: $P_1, P_2, P_3,$ dan $P_4$.
   * Seluruh sistem kini mengakui $P_5$ sebagai pemimpin sah yang baru.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (HUKUM AMDAHL & MODEL MAPREDUCE)

### Soal UAS 1: Analisis Batas Peningkatan Kecepatan (Hukum Amdahl)
**Deskripsi Soal:**
Sebuah program simulasi dinamika fluida komputasional memiliki waktu eksekusi sekuensial total 100 detik pada satu prosesor tunggal.
Berdasarkan profil kode, diketahui bahwa:
* $80\%$ dari total waktu eksekusi merupakan perhitungan matriks intensif yang **dapat dibagi secara paralel sempurna (*perfectly parallelizable*)**.
* $20\%$ sisanya merupakan pembacaan file input dan penulisan output disk yang **mutlak harus dijalankan secara serial (*strictly sequential*)**.

**Tugas:**
1. Hitung peningkatan kecepatan (*Speedup*) dan waktu eksekusi jika program dijalankan pada komputer dengan **4 prosesor**!
2. Hitung Speedup dan waktu eksekusi jika menggunakan **16 prosesor**!
3. Hitung **Batas Maksimal Peningkatan Kecepatan Teoritis ($\text{Speedup}_{\max}$)** jika kita menggunakan jumlah prosesor tak berhingga ($N \to \infty$)!

**Kunci Pembahasan & Solusi:**
Berdasarkan Hukum Amdahl:
$$\text{Speedup} = \frac{1}{(1 - p) + \frac{p}{N}}$$
Diketahui: porsi paralel $p = 0.80$, porsi serial $(1 - p) = 0.20$, waktu awal $T_1 = 100$ detik.

1. **Untuk $N = 4$ Prosesor:**
   $$\text{Speedup}_4 = \frac{1}{0.20 + \frac{0.80}{4}} = \frac{1}{0.20 + 0.20} = \frac{1}{0.40} = \mathbf{2.5\times}$$
   Waktu eksekusi baru:
   $$T_4 = \frac{T_1}{\text{Speedup}_4} = \frac{100}{2.5} = \mathbf{40 \text{ detik}}$$

2. **Untuk $N = 16$ Prosesor:**
   $$\text{Speedup}_{16} = \frac{1}{0.20 + \frac{0.80}{16}} = \frac{1}{0.20 + 0.05} = \frac{1}{0.25} = \mathbf{4.0\times}$$
   Waktu eksekusi baru:
   $$T_{16} = \frac{100}{4.0} = \mathbf{25 \text{ detik}}$$

3. **Batas Maksimal Teoritis ($N \to \infty$):**
   $$\text{Speedup}_{\max} = \lim_{N \to \infty} \frac{1}{(1 - p) + \frac{p}{N}} = \frac{1}{1 - p} = \frac{1}{0.20} = \mathbf{5.0\times}$$
   Waktu eksekusi minimum absolut:
   $$T_{\min} = \frac{100}{5.0} = \mathbf{20 \text{ detik}}$$
   *Wawasan Penting:* Berapapun banyaknya miliaran prosesor yang ditambahkan, program tersebut tidak akan pernah bisa berjalan lebih cepat dari 20 detik karena dibatasi oleh 20% kode serialnya.

---

### Soal UAS 2: Desain Pemrosesan Big Data MapReduce (Word Count & Inverted Index)
**Deskripsi Soal:**
Diberikan dua dokumen teks masukan dalam cluster HDFS:
* Dokumen 1 (`Doc1`): `"informatika undip jaya"`
* Dokumen 2 (`Doc2`): `"belajar informatika undip"`

Tuliskan alur kerja lengkap fungsi **Map**, fase **Shuffle & Sort**, dan fungsi **Reduce** dalam pseudokode formal untuk menghasilkan rekapitulasi frekuensi kemunculan setiap kata (*WordCount*)!

**Kunci Pembahasan & Solusi:**
1. **Fase Map:**
   * Diimplementasikan oleh fungsi `map(document_id, text)`:
     ```text
     function map(String key, String value):
         for each word w in value.split():
             EmitIntermediate(w, 1)
     ```
   * *Keluaran Map Worker 1 (Doc1):*
     `("informatika", 1), ("undip", 1), ("jaya", 1)`
   * *Keluaran Map Worker 2 (Doc2):*
     `("belajar", 1), ("informatika", 1), ("undip", 1)`

2. **Fase Shuffle & Sort (Dikelola Otomatis oleh Framework Terdistribusi):**
   Sistem mengumpulkan semua tuple keluaran worker, mengurutkan berdasarkan kunci, dan mengelompokkan nilai-nilai dengan kunci yang sama ke dalam list:
   * `"belajar"` $\rightarrow [1]$
   * `"informatika"` $\rightarrow [1, 1]$
   * `"jaya"` $\rightarrow [1]$
   * `"undip"` $\rightarrow [1, 1]$

3. **Fase Reduce:**
   * Diimplementasikan oleh fungsi `reduce(word, list_of_counts)`:
     ```text
     function reduce(String key, Iterator values):
         int sum = 0
         for each v in values:
             sum += v
         Emit(key, sum)
     ```
   * *Hasil Akhir Reducer:*
     * `("belajar", 1)`
     * `("informatika", 2)`
     * `("jaya", 1)`
     * `("undip", 2)`

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan Teorema CAP dan mengapa basis data terdistribusi modern di internet (seperti Google Spanner atau Apache Cassandra) tidak mungkin mencapai konsistensi kuat dan ketersediaan 100% secara bersamaan saat terjadi partisi jaringan?"
**Jawaban Komprehensif:**
* Teorema CAP membuktikan bahwa saat terjadi **Partisi Jaringan (*Network Partition - P*)**—yaitu ketika kabel jaringan putus atau paket antar-node terisolasi menjadi dua kelompok terpisah—arsitektur sistem secara matematis dipaksa memilih antara:
  1. **Memilih Ketersediaan (*Availability - AP*):** Kedua kelompok node yang terisolasi tetap melayani permintaan baca dan tulis dari pengguna lokal masing-masing. Namun, data pada kelompok $A$ tidak bisa disinkronkan ke kelompok $B$. Akibatnya, terjadi perbedaan versi data (*Inconsistency / Split-Brain*).
  2. **Memilih Konsistensi (*Consistency - CP*):** Demi memastikan tidak ada pembacaan data usang, kelompok node yang kehilangan kuorum mayoritas menolak seluruh permintaan tulis dan mengembalikan error (*Service Unavailable*). Ketersediaan sistem dikorbankan demi menjaga integritas data yang akurat.
* Karena di dunia nyata kabel optik bawah laut atau switch router pasti memiliki probabilitas gagal (*Partition Tolerance is non-negotiable*), maka sistem mustahil menjamin $C$ dan $A$ secara simultan saat partisi tersebut terjadi.

### Q2: "Jelaskan perbedaan model memori bersama (Shared Memory / OpenMP) dan model pengiriman pesan (Distributed Memory / MPI) serta kapan kita memilih salah satunya!"
**Jawaban Komprehensif:**
* **Shared Memory (OpenMP):**
  * Semua unit prosesor/thread berbagi satu ruang alamat memori fisik yang sama (RAM bersama).
  * Komunikasi antar-thread sangat cepat melalui variabel memori langsung.
  * *Kelemahan:* Dibatasi oleh kapasitas fisik satu motherboard server tunggal (skalabilitas vertikal terbatas) dan rentan *race conditions*.
* **Distributed Memory (MPI):**
  * Setiap prosesor berada pada komputer/server yang berbeda dengan RAM pribadi masing-masing yang terisolasi.
  * Komunikasi data antar-simpul wajib dilakukan secara eksplisit melalui pengiriman paket pesan di jaringan (*network sockets*).
  * *Kelebihan:* Skalabilitas tak terbatas (dapat menghubungkan puluhan ribu server komoditas membentuk superkomputer cluster).
* **Kapan Memilih:** Gunakan **OpenMP** untuk memaksimalkan performa aplikasi multi-core pada satu unit PC/server kerja workstation. Gunakan **MPI** untuk komputasi berskala raksasa (simulasi cuaca, pelatihan AI model besar, analisis genomik) yang melampaui kapasitas RAM dan prosesor satu mesin fisik.
