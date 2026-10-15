# Bank Contoh Soal & Pembahasan: Manajemen Basis Data

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Manajemen Basis Data Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Satriyo Adhy, S.Si., M.T., Beta Noranita, S.Si., M.Kom., dkk. & Bank Soal HMIF 2018–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (STORED PROCEDURE, TRIGGER & INDEKS B+ TREE)

### Soal UTS 1: Pembuatan Stored Procedure Perhitungan Transaksi Akademik (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan skema tabel basis data akademik berikut:
* `mahasiswa(nim VARCHAR(14) PK, nama VARCHAR(100), total_sks INT, ipk DECIMAL(3,2))`
* `mata_kuliah(kode_mk VARCHAR(10) PK, nama_mk VARCHAR(100), sks INT)`
* `krs(id_krs INT PK AUTO_INCREMENT, nim VARCHAR(14), kode_mk VARCHAR(10), semester INT, nilai_huruf CHAR(2), bobot DECIMAL(3,2))`

Buatlah sebuah **Stored Procedure** bernama `sp_hitung_ipk_kumulatif` dengan parameter masukan `p_nim VARCHAR(14)` yang melakukan:
1. Menghitung total SKS lulus (semua mata kuliah dengan bobot $> 0$).
2. Menghitung nilai IPK kumulatif dengan rumus:
   $$\text{IPK} = \frac{\sum (\text{sks} \times \text{bobot})}{\sum \text{sks}}$$
3. Memperbarui kolom `total_sks` dan `ipk` pada tabel `mahasiswa` untuk mahasiswa bersangkutan.
4. Jika mahasiswa belum mengambil mata kuliah sama sekali, beri nilai default IPK $= 0.00$ dan SKS $= 0$.

**Kunci Pembahasan & Solusi:**
```sql
DELIMITER $$

CREATE PROCEDURE sp_hitung_ipk_kumulatif(IN p_nim VARCHAR(14))
BEGIN
    DECLARE v_total_sks INT DEFAULT 0;
    DECLARE v_total_bobot_sks DECIMAL(10,2) DEFAULT 0.00;
    DECLARE v_ipk_akhir DECIMAL(3,2) DEFAULT 0.00;

    -- 1. Hitung total SKS dan total perkalian (SKS * Bobot)
    SELECT 
        COALESCE(SUM(m.sks), 0),
        COALESCE(SUM(m.sks * k.bobot), 0.00)
    INTO 
        v_total_sks, 
        v_total_bobot_sks
    FROM krs k
    JOIN mata_kuliah m ON k.kode_mk = m.kode_mk
    WHERE k.nim = p_nim AND k.nilai_huruf IS NOT NULL;

    -- 2. Hitung IPK Kumulatif (Cegah pembagian dengan nol)
    IF v_total_sks > 0 THEN
        SET v_ipk_akhir = ROUND(v_total_bobot_sks / v_total_sks, 2);
    ELSE
        SET v_ipk_akhir = 0.00;
    END IF;

    -- 3. Perbarui tabel master mahasiswa
    UPDATE mahasiswa
    SET total_sks = v_total_sks,
        ipk = v_ipk_akhir
    WHERE nim = p_nim;

    -- Tampilkan konfirmasi hasil
    SELECT p_nim AS nim, v_total_sks AS total_sks_diperbarui, v_ipk_akhir AS ipk_terkini;
END $$

DELIMITER ;
```

---

### Soal UTS 2: Konstruksi Penyisipan Kunci pada Indeks B+ Tree
**Deskripsi Soal:**
Diberikan sebuah struktur indeks **B+ Tree orde $m = 3$** (setiap simpul dapat menampung maksimal $m - 1 = 2$ kunci dan memiliki maksimal $3$ penunjuk anak).
Simpul daun memuat maksimal $2$ record data.
Gambarkan langkah demi langkah pembentukan B+ Tree saat urutan kunci berikut disisipkan satu per satu:
$$\mathbf{10, 20, 30, 40, 50}$$

**Kunci Pembahasan & Solusi:**
1. **Sisipkan Kunci 10 dan 20:**
   Simpul daun awal masih memiliki ruang:
   ```text
   [ 10 | 20 ] (Akar sekaligus Daun)
   ```
2. **Sisipkan Kunci 30 (Kelebihan Kapasitas / Overflow):**
   * Kunci sementara: `[ 10, 20, 30 ]` (melebihi kapasitas maksimal 2 kunci).
   * Terjadi **Splitting Simpul Daun**:
     * Simpul daun kiri memuat: `[ 10 ]`
     * Simpul daun kanan memuat: `[ 20 | 30 ]`
     * Kunci pemandu `20` dinaikkan (*copied up*) menjadi simpul Akar baru:
   ```text
            [ 20 ] (Akar)
           /      \
      [ 10 ] ---> [ 20 | 30 ] (Daun saling terhubung linked list)
   ```
