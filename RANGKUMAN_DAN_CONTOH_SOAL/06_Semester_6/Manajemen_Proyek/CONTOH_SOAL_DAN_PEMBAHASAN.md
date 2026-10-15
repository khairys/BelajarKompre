# Bank Contoh Soal & Pembahasan: Manajemen Proyek Teknologi Informasi

> **Sumber Rujukan:** Kumpulan Berkas Ujian Tengah Semester (UTS) & Ujian Akhir Semester (UAS) Manajemen Proyek / Manajemen Proyek Perangkat Lunak Departemen Informatika Universitas Diponegoro (Koleksi Pengampu & Bank Soal HMIF 2022–2025).

---

## 🎯 BAGIAN 1: CONTOH SOAL UTS (FRAMEWORK MANAJEMEN PROYEK, CPM & PERT)

### Soal UTS 1: Analisis Kerangka Kerja & Faktor Keberhasilan Proyek (Soal Asli UTS Undip 2023)
**Deskripsi Soal:**
1. Jelaskan definisi formal dari **Manajemen Proyek (*Project Management*)** menurut standar PMBOK!
2. Paparkan komponen dalam **Project Management Framework**, mencakup: *Project Stakeholders*, *10 Project Management Knowledge Areas*, serta *Tools and Techniques*!
3. Jelaskan konsep segitiga batasan **Triple Constraint** dan sebutkan faktor-faktor penentu keberhasilan suatu proyek perangkat lunak (*Project Success Factors*)!

**Kunci Pembahasan & Solusi:**
1. **Definisi Manajemen Proyek (PMBOK Guide):**
   Manajemen Proyek adalah *"penerapan pengetahuan (*knowledge*), keterampilan (*skills*), alat bantu (*tools*), dan teknik (*techniques*) pada aktivitas-aktivitas proyek untuk memenuhi kebutuhan dan ekspektasi pemangku kepentingan proyek."* Manajemen proyek mengintegrasikan serangkaian proses terstruktur untuk memastikan sasaran proyek tercapai secara optimal.
2. **Komponen Project Management Framework:**
   * **Project Stakeholders:** Individu atau organisasi yang terlibat aktif dalam proyek atau yang kepentingannya terpengaruh secara positif maupun negatif oleh eksekusi proyek (e.g., Sponsor, Project Manager, Tim Proyek, Klien/Pengguna Akhir).
   * **10 Knowledge Areas:**
     1. *Project Integration Management* (Koordinasi menyeluruh)
     2. *Project Scope Management* (Manajemen ruang lingkup)
     3. *Project Schedule/Time Management* (Penjadwalan aktivitas)
     4. *Project Cost Management* (Anggaran dan biaya)
     5. *Project Quality Management* (Standar mutu)
     6. *Project Resource Management* (SDM dan peralatan)
     7. *Project Communications Management* (Arus informasi)
     8. *Project Risk Management* (Identifikasi dan mitigasi risiko)
     9. *Project Procurement Management* (Pengadaan kontrak vendor)
     10. *Project Stakeholder Management* (Keterlibatan pemangku kepentingan)
   * **Tools and Techniques:** Instrumen metodologis (e.g., Gantt Chart, Network Diagram WBS, CPM, Earned Value Management, Matriks RACI).
3. **Konsep Triple Constraint & Faktor Keberhasilan Proyek:**
   * Tiga batasan yang saling mengunci: **Scope** (apa yang harus dikerjakan), **Time** (jadwal batas waktu), dan **Cost** (anggaran biaya). Jika klien meminta penambahan ruang lingkup fitur di tengah jalan, maka waktu harus diperpanjang atau anggaran biaya harus ditambah, jika tidak kualitas (*Quality*) produk akhir akan rusak.
   * **Kriteria Keberhasilan Proyek:**
     1. Proyek selesai tepat waktu (*on-time*).
     2. Biaya tidak melampaui pagu anggaran yang disetujui (*on-budget*).
     3. Hasil deliverable memenuhi seluruh spesifikasi fungsional dan disetujui oleh sponsor (*met scope & satisfied client*).
     4. Menghasilkan *Return on Investment (ROI)* yang menguntungkan bagi organisasi.

