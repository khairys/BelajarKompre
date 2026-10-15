# Bank Contoh Soal & Pembahasan: Struktur Data

> Sumber rujukan: Bank soal UTS & UAS Struktur Data Departemen Informatika Universitas Diponegoro (Koleksi Dosen Pengampu & HMIF 2017–2023).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (POINTER, LINKED LIST & ADT LINIER)

### Soal UTS 1: Analisis Kesalahan Bug Pointer pada Linked List (Soal Asli UAS Undip 2023)
**Deskripsi Soal:**
Diberikan algoritma pencarian elemen $X$ pada sebuah Single Linked List $L$ berikut:
```pascal
P <- First(L)
while (Next(P) =/= NIL and (X =/= Info(P))) do
    P <- Next(P)
{ Next(P) = NIL or X = Info(P) }
```
1. Jelaskan kesalahan fatal (*runtime error / bug*) yang terdapat pada algoritma pencarian di atas jika list $L$ adalah **list kosong** atau jika $X$ **tidak ditemukan** di dalam list!
2. Tuliskan perbaikan algoritma pencarian elemen pada list linier yang benar dan aman dari *null pointer dereference*!

**Kunci Pembahasan & Solusi:**
1. **Analisis Kesalahan:**
   * **Kasus List Kosong:** Jika list $L$ kosong, maka `First(L)` bernilai `NIL`. Dengan demikian, nilai awal dari pointer `P` adalah `NIL`. Pada evaluasi kondisi `while`, program mencoba mengeksekusi `Next(P)` di mana `P` bernilai `NIL`. Men-dereferensikan pointer `NIL` akan menyebabkan program mengalami *crash* seketika (**Null Pointer Dereference / Segmentation Fault**).
   * **Kasus $X$ Tidak Ditemukan:** Jika $X$ tidak ada di dalam list, perulangan akan berhenti saat `Next(P) == NIL` (elemen terakhir). Namun, elemen terakhir tersebut (`Info(P)`) belum sempat diperiksa apakah sama dengan $X$ atau bukan. Jika kondisi berhenti dievaluasi di luar loop, kode sering kali salah menyimpulkan.
2. **Perbaikan Algoritma yang Benar (Standar Inggriani Liem / Undip):**
   ```text
   { Algoritma Pencarian Elemen X yang Aman }
   P <- First(L)
   Found <- false

   while (P =/= NIL and not Found) do
       if Info(P) == X then
           Found <- true
       else
           P <- Next(P)
       endif
   endwhile

   { P = NIL (tidak ditemukan) or Found = true (ditemukan di alamat P) }
   if Found then
       output("Elemen ditemukan pada alamat:", P)
   else
       output("Elemen tidak ditemukan di dalam list")
   endif
   ```
   *(Kunci Perbaikan: Kondisi `P =/= NIL` selalu diperiksa terlebih dahulu sebelum mengakses `Info(P)` menggunakan sifat evaluasi sirkuit-pendek / short-circuit boolean).*

---

### Soal UTS 2: Operasi Irisan Dua Linked List (IntersectList - Soal Asli Undip 2023)
**Deskripsi Soal:**
Buatlah sebuah prosedur dalam pseudokode formal:
$$\text{Procedure IntersectList(input } L_1: \text{List}, \text{input } L_2: \text{List}, \text{output } L_3: \text{List})$$
yang menghasilkan list baru $L_3$ yang berisi elemen-elemen irisan ($L_1 \cap L_2$), yaitu elemen yang muncul pada $L_1$ **sekaligus** muncul pada $L_2$! Elemen pada $L_3$ tidak boleh duplikat. Gunakan hanya primitif ADT List: `First`, `Next`, `Info`, `Alokasi`, `InsertLast`.

