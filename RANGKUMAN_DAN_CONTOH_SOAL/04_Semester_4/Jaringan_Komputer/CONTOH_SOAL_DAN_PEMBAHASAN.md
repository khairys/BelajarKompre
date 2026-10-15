# Bank Contoh Soal & Pembahasan: Jaringan Komputer

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Jaringan Komputer Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Dr. Ir. Aris Puji Widodo, M.T., Adi Wibowo, S.Si., M.Kom., Ph.D., Panji Wisnu Wirawan, S.T., M.T., dkk. & Arsip HMIF 2017–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (SUBNETTING, CRC & DATA LINK)

### Soal UTS 1: Desain Subnetting VLSM & CIDR (Soal Wajib UTS Undip)
**Deskripsi Soal:**
Departemen Informatika Universitas Diponegoro memperoleh alokasi satu blok alamat IP publik kelas C:
$$\mathbf{192.168.10.0/24}$$
Jaringan tersebut harus dibagi menjadi 4 buah subnet independen dengan kebutuhan host sebagai berikut:
1. **Subnet A (Lab Riset AI):** Membutuhkan **60 host** komputer.
2. **Subnet B (Lab Software Engineering):** Membutuhkan **28 host** komputer.
3. **Subnet C (Ruang Dosen & Administrasi):** Membutuhkan **12 host** komputer.
4. **Subnet D (Jalur Point-to-Point Antar-Router):** Membutuhkan **2 host** (antarmuka router).

**Tugas:**
Rancanglah pengalamatan jaringan menggunakan metode **VLSM (*Variable Length Subnet Masking*)** yang paling efisien (tanpa pemborosan IP)! Tentukan untuk setiap subnet:
* Prefix CIDR dan Subnet Mask desimal
* Network Address
* Rentang Usable IP Address (Host Pertama – Host Terakhir)
* Broadcast Address

**Kunci Pembahasan & Solusi:**
*Prinsip Dasar VLSM:* Urutkan alokasi dari subnet yang membutuhkan jumlah host **terbesar ke terkecil**!
Rumus kapasitas host: $2^h - 2 \ge N_{\text{host}}$ ($h$ = jumlah bit host, prefix $= 32 - h$).

1. **Subnet A (Kebutuhan: 60 host):**
   * Cari $h$: $2^5 - 2 = 30$ (kurang), $2^6 - 2 = 62 \ge 60$ $\implies h = 6$ bit host.
   * Prefix: $32 - 6 = \mathbf{/26}$.
   * Subnet Mask: $255.255.255.192$ (karena $11000000_2 = 192$).
   * Ukuran Blok: $2^6 = 64$ IP.
   * **Network Address:** `192.168.10.0/26`
   * **Rentang IP Valid:** `192.168.10.1` s.d. `192.168.10.62`
   * **Broadcast Address:** `192.168.10.63`

2. **Subnet B (Kebutuhan: 28 host):**
   * Blok dimulai tepat setelah broadcast Subnet A: IP awal = `192.168.10.64`.
   * Cari $h$: $2^5 - 2 = 30 \ge 28 \implies h = 5$ bit host.
   * Prefix: $32 - 5 = \mathbf{/27}$.
   * Subnet Mask: $255.255.255.224$ (karena $11100000_2 = 224$).
   * Ukuran Blok: $2^5 = 32$ IP.
   * **Network Address:** `192.168.10.64/27`
   * **Rentang IP Valid:** `192.168.10.65` s.d. `192.168.10.94`
   * **Broadcast Address:** `192.168.10.95`

3. **Subnet C (Kebutuhan: 12 host):**
   * Blok dimulai pada IP = `192.168.10.96`.
   * Cari $h$: $2^4 - 2 = 14 \ge 12 \implies h = 4$ bit host.
   * Prefix: $32 - 4 = \mathbf{/28}$.
   * Subnet Mask: $255.255.255.240$ (karena $11110000_2 = 240$).
   * Ukuran Blok: $2^4 = 16$ IP.
   * **Network Address:** `192.168.10.96/28`
   * **Rentang IP Valid:** `192.168.10.97` s.d. `192.168.10.110`
   * **Broadcast Address:** `192.168.10.111`