---

### Soal UTS 2: Analisis Jalur Kritis (Critical Path Method - CPM)
**Deskripsi Soal:**
Diberikan daftar aktivitas proyek perangkat lunak dengan dependensi dan durasi hari kerja:

| Aktivitas | Deskripsi | Aktivitas Pendahulu (*Predecessor*) | Durasi (Hari) |
|:---:|:---|:---:|:---:|
| **A** | Elisitasi Kebutuhan | - | 4 |
| **B** | Desain Arsitektur & Database | A | 6 |
| **C** | Pembuatan Desain UI/UX | A | 3 |
| **D** | Pengembangan Modul Backend | B | 8 |
| **E** | Pengembangan Modul Frontend | C | 5 |
| **F** | Pengujian Terintegrasi & QA | D, E | 4 |
| **G** | Deployment & UAT | F | 2 |

**Tugas:**
1. Gambarkan diagram jaringan kerja proyek (*Activity-on-Node / AON*)!
2. Tentukan seluruh jalur (*paths*) yang mungkin dari awal hingga akhir beserta total durasinya!
3. Identifikasi **Jalur Kritis (*Critical Path*)** dan durasi minimum penyelesaian proyek!
4. Hitung nilai **Total Float (Slack)** untuk aktivitas **C** dan **E**!

**Kunci Pembahasan & Solusi:**
1. **Diagram Jaringan Kerja (AON):**
   * Jalur 1: $A \rightarrow B \rightarrow D \rightarrow F \rightarrow G$
   * Jalur 2: $A \rightarrow C \rightarrow E \rightarrow F \rightarrow G$

2. **Perhitungan Durasi Masing-Masing Jalur:**
   * **Durasi Jalur 1:**
     $$\text{Durasi}_1 = \text{Dur}(A) + \text{Dur}(B) + \text{Dur}(D) + \text{Dur}(F) + \text{Dur}(G) = 4 + 6 + 8 + 4 + 2 = \mathbf{24 \text{ hari}}$$
   * **Durasi Jalur 2:**
     $$\text{Durasi}_2 = \text{Dur}(A) + \text{Dur}(C) + \text{Dur}(E) + \text{Dur}(F) + \text{Dur}(G) = 4 + 3 + 5 + 4 + 2 = \mathbf{18 \text{ hari}}$$

3. **Jalur Kritis (*Critical Path*):**
   Jalur terpanjang adalah **Jalur 1: $A \rightarrow B \rightarrow D \rightarrow F \rightarrow G$** dengan durasi **$24$ hari**.
   Durasi minimum proyek selesai adalah **24 hari kerja**.

4. **Perhitungan Float/Slack pada Jalur Non-Kritis ($C$ dan $E$):**
   * Aktivitas $F$ baru bisa dimulai setelah KEDUA aktivitas $D$ dan $E$ selesai.
   * Aktivitas $D$ selesai pada hari ke: $4 + 6 + 8 = 18$.
   * Maka aktivitas $F$ paling cepat dimulai pada hari ke-18 ($ES(F) = 18$).
   * Aktivitas $E$ selesai pada hari ke: $4 + 3 + 5 = 12$ ($EF(E) = 12$).
   * Karena $F$ baru dimulai hari ke-18, maka $E$ paling lambat boleh selesai pada hari ke-18 ($LF(E) = 18$).
   * **Total Float Aktivitas E:**
     $$\text{Float}(E) = LF(E) - EF(E) = 18 - 12 = \mathbf{6 \text{ hari}}$$
   * **Total Float Aktivitas C:**
     $$\text{Float}(C) = \mathbf{6 \text{ hari}}$$
   * *Artinya:* Pengerjaan UI/UX (C) dan Frontend (E) dapat ditunda atau diperlambat hingga maksimal 6 hari tanpa menunda tanggal penyelesaian akhir proyek.