**Kunci Pembahasan & Solusi:**
```text
Procedure IntersectList(input L1: List, input L2: List, output L3: List)
{ Menghasilkan L3 sebagai himpunan irisan antara L1 dan L2 tanpa duplikasi }
Kamus Lokal:
    P1, P2, P3 : address
    foundInL2  : boolean
    alreadyInL3: boolean

Algoritma:
    CreateEmpty(L3) { Inisialisasi L3 kosong: First(L3) <- NIL }

    P1 <- First(L1)
    while (P1 =/= NIL) do
        { 1. Periksa apakah elemen Info(P1) ada di L2 }
        P2 <- First(L2)
        foundInL2 <- false
        while (P2 =/= NIL and not foundInL2) do
            if Info(P2) == Info(P1) then
                foundInL2 <- true
            else
                P2 <- Next(P2)
            endif
        endwhile

        { 2. Jika ada di L2, periksa apakah sudah pernah dimasukkan ke L3 }
        if foundInL2 then
            P3 <- First(L3)
            alreadyInL3 <- false
            while (P3 =/= NIL and not alreadyInL3) do
                if Info(P3) == Info(P1) then
                    alreadyInL3 <- true
                else
                    P3 <- Next(P3)
                endif
            endwhile

            { 3. Jika belum ada di L3, alokasikan dan sisipkan ke L3 }
            if not alreadyInL3 then
                address PNew <- Alokasi(Info(P1))
                if PNew =/= NIL then
                    InsertLast(L3, PNew)
                endif
            endif
        endif

        P1 <- Next(P1)
    endwhile
```

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (BINARY TREE, BST & POHON SEIMBANG AVL)

### Soal UAS 1: Rekonstruksi Pohon Biner dari Preorder dan Inorder Traversal
**Deskripsi Soal:**
Hasil penelusuran (*traversal*) pada sebuah Pohon Biner (*Binary Tree*) menghasilkan urutan simpul sebagai berikut:
* **Preorder :** `[ A, B, D, E, C, F ]`
* **Inorder  :** `[ D, B, E, A, F, C ]`

1. Rekonstruksikan dan gambarkan struktur pohon biner aslinya!
2. Tentukan urutan hasil kunjungan penelusuran secara **Postorder**!

**Kunci Pembahasan & Solusi:**
1. **Langkah-Langkah Rekonstruksi Pohon:**
   * **Langkah 1 (Akar Utama):** Elemen pertama pada Preorder selalu merupakan **Akar Utama (*Root*)**. Maka Akar $= \mathbf{A}$.
   * **Langkah 2 (Membagi Subpohon Kiri & Kanan via Inorder):**
     * Cari posisi $A$ pada urutan Inorder: `[ D, B, E ]` berada di sebelah kiri $A$, dan `[ F, C ]` berada di sebelah kanan $A$.
     * Maka Subpohon Kiri memuat himpunan simpul $\{D, B, E\}$ dan Subpohon Kanan memuat himpunan simpul $\{F, C\}$.
   * **Langkah 3 (Subpohon Kiri):**
     * Pada Preorder, di antara $\{D, B, E\}$, simpul yang muncul paling pertama adalah $B$. Maka $B$ adalah akar dari subpohon kiri.
     * Lihat posisi $B$ pada Inorder: $D$ di sebelah kiri $B$, dan $E$ di sebelah kanan $B$.
     * Jadi, $D$ adalah anak kiri dari $B$, dan $E$ adalah anak kanan dari $B$.
   * **Langkah 4 (Subpohon Kanan):**
     * Pada Preorder, di antara $\{F, C\}$, simpul yang muncul pertama adalah $C$. Maka $C$ adalah akar dari subpohon kanan.
     * Lihat posisi $C$ pada Inorder: $F$ berada di sebelah kiri $C$.
     * Jadi, $F$ adalah anak kiri dari $C$, dan $C$ tidak memiliki anak kanan.
2. **Struktur Pohon Biner Hasil Rekonstruksi:**
   ```text
           A
          / \
         B   C
        / \  /
       D   E F
   ```
3. **Hasil Kunjungan Postorder (Left, Right, Root):**
   * Subpohon kiri: Kunjungi $D \rightarrow E \rightarrow B$.
   * Subpohon kanan: Kunjungi $F \rightarrow C$.
   * Akar utama: $A$.
   * Urutan Postorder: **`[ D, E, B, F, C, A ]`**.

---

### Soal UAS 2: Penghapusan Simpul Beranak Dua pada Binary Search Tree (BST)
**Deskripsi Soal:**
Diberikan sebuah Binary Search Tree (BST) yang memuat kunci-kunci: `[50, 30, 70, 20, 40, 60, 80]`.
Gambarkan langkah-langkah penghapusan simpul nilai **$50$ (akar dengan dua anak)** menggunakan metode penggantian **Inorder Successor**!

