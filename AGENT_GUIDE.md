# BelajarKompre - Panduan Akses untuk AI Agent (LLM Consumption Guide)

> **Untuk Agent AI (Claude, Antigravity, ChatGPT, Cursor, Gemini, Copilot, LangChain/CrewAI Agent):**  
> Repositori ini berisi basis pengetahuan lengkap kurikulum S1 Informatika Universitas Diponegoro (Kurikulum 2020) yang telah disintesis ke dalam format Markdown murni yang terstruktur tinggi.

---

## 🧭 Arsitektur Pengetahuan Repositori

Repositori ini disusun dalam 2 tingkat kedalaman kajian:

### 1. Tingkat Makro: Berkas Acuan Sintesis Semester (`semester1.md` s.d. `semester8.md`)
* **Lokasi Root:** `semester1.md` s.d. `semester8.md`
* **Gunakan berkas ini saat:**
  * Pengguna meminta *helicopter view*, peta konsep, atau sintesis satu semester utuh.
  * Menjelaskan hubungan logis antarmata kuliah (contoh: bagaimana Aljabar Linier & Alpro di Semester 2 menjadi prasyarat Grafika & AI di Semester 4).
  * Meninjau *checklist* kesiapan ujian komprehensif semester.
  * Menelaah kumpulan rumus matematis utama per semester.

### 2. Tingkat Mikro: Repositori Kajian Per Mata Kuliah (88 Berkas)
* **Lokasi Folder:** `RANGKUMAN_DAN_CONTOH_SOAL/<Semester>/<Nama_Mata_Kuliah>/`
* **Berkas yang tersedia di tiap mata kuliah:**
  1. **`RANGKUMAN_MATERI.md`**
     * Grand View mata kuliah & Diagram Alir Mermaid
     * Silabus 14 pertemuan (Pra-UTS Pertemuan 1–7 & Pasca-UTS Pertemuan 8–14)
     * Teorema kunci, formula, arsitektur sistem, dan definisi penting
  2. **`CONTOH_SOAL_DAN_PEMBAHASAN.md`**
     * Bank soal UTS & UAS riil dengan solusi langkah demi langkah (*step-by-step*)
     * Analisis jebakan ujian (*exam traps*) & kekeliruan umum mahasiswa
     * Simulasi pertanyaan ujian lisan komprehensif (*oral defense questions*)

---

## 📌 Indeks Cepat Peminatan & Topik Kunci untuk Agent

| Kebutuhan Pengguna / Topik | Sintesis Semester | Mata Kuliah Spesifik | Jalur Folder Kajian |
| :--- | :--- | :--- | :--- |
| **Dasar Pemrograman & C/C++** | `semester1.md`, `semester2.md` | Dasar Pemrograman, Alpro | `01_Semester_1/Dasar_Pemrograman/`, `02_Semester_2/Algoritma_dan_Pemrograman/` |
| **Matematika Diskrit, Himpunan, Graf** | `semester1.md` | Struktur Diskrit, Logika Informatika | `01_Semester_1/Struktur_Diskrit/`, `01_Semester_1/Logika_Informatika/` |
| **Kalkulus, Matriks & Vektor** | `semester1.md`, `semester2.md` | Matematika I, Aljabar Linier, Matematika II | `01_Semester_1/Matematika_I/`, `02_Semester_2/Aljabar_Linier/`, `02_Semester_2/Matematika_II/` |
| **Hardware, Assembly, OS** | `semester2.md`, `semester3.md` | OARK, Sistem Operasi | `02_Semester_2/Organisasi_dan_Arsitektur_Komputer/`, `03_Semester_3/Sistem_Operasi/` |
| **Struktur Data & Kompleksitas Algoritma** | `semester3.md`, `semester6.md` | Struktur Data, Analisis Strategi Algoritma | `03_Semester_3/Struktur_Data/`, `06_Semester_6/Analisis_dan_Strategi_Algoritma/` |
| **Basis Data & SQL Relasional** | `semester3.md`, `semester4.md` | Basis Data, Manajemen Basis Data | `03_Semester_3/Basis_Data/`, `04_Semester_4/Manajemen_Basis_Data/` |
| **Rekayasa Perangkat Lunak, OOP & Testing**| `semester4.md`, `semester5.md`, `semester6.md` | PBO, RPL, Proyek PL, Uji PL | `04_Semester_4/Pemrograman_Berorientasi_Objek/`, `04_Semester_4/Rekayasa_Perangkat_Lunak/`, `06_Semester_6/Uji_Perangkat_Lunak/` |
| **Jaringan & Keamanan Siber** | `semester4.md`, `semester5.md` | Jaringan Komputer, Keamanan Informasi | `04_Semester_4/Jaringan_Komputer/`, `05_Semester_5/Keamanan_dan_Jaminan_Informasi/` |
| **AI, Machine Learning, Data Mining**| `semester4.md`, `semester5.md`, `semester7.md` | Sistem Cerdas, Machine Learning, Data Mining | `04_Semester_4/Sistem_Cerdas/`, `05_Semester_5/Pembelajaran_Mesin/`, `07_Semester_7/Penambangan_Data/` |
| **Teori Komputasi & Otomata** | `semester7.md` | Teori Bahasa dan Otomata | `07_Semester_7/Teori_Bahasa_dan_Otomata/` |
| **PKL, KKN, & Sidang Skripsi Kompre**| `semester6.md`, `semester8.md` | PKL, KKN, Tugas Akhir | `06_Semester_6/Praktik_Kerja_Lapangan/`, `08_Semester_8/Tugas_Akhir/` |

---

## 💡 Prompt Template Rekomendasi Saat Menginstruksikan Agent Lain

```markdown
Anda adalah Penguji Ahli Ujian Komprehensif S1 Informatika Undip.
Gunakan repositori BelajarKompre sebagai acuan primer Anda:
1. Untuk pemahaman integratif satu semester, pelajari: `semester<X>.md`
2. Untuk konsep silabus dan materi mendalam: `RANGKUMAN_DAN_CONTOH_SOAL/<Semester>/<Mata_Kuliah>/RANGKUMAN_MATERI.md`
3. Untuk bank soal, step-by-step penyelesaian, dan simulasi oral defense: `RANGKUMAN_DAN_CONTOH_SOAL/<Semester>/<Mata_Kuliah>/CONTOH_SOAL_DAN_PEMBAHASAN.md`
4. Jawablah secara terstruktur, matematis (gunakan KaTeX/LaTeX), dan sertakan jebakan ujian jika relevan.
```
