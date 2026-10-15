# Bank Contoh Soal & Pembahasan: Dasar Pemrograman

> Sumber rujukan: Kurasi soal UTS & UAS Informatika Undip tahun 2018–2025.

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (TIPE DATA BENTUKAN & REKURSI)

### Soal UTS 1: ADT Point & Jarak Euclidean
**Deskripsi Soal:**
Diberikan definisi Tipe Data Bentukan (*Abstract Data Type*) `Point` yang merepresentasikan titik 2 dimensi:
* Konstruktor: `MakePoint(x, y)` $\rightarrow$ Point
* Selektor: `Absis(P)` $\rightarrow$ integer/real, `Ordinat(P)` $\rightarrow$ integer/real

**Pertanyaan:**
1. Buatlah fungsi `Kuadran(P)` yang mengembalikan nilai kuadran (1, 2, 3, atau 4) dari sebuah titik $P$ (asumsikan titik tidak berada di sumbu $X$ atau $Y$).
2. Buatlah fungsi `Jarak(P1, P2)` yang menghitung jarak Euclidean antara dua titik $P_1$ dan $P_2$.

**Kunci Pembahasan & Solusi:**
```text
Kuadran : Point -> integer
Kuadran(P):
  depend on (Absis(P), Ordinat(P))
    Absis(P) > 0 and Ordinat(P) > 0 : 1
    Absis(P) < 0 and Ordinat(P) > 0 : 2
    Absis(P) < 0 and Ordinat(P) < 0 : 3
    Absis(P) > 0 and Ordinat(P) < 0 : 4

Jarak : Point x Point -> real
Jarak(P1, P2):
  sqrt( (Absis(P1) - Absis(P2))^2 + (Ordinat(P1) - Ordinat(P2))^2 )
```

---

### Soal UTS 2: Rekursi Perpangkatan & FPB
**Deskripsi Soal:**
Buatlah fungsi fungsional rekursif untuk menghitung perpangkatan bilangan bulat: $Pangkat(a, b) = a^b$ untuk $a \ge 0, b \ge 0$ tanpa menggunakan perulangan `for`/`while` atau operator bawaan `**`.

**Kunci Pembahasan & Solusi:**
* **Basis:** Jika $b = 0$, nilai $a^0 = 1$.
* **Rekurens:** Jika $b > 0$, maka $a \times Pangkat(a, b - 1)$.

```text
Pangkat : integer x integer -> integer
Pangkat(a, b):
  Basis    : if b == 0 -> 1
  Rekurens : if b > 0  -> a * Pangkat(a, b - 1)
```

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (LIST LINIER, SET & POHON BINER)

### Soal UAS 1: Membalik List Linier (`Inverse`)
**Deskripsi Soal:**
Diberikan list linier $L$. Buatlah fungsi fungsional `Inverse(L)` yang mengembalikan list dengan urutan elemen terbalik.
Contoh: `Inverse([1, 2, 3])` $\rightarrow$ `[3, 2, 1]`. Gunakan hanya primitif: `Konso`, `Konsi`, `FirstElmt`, `Tail`, `IsEmpty`.

**Kunci Pembahasan & Solusi:**
* **Basis:** Jika `IsEmpty(L)`, kembalikan `[]`.
* **Rekurens:** Elemen pertama dipindahkan ke paling belakang menggunakan `Konsi`: `Konsi(Inverse(Tail(L)), FirstElmt(L))`.

```text
Inverse : List -> List
Inverse(L):
  Basis    : if IsEmpty(L) -> []
  Rekurens : Konsi(Inverse(Tail(L)), FirstElmt(L))
```

---

### Soal UAS 2: Pengujian Himpunan Bagian (`IsSubset`)
**Deskripsi Soal:**
Diberikan dua himpunan (*Set*) $S_1$ dan $S_2$. Buatlah fungsi predikat `IsSubset(S1, S2)` yang menghasilkan `True` jika seluruh elemen $S_1$ merupakan anggota dari $S_2$.
*(Asumsikan primitif `IsMember(x, S)` sudah tersedia).*

**Kunci Pembahasan & Solusi:**
* **Basis 1:** Jika `IsEmpty(S1)`, maka `True` (himpunan kosong adalah subset dari semua himpunan).
* **Rekurens:** Elemen pertama $S_1$ harus ada di $S_2$, DAN sisa elemen $S_1$ (`Tail(S1)`) juga harus subset dari $S_2$.

```text
IsSubset : Set x Set -> boolean
IsSubset(S1, S2):
  Basis    : if IsEmpty(S1) -> True
  Rekurens : IsMember(FirstElmt(S1), S2) and IsSubset(Tail(S1), S2)
```

---

### Soal UAS 3: Menghitung Kedalaman / Tinggi Pohon Biner (`TinggiPohon`)
**Deskripsi Soal:**
Diberikan sebuah pohon biner $P$. Buatlah fungsi `TinggiPohon(P)` untuk menghitung kedalaman maksimum pohon biner tersebut.
Contoh: Pohon dengan 1 node memiliki tinggi 1. Pohon kosong memiliki tinggi 0.

**Kunci Pembahasan & Solusi:**
* **Basis:** Jika `IsTreeEmpty(P)` $\rightarrow 0$.
* **Rekurens:** $1 + \max(TinggiPohon(Left(P)), TinggiPohon(Right(P)))$.

```text
TinggiPohon : PohonBiner -> integer
TinggiPohon(P):
  Basis    : if IsTreeEmpty(P) -> 0
  Rekurens : 1 + max(TinggiPohon(Left(P)), TinggiPohon(Right(P)))
```

---

## 🎓 BAGIAN 3: SIMULASI PERTANYAAN SIDANG UJIAN KOMPREHENSIF

Pertanyaan-pertanyaan di bawah ini adalah pertanyaan klasik yang sering diajukan dosen penguji sidang komprehensif untuk menguji pemahaman fungsional mahasiswa:

1. **Penguji:** *"Apa perbedaan primitif `Konso` dan `Konsi` pada List?"*
   * **Jawaban:** `Konso(e, L)` (Konstruksi O) menyisipkan elemen di posisi **paling awal/depan** list, sedangkan `Konsi(L, e)` (Konstruksi I) menyisipkan elemen di posisi **paling belakang/akhir** list.

2. **Penguji:** *"Mengapa pada pemrosesan list fungsional, operasi rekursi hampir selalu menggunakan `FirstElmt` dan `Tail`, bukan indeks array?"*
   * **Jawaban:** Karena list fungsional dimodelkan sebagai struktur data dinamis berantai rekursif di mana akses kepala (`FirstElmt`) dan ekor (`Tail`) bernilai konstan $\mathcal{O}(1)$, tanpa mutasi alamat array atau variabel indeks.

3. **Penguji:** *"Apa yang dimaksud dengan Basis dan Rekurens pada fungsi rekursif, dan apa konsekuensinya jika Basis tidak terdefinisi dengan benar?"*
   * **Jawaban:** Basis adalah kondisi terminasi berhentinya pemanggilan rekursif untuk ukuran data paling kecil, sedangkan Rekurens adalah langkah induksi untuk mengecilkan ukuran data. Jika basis salah atau tidak tercapai, program akan mengalami *infinite recursion* yang memicu *Stack Overflow Error*.