3. **Sisipkan Kunci 40:**
   * Kunci 40 masuk ke simpul daun kanan karena $40 \ge 20$.
   * Simpul daun kanan menjadi `[ 20, 30, 40 ]` (Overflow).
   * Daun kanan dipecah: daun kiri `[ 20 ]`, daun kanan baru `[ 30 | 40 ]`.
   * Kunci `30` dinaikkan ke simpul akar:
   ```text
            [ 20 | 30 ] (Akar)
           /     |     \
      [ 10 ] -> [ 20 ] -> [ 30 | 40 ]
   ```
4. **Sisipkan Kunci 50:**
   * Kunci 50 masuk ke daun paling kanan: `[ 30, 40, 50 ]` (Overflow).
   * Daun dipecah menjadi `[ 30 ]` dan `[ 40 | 50 ]`. Kunci `40` dinaikkan ke akar.
   * Simpul akar kini mengalami **Overflow**: `[ 20, 30, 40 ]`.
   * Terjadi **Splitting pada Simpul Internal Akar**:
     * Kunci tengah `30` dinaikkan (*pushed up*) menjadi Akar Baru Level 3.
     * Simpul anak internal kiri: `[ 20 ]`, anak internal kanan: `[ 40 ]`.
5. **Struktur Akhir B+ Tree Pasca-Penyisipan 50:**
   ```text
                 [ 30 ] (Akar Utama)
                /      \
           [ 20 ]      [ 40 ] (Simpul Internal)
          /      \    /      \
       [10] -> [20] -> [30] -> [40 | 50] (Simpul Daun)
   ```
   *(Semua daun berada pada level yang seimbang sempurna dan terhubung linked list).*

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (SERIALIZABILITY, CONCURRENCY & ARIES)

### Soal UAS 1: Pengujian Conflict Serializability Jadwal Konkuren (Soal Asli UAS Undip 2023)
**Deskripsi Soal:**
Diberikan sebuah jadwal konkuren $S$ yang melibatkan 3 transaksi ($T_1, T_2, T_3$) sebagai berikut:
$$S: R_1(X); \; R_2(Z); \; R_1(Z); \; W_3(X); \; R_3(Y); \; W_1(X); \; W_2(Z); \; W_3(Y)$$
1. Daftarkan seluruh pasangan operasi yang saling berkonflik (*conflicting operations*) beserta transaksi yang terlibat!
2. Gambarkan **Graf Presedensi (*Precedence / Serialization Graph*)**!
3. Simpulkan apakah jadwal $S$ tersebut bersifat **Conflict Serializable** atau tidak! Jika iya, tentukan jadwal serial yang ekuivalen dengannya!

**Kunci Pembahasan & Solusi:**
1. **Identifikasi Pasangan Operasi Konflik ($T_i \ne T_j$, item data sama, minimal satu Write):**
   * **Pada Item Data $X$:**
     * $R_1(X)$ mendahului $W_3(X)$ $\implies$ Busur: $\mathbf{T_1 \rightarrow T_3}$
     * $W_3(X)$ mendahului $W_1(X)$ $\implies$ Busur: $\mathbf{T_3 \rightarrow T_1}$
   * **Pada Item Data $Z$:**
     * $R_1(Z)$ mendahului $W_2(Z)$ $\implies$ Busur: $\mathbf{T_1 \rightarrow T_2}$
     * $R_2(Z)$ mendahului $W_2(Z)$ $\implies$ Tidak menimbulkan busur antar-transaksi (sama-sama transaksi $T_2$).
   * **Pada Item Data $Y$:**
     * $R_3(Y)$ mendahului $W_3(Y)$ $\implies$ Transaksi sama ($T_3$).

2. **Analisis Graf Presedensi:**
   * Terdapat busur dari $T_1$ ke $T_3$ (akibat konflik $R_1(X)$ dan $W_3(X)$).
   * Terdapat busur dari $T_3$ ke $T_1$ (akibat konflik $W_3(X)$ dan $W_1(X)$).
   * Hal ini membentuk sebuah **SIKLUS TERTUTUP (*Directed Cycle*)**:
     $$T_1 \rightleftarrows T_3$$

3. **Kesimpulan:**
   * Karena Graf Presedensi memuat siklus ($T_1 \rightarrow T_3 \rightarrow T_1$), maka jadwal transaksi $S$ **TIDAK CONFLICT SERIALIZABLE**.
   * Jadwal ini tidak dapat diubah menjadi urutan eksekusi serial apapun tanpa mengubah hasil akhir basis data (rawan anomali inkonsistensi data).

---

### Soal UAS 2: Pencegahan Deadlock Berbasis Timestamp (Wait-Die vs Wound-Wait)
**Deskripsi Soal:**
Tiga transaksi memiliki stempel waktu (*timestamp*):
* $TS(T_1) = 10$ (Paling Tua)
* $TS(T_2) = 20$
* $TS(T_3) = 30$ (Paling Muda)