4. **Subnet D (Kebutuhan: 2 host Point-to-Point):**
   * Blok dimulai pada IP = `192.168.10.112`.
   * Cari $h$: $2^2 - 2 = 2 \ge 2 \implies h = 2$ bit host.
   * Prefix: $32 - 2 = \mathbf{/30}$.
   * Subnet Mask: $255.255.255.252$ (karena $11111100_2 = 252$).
   * Ukuran Blok: $2^2 = 4$ IP.
   * **Network Address:** `192.168.10.112/30`
   * **Rentang IP Valid:** `192.168.10.113` s.d. `192.168.10.114`
   * **Broadcast Address:** `192.168.10.115`

*Ringkasan Tabel Perancangan VLSM:*

| Subnet | Kebutuhan | Prefix | Subnet Mask | Network ID | Host Range | Broadcast |
|:---|:---:|:---:|:---|:---|:---|:---|
| **Subnet A** | 60 | `/26` | `255.255.255.192` | `192.168.10.0` | `192.168.10.1 - 192.168.10.62` | `192.168.10.63` |
| **Subnet B** | 28 | `/27` | `255.255.255.224` | `192.168.10.64` | `192.168.10.65 - 192.168.10.94` | `192.168.10.95` |
| **Subnet C** | 12 | `/28` | `255.255.255.240` | `192.168.10.96` | `192.168.10.97 - 192.168.10.110` | `192.168.10.111` |
| **Subnet D** | 2 | `/30` | `255.255.255.252` | `192.168.10.112` | `192.168.10.113 - 192.168.10.114` | `192.168.10.115` |

---

### Soal UTS 2: Deteksi Galat CRC Polinomial Modulo-2 (Soal Asli Undip)
**Deskripsi Soal:**
Sebuah pemancar ingin mengirimkan pesan data $D = \mathbf{1010001101}$ menggunakan generator polinomial:
$$G(x) = x^4 + x + 1$$
1. Tentukan representasi bit biner dari polinomial pembagi $G(x)$!
2. Hitung deretan bit redundansi FCS (*Frame Check Sequence*) $R$ menggunakan pembagian biner modulo-2 (XOR)!
3. Tuliskan deretan frame lengkap $T$ yang dikirimkan ke saluran transmisi!

**Kunci Pembahasan & Solusi:**
1. **Representasi Bit Generator $G(x)$:**
   $$G(x) = 1\cdot x^4 + 0\cdot x^3 + 0\cdot x^2 + 1\cdot x^1 + 1\cdot x^0 \implies \mathbf{10011}$$
   Derajat polinomial $r = 4$, sehingga pengirim menambahkan $r = 4$ buah bit nol di belakang data $D$.

2. **Pembagian Biner Modulo-2 ($D \cdot 2^4$ dibagi $G$):**
   * Data yang ditambahi nol: `10100011010000`
   * Pembagi: `10011`
   ```text
   10100011010000
   10011             (XOR pada 5 bit pertama)
   -----
     11101
     10011
     -----
      11101
      10011
      -----
       11100
       10011
       -----
        11110
        10011
        -----
         11010
         10011
         -----
          10010
          10011
          -----
           0001 (Sisa pembagian 4-bit) -> 0001
   ```
   * Sisa pembagian modulo-2 ($R$) $= \mathbf{0001}$.

3. **Frame Lengkap yang Ditransmisikan ($T$):**
   Gabungkan data asli $D$ dengan $R$:
   $$T = D \,\|\, R = \mathbf{10100011010001}$$
   *(Di sisi penerima, frame $T$ dibagi kembali dengan $G=10011$. Jika sisa pembagian sama dengan 0000, paket diterima tanpa galat).*

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (ROUTING, TCP HANDSHAKE & KONTROL KONGESTI)

### Soal UAS 1: Algoritma Routing Dijkstra pada Link-State OSPF
**Deskripsi Soal:**
Diberikan topologi jaringan dengan 5 buah router: $A, B, C, D, E$ dengan bobot (*cost*) tautan sebagai berikut:
* $A-B: 2, \quad A-C: 5$
* $B-C: 2, \quad B-D: 4, \quad B-E: 7$
* $C-D: 1, \quad C-E: 6$
* $D-E: 3$

Gunakan **Algoritma Dijkstra** untuk mencari rute terpendek (*least-cost path*) dan tabel *forwarding* dari router sumber **$A$** ke semua router lainnya!

