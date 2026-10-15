# Bank Contoh Soal & Pembahasan: Keamanan dan Jaminan Informasi

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Keamanan dan Jaminan Informasi Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Prof. Dr. Ir. Rahmat Gernowo, M.Si., Dr. Aris Puji Widodo, M.T., dkk. & Bank Soal HMIF 2019–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (CIA TRIAD, MANAJEMEN RISIKO ALE & KENDALI AKSES)

### Soal UTS 1: Analisis Kuantitatif Manajemen Risiko Keamanan Informasi (Soal Asli UTS Undip)
**Deskripsi Soal:**
Pusat Data Universitas Diponegoro memiliki server basis data akademik primer dengan nilai aset (*Asset Value - AV*) ditaksir sebesar **Rp 500.000.000,-**.
Berdasarkan data historis dan ancaman siber terbaru, server tersebut rentan terhadap serangan pemerasan *Ransomware*:
* Jika serangan sukses terjadi, diperkirakan $60\%$ data dan operasional kampus lumpuh sementara (*Exposure Factor - EF* $= 0.60$).
* Probabilitas terjadinya insiden serangan diperkirakan terjadi sekali setiap 2 tahun (*Annualized Rate of Occurrence - ARO* $= 0.5$).
* Tim Keamanan Siber mengusulkan pengadaan sistem *Automated Air-Gapped Immutable Backup & EDR Software* dengan biaya lisensi dan pemeliharaan tahunan (*Annualized Cost of Safeguard - ACS*) sebesar **Rp 45.000.000,- / tahun**.
* Sistem pengamanan baru tersebut dijamin mampu menekan frekuensi keberhasilan serangan menjadi hanya sekali setiap 10 tahun ($\text{ARO}_{\text{baru}} = 0.1$) dan mereduksi dampak kerusakan menjadi $10\%$ ($\text{EF}_{\text{baru}} = 0.10$).

**Tugas:**
1. Hitung nilai **Single Loss Expectancy (SLE)** awal sebelum pengamanan!
2. Hitung nilai **Annualized Loss Expectancy (ALE)** awal sebelum pengamanan!
3. Hitung nilai **$\text{ALE}_{\text{setelah}}$** penerapan sistem pengamanan baru!
4. Lakukan **Cost-Benefit Analysis (CBA)**! Apakah investasi sistem pengamanan baru tersebut layak secara finansial bagi universitas?

**Kunci Pembahasan & Solusi:**
1. **Perhitungan SLE Awal:**
   $$\text{SLE}_{\text{awal}} = \text{AV} \times \text{EF}_{\text{awal}} = \text{Rp } 500.000.000 \times 0.60 = \mathbf{\text{Rp } 300.000.000,-}$$

2. **Perhitungan ALE Awal:**
   $$\text{ALE}_{\text{awal}} = \text{SLE}_{\text{awal}} \times \text{ARO}_{\text{awal}} = \text{Rp } 300.000.000 \times 0.5 = \mathbf{\text{Rp } 150.000.000,- / \text{tahun}}$$

3. **Perhitungan ALE Setelah Penerapan Pengamanan Baru:**
   $$\text{SLE}_{\text{baru}} = \text{AV} \times \text{EF}_{\text{baru}} = \text{Rp } 500.000.000 \times 0.10 = \text{Rp } 50.000.000,-$$
   $$\text{ALE}_{\text{baru}} = \text{SLE}_{\text{baru}} \times \text{ARO}_{\text{baru}} = \text{Rp } 50.000.000 \times 0.1 = \mathbf{\text{Rp } 5.000.000,- / \text{tahun}}$$

4. **Analisis Kelayakan Finansial (Cost-Benefit Analysis):**
   $$\text{Penghematan Kerugian Kotor} = \text{ALE}_{\text{awal}} - \text{ALE}_{\text{baru}} = \text{Rp } 150.000.000 - \text{Rp } 5.000.000 = \text{Rp } 145.000.000,-$$
   $$\text{Nilai Manfaat Bersih (Net Benefit)} = (\text{ALE}_{\text{awal}} - \text{ALE}_{\text{baru}}) - \text{ACS}$$
   $$\text{Nilai Manfaat Bersih} = \text{Rp } 145.000.000 - \text{Rp } 45.000.000 = \mathbf{+\text{Rp } 100.000.000,- / \text{tahun}}$$
   *Kesimpulan:* Investasi sistem pengamanan baru **SANGAT LAYAK (Direkomendasikan)** karena memberikan penghematan risiko finansial bersih sebesar **Rp 100.000.000,- per tahun**.

