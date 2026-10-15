# Bank Contoh Soal & Pembahasan: Sistem Cerdas

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Sistem Cerdas / Kecerdasan Buatan Departemen Informatika Universitas Diponegoro (Koleksi Pengampu Prof. Dr. Retno Kusumaningrum, S.Si., M.Kom., Sukmawati Nur Endah, S.Si., M.Kom., dkk. & Bank Soal HMIF 2017–2024).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (A* SEARCH, ALPHA-BETA PRUNING & LOGIKA WUMPUS)

### Soal UTS 1: Algoritma Pencarian Heuristik A* Search (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan graf peta perjalanan antar-kota dengan biaya riil jalan antarkota ($g$) dan nilai estimasi jarak garis lurus heuristik ($h$) ke kota tujuan akhir **$G$** sebagai berikut:
* **Tabel Nilai Heuristik Menuju Goal ($G$):**
  * $h(S) = 10, \quad h(A) = 7, \quad h(B) = 6, \quad h(C) = 4, \quad h(D) = 2, \quad h(G) = 0$.
* **Biaya Tautan Antar-Kota ($g$):**
  * $S \rightarrow A: 3, \quad S \rightarrow B: 4$
  * $A \rightarrow B: 2, \quad A \rightarrow C: 5$
  * $B \rightarrow C: 3, \quad B \rightarrow D: 5$
  * $C \rightarrow D: 1, \quad C \rightarrow G: 6$
  * $D \rightarrow G: 3$

Tentukan rute terpendek yang ditemukan oleh **Algoritma A\* Search** dari kota awal **$S$** ke kota tujuan **$G$**! Tuliskan tabel penelusuran status simpul (*Open List / Priority Queue* dan *Closed List*) pada setiap iterasi!

**Kunci Pembahasan & Solusi:**
Rumus evaluasi: $f(n) = g(n) + h(n)$.

1. **Inisialisasi:**
   * Masukkan simpul awal $S$ ke Open List:
     $g(S) = 0, \quad h(S) = 10 \implies f(S) = 0 + 10 = \mathbf{10}$.
   * Open List: $\{ (S, f=10) \}$
   * Closed List: $\{ \}$

2. **Iterasi 1:**
   * Ambil simpul dengan $f$ terkecil dari Open List: **$S$**.
   * Closed List: $\{ S \}$.
   * Kembangkan anak-anak dari $S$:
     * Anak $A$: $g(A) = g(S) + c(S,A) = 0 + 3 = 3$, $h(A) = 7 \implies f(A) = 3 + 7 = \mathbf{10}$.
     * Anak $B$: $g(B) = g(S) + c(S,B) = 0 + 4 = 4$, $h(B) = 6 \implies f(B) = 4 + 6 = \mathbf{10}$.
   * Open List: $\{ (A, f=10), (B, f=10) \}$.

3. **Iterasi 2:**
   * Pilih simpul **$A$** (prioritas abjad saat nilai $f$ kembar).
   * Closed List: $\{ S, A \}$.
   * Kembangkan tetangga $A$:
     * Menuju $B$: $g(B \text{ via } A) = 3 + 2 = 5$. Nilai $g$ ini lebih besar daripada $g(B \text{ langsung}) = 4$, abaikan jalur via $A$.
     * Menuju $C$: $g(C) = 3 + 5 = 8$, $h(C) = 4 \implies f(C) = 8 + 4 = \mathbf{12}$.
   * Open List: $\{ (B, f=10), (C, f=12) \}$.

4. **Iterasi 3:**
   * Pilih simpul **$B$** ($f=10$).
   * Closed List: $\{ S, A, B \}$.
   * Kembangkan tetangga $B$:
     * Menuju $C$: $g(C \text{ via } B) = 4 + 3 = 7$ (lebih kecil dari 8!). Perbarui $g(C) = 7, h(C) = 4 \implies f(C) = 7 + 4 = \mathbf{11}$.
     * Menuju $D$: $g(D) = 4 + 5 = 9$, $h(D) = 2 \implies f(D) = 9 + 2 = \mathbf{11}$.
   * Open List: $\{ (C, f=11), (D, f=11) \}$.