---

## 🎯 BAGIAN 2: CONTOH SOAL UAS (EARNED VALUE MANAGEMENT - EVM)

### Soal UAS 1: Pengendalian Biaya & Jadwal Menggunakan Earned Value Management (EVM)
**Deskripsi Soal:**
Sebuah proyek pengembangan sistem informasi terintegrasi rumah sakit memiliki total anggaran biaya (*Budget at Completion - BAC*) sebesar **Rp 200.000.000,-** dengan jadwal durasi pengerjaan direncanakan selesai dalam **10 bulan** (rata-rata linier Rp 20.000.000,- / bulan).
Pada akhir **Bulan ke-5**, manajer proyek melakukan audit evaluasi kinerja berkala:
* Berdasarkan jadwal, proyek seharusnya telah selesai $50\%$ pada bulan ke-5.
* Namun secara riil di lapangan, hasil pekerjaan yang telah tuntas diverifikasi baru mencapai **$40\%$**.
* Tim akuntansi melaporkan total pengeluaran uang kas riil yang telah dibayarkan (*Actual Cost*) adalah sebesar **Rp 95.000.000,-**.

**Tugas:**
1. Hitung nilai **Planned Value (PV)**, **Earned Value (EV)**, dan **Actual Cost (AC)** pada bulan ke-5!
2. Hitung **Cost Variance (CV)** dan **Schedule Variance (SV)**! Jelaskan status keuangan dan jadwal proyek!
3. Hitung **Cost Performance Index (CPI)** dan **Schedule Performance Index (SPI)**!
4. Hitung perkiraan total biaya akhir penyelesaian proyek (**Estimate at Completion - EAC**)!

**Kunci Pembahasan & Solusi:**
1. **Perhitungan Tiga Parameter Dasar EVM:**
   * $\text{PV} = 50\% \times \text{BAC} = 0.50 \times \text{Rp } 200.000.000 = \mathbf{\text{Rp } 100.000.000,-}$
   * $\text{EV} = 40\% \times \text{BAC} = 0.40 \times \text{Rp } 200.000.000 = \mathbf{\text{Rp } 80.000.000,-}$
   * $\text{AC} = \mathbf{\text{Rp } 95.000.000,-}$

2. **Analisis Varians Biaya & Jadwal:**
   * **Cost Variance (CV):**
     $$\text{CV} = \text{EV} - \text{AC} = \text{Rp } 80.000.000 - \text{Rp } 95.000.000 = \mathbf{-\text{Rp } 15.000.000,-}$$
     Karena nilai $\text{CV} < 0$, proyek berstatus **OVER BUDGET (Boros / Melebihi Anggaran)** sebesar Rp 15 juta.
   * **Schedule Variance (SV):**
     $$\text{SV} = \text{EV} - \text{PV} = \text{Rp } 80.000.000 - \text{Rp } 100.000.000 = \mathbf{-\text{Rp } 20.000.000,-}$$
     Karena nilai $\text{SV} < 0$, proyek berstatus **BEHIND SCHEDULE (Terlambat dari Jadwal)** senilai volume Rp 20 juta.

3. **Perhitungan Indeks Efisiensi Kinerja:**
   * **Cost Performance Index (CPI):**
     $$\text{CPI} = \frac{\text{EV}}{\text{AC}} = \frac{80.000.000}{95.000.000} \approx \mathbf{0.842}$$
     *(Artinya: Untuk setiap Rp 1.000,- uang kas yang dibelanjakan, proyek hanya menghasilkan pekerjaan senilai Rp 842,-).*
   * **Schedule Performance Index (SPI):**
     $$\text{SPI} = \frac{\text{EV}}{\text{PV}} = \frac{80.000.000}{100.000.000} = \mathbf{0.800}$$
     *(Artinya: Laju kemajuan proyek hanya berjalan pada kecepatan $80\%$ dari jadwal rencana).*