**Kunci Pembahasan & Solusi:**
*Inisialisasi:*
Himpunan simpul terjangkau pasti $N' = \{A\}$.
Jarak awal dari $A$: $D(B)=2, D(C)=5, D(D)=\infty, D(E)=\infty$.

* **Iterasi 1:**
  * Simpul di luar $N'$ dengan jarak minimum adalah $B$ ($D(B)=2$).
  * Masukkan $B$ ke $N' \implies N' = \{A, B\}$.
  * Perbarui jarak tetangga $B$:
    * $D(C) = \min(D(C), D(B) + c(B,C)) = \min(5, 2 + 2) = \mathbf{4}$ (via $B$).
    * $D(D) = \min(\infty, D(B) + c(B,D)) = \min(\infty, 2 + 4) = \mathbf{6}$ (via $B$).
    * $D(E) = \min(\infty, D(B) + c(B,E)) = \min(\infty, 2 + 7) = \mathbf{9}$ (via $B$).
* **Iterasi 2:**
  * Simpul minimum di luar $N'$ adalah $C$ ($D(C)=4$).
  * Masukkan $C$ ke $N' \implies N' = \{A, B, C\}$.
  * Perbarui jarak tetangga $C$:
    * $D(D) = \min(6, D(C) + c(C,D)) = \min(6, 4 + 1) = \mathbf{5}$ (via $C$).
    * $D(E) = \min(9, D(C) + c(C,E)) = \min(9, 4 + 6) = 9$.
* **Iterasi 3:**
  * Simpul minimum di luar $N'$ adalah $D$ ($D(D)=5$).
  * Masukkan $D$ ke $N' \implies N' = \{A, B, C, D\}$.
  * Perbarui jarak tetangga $D$:
    * $D(E) = \min(9, D(D) + c(D,E)) = \min(9, 5 + 3) = \mathbf{8}$ (via $D$).
* **Iterasi 4:**
  * Masukkan $E$ ke $N' \implies N' = \{A, B, C, D, E\}$. Selesai.

*Tabel Hasil Rute Terpendek & Forwarding Router $A$:*

| Tujuan | Least-Cost | Jalur Lengkap | Next-Hop dari $A$ |
|:---:|:---:|:---|:---:|
| **B** | 2 | $A \rightarrow B$ | Antarmuka menuju $B$ |
| **C** | 4 | $A \rightarrow B \rightarrow C$ | Antarmuka menuju $B$ |
| **D** | 5 | $A \rightarrow B \rightarrow C \rightarrow D$ | Antarmuka menuju $B$ |
| **E** | 8 | $A \rightarrow B \rightarrow C \rightarrow D \rightarrow E$ | Antarmuka menuju $B$ |

---

### Soal UAS 2: TCP Flow Control & Congestion Control (AIMD Analysis)
**Deskripsi Soal:**
Pada awal transmisi, ambang batas *Slow-Start Threshold* ($ssthresh$) disetel sebesar $16$ MSS. Koneksi dimulai dengan $cwnd = 1$ MSS.
1. Pada RTT ke berapa $cwnd$ beralih dari fase **Slow Start** ke fase **Congestion Avoidance**?
2. Pada RTT ke-7, nilai $cwnd = 20$ MSS dan terjadi peristiwa **3 Duplicate ACK**. Tentukan nilai $ssthresh$ dan $cwnd$ baru pada awal RTT ke-8 menggunakan algoritma TCP Reno!
3. Jika pada RTT ke-10 terjadi peristiwa **Timeout**, tentukan nilai $ssthresh$ dan $cwnd$ baru!

**Kunci Pembahasan & Solusi:**
1. **Transisi Slow Start ke Congestion Avoidance:**
   * Pada Slow Start, $cwnd$ berlipat ganda setiap RTT:
     * RTT 1: $cwnd = 1$
     * RTT 2: $cwnd = 2$
     * RTT 3: $cwnd = 4$
     * RTT 4: $cwnd = 8$
     * RTT 5: $cwnd = 16$
   * Pada RTT 5, $cwnd$ telah mencapai $ssthresh = 16$. Maka pada **RTT ke-6**, algoritma beralih ke **Congestion Avoidance (Additive Increase)** dengan kenaikan linier $+1$ MSS per RTT.

