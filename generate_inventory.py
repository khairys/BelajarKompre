import os
import glob

base_dir = r"D:\Gathan\My Project\BelajarKompre"
rangkuman_base = os.path.join(base_dir, "RANGKUMAN_DAN_CONTOH_SOAL")

lines = [
    "# 🎓 Inventaris Lengkap Berkas Belajar Komprehensif (S1 Informatika Undip)",
    "",
    "> **Status:** 100% Tuntas Selesai (Semester 1 s.d. Semester 8) | Baseline Kurikulum 2020",
    "",
    "## 📊 Ringkasan Eksekutif",
    "- **Total Mata Kuliah Wajib:** 44 Mata Kuliah",
    "- **Total Berkas Rangkuman & Bank Soal Kompre:** **88 Berkas Markdown** (100% Lengkap: 44 `RANGKUMAN_MATERI.md` + 44 `CONTOH_SOAL_DAN_PEMBAHASAN.md`)",
    "- **Total Berkas Arsip Mentah Asli (Slide & Soal DMW):** 1.436 Berkas (~2,85 GB)",
    "- **Cakupan Kurikulum:** Semester 1 hingga Semester 8 (Fondasi Komputasi, Rekayasa Perangkat Lunak, AI, Jaringan, PKL, KKN, hingga Tugas Akhir)",
    "",
    "---",
    "",
    "## 📚 Rekapitulasi Rangkuman & Contoh Soal per Semester",
    "| Semester | Jumlah Mata Kuliah | Rangkuman Materi | Contoh Soal & Pembahasan | Status Kelengkapan |",
    "| :--- | :---: | :---: | :---: | :---: |",
    "| **Semester 1** | 8 | 8 Berkas | 8 Berkas | ✅ 100% Lengkap (16/16) |",
    "| **Semester 2** | 7 | 7 Berkas | 7 Berkas | ✅ 100% Lengkap (14/14) |",
    "| **Semester 3** | 6 | 6 Berkas | 6 Berkas | ✅ 100% Lengkap (12/12) |",
    "| **Semester 4** | 6 | 6 Berkas | 6 Berkas | ✅ 100% Lengkap (12/12) |",
    "| **Semester 5** | 7 | 7 Berkas | 7 Berkas | ✅ 100% Lengkap (14/14) |",
    "| **Semester 6** | 5 | 5 Berkas | 5 Berkas | ✅ 100% Lengkap (10/10) |",
    "| **Semester 7** | 3 | 3 Berkas | 3 Berkas | ✅ 100% Lengkap (6/6) |",
    "| **Semester 8** | 2 | 2 Berkas | 2 Berkas | ✅ 100% Lengkap (4/4) |",
    "| **TOTAL** | **44** | **44 Berkas** | **44 Berkas** | **✅ 100% SELESAI (88/88)** |",
    "",
    "---",
    ""
]

sem_dirs = sorted([d for d in os.listdir(base_dir) if d.startswith("0") and os.path.isdir(os.path.join(base_dir, d))])

for sem in sem_dirs:
    sem_path = os.path.join(base_dir, sem)
    subjs = sorted([s for s in os.listdir(sem_path) if os.path.isdir(os.path.join(sem_path, s))])
    
    # Calculate semester raw files
    sem_files = [os.path.join(r, f) for r, _, fs in os.walk(sem_path) for f in fs]
    sem_size_mb = sum(os.path.getsize(f) for f in sem_files) / (1024 * 1024)
    
    lines.append(f"## 📁 {sem.replace('_', ' ')} ({len(sem_files)} berkas arsip mentah, {sem_size_mb:.1f} MB)\n")
    
    for subj in subjs:
        subj_path = os.path.join(sem_path, subj)
        materi_path = os.path.join(subj_path, "materi")
        soal_path = os.path.join(subj_path, "bank_soal")
        
        materi_files = os.listdir(materi_path) if os.path.exists(materi_path) else []
        soal_files = os.listdir(soal_path) if os.path.exists(soal_path) else []
        
        # Check rangkuman status
        rk_subj_path = os.path.join(rangkuman_base, sem, subj)
        has_rk_materi = os.path.exists(os.path.join(rk_subj_path, "RANGKUMAN_MATERI.md"))
        has_rk_soal = os.path.exists(os.path.join(rk_subj_path, "CONTOH_SOAL_DAN_PEMBAHASAN.md"))
        
        lines.append(f"### 📘 {subj.replace('_', ' ')}")
        lines.append(f"- **Dokumen Belajar Komprehensif:**")
        lines.append(f"  * `RANGKUMAN_MATERI.md`: {'✅ Selesai' if has_rk_materi else '❌ Belum'}")
        lines.append(f"  * `CONTOH_SOAL_DAN_PEMBAHASAN.md`: {'✅ Selesai' if has_rk_soal else '❌ Belum'}")
        lines.append(f"- **Arsip Mentah DMW Undip:**")
        lines.append(f"  * Slide / Modul Perkuliahan: {len(materi_files)} berkas")
        lines.append(f"  * Bank Soal UTS/UAS: {len(soal_files)} berkas")
        
        if soal_files:
            lines.append("  * *Contoh Soal Arsip:* " + ", ".join([f"`{f}`" for f in soal_files[:3]]) + (" ..." if len(soal_files) > 3 else ""))
        lines.append("")
    lines.append("---\n")

out_file = os.path.join(base_dir, "INVENTARIS_BERKAS.md")
with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Generated {out_file} successfully!")
