# Bank Contoh Soal & Pembahasan: Algoritma dan Pemrograman

> Sumber rujukan: Bank soal UTS & UAS Algoritma dan Pemrograman Departemen Informatika Universitas Diponegoro (Koleksi Pengampu: Dr. Aris Puji Widodo, M.T. & Tim Dosen Alpro, 2018–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (STRUKTUR KONTROL, FUNGSI & POINTER)

### Soal UTS 1: Konversi Waktu & Validasi Input (Soal Asli Alpro Undip)
**Deskripsi Soal:**
Buatlah sebuah program lengkap dalam bahasa C yang membaca total durasi waktu dalam satuan **detik** (bilangan bulat positif) dari keyboard. 
1. Lakukan validasi input: jika nilai detik $< 0$, program harus menampilkan pesan error dan meminta input ulang hingga benar.
2. Konversikan total detik tersebut ke dalam format baku: **Jam, Menit, dan Detik** ($1\text{ Jam} = 3600\text{ detik}$, $1\text{ Menit} = 60\text{ detik}$).
3. Tampilkan hasil konversi dengan format tampilan rapi `HH:MM:SS` (misal 3665 detik $\rightarrow$ `01:01:05`).

**Kunci Pembahasan & Solusi (Kode C):**
```c
#include <stdio.h>

int main() {
    int total_detik;
    int jam, menit, detik, sisa;

    // 1. Validasi Input menggunakan perulangan do-while
    do {
        printf("Masukkan total waktu dalam detik (>= 0): ");
        if (scanf("%d", &total_detik) != 1) {
            printf("Input bukan angka!\n");
            return 1;
        }
        if (total_detik < 0) {
            printf("Error: Durasi waktu tidak boleh negatif! Coba lagi.\n");
        }
    } while (total_detik < 0);

    // 2. Logika Konversi Matematika Pembagian Bulat dan Modulo
    jam = total_detik / 3600;
    sisa = total_detik % 3600;
    menit = sisa / 60;
    detik = sisa % 60;

    // 3. Menampilkan Output dengan format 2 digit (%02d)
    printf("\nHasil Konversi Waktu:\n");
    printf("%d detik setara dengan %d Jam, %d Menit, %d Detik\n", 
           total_detik, jam, menit, detik);
    printf("Format Baku: [%02d:%02d:%02d]\n", jam, menit, detik);

    return 0;
}
```

---

### Soal UTS 2: Mekanisme Passing Parameter Pointer (Swap Function)
**Deskripsi Soal:**
Diberikan potongan kode fungsi berikut:
```c
void tukar_salah(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}
```
1. Jelaskan mengapa fungsi `tukar_salah` di atas **gagal** menukar nilai dua variabel di fungsi `main`!
2. Perbaikilah fungsi tersebut menggunakan konsep **Pointer / Pass by Reference** agar pertukaran nilai di memori berhasil, dan sertakan contoh pemanggilannya di `main`!

**Kunci Pembahasan & Solusi:**
1. **Analisis Kegagalan `tukar_salah`:**
   Bahasa C secara default menerapkan mekanisme **Pass by Value**. Ketika fungsi `tukar_salah(x, y)` dipanggil, nilai variabel `x` dan `y` disalin (*cloned*) ke variabel lokal baru `a` dan `b` pada *call stack* fungsi tersebut. Pertukaran nilai yang terjadi di dalam badan fungsi hanya memanipulasi salinan lokal tersebut. Ketika eksekusi fungsi selesai, *stack frame* fungsi dihancurkan, dan nilai variabel asli `x` dan `y` di fungsi `main` sama sekali tidak berubah.
2. **Perbaikan Kode Menggunakan Pointer:**
   Untuk mengubah variabel asli pemanggil, fungsi harus menerima **alamat memori** variabel (*Pass by Reference*) menggunakan pointer:
   ```c
   #include <stdio.h>

   // Fungsi swap yang benar menerima pointer ke integer
   void tukar_benar(int *a, int *b) {
       int temp = *a;  // Ambil nilai yang berada di alamat a
       *a = *b;        // Simpan nilai alamat b ke alamat a
       *b = temp;      // Simpan nilai temp ke alamat b
   }

   int main() {
       int x = 10, y = 25;
       printf("Sebelum ditukar: x = %d, y = %d\n", x, y);

       // Kirim alamat memori x dan y menggunakan operator &
       tukar_benar(&x, &y);

       printf("Setelah ditukar: x = %d, y = %d\n", x, y);
       // Output: x = 25, y = 10 (Berhasil ditukar!)
       return 0;
   }
   ```

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (STRUCT, SORTING, SEARCHING & FILE I/O)

### Soal UAS 1: Array of Struct & Sorting Nilai Mahasiswa
**Deskripsi Soal:**
Sebuah program di jurusan Informatika Undip perlu mengelola data nilai mahasiswa.
1. Definisikan tipe data bentukan (`struct`) bernama `Mahasiswa` yang memuat field: `nim` (string maks 15 karakter), `nama` (string maks 50 karakter), dan `nilai_akhir` (float).
2. Tuliskan fungsi `urutkan_mahasiswa` yang mengurutkan array bertipe `Mahasiswa` sebanyak $N$ elemen secara **Descending** (dari nilai akhir tertinggi ke terendah) menggunakan algoritma **Selection Sort**!

**Kunci Pembahasan & Solusi (Kode C):**
```c
#include <stdio.h>
#include <string.h>

// 1. Definisi Tipe Bentukan Struct Mahasiswa
typedef struct {
    char nim[15];
    char nama[50];
    float nilai_akhir;
} Mahasiswa;

// 2. Fungsi Selection Sort Descending
void urutkan_mahasiswa(Mahasiswa data[], int n) {
    int i, j, max_idx;
    Mahasiswa temp;

    for (i = 0; i < n - 1; i++) {
        // Cari indeks mahasiswa dengan nilai terbesar di sisa array
        max_idx = i;
        for (j = i + 1; j < n; j++) {
            if (data[j].nilai_akhir > data[max_idx].nilai_akhir) {
                max_idx = j;
            }
        }
        // Tukar posisi jika ditemukan nilai yang lebih tinggi
        if (max_idx != i) {
            temp = data[i];
            data[i] = data[max_idx];
            data[max_idx] = temp;
        }
    }
}
```

---

### Soal UAS 2: Implementasi Binary Search (Pencarian Bagi-Dua)
**Deskripsi Soal:**
Diberikan sebuah array integer terurut menaik: `A = [12, 18, 25, 33, 47, 56, 68, 79, 91, 99]`.
1. Tuliskan fungsi iteratif `binary_search(int arr[], int n, int target)` dalam bahasa C yang mengembalikan indeks posisi elemen jika ditemukan, atau `-1` jika tidak ditemukan!
2. Buatlah tabel jejak pencarian (*trace table*) yang menunjukkan pergerakan variabel `low`, `high`, dan `mid` saat mencari target angka **$68$**!

**Kunci Pembahasan & Solusi:**
1. **Implementasi Fungsi C:**
   ```c
   int binary_search(int arr[], int n, int target) {
       int low = 0;
       int high = n - 1;

       while (low <= high) {
           int mid = low + (high - low) / 2; // Mencegah integer overflow

           if (arr[mid] == target) {
               return mid; // Elemen ditemukan di indeks mid
           } else if (arr[mid] < target) {
               low = mid + 1; // Cari di paruh kanan
           } else {
               high = mid - 1; // Cari di paruh kiri
           }
       }
       return -1; // Elemen tidak ditemukan
   }
   ```
2. **Tabel Jejak Pencarian (Tracing untuk Target $= 68$ pada $N=10$):**

| Langkah | `low` | `high` | `mid` | `arr[mid]` | Evaluasi | Aksi Pergeseran |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Iterasi 1 | 0 | 9 | $(0+9)/2 = 4$ | $47$ | $47 < 68$ | Pindah ke kanan: `low = mid + 1 = 5` |
| Iterasi 2 | 5 | 9 | $(5+9)/2 = 7$ | $79$ | $79 > 68$ | Pindah ke kiri: `high = mid - 1 = 6` |
| Iterasi 3 | 5 | 6 | $(5+6)/2 = 5$ | $56$ | $56 < 68$ | Pindah ke kanan: `low = mid + 1 = 6` |
| Iterasi 4 | 6 | 6 | $(6+6)/2 = 6$ | $68$ | $68 == 68$ | **Ditemukan pada indeks ke-6!** |

Hanya membutuhkan **4 kali perbandingan**, jauh lebih cepat daripada Linear Search yang membutuhkan 7 kali perbandingan.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan apa itu Segmentation Fault dan Memory Leak dalam bahasa C, serta bagaimana cara menghindarinya!"
**Jawaban Komprehensif:**
* **Segmentation Fault (Segfault):** Kesalahan fatal runtime yang terjadi ketika program mencoba mengakses blok memori yang tidak diizinkan atau tidak valid oleh sistem operasi. Penyebab umum: men-dereference *null pointer* (`*ptr` saat `ptr == NULL`), mengakses indeks array di luar batas (*buffer overflow*), atau menulis ke segmen memori *read-only*. Cara menghindari: selalu validasi keberadaan pointer sebelum digunakan dan patuhi batas ukuran array.
* **Memory Leak:** Kondisi di mana memori dinamis yang dialokasikan di area *Heap* (melalui `malloc` atau `calloc`) tidak pernah dibebaskan kembali ke sistem operasi menggunakan fungsi `free()`, sementara pointer penunjuknya hilang. Akumulasi kebocoran memori ini dapat menyebabkan sistem kehabisan RAM (*Out of Memory*). Cara menghindari: setiap pemanggilan `malloc()` harus memiliki pasangan pemanggilan `free()` yang tepat.

### Q2: "Mengapa Binary Search memiliki kompleksitas waktu $O(\log N)$ dan apa prasyarat mutlak sebelum algoritma ini dapat dieksekusi?"
**Jawaban Komprehensif:**
* **Alasan Kompleksitas $O(\log N)$:** Pada setiap iterasi, algoritma membandingkan elemen tengah (*mid*) dengan target. Jika tidak cocok, seluruh separuh ruang pencarian (setengah dari sisa data) langsung diabaikan. Jumlah elemen berkurang secara eksponensial: $N \rightarrow N/2 \rightarrow N/4 \rightarrow \dots \rightarrow 1$. Jumlah langkah maksimum untuk mereduksi $N$ menjadi 1 adalah $\log_2 N$.
* **Prasyarat Mutlak:** Kumpulan data pada array **wajib sudah terurut (*sorted*)** berdasarkan kunci pencarian. Jika data belum terurut, binary search akan menghasilkan keputusan pergeseran `low`/`high` yang salah dan gagal menemukan data.