2. **Peristiwa 3 Duplicate ACK pada RTT 7 ($cwnd = 20$ MSS):**
   * *Mekanisme Fast Recovery (TCP Reno):*
     $$ssthresh_{\text{baru}} = \frac{cwnd}{2} = \frac{20}{2} = \mathbf{10} \text{ MSS}$$
     $$cwnd_{\text{baru}} = ssthresh_{\text{baru}} = \mathbf{10} \text{ MSS} \quad (\text{atau } 10 + 3 = 13 \text{ saat inflasi buffer})$$
   * Koneksi langsung melanjutkan fase Congestion Avoidance tanpa jatuh ke $1$ MSS.

3. **Peristiwa Timeout pada RTT 10 (misalkan saat itu $cwnd = 12$ MSS):**
   * *Mekanisme Reaksi Timeout:* Kehilangan timeout menandakan kemacetan jaringan yang sangat parah (*severe congestion*).
     $$ssthresh_{\text{baru}} = \frac{cwnd}{2} = \frac{12}{2} = \mathbf{6} \text{ MSS}$$
     $$cwnd_{\text{baru}} = \mathbf{1} \text{ MSS}$$
   * Koneksi jatuh kembali ke fase **Slow Start** dari awal.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan secara runtut apa yang terjadi pada arsitektur 5 layer TCP/IP saat pengguna mengetik 'https://kulon2.undip.ac.id' di browser dan menekan tombol Enter!"
**Jawaban Komprehensif:**
1. **Application Layer (Resolusi DNS & HTTP Request):**
   * Browser memeriksa cache lokal; jika belum ada, sistem membuat kueri **DNS** (UDP port 53) untuk mencari alamat IP server `kulon2.undip.ac.id`.
   * Setelah IP diperoleh, browser menyiapkan pesan permintaan `GET / HTTPS` melalui protokol TLS/SSL.
2. **Transport Layer (TCP Handshake & Enkripsi TLS):**
   * Sistem operasi klien membuka koneksi TCP ke port 443 server melalui **TCP 3-Way Handshake** (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`).
   * Dilanjutkan dengan negosiasi jabat tangan keamanan **TLS Handshake** (pertukaran sertifikat X.509, autentikasi kunci publik, dan negosiasi *Symmetric Session Key* AES).
3. **Network Layer (Enkapsulasi IP & Routing):**
   * Segmen TCP dibungkus dalam paket IPv4/IPv6 dengan IP sumber (klien) dan IP tujuan (server).
   * Router gerbang (*default gateway*) melakukan inspeksi routing table untuk meneruskan paket melintasi antrean router ISP internet.
4. **Data Link & Physical Layer (Framing & Transmisi Bit):**
   * Paket dienkapsulasi menjadi frame Ethernet dengan menambahkan MAC Address router terdekat (didapat via protokol **ARP**).
   * Frame diubah menjadi modulasi sinyal fisik (tegangan kabel tembaga atau pulsa foton fiber optik) menuju server.
   * Di server Undip, proses dibalik (*decapsulation*), server mengembalikan respon `HTTP 200 OK`, dan halaman web dirender oleh browser pengguna.

### Q2: "Kapan kita wajib memilih UDP daripada TCP dalam perancangan sistem terdistribusi, padahal UDP tidak menjamin paket pasti sampai?"
**Jawaban Komprehensif:**
Kita wajib memilih UDP ketika **latensi rendah (*low latency*) dan ketepatan waktu (*real-time constraint*) jauh lebih penting daripada keutuhan 100% data**. Contoh kasus:
* **Audio/Video Streaming & VoIP (misal Zoom / Google Meet):** Menunggu paket suara yang hilang untuk ditransmisi ulang (fitur TCP) akan menyebabkan jeda beku (*glitch / stutter*) yang mengganggu percakapan manusia. Paket audio yang terlambat 2 detik tidak ada gunanya lagi diputar.
* **Game Daring Multiplayer:** Informasi koordinat posisi pemain harus diperbarui instan puluhan kali per detik (*tick-rate*); pembaruan posisi terbaru langsung menggantikan data lama.
* **Kueri Ringkas Request-Response (DNS Query):** Menggunakan TCP memerlukan 3-way handshake (1.5 RTT) hanya untuk menanyakan satu IP singkat. Dengan UDP, klien langsung mengirim 1 paket kueri dan server langsung membalas 1 paket jawaban (hemat latensi 1 RTT).