**Kunci Pembahasan & Solusi:**
1. **Kondisi Awal BST:**
   ```text
           50 (Akar yang akan dihapus)
          /  \
        30    70
       /  \  /  \
      20  40 60  80
   ```
2. **Langkah 1: Mencari Inorder Successor dari Simpul 50:**
   * *Inorder Successor* adalah simpul dengan nilai terkecil pada **Subpohon Kanan**.
   * Masuk ke anak kanan (simpul $70$), lalu telusuri cabang paling kiri hingga mentok: simpul **$60$**.
3. **Langkah 2: Salin Nilai Suksesor ke Simpul yang Dihapus:**
   * Ganti nilai $50$ pada akar menjadi nilai suksesor: **$60$**.
4. **Langkah 3: Hapus Simpul Suksesor dari Posisi Semulanya:**
   * Simpul $60$ semula adalah simpul daun (tanpa anak). Putuskan hubungan dari induknya ($70$).
5. **Struktur Akhir BST Pasca-Penghapusan:**
   ```text
           60
          /  \
        30    70
       /  \     \
      20  40    80
   ```
   *(BST tetap mempertahankan sifat terurutnya: $Inorder = [20, 30, 40, 60, 70, 80]$).*

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan kelebihan dan kelemahan Linked List dibandingkan Array statis, serta kapan Anda harus memilih salah satunya!"
**Jawaban Komprehensif:**
* **Perbandingan Karakteristik:**
  * **Ukuran Alokasi:** Array berukuran tetap (*fixed size*) yang ditentukan saat kompilasi sehingga rawan pemborosan memori jika dialokasikan terlalu besar atau *overflow* jika terlalu kecil. Linked List berukuran dinamis yang dapat tumbuh dan menyusut sesuai kebutuhan saat runtime (*heap allocation*).
  * **Operasi Akses:** Array mendukung akses acak instan $O(1)$ via indeks memori fisik kontigu (`arr[i]`). Linked List membutuhkan penelusuran sekuensial $O(N)$ dari `First`.
  * **Operasi Sisip/Hapus:** Menyisipkan elemen di awal array membutuhkan pergeseran seluruh elemen lain sebesar $O(N)$. Pada Linked List, penyisipan/penghapusan di awal hanya memerlukan modifikasi pointer sebesar $O(1)$.
* **Kapan Memilih:**
  * Pilih **Array** jika ukuran data relatif stabil dan aplikasi sering melakukan pembacaan elemen secara acak (misal tabel pencarian / *lookup table*).
  * Pilih **Linked List** jika ukuran data sangat dinamis dan aplikasi sering melakukan operasi penambahan dan penghapusan elemen secara berulang di posisi depan/tengah.

### Q2: "Bagaimana cara kerja algoritma Floyd's Tortoise and Hare (Two-Pointer) untuk mendeteksi adanya siklus (loop) pada sebuah Linked List tanpa menggunakan memori tambahan?"
**Jawaban Komprehensif:**
Algoritma ini menggunakan dua pointer penunjuk yang bergerak melintasi list dengan kecepatan berbeda:
1. Pointer **Kura-Kura (*Slow Pointer*)** bergerak maju $1$ langkah setiap iterasi (`slow = slow->next`).
2. Pointer **Kelinci (*Fast Pointer*)** bergerak maju $2$ langkah setiap iterasi (`fast = fast->next->next`).
* **Logika Deteksi:**
  * Jika list tidak memuat siklus (list linier berhingga), maka pointer Kelinci akan mencapai ujung list (`fast == NULL` atau `fast->next == NULL`).
  * Jika list memuat siklus melingkar tertutup, pointer Kelinci yang lebih cepat pada akhirnya **pasti akan mengejar dan bertemu pada simpul yang tepat sama dengan pointer Kura-Kura** (`slow == fast`).
Algoritma ini membuktikan keberadaan siklus dalam kompleksitas waktu linier $O(N)$ dengan efisiensi ruang memori tambahan konstan murni $O(1)$.