4. **Proyeksi Estimasi Biaya Akhir (Estimate at Completion - EAC):**
   Asumsi kinerja pengeluaran saat ini berlanjut hingga akhir proyek:
   $$\text{EAC} = \frac{\text{BAC}}{\text{CPI}} = \frac{\text{Rp } 200.000.000}{0.842} \approx \mathbf{\text{Rp } 237.529.691,-}$$
   *Kesimpulan:* Jika tidak dilakukan koreksi perbaikan manajerial, proyek diperkirakan akan mengalami defisit pembengkakan biaya (*cost overrun*) sebesar **Rp 37.529.691,-** di akhir masa pengerjaan.

---

## 🎯 BAGIAN 3: SIMULASI UJIAN LISAN KOMPREHENSIF (*ORAL DEFENSE*)

### Q1: "Jelaskan apa yang dimaksud dengan Scope Creep dalam manajemen proyek perangkat lunak, apa bahayanya, dan bagaimana mekanisme Change Control Board (CCB) mencegahnya?"
**Jawaban Komprehensif:**
* **Definisi Scope Creep:** Kecenderungan bertambahnya fitur, fungsi, atau ruang lingkup proyek secara liar, tidak terkendali, dan terus-menerus tanpa penyesuaian yang sepadan terhadap alokasi waktu jadwal, anggaran biaya, dan ketersediaan sumber daya manusia.
* **Bahaya Scope Creep:** Menyebabkan kelelahan tim pengembang (*burnout*), penundaan tanggal rilis produk berbulan-bulan, kerugian finansial developer, dan rusaknya hubungan kemitraan dengan klien.
* **Pencegahan via Change Control Board (CCB):**
  Setiap permintaan perubahan fitur baru tidak boleh langsung dieksekusi begitu saja oleh programmer atas permintaan lisan klien. Klien wajib mengisi formulir formal *Change Request Form*. Komite **Change Control Board (CCB)** yang beranggotakan perwakilan sponsor, manajer proyek, dan arsitek teknis akan menganalisis dampak perubahan terhadap *Triple Constraint*. Jika CCB menyetujui, maka anggaran biaya dan jadwal kontrak resmi diamandemen sebelum kode baru ditulis.

### Q2: "Kapan Manajer Proyek harus memilih strategi Fast Tracking dibandingkan Crashing ketika jadwal proyek mengalami keterlambatan kritis?"
**Jawaban Komprehensif:**
Dua teknik kompresi jadwal (*Schedule Compression Techniques*):
1. **Crashing:** Mempercepat durasi aktivitas pada jalur kritis dengan cara **menambahkan sumber daya tambahan** (misal: merekrut programmer senior baru atau memberlakukan lembur berbayar).
   * *Kelemahan:* Menaikkan biaya pengeluaran proyek (*increases cost*).
   * *Kapan Dipilih:* Jika anggaran dana tambahan tersedia melimpah dan risiko keterlambatan membawa denda wanprestasi yang jauh lebih mahal daripada biaya lembur.
2. **Fast Tracking:** Menjalankan aktivitas-aktivitas yang semula direncanakan berurutan secara paralel/simultan (misal: memulai penulisan kode modul backend sebelum desain detail arsitektur 100% selesai ditandatangani).
   * *Kelemahan:* Meningkatkan risiko terjadinya pekerjaan ulang (*rework*) dan bug kritis (*increases risk*).
   * *Kapan Dipilih:* Jika anggaran biaya proyek sudah terkunci mati (*fixed budget* / tidak ada dana tambahan), namun tim bersedia mengelola risiko koordinasi paralel yang tinggi demi mengejar tenggat waktu.