---

### Soal UTS 2: Penerapan Model Kendali Akses Bell-LaPadula vs Model Biba
**Deskripsi Soal:**
Dalam sebuah organisasi militer dan perbankan, terdapat 3 tingkat klasifikasi keamanan:
$$\text{Top Secret (TS)} > \text{Secret (S)} > \text{Unclassified (U)}$$
Terdapat 2 personel: Jenderal $A$ ($\text{Clearance} = \text{TS}$) dan Prajurit $B$ ($\text{Clearance} = \text{U}$).
Terdapat 2 dokumen: Dokumen Dok-1 ($\text{Label} = \text{TS}$) dan Dokumen Dok-2 ($\text{Label} = \text{U}$).

Evaluasi apakah aksi berikut **DIIZINKAN** atau **DITOLAK**:
1. Di bawah **Model Bell-LaPadula (Fokus Kerahasian)**:
   * Aksi 1: Prajurit $B$ mencoba membaca (*Read*) Dok-1.
   * Aksi 2: Jenderal $A$ mencoba menulis (*Write*) informasi ke Dok-2.
2. Di bawah **Model Biba (Fokus Integritas)**:
   * Aksi 3: Jenderal $A$ mencoba membaca (*Read*) Dok-2.
   * Aksi 4: Prajurit $B$ mencoba memodifikasi (*Write*) Dok-1.

**Kunci Pembahasan & Solusi:**
1. **Model Bell-LaPadula (Menjaga Kerahasiaan / No Leakage):**
   * *Aksi 1 (Prajurit $B$ membaca Dok-1):* **DITOLAK**. Melanggar aturan *Simple Security Property* (**No Read Up**). Subjek ber-clearance rendah ($U$) dilarang membaca objek berlabel lebih tinggi ($TS$).
   * *Aksi 2 (Jenderal $A$ menulis ke Dok-2):* **DITOLAK**. Melanggar aturan $\star$-Property (**No Write Down**). Subjek ber-clearance tinggi ($TS$) dilarang menulis ke objek berklasifikasi lebih rendah ($U$) untuk mencegah kebocoran informasi rahasia ke publik secara tidak sengaja maupun disengaja oleh trojan horse.
2. **Model Biba (Menjaga Integritas / No Contamination):**
   * *Aksi 3 (Jenderal $A$ membaca Dok-2):* **DITOLAK**. Melanggar aturan *Simple Integrity Property* (**No Read Down**). Subjek dengan integritas tinggi ($TS$) dilarang membaca data dari sumber berintegritas rendah ($U$) agar keputusannya tidak terkontaminasi oleh data yang belum tervalidasi kebenarannya.
   * *Aksi 4 (Prajurit $B$ menulis ke Dok-1):* **DITOLAK**. Melanggar aturan $\star$-Integrity Property (**No Write Up**). Subjek berintegritas rendah ($U$) dilarang menulis atau merusak objek yang berintegritas tinggi ($TS$).

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (KRIPTOGRAFI RSA, DIGITAL SIGNATURE & PKI)

### Soal UAS 1: Perhitungan Matematis Kriptografi Asimetris RSA (Soal Asli UAS Undip)
**Deskripsi Soal:**
Diberikan parameter algoritma RSA sederhana:
* Dua bilangan prima: $p = 7$ dan $q = 11$.
* Kunci publik enkripsi: $e = 13$.

**Tugas:**
1. Hitung modulus sistem $n$ dan fungsi totient Euler $\phi(n)$!
2. Periksa apakah nilai $e = 13$ valid sebagai pasangan $\phi(n)$!
3. Hitung nilai kunci privat dekripsi $d$ menggunakan *Extended Euclidean Algorithm*!
4. Jika plaintext pesan adalah integer $M = 5$, hitung ciphertext $C$ hasil enkripsi!
5. Lakukan proses dekripsi pada ciphertext $C$ dan buktikan pesan kembali menjadi $M = 5$!

**Kunci Pembahasan & Solusi:**
1. **Perhitungan Modulus $n$ dan Totient $\phi(n)$:**
   $$n = p \times q = 7 \times 11 = \mathbf{77}$$
   $$\phi(n) = (p - 1)(q - 1) = (7 - 1)(11 - 1) = 6 \times 10 = \mathbf{60}$$

