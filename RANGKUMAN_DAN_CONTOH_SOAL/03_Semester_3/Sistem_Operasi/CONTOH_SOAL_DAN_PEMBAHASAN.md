# Bank Contoh Soal & Pembahasan: Sistem Operasi

> Sumber rujukan: Bank soal UTS & UAS Sistem Operasi Departemen Informatika Universitas Diponegoro (Koleksi HMIF & Dosen Pengampu Sisop, 2018–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (PENJADWALAN CPU & SINKRONISASI)

### Soal UTS 1: Komparasi Penjadwalan CPU (FCFS, SRTF & Round Robin)
**Deskripsi Soal:**
Diberikan 4 proses yang tiba pada waktu kedatangan (*Arrival Time - AT*) dan durasi waktu eksekusi CPU (*Burst Time - BT*) dalam satuan milidetik berikut:

| Proses | Arrival Time (ms) | Burst Time (ms) |
|:---:|:---:|:---:|
| $P_1$ | 0 | 8 |
| $P_2$ | 1 | 4 |
| $P_3$ | 2 | 9 |
| $P_4$ | 3 | 5 |

1. Gambarkan **Gantt Chart** dan hitunglah **Average Waiting Time (AWT)** untuk algoritma **FCFS (First-Come, First-Served)**!
2. Gambarkan **Gantt Chart** dan hitunglah **Average Waiting Time (AWT)** untuk algoritma **SRTF (Shortest Remaining Time First / Preemptive SJF)**!
3. Gambarkan **Gantt Chart** untuk algoritma **Round Robin (RR)** dengan time quantum $q = 4\text{ ms}$!

**Kunci Pembahasan & Solusi:**
1. **Analisis Algoritma FCFS:**
   * Urutan kedatangan: $P_1(0) \rightarrow P_2(1) \rightarrow P_3(2) \rightarrow P_4(3)$.
   * **Gantt Chart FCFS:**
     `[  P1 (0 - 8)  |  P2 (8 - 12)  |  P3 (12 - 21)  |  P4 (21 - 26)  ]`
   * **Perhitungan Waiting Time ($WT = \text{Start Time} - \text{Arrival Time}$):**
     * $WT(P_1) = 0 - 0 = 0\text{ ms}$
     * $WT(P_2) = 8 - 1 = 7\text{ ms}$
     * $WT(P_3) = 12 - 2 = 10\text{ ms}$
     * $WT(P_4) = 21 - 3 = 18\text{ ms}$
     $$\mathbf{AWT_{\text{FCFS}} = \frac{0 + 7 + 10 + 18}{4} = \frac{35}{4} = 8.75\text{ ms}}$$
2. **Analisis Algoritma SRTF (Preemptive):**
   * $t = 0$: $P_1$ masuk (sisa BT: 8).
   * $t = 1$: $P_2$ tiba (BT: 4). Sisa $P_1 = 7$. Karena $4 < 7$, $P_1$ dipotong (*preempted*), $P_2$ dieksekusi.
   * $t = 2$: $P_3$ tiba (BT: 9). Sisa $P_2 = 3$. $P_2$ lanjut jalan.
   * $t = 3$: $P_4$ tiba (BT: 5). Sisa $P_2 = 2$. $P_2$ lanjut jalan.
   * $t = 5$: $P_2$ selesai! Proses siap: $P_4(\text{sisa } 5), P_1(\text{sisa } 7), P_3(\text{sisa } 9)$. Terpendek adalah $P_4$.
   * $t = 10$: $P_4$ selesai! Proses siap: $P_1(\text{sisa } 7), P_3(\text{sisa } 9)$. Terpendek adalah $P_1$.
   * $t = 17$: $P_1$ selesai! Terakhir eksekusi $P_3$.
   * $t = 26$: $P_3$ selesai.
   * **Gantt Chart SRTF:**
     `[ P1 (0-1) | P2 (1-5) | P4 (5-10) | P1 (10-17) | P3 (17-26) ]`
   * **Perhitungan Waiting Time ($WT = \text{Completion Time} - AT - BT$):**
     * $WT(P_1) = 17 - 0 - 8 = 9\text{ ms}$
     * $WT(P_2) = 5 - 1 - 4 = 0\text{ ms}$
     * $WT(P_3) = 26 - 2 - 9 = 15\text{ ms}$
     * $WT(P_4) = 10 - 3 - 5 = 2\text{ ms}$
     $$\mathbf{AWT_{\text{SRTF}} = \frac{9 + 0 + 15 + 2}{4} = \frac{26}{4} = 6.50\text{ ms}}$$
     *(SRTF lebih cepat 2.25 ms dibanding FCFS!).*
3. **Analisis Round Robin ($q = 4\text{ ms}$):**
   * $t=0$: Jalankan $P_1$ selama $4\text{ ms}$ ($0 - 4$). Sisa $P_1 = 4$. Antrean ready: $P_2, P_3, P_4, P_1$.
   * $t=4$: Jalankan $P_2$ selama $4\text{ ms}$ ($4 - 8$). $P_2$ selesai! Sisa antrean: $P_3, P_4, P_1$.
   * $t=8$: Jalankan $P_3$ selama $4\text{ ms}$ ($8 - 12$). Sisa $P_3 = 5$. Antrean: $P_4, P_1, P_3$.
   * $t=12$: Jalankan $P_4$ selama $4\text{ ms}$ ($12 - 16$). Sisa $P_4 = 1$. Antrean: $P_1, P_3, P_4$.
   * $t=16$: Jalankan $P_1$ selama $4\text{ ms}$ ($16 - 20$). $P_1$ selesai! Antrean: $P_3, P_4$.
   * $t=20$: Jalankan $P_3$ selama $4\text{ ms}$ ($20 - 24$). Sisa $P_3 = 1$. Antrean: $P_4, P_3$.
   * $t=24$: Jalankan $P_4$ selama $1\text{ ms}$ ($24 - 25$). $P_4$ selesai!
   * $t=25$: Jalankan $P_3$ selama $1\text{ ms}$ ($25 - 26$). $P_3$ selesai!

---

### Soal UTS 2: Sinkronisasi Bounded-Buffer menggunakan Semaphore
**Deskripsi Soal:**
Masalah Produsen-Konsumen (*Producer-Consumer*) berbagi sebuah penyangga berukuran terbatas $N$ (*bounded buffer*). Tuliskan pseudokode solusi sinkronisasi proses Produsen dan Konsumen menggunakan **Semaphore** untuk mencegah terjadinya *race condition* dan *deadlock*!

**Kunci Pembahasan & Solusi:**
Inisialisasi 3 buah Semaphore:
* `semaphore mutex = 1;` (Binary semaphore untuk mutual exclusion saat mengakses buffer)
* `semaphore empty = N;` (Counting semaphore untuk menghitung slot kosong)
* `semaphore full = 0;`  (Counting semaphore untuk menghitung slot yang terisi data)

```c
// Kode untuk Proses Produsen (Producer)
do {
    // 1. Memproduksi sebuah item baru
    Item next_produced = produce_item();

    wait(empty); // Tunggu sampai ada slot kosong (decrement empty)
    wait(mutex); // Masuk ke Critical Section

    // 2. Tambahkan item ke dalam buffer
    add_to_buffer(next_produced);

    signal(mutex); // Keluar dari Critical Section
    signal(full);  // Beritahu konsumen ada slot baru yang terisi (increment full)
} while (true);

// Kode untuk Proses Konsumen (Consumer)
do {
    wait(full);  // Tunggu sampai ada minimal satu slot terisi data
    wait(mutex); // Masuk ke Critical Section

    // 3. Ambil item dari buffer
    Item next_consumed = remove_from_buffer();

    signal(mutex); // Keluar dari Critical Section
    signal(empty); // Beritahu produsen ada slot yang sudah kosong kembali

    // 4. Mengonsumsi item
    consume_item(next_consumed);
} while (true);
```
*(Catatan Penting: Urutan `wait(empty)` sebelum `wait(mutex)` mutlak tidak boleh dibalik! Jika dibalik, sistem akan mengalami DEADLOCK saat buffer penuh).*

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (ALGORITMA BANKER, PAGE REPLACEMENT & DISK)

### Soal UAS 1: Deadlock Avoidance Menggunakan Algoritma Banker
**Deskripsi Soal:**
Sebuah sistem memiliki 5 proses ($P_0, P_1, P_2, P_3, P_4$) dan 3 jenis sumber daya ($A, B, C$) dengan total unit: $A=10, B=5, C=7$. Status sistem saat ini:

| Proses | Allocation ($A, B, C$) | Max ($A, B, C$) | Available ($A, B, C$) |
|:---:|:---:|:---:|:---:|
| $P_0$ | 0, 1, 0 | 7, 5, 3 | **3, 3, 2** |
| $P_1$ | 2, 0, 0 | 3, 2, 2 | |
| $P_2$ | 3, 0, 2 | 9, 0, 2 | |
| $P_3$ | 2, 1, 1 | 2, 2, 2 | |
| $P_4$ | 0, 0, 2 | 4, 3, 3 | |

1. Hitung dan tuliskan isi **Matriks Kebutuhan (*Need Matrix*)**!
2. Buktikan apakah sistem saat ini berada dalam **Safe State**! Tunjukkan urutan proses eksekusi amannya (*Safe Sequence*)!

**Kunci Pembahasan & Solusi:**
1. **Matriks Need ($\text{Need} = \text{Max} - \text{Allocation}$):**
   * $\text{Need}(P_0) = (7-0, 5-1, 3-0) = \mathbf{(7, 4, 3)}$
   * $\text{Need}(P_1) = (3-2, 2-0, 2-0) = \mathbf{(1, 2, 2)}$
   * $\text{Need}(P_2) = (9-3, 0-0, 2-2) = \mathbf{(6, 0, 0)}$
   * $\text{Need}(P_3) = (2-2, 2-1, 2-1) = \mathbf{(0, 1, 1)}$
   * $\text{Need}(P_4) = (4-0, 3-0, 3-2) = \mathbf{(4, 3, 1)}$
2. **Pengujian Safe State:**
   Vektor awal $\text{Work} = \text{Available} = \mathbf{(3, 3, 2)}$.
   * **Langkah 1:** Periksa $P_1$: $\text{Need}(P_1) = (1, 2, 2) \le \text{Work}(3, 3, 2)$ (**Memenuhi!**).
     * $P_1$ dialokasikan hingga selesai, lalu melepaskan sumber dayanya:
     * $\text{Work} = \text{Work} + \text{Alloc}(P_1) = (3, 3, 2) + (2, 0, 0) = \mathbf{(5, 3, 2)}$.
   * **Langkah 2:** Periksa $P_3$: $\text{Need}(P_3) = (0, 1, 1) \le \text{Work}(5, 3, 2)$ (**Memenuhi!**).
     * $P_3$ selesai dan melepaskan sumber daya:
     * $\text{Work} = (5, 3, 2) + (2, 1, 1) = \mathbf{(7, 4, 3)}$.
   * **Langkah 3:** Periksa $P_4$: $\text{Need}(P_4) = (4, 3, 1) \le \text{Work}(7, 4, 3)$ (**Memenuhi!**).
     * $P_4$ selesai:
     * $\text{Work} = (7, 4, 3) + (0, 0, 2) = \mathbf{(7, 4, 5)}$.
   * **Langkah 4:** Periksa $P_0$: $\text{Need}(P_0) = (7, 4, 3) \le \text{Work}(7, 4, 5)$ (**Memenuhi!**).
     * $P_0$ selesai:
     * $\text{Work} = (7, 4, 5) + (0, 1, 0) = \mathbf{(7, 5, 5)}$.
   * **Langkah 5:** Periksa $P_2$: $\text{Need}(P_2) = (6, 0, 0) \le \text{Work}(7, 5, 5)$ (**Memenuhi!**).
     * $P_2$ selesai: $\text{Work} = (7, 5, 5) + (3, 0, 2) = \mathbf{(10, 5, 7)}$ (seluruh sumber daya kembali).
3. **Kesimpulan:**
   Karena seluruh proses dapat selesai dieksekusi tanpa terjebak deadlock, sistem berada dalam **Safe State** dengan salah satu urutan eksekusi aman (*Safe Sequence*):
   $$\mathbf{\langle P_1, P_3, P_4, P_0, P_2 \rangle}$$

---

### Soal UAS 2: Penjadwalan Head Hard Disk (Soal Asli UAS Undip 2024)
**Deskripsi Soal:**
Sebuah disk drive memiliki 200 silinder (bernomor $0$ s.d. $199$). Posisi head saat ini berada pada **silinder 53**. Antrean permintaan akses lintasan silinder yang masuk secara berurutan adalah:
$$98, \; 183, \; 37, \; 122, \; 14, \; 124, \; 65, \; 67$$
Hitunglah total jarak pergerakan head (dalam jumlah silinder) menggunakan algoritma **Shortest Seek Time First (SSTF)**!

**Kunci Pembahasan & Solusi:**
1. **Prinsip SSTF:** Selalu memilih silinder yang memiliki selisih jarak terdekat dari posisi head saat itu.
2. **Penelusuran Langkah demi Langkah dari Posisi Awal $= 53$:**
   * Dari $53$, jarak terdekat adalah ke **$65$** ($|65 - 53| = 12$).
   * Dari $65$, jarak terdekat adalah ke **$67$** ($|67 - 65| = 2$).
   * Dari $67$, jarak terdekat adalah ke **$37$** ($|37 - 67| = 30$, bandingkan ke 98 jaraknya 31).
   * Dari $37$, jarak terdekat adalah ke **$14$** ($|14 - 37| = 23$).
   * Dari $14$, seluruh permintaan di sisi kiri habis. Menyeberang ke sisa permintaan: terdekat adalah ke **$98$** ($|98 - 14| = 84$).
   * Dari $98$, terdekat ke **$122$** ($|122 - 98| = 24$).
   * Dari $122$, terdekat ke **$124$** ($|124 - 122| = 2$).
   * Dari $124$, terdekat ke **$183$** ($|183 - 124| = 59$).
3. **Total Pergerakan Head Silinder:**
   $$\begin{aligned}
   \text{Total Jarak} &= 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59 \\
   &= \mathbf{236 \text{ silinder}}
   \end{aligned}$$
   *(Bandingkan dengan FCFS yang membutuhkan total 640 silinder, SSTF jauh lebih efisien!).*

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Sebutkan dan jelaskan 4 syarat mutlak terjadinya Deadlock menurut Coffman, dan bagaimana strategi pencegahannya (Deadlock Prevention)?"
**Jawaban Komprehensif:**
Empat syarat Coffman yang wajib terjadi serentak agar deadlock muncul adalah:
1. **Mutual Exclusion:** Sumber daya hanya dapat digunakan oleh 1 proses pada satu waktu. *(Pencegahan: Sulit dicegah untuk hardware intrinsik seperti printer).*
2. **Hold and Wait:** Proses memegang sumber daya sambil menunggu sumber daya lain. *(Pencegahan: Wajibkan proses meminta seluruh sumber daya sekaligus di awal sebelum mulai berjalan).*
3. **No Preemption:** Sumber daya yang dipegang tidak boleh dirampas paksa. *(Pencegahan: Jika proses meminta sumber daya yang tidak tersedia, maka seluruh sumber daya yang sedang dipegangnya harus dilepaskan kembali).*
4. **Circular Wait:** Adanya siklus lingkaran saling tunggu antar-proses. *(Pencegahan: Beri nomor urut linier pada seluruh tipe sumber daya; proses hanya diizinkan meminta sumber daya yang nomor urutnya lebih tinggi dari yang dipegangnya).*
Menghilangkan minimal salah satu dari 4 syarat di atas secara permanen menjamin deadlock tidak akan pernah terjadi.

### Q2: "Jelaskan apa itu Thrashing dalam memori virtual dan bagaimana sistem operasi mendeteksi serta mengatasinya?"
**Jawaban Komprehensif:**
* **Definisi Thrashing:** Kondisi patologis di mana aktivitas pemindahan halaman (*paging / page fault handling*) menyita hampir seluruh waktu CPU ($>99\%$), sementara komputasi produktif proses nyaris terhenti (utilisasi CPU turun drastis). Ini terjadi ketika total ukuran alokasi frame fisik kurang dari kebutuhan himpunan kerja (*Working Set*) proses-proses yang berjalan.
* **Mekanisme Penanganan OS:**
  1. Menggunakan **Working-Set Model**: OS memantau parameter $\Delta$ (jendela halaman yang baru saja diakses). Jika total kebutuhan $\sum WSS_i > \text{Total RAM Fisik}$, OS secara agresif menangguhkan (*suspend*) beberapa proses dan men-swap keluar seluruh datanya ke disk.
  2. Pengurangan tingkat multipemrograman (*reduce degree of multiprogramming*) hingga alokasi frame untuk proses yang tersisa kembali mencukupi.