5. **Iterasi 4:**
   * Pilih simpul **$C$** ($f=11$).
   * Closed List: $\{ S, A, B, C \}$.
   * Kembangkan tetangga $C$:
     * Menuju $D$: $g(D \text{ via } C) = 7 + 1 = 8$ (lebih kecil dari 9!). Perbarui $g(D) = 8, h(D) = 2 \implies f(D) = 8 + 2 = \mathbf{10}$.
     * Menuju $G$: $g(G) = 7 + 6 = 13$, $h(G) = 0 \implies f(G) = 13 + 0 = \mathbf{13}$.
   * Open List: $\{ (D, f=10), (G, f=13) \}$.

6. **Iterasi 5:**
   * Pilih simpul **$D$** ($f=10$).
   * Closed List: $\{ S, A, B, C, D \}$.
   * Kembangkan tetangga $D$:
     * Menuju $G$: $g(G \text{ via } D) = 8 + 3 = 11$, $h(G) = 0 \implies f(G) = 11 + 0 = \mathbf{11}$.
   * Open List: $\{ (G, f=11), (G_{\text{lama}}, f=13) \}$.

7. **Iterasi 6:**
   * Ambil simpul minimum: **$G$** ($f=11$).
   * Karena $G$ adalah simpul tujuan (*Goal*) dan dikeluarkan dari Open List, pencarian dihentikan.

*Hasil Akhir:*
* Rute Optimal Terpendek: $\mathbf{S \rightarrow B \rightarrow C \rightarrow D \rightarrow G}$
* Total Biaya Lintasan Nyata: $g(G) = 4 + 3 + 1 + 3 = \mathbf{11}$.

---

### Soal UTS 2: Pohon Minimax & Alpha-Beta Pruning
**Deskripsi Soal:**
Diberikan pohon permainan 2-pemain dengan kedalaman 3 berikut (Akar adalah MAX). Nilai utilitas daun dari kiri ke kanan adalah:
`[ 3, 5, 6, 9, 1, 2, 0, -1 ]`.
Gunakan algoritma **Alpha-Beta Pruning** untuk menentukan nilai minimax pada akar dan tandai cabang-cabang mana saja yang dipangkas (*pruned*)!

**Kunci Pembahasan & Solusi:**
```text
               MAX (Root)
             /            \
          MIN_1          MIN_2
         /     \        /     \
       N1       N2     N3      N4
      /  \     /  \   /  \    /  \
     3    5   6    9 1    2  0   -1
```
1. **Penelusuran Subpohon Kiri (MIN_1):**
   * Masuk ke simpul daun kiri paling bawah $N_1$:
     * Daun $3$: MIN memperbarui $\beta_1 = \min(\infty, 3) = 3$.
     * Daun $5$: $\min(3, 5) = 3$. Nilai simpul $N_1 = 3$.
   * Kembali ke MIN_1: $\beta(\text{MIN}_1) = \min(\infty, 3) = 3$.
   * Masuk ke simpul $N_2$:
     * Daun $6$: MIN memperbarui nilainya menjadi $6$.
     * Daun $9$: $\min(6, 9) = 6$. Nilai simpul $N_2 = 6$.
   * Kembali ke MIN_1: $\beta(\text{MIN}_1) = \min(3, 6) = 3$.
   * Nilai simpul MIN_1 $= 3$.
2. **Kembali ke Akar (MAX):**
   * Akar MAX menerima nilai dari anak kiri $= 3$.
   * Akar memperbarui $\alpha = \max(-\infty, 3) = \mathbf{3}$.
3. **Penelusuran Subpohon Kanan (MIN_2) - Kondisi Pruning:**
   * Nilai awal pada MIN_2: $\alpha = 3, \beta = +\infty$.
   * Masuk ke simpul $N_3$:
     * Daun $1$: $\beta(N_3) = \min(\infty, 1) = 1$.
     * Daun $2$: $\min(1, 2) = 1$. Nilai simpul $N_3 = 1$.
   * Nilai $1$ dikembalikan ke MIN_2:
     * MIN_2 memperbarui $\beta(\text{MIN}_2) = \min(+\infty, 1) = \mathbf{1}$.
   * **Pengujian Kondisi Pemangkasan (*Pruning Check*):**
     * Pada simpul MIN_2, saat ini $\alpha = 3$ dan $\beta = 1$.
     * Karena $\mathbf{\alpha \ge \beta}$ ($3 \ge 1$), maka **SELURUH CABANG SIMPUL $N_4$ (daun $0$ dan $-1$) DIPANGKAS (*PRUNED*)!**
   * *Alasan Matematis:* Akar MAX sudah memiliki alternatif pasti bernilai 3 dari cabang kiri. Simpul MIN_2 di sebelah kanan dijamin akan menghasilkan nilai paling tinggi 1 (karena pemain MIN akan selalu memilih nilai terkecil). Pemain MAX yang rasional tidak akan pernah memilih cabang kanan.