2. **Validasi Kunci Publik $e$:**
   Syarat: $1 < e < \phi(n)$ dan $\gcd(e, \phi(n)) = 1$ (relatif prima).
   $\gcd(13, 60) = 1$. Nilai $e = 13$ **VALID**.

3. **Perhitungan Kunci Privat $d$ ($e \cdot d \equiv 1 \pmod{\phi(n)}$):**
   $$13d \equiv 1 \pmod{60} \implies 13d - 60k = 1$$
   * Menguji nilai $k$:
     * Jika $k = 1 \implies 13d = 61$ (tidak habis dibagi 13).
     * Jika $k = 2 \implies 13d = 121$ (tidak habis).
     * Jika $k = 8 \implies 13d = 60(8) + 1 = 481 \implies d = \frac{481}{13} = \mathbf{37}$.
   * Kunci Publik: $(e=13, n=77)$ | Kunci Privat: $(d=37, n=77)$.

4. **Proses Enkripsi Pesan ($M = 5$):**
   $$C = M^e \pmod n = 5^{13} \pmod{77}$$
   * Hitung dengan pemangkatan modular bertingkat:
     * $5^2 = 25$
     * $5^4 = 25^2 = 625 \equiv 9 \pmod{77}$ (karena $77 \times 8 = 616$)
     * $5^8 = 9^2 = 81 \equiv 4 \pmod{77}$
     * $5^{13} = 5^8 \times 5^4 \times 5^1 = 4 \times 9 \times 5 = 180 \pmod{77}$
     * $180 = (77 \times 2) + 26 \implies \mathbf{C = 26}$.

5. **Proses Dekripsi Ciphertext ($C = 26$):**
   $$M = C^d \pmod n = 26^{37} \pmod{77}$$
   * Hitung pemangkatan modular:
     * $26^1 = 26$
     * $26^2 = 676 = (77 \times 8) + 60 \equiv -17 \pmod{77}$
     * $26^4 = (-17)^2 = 289 \equiv 58 \equiv -19 \pmod{77}$
     * $26^8 = (-19)^2 = 361 \equiv 53 \equiv -24 \pmod{77}$
     * $26^{16} = (-24)^2 = 576 \equiv 37 \pmod{77}$
     * $26^{32} = 37^2 = 1369 \equiv 60 \equiv -17 \pmod{77}$
     * $26^{37} = 26^{32} \times 26^4 \times 26^1 \equiv (-17) \times (-19) \times 26 \equiv 323 \times 26 \equiv 15 \times 26 = 390 \pmod{77}$
     * $390 = (77 \times 5) + 5 \implies \mathbf{M = 5}$ **(Terbukti Sempurna Kembali ke Asal)**.

---

### Soal UAS 2: Alur Pembuatan & Verifikasi Digital Signature
**Deskripsi Soal:**
Jelaskan alur teknis pertukaran data yang aman ketika Pengirim (Alice) mengirimkan dokumen kontrak hukum digital kepada Penerima (Bob) menggunakan **Digital Signature** dan **Enkripsi Hibrida**:
1. Bagaimana Alice membuat tanda tangan digital atas dokumen tersebut?
2. Bagaimana Bob memverifikasi bahwa dokumen tersebut benar-benar dari Alice dan belum pernah diubah di tengah jalan?
3. Mengapa Alice tidak boleh menandatangani langsung dokumen utuh, melainkan harus menandatangani nilai *hash digest*-nya?

**Kunci Pembahasan & Solusi:**
1. **Proses Penandatanganan Digital oleh Alice:**
   * Alice memasukkan dokumen kontrak $M$ ke fungsi hash kriptografis satu-arah (misal: SHA-256) untuk menghasilkan intisari dokumen unik yang ringkas: $h = H(M)$.
   * Alice mengenkripsi nilai hash $h$ menggunakan **Kunci Privat Alice ($K_{\text{priv, Alice}}$)**:
     $$S = E_{K_{\text{priv, Alice}}}(h)$$
   * Tanda tangan digital $S$ dilampirkan bersama dokumen asli $M$ dan dikirimkan ke Bob.