Jelaskan apa yang terjadi pada skenario berikut di bawah skema **Wait-Die** dan skema **Wound-Wait**:
* **Kasus A:** Transaksi $T_1$ meminta kunci data yang sedang dipegang oleh $T_3$.
* **Kasus B:** Transaksi $T_3$ meminta kunci data yang sedang dipegang oleh $T_1$.

**Kunci Pembahasan & Solusi:**
* **Skema Wait-Die (Non-Preemptive):**
  * *Aturan:* Jika transaksi tua meminta dari muda $\implies$ Boleh **Menunggu (*Wait*)**. Jika transaksi muda meminta dari tua $\implies$ Transaksi muda **Mati (*Die / Rollback*)**.
  * **Kasus A ($T_1$ meminta ke $T_3$):** Karena $TS(T_1) = 10 < TS(T_3) = 30$ ($T_1$ lebih tua), maka **$T_1$ diizinkan MENUNGGU (*Wait*)** hingga $T_3$ melepaskan kunci.
  * **Kasus B ($T_3$ meminta ke $T_1$):** Karena $TS(T_3) = 30 > TS(T_1) = 10$ ($T_3$ lebih muda), maka **$T_3$ langsung DIBUNUH/DIBATALKAN (*Die / Aborted & Rollback*)** dan dapat mengulang nanti dengan timestamp aslinya.
* **Skema Wound-Wait (Preemptive):**
  * *Aturan:* Jika transaksi tua meminta dari muda $\implies$ Transaksi tua **Melukai/Merebut (*Wound*)** kunci dan memaksa transaksi muda di-rollback. Jika transaksi muda meminta dari tua $\implies$ Transaksi muda diizinkan **Menunggu (*Wait*)**.
  * **Kasus A ($T_1$ meminta ke $T_3$):** Karena $T_1$ lebih tua dari $T_3$, maka **$T_1$ MELUKAI $T_3$ (*Wound*)**. Transaksi $T_3$ di-abort/rollback, dan kunci diserahkan seketika ke $T_1$.
  * **Kasus B ($T_3$ meminta ke $T_1$):** Karena $T_3$ lebih muda dari $T_1$, maka **$T_3$ diizinkan MENUNGGU (*Wait*)** hingga $T_1$ menyelesaikan transaksinya.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa indeks B+ Tree lebih disukai sebagai indeks tabel pada DBMS komersial (seperti MySQL InnoDB atau PostgreSQL) dibandingkan Hash Index?"
**Jawaban Komprehensif:**
Hash Index hanya efisien untuk pencarian kesetaraan persis (*exact-match point queries*, misal `WHERE id = 100`) dengan kompleksitas $O(1)$. Namun, Hash Index tidak dapat mendukung operasi:
1. **Kueri Rentang (*Range Queries*):** Klausa seperti `WHERE tanggal BETWEEN '2024-01-01' AND '2024-12-31'` atau `WHERE gaji > 5000000` tidak dapat dieksekusi via hash karena fungsi hash menyebarkan data secara acak di bucket memori. Pada B+ Tree, simpul-simpul daun saling terhubung membentuk *doubly linked list* berurutan, sehingga kueri rentang hanya memerlukan pencarian simpul batas bawah lalu penelusuran linier ke depan.
2. **Pengurutan (*ORDER BY / GROUP BY*):** B+ Tree menyimpan data dalam urutan terurut secara permanen, mengeliminasi kebutuhan proses *filesort* yang mahal di memori.
3. **Pencarian Awalan String (*Prefix Matching*):** Kueri seperti `WHERE nama LIKE 'Budi%'` didukung penuh oleh B+ Tree, namun gagal total pada Hash Index.

### Q2: "Jelaskan prinsip Write-Ahead Logging (WAL) dan mengapa DBMS tidak langsung menulis perubahan data langsung ke tabel di hard disk setiap kali pengguna melakukan transaksi COMMIT!"
**Jawaban Komprehensif:**
Jika DBMS menulis setiap baris data yang dimodifikasi langsung ke file tabel di disk saat transaksi di-commit (*In-Place Random Disk Writes*), performa sistem akan anjlok drastis karena terjadinya *Disk Head Thrashing* (I/O acak sangat lambat).
Melalui **Write-Ahead Logging (WAL)**:
* Modifikasi data dilakukan di halaman memori RAM (*buffer pool*).
* Catatan log perubahan (*log records*) berukuran sangat kecil ditulis ke disk secara berurutan (*Sequential Append-Only Write*) yang ribuan kali lebih cepat daripada I/O acak.
* Aturan WAL menjamin bahwa catatan log wajib tertulis di disk sebelum halaman data asli ditulis ke disk.
* Jika listrik padam seketika, data di RAM yang hilang dapat direkonstruksi 100% sempurna dengan membaca ulang catatan log berurutan tersebut saat proses pemulihan (*Redo phase*), sehingga properti *Durability* dan *Atomicity* tetap terjamin tanpa mengorbankan performa transaksional tinggi.