4. **Hasil Akhir:**
   * Nilai Akar MAX $= \mathbf{3}$.
   * Cabang yang dipangkas: Subpohon $N_4$ (daun 0 dan -1).

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (LOGIKA FUZZY & CERTAINTY FACTOR)

### Soal UAS 1: Penalaran Logika Fuzzy Metode Mamdani (Soal Asli UAS Undip)
**Deskripsi Soal:**
Sistem pendingin ruangan pintar memiliki 2 masukan sensor: **Suhu ($T$)** dan **Kelembaban ($H$)**, dengan keluaran **Kecepatan Kipas ($K$)**.
* Fungsi Keanggotaan Suhu ($T$):
  * Dingin: $\mu(T) = \frac{25 - T}{10}$ untuk $15 \le T \le 25$
  * Panas: $\mu(T) = \frac{T - 20}{10}$ untuk $20 \le T \le 30$
* Fungsi Keanggotaan Kelembaban ($H$):
  * Kering: $\mu(H) = 0.4$
  * Lembab: $\mu(H) = 0.8$
* Basis Aturan Fuzzy:
  * Aturan 1: `IF Suhu Dingin AND Kelembaban Kering THEN Kipas Lambat (Konstanta = 1000 rpm)`
  * Aturan 2: `IF Suhu Panas AND Kelembaban Lembab THEN Kipas Cepat (Konstanta = 3000 rpm)`

Jika sensor membaca suhu saat ini $T = 26^\circ\text{C}$:
1. Hitung derajat keanggotaan fuzzifikasi untuk Suhu Dingin dan Suhu Panas!
2. Hitung nilai $\alpha$-predikat untuk Aturan 1 dan Aturan 2 menggunakan operator Fuzzy AND (min)!
3. Hitung kecepatan putaran kipas menggunakan metode defuzzifikasi rata-rata terbobot (*Weighted Average*)!

**Kunci Pembahasan & Solusi:**
1. **Fuzzifikasi Masukan Suhu ($T = 26^\circ\text{C}$):**
   * $\mu_{\text{Dingin}}(26) = 0$ (karena $T > 25^\circ\text{C}$).
   * $\mu_{\text{Panas}}(26) = \frac{26 - 20}{30 - 20} = \frac{6}{10} = \mathbf{0.6}$.

2. **Evaluasi Aturan Fuzzy ($\alpha$-predikat via MIN):**
   * **Aturan 1:**
     $$\alpha_1 = \min(\mu_{\text{Dingin}}, \mu_{\text{Kering}}) = \min(0, 0.4) = \mathbf{0.0}$$
   * **Aturan 2:**
     $$\alpha_2 = \min(\mu_{\text{Panas}}, \mu_{\text{Lembab}}) = \min(0.6, 0.8) = \mathbf{0.6}$$

3. **Defuzzifikasi (*Weighted Average*):**
   $$K^* = \frac{(\alpha_1 \times K_1) + (\alpha_2 \times K_2)}{\alpha_1 + \alpha_2}$$
   $$K^* = \frac{(0.0 \times 1000) + (0.6 \times 3000)}{0.0 + 0.6} = \frac{1800}{0.6} = \mathbf{3000} \text{ rpm}$$
   *Kecepatan kipas yang disetel oleh kontroler cerdas adalah:* **$3000$ rpm**.

---

### Soal UAS 2: Sistem Pakar dengan Ketidakpastian (Certainty Factor Kombinasi)
**Deskripsi Soal:**
Sistem pakar diagnosis penyakit tanaman cabai memiliki aturan:
* Rule 1: `IF Daun Menguning THEN Terinfeksi Virus Geminivirus (CF Rule 1 = 0.8)`
* Rule 2: `IF Daun Mengkerut THEN Terinfeksi Virus Geminivirus (CF Rule 2 = 0.7)`