2. **Proses Verifikasi oleh Bob:**
   * Bob menerima pasangan $(M, S)$.
   * Bob menghitung sendiri nilai hash dari dokumen $M$ yang diterimanya menggunakan fungsi hash yang sama: $h_1 = H(M)$.
   * Bob mendekripsi tanda tangan digital $S$ menggunakan **Kunci Publik Alice ($K_{\text{pub, Alice}}$)** untuk membuka hash asli:
     $$h_2 = D_{K_{\text{pub, Alice}}}(S)$$
   * **Pengujian Integritas & Autentisitas:**
     * Jika $h_1 == h_2$, maka tanda tangan dinyatakan **VALID**: Dokumen dijamin 100% asli berasal dari Alice (tidak dapat disangkal / *Non-repudiation*) dan isinya tidak pernah diubah oleh peretas di tengah jalan (*Integrity*).
     * Jika $h_1 \ne h_2$, verifikasi **GAGAL** (dokumen rusak atau dipalsukan).
3. **Mengapa Menandatangani Hash, Bukan Dokumen Utuh:**
   * Operasi enkripsi asimetris (RSA/ECC) sangat lambat dan membutuhkan komputasi CPU yang tinggi. Menandatangani dokumen berukuran puluhan megabyte secara langsung akan membuat sistem lambat dan menghasilkan ukuran signature yang sangat besar. Nilai hash memiliki ukuran tetap (*fixed size*, misal 256 bit untuk SHA-256) sehingga proses penandatanganan berjalan instan dalam hitungan milidetik.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa sistem keamanan modern (seperti HTTPS / TLS) menggunakan model Enkripsi Hibrida (Hybrid Encryption) alih-alih hanya menggunakan kriptografi asimetris saja?"
**Jawaban Komprehensif:**
Kriptografi asimetris (seperti RSA atau ECC) memiliki keunggulan luar biasa dalam menyelesaikan masalah distribusi kunci tanpa memerlukan saluran rahasia sebelumnya. Namun, algoritma asimetris bekerja ribuan kali lebih lambat daripada algoritma simetris dan mengonsumsi daya komputasi CPU serta memori yang sangat tinggi.
Oleh karena itu, arsitektur keamanan modern menggunakan **Enkripsi Hibrida**:
1. **Fase Awal (Handshake):** Kriptografi Asimetris hanya digunakan di awal sesi komunikasi untuk saling memverifikasi identitas server via sertifikat digital X.509 dan menyepakati satu **Kunci Rahasia Sesi Simetris (*Symmetric Session Key*)** secara aman.
2. **Fase Transmisi Data Massal:** Setelah kunci sesi disepakati, seluruh pertukaran data aplikasi (seperti streaming HTML, video, file transfer) dienkripsi menggunakan **Kriptografi Simetris (AES-GCM)** yang sangat cepat dan didukung oleh instruksi akselerasi perangkat keras CPU (*AES-NI*).

### Q2: "Jelaskan prinsip arsitektur keamanan Zero Trust dan mengapa model keamanan perimeter tradisional (Castle-and-Moat) sudah tidak relevan lagi!"
**Jawaban Komprehensif:**
* **Model Tradisional Castle-and-Moat (Perimeter-Based Security):**
  Mengasumsikan bahwa semua entitas di luar jaringan kantor/kampus adalah musuh, sedangkan siapa pun yang sudah berada di dalam jaringan internal (misal terhubung kabel LAN atau VPN kantor) otomatis dianggap tepercaya (*trusted*). Model ini gagal total ketika penyerang berhasil menembus satu komputer karyawan via malware phising; penyerang leluasa melakukan pergerakan lateral (*lateral movement*) ke seluruh server database internal tanpa hambatan.
* **Prinsip Arsitektur Zero Trust:**
  Menerapkan doktrin: **"Never Trust, Always Verify" (Jangan Pernah Percaya, Selalu Verifikasi)**.
  1. *Verifikasi Eksplisit:* Setiap upaya akses ke data atau layanan—baik berasal dari dalam kantor maupun luar negeri—wajib diautentikasi dan diotorisasi secara terus-menerus (*continuous authentication*).
  2. *Prinsip Hak Akses Terkecil (Least Privilege):* Pengguna hanya diberikan akses terbatas pada apa yang benar-benar mereka butuhkan saat itu (*Just-In-Time and Just-Enough-Access*).
  3. *Asumsikan Terjadi Kebocoran (Assume Breach):* Membagi jaringan menjadi segmen-segmen kecil (*micro-segmentation*) dan mengenkripsi seluruh komunikasi data antar-layanan (*end-to-end encryption*), sehingga jika satu perangkat terinfeksi, dampaknya terlokalisasi dan tidak merambat ke sistem lain.
