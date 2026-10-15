# Bank Contoh Soal & Pembahasan: Logika Informatika

> Sumber rujukan: Bank soal UTS & UAS Logika Informatika Departemen Informatika Universitas Diponegoro (Koleksi HMIF & Kulon Undip 2017–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (LOGIKA PROPOSISIONAL, TABLEAUX & RESOLUSI)

### Soal UTS 1: Penerjemahan Bahasa Alami & Pembuktian Validitas via Semantic Tableaux (Soal Asli UTS Undip)
**Deskripsi Soal:**
Diberikan argumen penalaran berikut:
* **Premis 1:** Jika Wisnu belajar rajin dan dia pandai, maka dia akan diterima di universitas.
* **Premis 2:** Jika Wisnu tidak belajar rajin, maka dia tidak akan mendapat beasiswa.
* **Konklusi:** Jadi, jika Wisnu pandai, maka dia akan diterima di universitas atau tidak akan mendapat beasiswa.

**Pertanyaan:**
1. Formulasikan argumen di atas ke dalam notasi logika proposisional simbolik!
2. Buktikan validitas argumen tersebut menggunakan metode **Semantic Tableaux (Pohon Semantik)**!

**Kunci Pembahasan & Solusi:**
1. **Simbolisasi Proposisi Atomik:**
   * $p$ : Wisnu belajar rajin
   * $q$ : Wisnu pandai
   * $r$ : Wisnu diterima di universitas
   * $s$ : Wisnu mendapat beasiswa
   * **Premis 1 ($P_1$):** $(p \land q) \to r$
   * **Premis 2 ($P_2$):** $\neg p \to \neg s$
   * **Konklusi ($C$):** $q \to (r \lor \neg s)$
2. **Pembuktian Validitas via Semantic Tableaux:**
   Untuk membuktikan argumen valid, kita tempatkan seluruh Premis dan **Negasi dari Konklusi** ($\neg C$) pada akar pohon:
   * (1) $(p \land q) \to r$ [Premis 1]
   * (2) $\neg p \to \neg s$ [Premis 2]
   * (3) $\neg [q \to (r \lor \neg s)]$ [Negasi Konklusi]

   *Langkah Ekspansi Tableaux:*
   * Dari (3) menggunakan Aturan $\alpha$ ($\neg(A \to B) \equiv A \text{ dan } \neg B$):
     * (4) $q$
     * (5) $\neg (r \lor \neg s)$
   * Dari (5) menggunakan Aturan $\alpha$ ($\neg(A \lor B) \equiv \neg A \text{ dan } \neg B$):
     * (6) $\neg r$
     * (7) $\neg \neg s \implies s$
   * Sekarang ekspansi Premis 2 baris (2) menggunakan Aturan $\beta$ ($\neg p \to \neg s \equiv \neg(\neg p) \lor \neg s \equiv p \lor \neg s$):
     * Cabang Kiri: $p$
     * Cabang Kanan: $\neg s$
       * Pada Cabang Kanan, terdapat $\neg s$ dan baris (7) memuat $s$. Terjadi kontradiksi! **Cabang Kanan TERTUTUP ($\times$)**.
   * Lanjutkan Cabang Kiri yang memuat $p$:
     * Sekarang ekspansi baris (1) $(p \land q) \to r \equiv \neg(p \land q) \lor r \equiv (\neg p \lor \neg q) \lor r$:
       * Sub-cabang 1: $\neg p \implies$ Berkontradiksi dengan $p$ dari cabang kiri! **TERTUTUP ($\times$)**.
       * Sub-cabang 2: $\neg q \implies$ Berkontradiksi dengan baris (4) yang memuat $q$! **TERTUTUP ($\times$)**.
       * Sub-cabang 3: $r \implies$ Berkontradiksi dengan baris (6) yang memuat $\neg r$! **TERTUTUP ($\times$)**.
3. **Kesimpulan:**
   Karena **seluruh cabang pohon semantik tertutup ($\times$)**, maka negasi konklusi terbukti mustahil (*kontradiksi*). Dengan demikian, argumen penalaran di atas terbukti **VALID**.

---

### Soal UTS 2: Pembuktian Konsekuensi Logis via Metode Resolusi Proposisional
**Deskripsi Soal:**
Buktikan bahwa $(p \lor q) \to r \models (q \to r) \land (p \to r)$ menggunakan metode **Resolusi Refutasi (Resolution Refutation)**!

**Kunci Pembahasan & Solusi:**
1. **Konversi Premis ke Bentuk Klausa (CNF):**
   $$P: (p \lor q) \to r \equiv \neg(p \lor q) \lor r \equiv (\neg p \land \neg q) \lor r$$
   Terapkan hukum distributif:
   $$(\neg p \lor r) \land (\neg q \lor r)$$
   Diperoleh dua klausa awal:
   * **Klausa 1 ($C_1$):** $\{\neg p, r\}$
   * **Klausa 2 ($C_2$):** $\{\neg q, r\}$
2. **Negasikan Konklusi dan Konversi ke Klausa:**
   $$\begin{aligned}
   \neg C &= \neg \big[ (q \to r) \land (p \to r) \big] \\
   &\equiv \neg(q \to r) \lor \neg(p \to r) \\
   &\equiv (q \land \neg r) \lor (p \land \neg r) \\
   &\equiv \neg r \land (p \lor q)
   \end{aligned}$$
   Diperoleh dua klausa dari negasi konklusi:
   * **Klausa 3 ($C_3$):** $\{\neg r\}$
   * **Klausa 4 ($C_4$):** $\{p, q\}$
3. **Langkah-Langkah Resolusi (Pencarian Resolvent):**
   * **Resolusi $C_1$ dan $C_3$:**
     $C_1 = \{\neg p, r\}$ dan $C_3 = \{\neg r\}$ (pasangan literal komplementer: $r$ dan $\neg r$)
     $$\mathbf{C_5 = \text{Res}(C_1, C_3) = \{\neg p\}}$$
   * **Resolusi $C_2$ dan $C_3$:**
     $C_2 = \{\neg q, r\}$ dan $C_3 = \{\neg r\}$ (komplementer: $r$ dan $\neg r$)
     $$\mathbf{C_6 = \text{Res}(C_2, C_3) = \{\neg q\}}$$
   * **Resolusi $C_4$ dan $C_5$:**
     $C_4 = \{p, q\}$ dan $C_5 = \{\neg p\}$ (komplementer: $p$ dan $\neg p$)
     $$\mathbf{C_7 = \text{Res}(C_4, C_5) = \{q\}}$$
   * **Resolusi $C_6$ dan $C_7$:**
     $C_6 = \{\neg q\}$ dan $C_7 = \{q\}$ (komplementer: $q$ dan $\neg q$)
     $$\mathbf{C_8 = \text{Res}(C_6, C_7) = \square \quad (\text{Klausa Kosong / Empty Clause})}$$
4. **Kesimpulan:**
   Dihasilkannya klausa kosong ($\square$) membuktikan bahwa premis bersama negasi konklusi tidak konsisten (*unsatisfiable*). Maka konsekuensi logis $(p \lor q) \to r \models (q \to r) \land (p \to r)$ **terbukti valid**.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (FIRST-ORDER LOGIC & KUANTOR)

### Soal UAS 1: Penerjemahan Bahasa Alami ke Logika Predikat Orde Pertama (FOL)
**Deskripsi Soal:**
Diberikan domain pembicaraan seluruh manusia di universitas:
* $\text{Mhs}(x)$ : $x$ adalah mahasiswa
* $\text{Dosen}(x)$ : $x$ adalah dosen
* $\text{Matkul}(y)$ : $y$ adalah mata kuliah
* $\text{Ambil}(x, y)$ : $x$ mengambil mata kuliah $y$
* $\text{Ajar}(x, y)$ : $x$ mengajar mata kuliah $y$
* $\text{Lulus}(x, y)$ : $x$ lulus pada mata kuliah $y$

Terjemahkan kalimat-kalimat berikut ke dalam formula First-Order Logic (FOL):
1. *"Setiap mahasiswa mengambil sekurang-kurangnya satu mata kuliah."*
2. *"Tidak ada dosen yang mengambil mata kuliah yang dia ajarkan sendiri."*
3. *"Ada mahasiswa yang lulus di semua mata kuliah yang dia ambil."*

**Kunci Pembahasan & Solusi:**
1. **Kalimat 1:**
   $$\forall x \Big( \text{Mhs}(x) \to \exists y \big( \text{Matkul}(y) \land \text{Ambil}(x, y) \big) \Big)$$
   *(Setiap mahasiswa mengimplikasikan ada mata kuliah $y$ sedemikian rupa sehingga ia mengambil $y$).*
2. **Kalimat 2:**
   Dapat ditulis dengan negasi kuantor eksistensial:
   $$\neg \exists x \exists y \Big( \text{Dosen}(x) \land \text{Matkul}(y) \land \text{Ajar}(x, y) \land \text{Ambil}(x, y) \Big)$$
   Atau ekuivalen menggunakan kuantor universal:
   $$\forall x \forall y \Big( (\text{Dosen}(x) \land \text{Matkul}(y) \land \text{Ajar}(x, y)) \to \neg \text{Ambil}(x, y) \Big)$$
3. **Kalimat 3:**
   $$\exists x \Big( \text{Mhs}(x) \land \forall y \big( (\text{Matkul}(y) \land \text{Ambil}(x, y)) \to \text{Lulus}(x, y) \big) \Big)$$

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Mengapa Logika Proposisional tidak cukup dalam pemodelan sistem cerdas komputer sehingga para ilmuwan mengembangkan First-Order Logic (FOL)?"
**Jawaban Komprehensif:**
Logika proposisional hanya menganggap proposisi sebagai unit atomik tunggal ($p, q, r$) yang bernilai benar atau salah. Ia memiliki keterbatasan mendasar:
1. **Tidak mampu mengekspresikan objek individu dan relasi di dalamnya:** Kalimat *"Socrates adalah manusia"* dan *"Plato adalah manusia"* harus dilambangkan dengan dua simbol variabel sama sekali tidak berhubungan ($p$ dan $q$), kehilangan fakta bahwa keduanya berbagi predikat yang sama.
2. **Tidak memiliki mekanisme kuantifikasi:** Logika proposisional tidak dapat menyatakan aturan generalisasi universal seperti *"Semua manusia fana"* ($\forall x (\text{Manusia}(x) \to \text{Fana}(x))$) tanpa harus menuliskan konjungsi tak terhingga dari setiap entitas di alam semesta. FOL mengatasi ini dengan memperkenalkan suku (*terms*), predikat, fungsi, dan kuantor ($\forall, \exists$).

### Q2: "Jelaskan perbedaan mendasar antara Modus Ponens dan Modus Tollens serta sebutkan fallacy (kekeliruan) yang sering terjadi pada keduanya!"
**Jawaban Komprehensif:**
* **Modus Ponens (Penegasan Anteseden):** Dari $p \to q$ dan $p$, kita dapat menarik kesimpulan $q$.
  * *Fallacy terkait:* **Affirming the Consequent** (Menegaskan Konsekuen), yaitu menyimpulkan $p$ dari $p \to q$ dan $q$ (contoh keliru: *"Jika hujan jalanan basah; jalanan basah; maka pasti hujan"* padahal bisa disiram mobil tangki).
* **Modus Tollens (Penyangkalan Konsekuen):** Dari $p \to q$ dan $\neg q$, kita dapat menarik kesimpulan $\neg p$.
  * *Fallacy terkait:* **Denying the Antecedent** (Menyangkal Anteseden), yaitu menyimpulkan $\neg q$ dari $p \to q$ dan $\neg p$ (contoh keliru: *"Jika tidak hujan, maka jalanan pasti tidak basah"*).

### Q3: "Bagaimana algoritma Resolusi bekerja dalam eksekusi bahasa pemrograman deklaratif seperti Prolog?"
**Jawaban Komprehensif:**
Prolog merepresentasikan basis pengetahuannya dalam bentuk **Klausa Horn** (klausa disjungsi dengan paling banyak satu literal positif). 
Ketika pengguna mengajukan kueri (*Goal*), Prolog:
1. Menegasikan kueri tersebut.
2. Melakukan pencarian pohon pembuktian dari atas ke bawah (*Top-Down SLD-Resolution: Selective Linear Definite clause resolution*).
3. Melakukan **Unifikasi** (pencocokan variabel dengan fakta/aturan).
4. Jika unifikasi berhasil meniadakan semua predikat tujuan hingga menghasilkan **klausa kosong ($\square$)**, maka kueri terbukti benar (*True*), dan Prolog menampilkan nilai instansiasi variabel pengganti yang ditemukan.