Petani mengamati tanaman dan memberikan tingkat keyakinan bukti:
* Keyakinan Daun Menguning: $CF(E_1) = 0.75$
* Keyakinan Daun Mengkerut: $CF(E_2) = 0.60$

Hitung nilai derajat kepastian akhir ($CF_{\text{akhir}}$) bahwa tanaman tersebut terinfeksi Geminivirus!

**Kunci Pembahasan & Solusi:**
1. **Hitung CF untuk Masing-Masing Bukti:**
   * $CF_1(H, E_1) = CF(E_1) \times CF(\text{Rule}_1) = 0.75 \times 0.8 = \mathbf{0.60}$
   * $CF_2(H, E_2) = CF(E_2) \times CF(\text{Rule}_2) = 0.60 \times 0.7 = \mathbf{0.42}$

2. **Kombinasikan Kedua Bukti ($CF_1 > 0$ dan $CF_2 > 0$):**
   $$CF_{\text{combine}}(CF_1, CF_2) = CF_1 + CF_2 \times (1 - CF_1)$$
   $$CF_{\text{combine}} = 0.60 + 0.42 \times (1 - 0.60)$$
   $$CF_{\text{combine}} = 0.60 + 0.42 \times (0.40) = 0.60 + 0.168 = \mathbf{0.768}$$
   *Tingkat kepastian akhir:* **$76.8\%$** yakin bahwa tanaman cabai terinfeksi Geminivirus.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan apa yang dimaksud dengan sifat Admissible pada fungsi heuristik algoritma A* Search, dan apa dampaknya jika sifat ini dilanggar?"
**Jawaban Komprehensif:**
Fungsi heuristik $h(n)$ dikatakan **Admissible** jika estimasi biaya yang dihitung tidak pernah melebih-lebihkan biaya riil minimum sesungguhnya yang dibutuhkan untuk mencapai tujuan (*never overestimates the true lowest cost*, yaitu $h(n) \le h^*(n)$ untuk semua simpul $n$).
* Contoh heuristik admissible di dunia nyata: Jarak garis lurus burung (*Euclidean Straight-Line Distance*) pada peta jalan. Jarak jalan raya berkelok pasti selalu lebih panjang atau sama dengan garis lurus.
* **Dampak Jika Admissible Dilanggar (*Overestimating Heuristic*):**
  Algoritma A\* **kehilangan jaminan optimalitasnya (*Loss of Optimality*)**. Algoritma mungkin secara prematur mengabaikan jalur terbaik yang sebenarnya murah hanya karena nilai heuristik palsu yang terlalu tinggi, dan malah memilih jalur suboptimal yang biaya aslinya jauh lebih mahal.

### Q2: "Mengapa Single-Layer Perceptron gagal menyelesaikan masalah logika XOR, dan bagaimana penambahan Hidden Layer pada Multi-Layer Perceptron (MLP) menyelesaikannya?"
**Jawaban Komprehensif:**
* Secara matematis, Single-Layer Perceptron hanya mampu membentuk sebuah **garis lurus pemisah tunggal (*Linear Decision Boundary / Hyperplane*)** pada ruang vektor fitur masukan:
  $$w_1 x_1 + w_2 x_2 + b = 0$$
* Pada tabel kebenaran XOR: titik $(0,0)$ dan $(1,1)$ menghasilkan keluaran $0$, sedangkan $(0,1)$ dan $(1,0)$ menghasilkan keluaran $1$. Keempat titik ini secara geometris membentuk susunan menyilang yang **tidak dapat dipisahkan oleh satu garis lurus tunggal manapun (*Non-linearly Separable*)**.
* **Solusi Multi-Layer Perceptron (MLP):**
  Penambahan lapisan tersembunyi (*Hidden Layer*) dengan fungsi aktivasi non-linier (seperti Sigmoid atau ReLU) mentransformasikan ruang masukan asli ke dalam **ruang representasi fitur baru berdimensi lebih tinggi (*manifold transformation*)**. Di ruang tersembunyi tersebut, titik-titik data yang semula menyilang diubah formasinya sehingga menjadi terpisahkan secara linier oleh lapisan keluaran (*Output Layer*).
