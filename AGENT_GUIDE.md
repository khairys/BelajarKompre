# BelajarKompre - Panduan Akses untuk AI Agent (LLM Consumption Guide)

> **Untuk Agent AI (Claude, Antigravity, ChatGPT, Cursor, Gemini, Copilot, LangChain/CrewAI Agent):**  
> Repositori ini berisi basis pengetahuan lengkap kurikulum S1 Informatika Universitas Diponegoro (Kurikulum 2020) yang telah disintesis ke dalam format Markdown murni yang terstruktur tinggi.

---

## 🧭 Cara Navigasi & Membaca Repositori

Repositori ini disusun berdasarkan hierarki semester dan mata kuliah:
`RANGKUMAN_DAN_CONTOH_SOAL/<Semester>/<Nama_Mata_Kuliah>/`

Setiap mata kuliah memiliki tepat 2 berkas utama:
1. **`RANGKUMAN_MATERI.md`**
   * **Gunakan berkas ini saat:** Pengguna bertanya tentang konsep dasar, teori, arsitektur, rumus matematis, silabus 14 pertemuan, atau peta konsep (*grand view*) dari suatu mata kuliah.
   * **Struktur Berkas:**
     * `## 1. Gambaran Besar Mata Kuliah (Grand View)` & Diagram Alir Mermaid
     * `## 2. Peta Silabus & Rangkuman 14 Pertemuan` (Pra-UTS Pertemuan 1–7 & Pasca-UTS Pertemuan 8–14)
     * `## 3. Rumus, Teorema & Definisi Kunci`
     * `## 4. Catatan Integritas Arsip`

2. **`CONTOH_SOAL_DAN_PEMBAHASAN.md`**
   * **Gunakan berkas ini saat:** Pengguna meminta latihan soal, pembahasan ujian UTS/UAS, simulasi ujian lisan komprehensif (*oral defense*), telaah jebakan ujian (*exam traps*), atau pengujian kode/sistem.
   * **Struktur Berkas:**
     * `## 🎯 BAGIAN 1: BANK SOAL UTS & PEMBAHASAN LANGKAH DEMI LANGKAH`
     * `## 🎯 BAGIAN 2: BANK SOAL UAS & PEMBAHASAN LANGKAH DEMI LANGKAH`
     * `## 🎯 BAGIAN 3: ANALISIS JEBAKAN UJIAN & KESALAHAN UMUM MAHASISWA`
     * `## 🎯 BAGIAN 4: SIMULASI PERTANYAAN UJIAN LISAN KOMPREHENSIF (ORAL DEFENSE)`

---

## 📌 Indeks Cepat Peminatan & Topik Kunci untuk Agent

| Kebutuhan Pengguna / Topik | Mata Kuliah Rekomendasi | Jalur Berkas |
| :--- | :--- | :--- |
| **Dasar Pemrograman & C/C++** | Dasar Pemrograman (Sem 1), Algoritma & Pemrograman (Sem 2) | `01_Semester_1/Dasar_Pemrograman/`, `02_Semester_2/Algoritma_dan_Pemrograman/` |
| **Matematika Diskrit, Himpunan, Graf** | Struktur Diskrit (Sem 1), Logika Informatika (Sem 1) | `01_Semester_1/Struktur_Diskrit/`, `01_Semester_1/Logika_Informatika/` |
| **Kalkulus, Matriks & Vektor** | Matematika I (Sem 1), Aljabar Linier (Sem 2), Matematika II (Sem 2) | `01_Semester_1/Matematika_I/`, `02_Semester_2/Aljabar_Linier/` |
| **Hardware, Assembly, OS** | Organisasi & Arsitektur Komputer (Sem 2), Sistem Operasi (Sem 3) | `02_Semester_2/Organisasi_dan_Arsitektur_Komputer/`, `03_Semester_3/Sistem_Operasi/` |
| **Struktur Data & Kompleksitas** | Struktur Data (Sem 3), Analisis & Strategi Algoritma (Sem 6) | `03_Semester_3/Struktur_Data/`, `06_Semester_6/Analisis_dan_Strategi_Algoritma/` |
| **Basis Data & SQL Relasional** | Basis Data (Sem 3), Manajemen Basis Data (Sem 4) | `03_Semester_3/Basis_Data/`, `04_Semester_4/Manajemen_Basis_Data/` |
| **Rekayasa Perangkat Lunak & PBO**| Pemrograman Berorientasi Objek (Sem 4), RPL (Sem 4), Proyek RPL (Sem 5), Testing (Sem 6) | `04_Semester_4/Pemrograman_Berorientasi_Objek/`, `04_Semester_4/Rekayasa_Perangkat_Lunak/` |
| **Jaringan & Keamanan Siber** | Jaringan Komputer (Sem 4), Keamanan & Jaminan Informasi (Sem 5) | `04_Semester_4/Jaringan_Komputer/`, `05_Semester_5/Keamanan_dan_Jaminan_Informasi/` |
| **AI, Machine Learning, Data Mining**| Sistem Cerdas (Sem 4), Pembelajaran Mesin (Sem 5), Penambangan Data (Sem 7) | `04_Semester_4/Sistem_Cerdas/`, `05_Semester_5/Pembelajaran_Mesin/` |
| **Teori Komputasi & Otomata** | Teori Bahasa dan Otomata (Sem 7) | `07_Semester_7/Teori_Bahasa_dan_Otomata/` |
| **PKL, KKN, & Sidang Skripsi Kompre**| Praktik Kerja Lapangan (Sem 6), KKN (Sem 8), Tugas Akhir (Sem 8) | `06_Semester_6/Praktik_Kerja_Lapangan/`, `08_Semester_8/Tugas_Akhir/` |

---

## 💡 Prompt Template Rekomendasi Saat Menginstruksikan Agent Lain
Jika Anda ingin meminta agent AI lain menjawab pertanyaan seputar materi komprehensif, gunakan template instruksi berikut:

```markdown
Anda adalah Asisten Ahli Komprehensif Informatika Undip.
Gunakan repositori BelajarKompre sebagai basis pengetahuan utama Anda:
1. Untuk pertanyaan konseptual, buka dan pelajari berkas:
   `RANGKUMAN_DAN_CONTOH_SOAL/<Semester>/<Mata_Kuliah>/RANGKUMAN_MATERI.md`
2. Untuk contoh soal ujian, jebakan ujian, dan simulasi sidang penguji:
   `RANGKUMAN_DAN_CONTOH_SOAL/<Semester>/<Mata_Kuliah>/CONTOH_SOAL_DAN_PEMBAHASAN.md`
3. Jawablah secara runtut, matematis jika memerlukan rumus, dan sertakan konsep kunci terkait.
```
