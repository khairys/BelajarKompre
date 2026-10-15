import os

base_dir = r"D:\Gathan\My Project\BelajarKompre"
target_root = os.path.join(base_dir, "RANGKUMAN_DAN_CONTOH_SOAL")

semesters_structure = {
    "01_Semester_1": [
        "Dasar_Sistem",
        "Dasar_Pemrograman",
        "Bahasa_Inggris",
        "Struktur_Diskrit",
        "Matematika_I",
        "Logika_Informatika",
        "Pancasila_dan_Kewarganegaraan",
        "Olah_Raga"
    ],
    "02_Semester_2": [
        "Organisasi_dan_Arsitektur_Komputer",
        "Algoritma_dan_Pemrograman",
        "Bahasa_Indonesia",
        "Internet_of_Things",
        "Matematika_II",
        "Aljabar_Linier",
        "Pendidikan_Agama"
    ],
    "03_Semester_3": [
        "Sistem_Operasi",
        "Struktur_Data",
        "Interaksi_Manusia_Komputer",
        "Basis_Data",
        "Metode_Numerik",
        "Statistika"
    ],
    "04_Semester_4": [
        "Jaringan_Komputer",
        "Pemrograman_Berorientasi_Objek",
        "Rekayasa_Perangkat_Lunak",
        "Manajemen_Basis_Data",
        "Grafika_dan_Komputasi_Visual",
        "Sistem_Cerdas"
    ],
    "05_Semester_5": [
        "Komputasi_Tersebar_dan_Paralel",
        "Pengembangan_Berbasis_Platform",
        "Proyek_Perangkat_Lunak",
        "Sistem_Informasi",
        "Keamanan_dan_Jaminan_Informasi",
        "Pembelajaran_Mesin",
        "Kewirausahaan"
    ],
    "06_Semester_6": [
        "Praktik_Kerja_Lapangan",
        "Analisis_dan_Strategi_Algoritma",
        "Uji_Perangkat_Lunak",
        "Manajemen_Proyek",
        "Masyarakat_dan_Etika_Profesi"
    ],
    "07_Semester_7": [
        "Metodologi_dan_Penulisan_Ilmiah",
        "Teori_Bahasa_dan_Otomata",
        "Penambangan_Data"
    ],
    "08_Semester_8": [
        "Tugas_Akhir",
        "Kuliah_Kerja_Nyata"
    ]
}

os.makedirs(target_root, exist_ok=True)
count = 0
for sem, subjs in semesters_structure.items():
    sem_path = os.path.join(target_root, sem)
    os.makedirs(sem_path, exist_ok=True)
    for subj in subjs:
        subj_path = os.path.join(sem_path, subj)
        os.makedirs(subj_path, exist_ok=True)
        count += 1

print(f"Berhasil membuat struktur folder RANGKUMAN_DAN_CONTOH_SOAL dengan {count} folder mata kuliah.")
