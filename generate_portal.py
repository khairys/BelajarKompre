import os
import json

base_dir = r"D:\Gathan\My Project\BelajarKompre"
rangkuman_base = os.path.join(base_dir, "RANGKUMAN_DAN_CONTOH_SOAL")

sem_dirs = sorted([d for d in os.listdir(base_dir) if d.startswith("0") and os.path.isdir(os.path.join(base_dir, d))])

TOPIC_MAPPING = {
    # Fondasi & Matematika
    "Dasar_Sistem": "Fondasi & Sistem",
    "Struktur_Diskrit": "Matematika & Logika",
    "Matematika_I": "Matematika & Logika",
    "Logika_Informatika": "Matematika & Logika",
    "Aljabar_Linier": "Matematika & Logika",
    "Matematika_II": "Matematika & Logika",
    "Metode_Numerik": "Matematika & Logika",
    "Statistika": "Matematika & Logika",
    "Teori_Bahasa_dan_Otomata": "Teori Komputasi",
    
    # Pemrograman & Algoritma
    "Dasar_Pemrograman": "Pemrograman & Algoritma",
    "Algoritma_dan_Pemrograman": "Pemrograman & Algoritma",
    "Struktur_Data": "Pemrograman & Algoritma",
    "Pemrograman_Berorientasi_Objek": "Pemrograman & Algoritma",
    "Analisis_dan_Strategi_Algoritma": "Pemrograman & Algoritma",
    
    # Perangkat Keras & Arsitektur
    "Organisasi_dan_Arsitektur_Komputer": "Sistem & Hardware",
    "Sistem_Operasi": "Sistem & Hardware",
    "Komputasi_Tersebar_dan_Paralel": "Sistem & Hardware",
    "Internet_of_Things": "Sistem & Hardware",
    
    # Basis Data & Rekayasa Perangkat Lunak
    "Basis_Data": "Basis Data & RPL",
    "Manajemen_Basis_Data": "Basis Data & RPL",
    "Rekayasa_Perangkat_Lunak": "Basis Data & RPL",
    "Pengembangan_Berbasis_Platform": "Basis Data & RPL",
    "Proyek_Perangkat_Lunak": "Basis Data & RPL",
    "Manajemen_Proyek": "Basis Data & RPL",
    "Uji_Perangkat_Lunak": "Basis Data & RPL",
    "Sistem_Informasi": "Basis Data & RPL",
    "Interaksi_Manusia_Komputer": "Basis Data & RPL",
    
    # Kecerdasan Buatan & Data
    "Sistem_Cerdas": "Kecerdasan Buatan",
    "Pembelajaran_Mesin": "Kecerdasan Buatan",
    "Penambangan_Data": "Kecerdasan Buatan",
    
    # Jaringan & Keamanan
    "Jaringan_Komputer": "Jaringan & Keamanan",
    "Keamanan_dan_Jaminan_Informasi": "Jaringan & Keamanan",
    
    # Humaniora, Kulminasi & Etika
    "Pancasila_dan_Kewarganegaraan": "Etika & Karakter",
    "Bahasa_Inggris": "Komunikasi & Bahasa",
    "Olah_Raga": "Kesehatan & Kebugaran",
    "Bahasa_Indonesia": "Komunikasi & Bahasa",
    "Pendidikan_Agama": "Etika & Karakter",
    "Kewirausahaan": "Bisnis & Inovasi",
    "Masyarakat_dan_Etika_Profesi": "Etika & Karakter",
    "Metodologi_dan_Penulisan_Ilmiah": "Riset & Penulisan",
    "Praktik_Kerja_Lapangan": "Kulminasi & Industri",
    "Kuliah_Kerja_Nyata": "Kulminasi & Pengabdian",
    "Tugas_Akhir": "Kulminasi & Skripsi"
}

SEMESTER_METADATA = {
    1: {
        "title": "Fondasi Komputasi & Pemrograman Fungsional",
        "badge": "8 Mata Kuliah Wajib",
        "sub": "Dasar Pemrograman, Dasar Sistem, Logika Informatika, Struktur Diskrit, Matematika I, Bahasa Inggris, Pancasila & Kewarganegaraan, Olah Raga",
        "url": "semester1.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/RANGKUMAN_SEMESTER_1.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester1.md",
        "desc": "Sintesis komprehensif semester pertama: paradigma fungsional & rekursi, gerbang logika digital, logika formal (proposisi & predikat), induksi matematika & relasi graf, kalkulus dasar diferensial-integral, serta tata bahasa teknis informatika."
    },
    2: {
        "title": "Algoritma Prosedural, Arsitektur Sistem & Aljabar",
        "badge": "7 Mata Kuliah Wajib",
        "sub": "Algoritma & Pemrograman, Aljabar Linier, Bahasa Indonesia, Internet of Things, Matematika II, Organisasi & Arsitektur Komputer, Pendidikan Agama",
        "url": "semester2.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/RANGKUMAN_SEMESTER_2.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester2.md",
        "desc": "Sintesis komprehensif semester kedua: pointer & manajemen memori bahasa C, ruang vektor & dekomposisi matriks, sensor & aktuator IoT, siklus instruksi CPU & pipelining, serta kalkulus multivariabel (turunan parsial & integral lipat)."
    },
    3: {
        "title": "Rekayasa Data, Sistem Inti & Analisis Numerik",
        "badge": "6 Mata Kuliah Wajib",
        "sub": "Basis Data, Interaksi Manusia & Komputer, Metode Numerik, Sistem Operasi, Statistika, Struktur Data",
        "url": "semester3.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/RANGKUMAN_SEMESTER_3.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester3.md",
        "desc": "Sintesis komprehensif semester ketiga: normalisasi data (1NF–BCNF) & relasional aljabar, proses OS & deadlock prevention, pohon seimbang AVL & heap, prinsip UI/UX usability, regresi/ANOVA, serta aproksimasi akar numerik."
    },
    4: {
        "title": "Rekayasa Perangkat Lunak, Jaringan & AI Dasar",
        "badge": "6 Mata Kuliah Wajib",
        "sub": "Grafika & Komputasi Visual, Jaringan Komputer, Manajemen Basis Data, Pemrograman Berorientasi Objek, Rekayasa Perangkat Lunak, Sistem Cerdas",
        "url": "semester4.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/RANGKUMAN_SEMESTER_4.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester4.md",
        "desc": "Sintesis komprehensif semester keempat: rendering rasterisasi & transformasi grafika, model OSI & subnetting IPv4/VLSM, konkurensi ACID transaksi DB, paradigma OOP SOLID, siklus Agile/Scrum & pemodelan UML, serta algoritma pencarian A* & rule-based AI."
    },
    5: {
        "title": "Keamanan Siber, Komputasi Skala Besar & Machine Learning",
        "badge": "7 Mata Kuliah Wajib",
        "sub": "Keamanan & Jaminan Informasi, Kewirausahaan, Komputasi Tersebar & Paralel, Pembelajaran Mesin, Pengembangan Berbasis Platform, Proyek Perangkat Lunak, Sistem Informasi",
        "url": "semester5.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/RANGKUMAN_SEMESTER_5.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester5.md",
        "desc": "Sintesis komprehensif semester kelima: kriptografi simetris/asimetris (AES, RSA, hashing), komputasi paralel MPI/OpenMP & Hukum Amdahl, algoritma supervised/unsupervised machine learning, arsitektur RESTful web, dan tata kelola sistem informasi."
    },
    6: {
        "title": "Analisis Algoritma Kompleks, Manajemen Proyek & Pengujian",
        "badge": "5 Mata Kuliah Wajib",
        "sub": "Analisis & Strategi Algoritma, Manajemen Proyek, Masyarakat & Etika Profesi, Praktik Kerja Lapangan, Uji Perangkat Lunak",
        "url": "semester6.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/06_Semester_6/RANGKUMAN_SEMESTER_6.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester6.md",
        "desc": "Sintesis komprehensif semester keenam: Teorema Master & Dynamic Programming, Earned Value Management (EVM / CPI / SPI), etika profesi komputasi ACM/IEEE, laporan PKL industri, serta pengujian perangkat lunak Black Box & White Box (Cyclomatic Complexity)."
    },
    7: {
        "title": "Teori Komputasi Lanjut, Data Mining & Metodologi Riset",
        "badge": "3 Mata Kuliah Wajib",
        "sub": "Metodologi & Penulisan Ilmiah, Penambangan Data, Teori Bahasa & Otomata",
        "url": "semester7.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/07_Semester_7/RANGKUMAN_SEMESTER_7.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester7.md",
        "desc": "Sintesis komprehensif semester ketujuh: hierarki tata bahasa Chomsky, ekivalensi DFA/NFA & Turing Machine, aturan asosiasi Apriori & klasterisasi data mining, serta perumusan problem statement dan struktur penulisan proposal skripsi."
    },
    8: {
        "title": "Kulminasi Akademik, Pengabdian Masyarakat & Tugas Akhir",
        "badge": "2 Mata Kuliah Wajib",
        "sub": "Kuliah Kerja Nyata (KKN), Tugas Akhir / Skripsi Komprehensif",
        "url": "semester8.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/08_Semester_8/RANGKUMAN_SEMESTER_8.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester8.md",
        "desc": "Sintesis komprehensif semester puncak: integrasi pengabdian masyarakat partisipatif (PRA), struktur manuskrip skripsi standar IMRaD, serta persiapan mental dan materi menghadapi sidang ujian sarjana komprehensif."
    }
}

# Build Embedded Markdown Content Registry
content_registry = {}

for i in range(1, 9):
    fn = os.path.join(base_dir, f"semester{i}.md")
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f:
            text = f.read()
            content_registry[f"semester{i}.md"] = text
            content_registry[f"RANGKUMAN_DAN_CONTOH_SOAL/{i:02d}_Semester_{i}/RANGKUMAN_SEMESTER_{i}.md"] = text

for root, dirs, files in os.walk(rangkuman_base):
    for f in files:
        if f.endswith(".md"):
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, base_dir).replace("\\", "/")
            with open(fp, "r", encoding="utf-8") as mf:
                content_registry[rel] = mf.read()

registry_json = json.dumps(content_registry, ensure_ascii=False)
registry_json = registry_json.replace("</script", "<\\/script").replace("</Script", "<\\/Script>")

data_tree = []
total_raw_materi = 0
total_raw_soal = 0
total_rk_materi = 0
total_rk_soal = 0
total_subjects = 0
all_topics = set()

for sem in sem_dirs:
    sem_path = os.path.join(base_dir, sem)
    subjs = sorted([s for s in os.listdir(sem_path) if os.path.isdir(os.path.join(sem_path, s))])
    sem_num = int(sem.split("_")[0])
    
    sem_obj = {
        "semester_id": sem,
        "semester_num": sem_num,
        "name": f"Semester {sem_num}",
        "subjects": []
    }
    
    for subj in subjs:
        total_subjects += 1
        subj_path = os.path.join(sem_path, subj)
        materi_path = os.path.join(subj_path, "materi")
        soal_path = os.path.join(subj_path, "bank_soal")
        
        materi_files = sorted(os.listdir(materi_path)) if os.path.exists(materi_path) else []
        soal_files = sorted(os.listdir(soal_path)) if os.path.exists(soal_path) else []
        
        total_raw_materi += len(materi_files)
        total_raw_soal += len(soal_files)
        
        rk_subj_path = os.path.join(rangkuman_base, sem, subj)
        rel_rk_materi = f"RANGKUMAN_DAN_CONTOH_SOAL/{sem}/{subj}/RANGKUMAN_MATERI.md"
        rel_rk_soal = f"RANGKUMAN_DAN_CONTOH_SOAL/{sem}/{subj}/CONTOH_SOAL_DAN_PEMBAHASAN.md"
        
        has_rk_m = os.path.exists(os.path.join(rk_subj_path, "RANGKUMAN_MATERI.md"))
        has_rk_s = os.path.exists(os.path.join(rk_subj_path, "CONTOH_SOAL_DAN_PEMBAHASAN.md"))
        
        if has_rk_m: total_rk_materi += 1
        if has_rk_s: total_rk_soal += 1
        
        topic = TOPIC_MAPPING.get(subj, "Umum")
        all_topics.add(topic)
        
        sem_obj["subjects"].append({
            "name": subj.replace("_", " "),
            "folder": subj,
            "semester_num": sem_num,
            "topic": topic,
            "materi_count": len(materi_files),
            "soal_count": len(soal_files),
            "materi_files": materi_files,
            "soal_files": soal_files,
            "has_rk_materi": has_rk_m,
            "has_rk_soal": has_rk_s,
            "url_rk_materi": rel_rk_materi,
            "url_rk_soal": rel_rk_soal,
            "gh_rk_materi": f"https://github.com/khairys/BelajarKompre/blob/main/{rel_rk_materi}",
            "gh_rk_soal": f"https://github.com/khairys/BelajarKompre/blob/main/{rel_rk_soal}"
        })
    data_tree.append(sem_obj)

total_raw_files = total_raw_materi + total_raw_soal
total_rk_files = total_rk_materi + total_rk_soal
sorted_topics = sorted(list(all_topics))

topic_pills_html = ' '.join([
    f'<button data-topic="{t}" class="topic-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-800 transition text-xs font-medium whitespace-nowrap cursor-pointer">{t}</button>'
    for t in sorted_topics
])

semester_meta_json = json.dumps(SEMESTER_METADATA, ensure_ascii=False)
data_tree_json = json.dumps(data_tree, ensure_ascii=False)

html_template = r"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BelajarKompre • Portal Kajian Komprehensif Informatika Undip</title>
  <meta name="description" content="Portal kajian kurikulum, 44 mata kuliah wajib, 8 sintesis semester, dan bank soal komprehensif S1 Informatika Universitas Diponegoro.">
  
  <!-- Favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%236366f1%22 stroke-width=%222%22><path d=%22M22 10v6M2 10l10-5 10 5-10 5z%22/><path d=%22M6 12v5c3 3 9 3 12 0v-5%22/></svg>">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Marked.js for Markdown -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
  <!-- KaTeX for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  
  <!-- Mermaid.js for Diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  
  <!-- Highlight.js for Code Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark-dimmed.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            brand: {
              50: '#eef2ff',
              100: '#e0e7ff',
              400: '#818cf8',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
              900: '#312e81',
            }
          }
        }
      }
    }
  </script>
  
  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #080c14; }
    ::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 9999px; }
    ::-webkit-scrollbar-thumb:hover { background: #334155; }
    
    /* KaTeX Math Styling */
    .katex { font-size: 1.05em; text-rendering: auto; }
    .katex-display {
      margin: 1.25rem 0 !important;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 0.85rem 1.25rem;
      background: #0d121f;
      border-radius: 0.75rem;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    /* Markdown Modal Typography */
    .markdown-body { line-height: 1.8; font-size: 0.95rem; color: #cbd5e1; }
    .markdown-body h1 { font-size: 1.75rem; font-weight: 800; color: #ffffff; margin-top: 2rem; margin-bottom: 0.75rem; border-bottom: 1px solid #1e293b; padding-bottom: 0.5rem; letter-spacing: -0.02em; }
    .markdown-body h2 { font-size: 1.35rem; font-weight: 700; color: #e2e8f0; margin-top: 2rem; margin-bottom: 0.75rem; border-bottom: 1px solid rgba(255, 255, 255, 0.06); padding-bottom: 0.4rem; scroll-margin-top: 5rem; }
    .markdown-body h3 { font-size: 1.15rem; font-weight: 600; color: #cbd5e1; margin-top: 1.5rem; margin-bottom: 0.5rem; scroll-margin-top: 5rem; }
    .markdown-body h4 { font-size: 1.02rem; font-weight: 600; color: #e2e8f0; margin-top: 1.25rem; margin-bottom: 0.4rem; }
    .markdown-body p { margin-bottom: 1rem; }
    .markdown-body ul, .markdown-body ol { padding-left: 1.5rem; margin-bottom: 1.25rem; }
    .markdown-body ul { list-style-type: disc; }
    .markdown-body ol { list-style-type: decimal; }
    .markdown-body li { margin-bottom: 0.35rem; }
    .markdown-body strong { color: #ffffff; font-weight: 600; }
    .markdown-body em { color: #94a3b8; }
    .markdown-body code { font-family: 'JetBrains Mono', monospace; background: #131b2e; color: #f43f5e; padding: 0.15rem 0.4rem; border-radius: 0.3rem; font-size: 0.88em; border: 1px solid rgba(255,255,255,0.06); }
    .markdown-body pre { background: #090d16; border: 1px solid #1e293b; padding: 1rem; border-radius: 0.75rem; overflow-x: auto; margin: 1.25rem 0; }
    .markdown-body pre code { background: transparent; color: #e2e8f0; padding: 0; font-size: 0.88em; border: none; }
    .markdown-body table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.88rem; overflow-x: auto; display: block; }
    .markdown-body th, .markdown-body td { border: 1px solid #1e293b; padding: 0.65rem 0.9rem; text-align: left; }
    .markdown-body th { background: #0f172a; color: #f8fafc; font-weight: 600; }
    .markdown-body tr:nth-child(even) { background: rgba(15, 23, 42, 0.5); }
    .markdown-body hr { border: 0; border-top: 1px solid #1e293b; margin: 2rem 0; }
    .markdown-body blockquote { border-left: 3px solid #6366f1; padding-left: 1rem; color: #94a3b8; margin: 1rem 0; font-style: normal; }
  </style>
</head>
<body class="bg-[#080c14] text-slate-100 min-h-screen selection:bg-indigo-500/25 selection:text-indigo-200 antialiased font-sans flex flex-col justify-between">

  <!-- Main Container -->
  <div>
    <!-- Top Announcement Bar -->
    <div class="border-b border-slate-800/80 bg-[#0b101c] py-2 px-4 text-xs text-slate-400">
      <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
        <div class="flex items-center gap-2">
          <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          <span class="font-medium text-slate-300">Kurikulum 2020 S1 Informatika Undip</span>
          <span class="text-slate-600">•</span>
          <span>44 Mata Kuliah Wajib • 8 Sintesis Komprehensif • 88 Kajian & Soal</span>
        </div>
        <div class="flex items-center gap-3">
          <a href="https://github.com/khairys/BelajarKompre" target="_blank" class="hover:text-slate-200 transition text-[11px] flex items-center gap-1 text-slate-400">
            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            <span>Repositori GitHub</span>
          </a>
        </div>
      </div>
    </div>

    <!-- Navigation Header -->
    <header class="sticky top-0 z-40 backdrop-blur-md bg-[#080c14]/90 border-b border-slate-800/80">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        <!-- Brand -->
        <div class="flex items-center gap-3 shrink-0">
          <div class="w-9 h-9 rounded-xl bg-indigo-600/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
              <path d="M6 12v5c3 3 9 3 12 0v-5"/>
            </svg>
          </div>
          <div>
            <a href="#" class="font-bold text-base tracking-tight text-white hover:text-indigo-400 transition flex items-center gap-2">
              BelajarKompre
              <span class="text-[10px] font-semibold tracking-wider uppercase px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700">Informatika</span>
            </a>
          </div>
        </div>

        <!-- Center Search Input in Nav on Desktop -->
        <div class="flex-1 max-w-lg hidden md:block">
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </div>
            <input id="navSearchInput" type="text"
                   placeholder="Cari mata kuliah, topik, materi (tekan / untuk fokus)..."
                   class="w-full bg-slate-900/80 border border-slate-800 rounded-xl pl-9 pr-9 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500/60 focus:ring-1 focus:ring-indigo-500/20 transition">
            <div id="navClearSearchBtn" class="absolute inset-y-0 right-0 pr-3 items-center cursor-pointer text-slate-500 hover:text-slate-300 hidden">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </div>
          </div>
        </div>

        <!-- Action Links -->
        <div class="flex items-center gap-2">
          <!-- llms.txt Link -->
          <a href="https://github.com/khairys/BelajarKompre/blob/main/llms.txt" target="_blank"
             class="hidden sm:inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-400 hover:text-slate-200 text-xs font-medium transition">
            <span>llms.txt</span>
          </a>

          <!-- GitHub Repo Link -->
          <a href="https://github.com/khairys/BelajarKompre" target="_blank"
             class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-sm transition">
            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            <span>GitHub</span>
          </a>
        </div>
      </div>
    </header>

    <!-- Mobile Search Bar -->
    <div class="p-4 md:hidden border-b border-slate-800/80 bg-[#080c14]">
      <div class="relative">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>
        <input id="mobileSearchInput" type="text"
               placeholder="Cari mata kuliah atau topik..."
               class="w-full bg-slate-900 border border-slate-800 rounded-xl pl-9 pr-9 py-2.5 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition">
        <div id="mobileClearSearchBtn" class="absolute inset-y-0 right-0 pr-3 items-center cursor-pointer text-slate-500 hover:text-slate-300 hidden">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </div>
      </div>
    </div>

    <!-- Hero / Headline Area -->
    <section class="border-b border-slate-800/60 bg-[#090e18] py-8 sm:py-10 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto flex flex-col md:flex-row md:items-end justify-between gap-6">
        <div class="max-w-3xl">
          <div class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-medium mb-3">
            <span>Repositori Terpadu Ujian Sarjana & Komprehensif</span>
          </div>
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white tracking-tight leading-tight">
            Portal Kajian Komprehensif Informatika
          </h1>
          <p class="mt-2.5 text-slate-400 text-xs sm:text-sm leading-relaxed max-w-2xl">
            Struktur kurikulum 44 mata kuliah wajib, 8 sintesis komprehensif semester, ratusan contoh soal asli beserta pembahasan, dan formula matematika KaTeX.
          </p>
        </div>

        <!-- Metrics Strip (Clean & Uncluttered) -->
        <div class="flex items-center gap-4 sm:gap-6 border-t md:border-t-0 md:border-l border-slate-800/80 pt-4 md:pt-0 md:pl-6 text-xs shrink-0">
          <div>
            <div class="text-xl font-bold text-white tracking-tight">__TOTAL_SUBJECTS__</div>
            <div class="text-slate-500 text-[11px] font-medium">Mata Kuliah Wajib</div>
          </div>
          <div class="w-px h-8 bg-slate-800"></div>
          <div>
            <div class="text-xl font-bold text-indigo-400 tracking-tight">8</div>
            <div class="text-slate-500 text-[11px] font-medium">Sintesis Semester</div>
          </div>
          <div class="w-px h-8 bg-slate-800"></div>
          <div>
            <div class="text-xl font-bold text-emerald-400 tracking-tight">__TOTAL_RK_FILES__</div>
            <div class="text-slate-500 text-[11px] font-medium">Kajian & Soal</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Main Navigation & Filters Container -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6">
      
      <!-- Primary Semester Segmented Controller -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-3 scrollbar-none border-b border-slate-800/70 text-xs font-medium">
        <button data-sem="all" class="sem-btn active px-3.5 py-1.5 rounded-lg bg-indigo-600 text-white whitespace-nowrap transition shadow-sm font-semibold cursor-pointer">
          Semua Semester (__TOTAL_SUBJECTS__)
        </button>
        <button data-sem="1" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 1
        </button>
        <button data-sem="2" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 2
        </button>
        <button data-sem="3" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 3
        </button>
        <button data-sem="4" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 4
        </button>
        <button data-sem="5" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 5
        </button>
        <button data-sem="6" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 6
        </button>
        <button data-sem="7" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 7
        </button>
        <button data-sem="8" class="sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer">
          Semester 8
        </button>
      </div>

      <!-- Secondary Filters: Topic Pills -->
      <div class="flex items-center gap-1.5 overflow-x-auto py-3 scrollbar-none text-xs">
        <span class="text-slate-500 font-medium shrink-0 mr-1 text-[11px]">Kategori:</span>
        <button data-topic="all" class="topic-btn active px-2.5 py-1 rounded-md bg-slate-800 text-slate-100 whitespace-nowrap border border-slate-700 font-medium transition text-xs cursor-pointer">
          Semua Bidang
        </button>
        __TOPICS_BUTTONS__
      </div>

      <!-- Dedicated Semester Context Header (Clean, only shows when a specific semester is active) -->
      <div id="semesterContextCard" style="display: none;" class="mt-2 p-5 rounded-xl bg-slate-900/60 border border-slate-800 transition-all">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="max-w-3xl">
            <div class="flex items-center gap-2 mb-1.5">
              <span id="semContextBadge" class="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-indigo-500/10 border border-indigo-500/30 text-indigo-400">
                8 Mata Kuliah
              </span>
              <h2 id="semContextTitle" class="text-base sm:text-lg font-bold text-white tracking-tight">
                Semester 1: Fondasi Komputasi & Pemrograman Fungsional
              </h2>
            </div>
            <p id="semContextDesc" class="text-xs text-slate-400 leading-relaxed">
              Sintesis komprehensif semester pertama...
            </p>
            <div id="semContextSub" class="text-[11px] text-slate-500 mt-2 font-mono">
              Dasar Pemrograman, Dasar Sistem...
            </div>
          </div>

          <!-- Action Buttons for the active semester -->
          <div class="flex items-center gap-2 shrink-0 self-start md:self-center">
            <a id="semContextGhLink" href="#" target="_blank"
               class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium border border-slate-700 transition flex items-center gap-1.5 cursor-pointer">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
              <span>GitHub</span>
            </a>
            <button id="semContextReadBtn" onclick=""
                    class="px-3.5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition shadow-sm flex items-center gap-1.5 active:scale-95 cursor-pointer">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
              <span id="semContextBtnLabel">Baca Sintesis Semester 1</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Main Course Grid Area -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      
      <!-- Result Bar -->
      <div class="flex items-center justify-between mb-5 pb-2 border-b border-slate-800/40">
        <div id="resultCount" class="text-xs font-medium text-slate-400">
          Menampilkan 44 mata kuliah
        </div>
        <div class="flex items-center gap-3 text-[11px] text-slate-500">
          <span class="flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-indigo-400"></span> Rangkuman Materi
          </span>
          <span class="flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span> Bank Soal
          </span>
        </div>
      </div>

      <!-- Course Cards Grid -->
      <div id="coursesGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Empty State -->
      <div id="emptyState" style="display: none;" class="text-center py-16 bg-slate-900/40 border border-slate-800 rounded-2xl p-6">
        <div class="w-12 h-12 rounded-full bg-slate-800/80 border border-slate-700 flex items-center justify-center mx-auto mb-3 text-slate-400">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>
        <h3 class="text-base font-semibold text-slate-200">Mata kuliah tidak ditemukan</h3>
        <p class="text-xs text-slate-500 max-w-sm mx-auto mt-1">Coba gunakan kata kunci pencarian lain atau pilih filter "Semua Semester".</p>
        <button onclick="resetFilters()" class="mt-4 px-3.5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-xs font-medium text-white transition cursor-pointer">
          Reset Filter & Pencarian
        </button>
      </div>
    </main>
  </div>

  <!-- Minimalist Modal Reader (Pristine, Zero Emojis, No Bottom Bar, Guaranteed Hidden Initially) -->
  <div id="markdownModal" style="display: none;" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm items-center justify-center p-2 sm:p-4">
    <div id="modalDialog" class="bg-[#0b101b] border border-slate-800 rounded-2xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-2xl overflow-hidden transition-all duration-150">
      
      <!-- Modal Header -->
      <div class="px-5 py-3.5 border-b border-slate-800 bg-[#0d1322] flex items-center justify-between gap-3 shrink-0">
        <div class="flex items-center gap-3 min-w-0 pr-2">
          <div class="w-8 h-8 rounded-lg bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 shrink-0">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          </div>
          <div class="min-w-0">
            <h2 id="modalTitle" class="text-sm sm:text-base font-bold text-white truncate leading-snug">Judul Dokumen</h2>
            <p id="modalSub" class="text-[11px] text-slate-400 truncate">Semester & Topik</p>
          </div>
        </div>
        
        <!-- Modal Actions -->
        <div class="flex items-center gap-1.5 shrink-0">
          <!-- Copy Markdown Button -->
          <button onclick="copyCurrentMarkdown()" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium border border-slate-700/80 transition flex items-center gap-1.5 cursor-pointer" title="Salin Sumber Markdown">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span id="copyBtnText" class="hidden sm:inline">Salin</span>
          </button>
          
          <!-- Fullscreen Toggle -->
          <button onclick="toggleFullscreenModal()" class="p-1.5 px-2 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium border border-slate-700/80 transition cursor-pointer" title="Layar Penuh (Toggle)">
            <svg id="fullscreenIcon" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6"/><path d="M9 21H3v-6"/><path d="M21 3l-7 7"/><path d="M3 21l7-7"/></svg>
          </button>
          
          <!-- Open in GitHub -->
          <a id="modalGithubLink" href="#" target="_blank"
             class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium border border-slate-700/80 transition cursor-pointer" title="Buka Berkas di GitHub">
            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            <span class="hidden md:inline">GitHub</span>
          </a>
          
          <!-- Close Button -->
          <button onclick="closeModal()" class="p-1.5 px-2 rounded-lg bg-slate-800/80 hover:bg-rose-500/20 hover:text-rose-300 border border-slate-700/80 text-slate-400 text-xs font-semibold transition active:scale-95 ml-1 cursor-pointer" title="Tutup (Esc)">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
        </div>
      </div>
      
      <!-- Table of Contents Quick Jump Bar -->
      <div id="modalToc" style="display: none;" class="px-5 py-2 bg-[#090d16] border-b border-slate-800/70 items-center gap-1.5 overflow-x-auto text-[11px] scrollbar-none shrink-0">
        <!-- Dynamically injected TOC pills -->
      </div>
      
      <!-- Modal Body (Pure Markdown Reader without annoying bottom banner) -->
      <div id="modalBody" class="p-6 sm:p-10 overflow-y-auto markdown-body text-slate-200">
        <!-- Markdown injected here -->
      </div>
    </div>
  </div>

  <!-- Clean Footer -->
  <footer class="mt-16 border-t border-slate-800/80 bg-[#060910] py-8 px-4 sm:px-6 lg:px-8 text-xs text-slate-500">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-2">
        <span class="font-bold text-slate-300">BelajarKompre</span>
        <span>• Departemen Informatika Universitas Diponegoro</span>
      </div>
      <div class="flex items-center gap-4 text-slate-400">
        <a href="https://github.com/khairys/BelajarKompre" target="_blank" class="hover:text-white transition">GitHub</a>
        <span>•</span>
        <a href="https://github.com/khairys/BelajarKompre/blob/main/INVENTARIS_BERKAS.md" target="_blank" class="hover:text-white transition">Inventaris Berkas</a>
        <span>•</span>
        <a href="https://github.com/khairys/BelajarKompre/blob/main/AGENT_GUIDE.md" target="_blank" class="hover:text-white transition">Agent Guide</a>
      </div>
      <div class="text-[11px]">
        Kurikulum 2020 • 44 Matkul • 8 Sintesis Semester • 88 Berkas Kajian
      </div>
    </div>
  </footer>

  <!-- Application Logic -->
  <script>
    // Initialize Mermaid
    mermaid.initialize({
      startOnLoad: false,
      theme: 'dark',
      themeVariables: {
        darkMode: true,
        background: '#090d16',
        primaryColor: '#6366f1',
        primaryBorderColor: '#818cf8',
        primaryTextColor: '#f8fafc',
        lineColor: '#64748b'
      }
    });

    const dataTree = __DATA_TREE_JSON__;
    const semesterMeta = __SEMESTER_META_JSON__;
    const contentRegistry = __REGISTRY_JSON__;
    
    // Helper to retrieve markdown content from embedded registry (Anti-CORS / 0ms instant)
    function getContentFromRegistry(url, backupUrl) {
      if (!url) return null;
      if (contentRegistry[url]) return contentRegistry[url];
      if (backupUrl && contentRegistry[backupUrl]) return contentRegistry[backupUrl];
      
      const normUrl = url.replace(/\\\\/g, '/');
      if (contentRegistry[normUrl]) return contentRegistry[normUrl];
      
      const filename = normUrl.split('/').pop();
      if (contentRegistry[filename]) return contentRegistry[filename];
      
      for (const key in contentRegistry) {
        if (key.endsWith(normUrl) || key.endsWith(filename)) {
          return contentRegistry[key];
        }
      }
      return null;
    }

    // Flatten subjects
    let allSubjects = [];
    dataTree.forEach(sem => {
      sem.subjects.forEach(subj => {
        allSubjects.push({
          ...subj,
          semester_name: sem.name
        });
      });
    });

    // State
    let currentSemester = 'all';
    let currentTopic = 'all';
    let searchQuery = '';
    let currentRawMarkdown = '';
    let isModalFullscreen = false;

    const coursesGrid = document.getElementById('coursesGrid');
    const resultCount = document.getElementById('resultCount');
    const emptyState = document.getElementById('emptyState');
    const navSearchInput = document.getElementById('navSearchInput');
    const navClearSearchBtn = document.getElementById('navClearSearchBtn');
    const mobileSearchInput = document.getElementById('mobileSearchInput');
    const mobileClearSearchBtn = document.getElementById('mobileClearSearchBtn');
    const semesterContextCard = document.getElementById('semesterContextCard');
    const modal = document.getElementById('markdownModal');
    const modalDialog = document.getElementById('modalDialog');
    const modalTitle = document.getElementById('modalTitle');
    const modalSub = document.getElementById('modalSub');
    const modalBody = document.getElementById('modalBody');
    const modalToc = document.getElementById('modalToc');
    const modalGithubLink = document.getElementById('modalGithubLink');

    // Render Course Cards
    function renderCourses() {
      const query = searchQuery.toLowerCase().trim();

      const filtered = allSubjects.filter(item => {
        if (currentSemester !== 'all' && item.semester_num.toString() !== currentSemester) {
          return false;
        }
        if (currentTopic !== 'all' && item.topic !== currentTopic) {
          return false;
        }
        if (query) {
          const matchName = item.name.toLowerCase().includes(query);
          const matchFolder = item.folder.toLowerCase().includes(query);
          const matchTopic = item.topic.toLowerCase().includes(query);
          const matchMateri = item.materi_files.some(f => f.toLowerCase().includes(query));
          const matchSoal = item.soal_files.some(f => f.toLowerCase().includes(query));
          return matchName || matchFolder || matchTopic || matchMateri || matchSoal;
        }
        return true;
      });

      resultCount.textContent = `Menampilkan ${filtered.length} dari ${allSubjects.length} mata kuliah`;

      if (filtered.length === 0) {
        coursesGrid.innerHTML = '';
        emptyState.style.display = 'block';
        return;
      }

      emptyState.style.display = 'none';

      coursesGrid.innerHTML = filtered.map(item => `
        <div class="group bg-[#0e1422] hover:bg-[#121a2c] border border-slate-800/80 hover:border-indigo-500/40 rounded-xl p-4 sm:p-5 flex flex-col justify-between transition-all duration-150">
          <div>
            <!-- Top Badges -->
            <div class="flex items-center justify-between gap-2 mb-2.5">
              <span class="px-2 py-0.5 rounded bg-slate-800/80 text-slate-300 font-semibold text-[11px] border border-slate-700/60">
                ${item.semester_name}
              </span>
              <span class="text-[11px] font-medium text-slate-400 px-2 py-0.5 rounded bg-slate-800/40">
                ${item.topic}
              </span>
            </div>

            <!-- Subject Title -->
            <h3 class="font-bold text-base text-white group-hover:text-indigo-300 transition-colors line-clamp-1 mb-1" title="${item.name}">
              ${item.name}
            </h3>
            
            <p class="text-[11px] text-slate-400 mb-4 flex items-center gap-1.5">
              <span>Arsip:</span>
              <span class="text-slate-300 font-medium">${item.materi_count} materi</span>
              <span>•</span>
              <span class="text-slate-300 font-medium">${item.soal_count} soal</span>
            </p>
          </div>

          <!-- Action Buttons -->
          <div class="space-y-2 pt-3 border-t border-slate-800/70">
            <div class="grid grid-cols-2 gap-2">
              <button onclick="openMarkdownViewer('${item.url_rk_materi}', 'Rangkuman: ${item.name}', '${item.semester_name} • ${item.topic}', '${item.gh_rk_materi}')"
                      class="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-lg bg-indigo-500/10 hover:bg-indigo-500/20 border border-indigo-500/30 hover:border-indigo-500/50 text-indigo-300 text-xs font-semibold transition active:scale-[0.98] cursor-pointer">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                <span>Rangkuman</span>
              </button>
              <button onclick="openMarkdownViewer('${item.url_rk_soal}', 'Bank Soal: ${item.name}', '${item.semester_name} • ${item.topic}', '${item.gh_rk_soal}')"
                      class="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-lg bg-sky-500/10 hover:bg-sky-500/20 border border-sky-500/30 hover:border-sky-500/50 text-sky-300 text-xs font-semibold transition active:scale-[0.98] cursor-pointer">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
                <span>Bank Soal</span>
              </button>
            </div>

            <!-- Expandable Archive Details Accordion -->
            <details class="text-[11px] text-slate-400 mt-1">
              <summary class="cursor-pointer select-none py-1 hover:text-slate-200 transition flex items-center justify-between text-[11px]">
                <span>Daftar berkas asli (${item.materi_count + item.soal_count})</span>
                <span class="text-xs opacity-60">▾</span>
              </summary>
              <div class="mt-1.5 p-2 rounded-lg bg-slate-950/80 border border-slate-800/80 space-y-1 max-h-28 overflow-y-auto">
                <div class="font-semibold text-slate-300 text-[10px]">Bank Soal (${item.soal_count}):</div>
                ${item.soal_files.length ? item.soal_files.slice(0, 4).map(f => `<div class="truncate text-[10px] text-amber-400/90 font-mono">• ${f}</div>`).join('') : '<div class="italic text-slate-600 text-[10px]">Tidak ada berkas soal mentah</div>'}
                <div class="font-semibold text-slate-300 text-[10px] pt-1">Slide Kuliah (${item.materi_count}):</div>
                ${item.materi_files.length ? item.materi_files.slice(0, 4).map(f => `<div class="truncate text-[10px] text-blue-400/90 font-mono">• ${f}</div>`).join('') : '<div class="italic text-slate-600 text-[10px]">Tidak ada berkas slide</div>'}
              </div>
            </details>
          </div>
        </div>
      `).join('');
    }

    // Semester Switcher
    function updateSemesterView(semVal) {
      currentSemester = semVal;
      
      document.querySelectorAll('.sem-btn').forEach(b => {
        if (b.getAttribute('data-sem') === semVal) {
          b.className = 'sem-btn px-3.5 py-1.5 rounded-lg bg-indigo-600 text-white whitespace-nowrap transition shadow-sm font-semibold cursor-pointer';
        } else {
          b.className = 'sem-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition cursor-pointer';
        }
      });

      if (semVal === 'all') {
        semesterContextCard.style.display = 'none';
      } else {
        const semNum = parseInt(semVal, 10);
        const meta = semesterMeta[semNum];
        if (meta) {
          document.getElementById('semContextBadge').textContent = meta.badge;
          document.getElementById('semContextTitle').textContent = `Semester ${semNum}: ${meta.title}`;
          document.getElementById('semContextDesc').textContent = meta.desc;
          document.getElementById('semContextSub').textContent = `Mata kuliah: ${meta.sub}`;
          document.getElementById('semContextGhLink').href = meta.gh_url;
          document.getElementById('semContextBtnLabel').textContent = `Buka Sintesis Semester ${semNum}`;
          
          const readBtn = document.getElementById('semContextReadBtn');
          readBtn.onclick = () => openSemesterSummary(semNum);
          
          semesterContextCard.style.display = 'block';
        }
      }
      renderCourses();
    }

    // Semester buttons event
    document.querySelectorAll('.sem-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        updateSemesterView(btn.getAttribute('data-sem'));
      });
    });

    function openSemesterSummary(semNum) {
      const meta = semesterMeta[semNum];
      if (!meta) return;
      openMarkdownViewer(
        meta.url,
        `Sintesis Komprehensif: Semester ${semNum}`,
        `${meta.badge} • ${meta.title}`,
        meta.gh_url,
        meta.backup_url
      );
    }

    // Topic buttons event
    document.querySelectorAll('.topic-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.topic-btn').forEach(b => {
          b.className = 'topic-btn px-3 py-1.5 rounded-lg bg-slate-900/80 hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-800 transition text-xs font-medium whitespace-nowrap cursor-pointer';
        });
        btn.className = 'topic-btn px-3 py-1.5 rounded-lg bg-indigo-600/20 text-indigo-300 border border-indigo-500/40 transition text-xs font-semibold whitespace-nowrap cursor-pointer';
        currentTopic = btn.getAttribute('data-topic');
        renderCourses();
      });
    });

    // Search synchronization
    function handleSearchInput(val) {
      searchQuery = val;
      navSearchInput.value = val;
      mobileSearchInput.value = val;

      if (val) {
        navClearSearchBtn.style.display = 'flex';
        mobileClearSearchBtn.style.display = 'flex';
      } else {
        navClearSearchBtn.style.display = 'none';
        mobileClearSearchBtn.style.display = 'none';
      }
      renderCourses();
    }

    navSearchInput.addEventListener('input', (e) => handleSearchInput(e.target.value));
    mobileSearchInput.addEventListener('input', (e) => handleSearchInput(e.target.value));

    function clearSearch() {
      handleSearchInput('');
    }

    navClearSearchBtn.addEventListener('click', clearSearch);
    mobileClearSearchBtn.addEventListener('click', clearSearch);

    function resetFilters() {
      clearSearch();
      currentTopic = 'all';
      document.querySelector('.topic-btn[data-topic="all"]').click();
      updateSemesterView('all');
    }

    // Global keyboard shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== navSearchInput && document.activeElement !== mobileSearchInput) {
        e.preventDefault();
        navSearchInput.focus();
      }
      if (e.key === 'Escape') {
        closeModal();
      }
    });

    // KaTeX Formula Cleaner Function
    function cleanKatexEquation(eq) {
      if (!eq) return '';
      let cleaned = eq.trim();
      cleaned = cleaned.replace(/&amp;/g, '&');
      cleaned = cleaned.replace(/&lt;/g, '<');
      cleaned = cleaned.replace(/&gt;/g, '>');
      // Auto-escape unescaped underscores inside \text{...} to prevent KaTeX parse errors
      cleaned = cleaned.replace(/\\text\{([^{}]+)\}/g, (match, inner) => {
        const fixed = inner.replace(/(?<!\\)_/g, '\\_');
        return '\\text{' + fixed + '}';
      });
      return cleaned;
    }

    // Markdown Parser with KaTeX & GitHub Callouts Support
    function renderMarkdownContent(raw) {
      currentRawMarkdown = raw;
      
      // STEP 1: Shield code blocks and inline code
      const codeList = [];
      let text = raw.replace(/(```[\s\S]*?```|`[^`\n]+?`)/g, (match) => {
        codeList.push(match);
        return `@@CODE_SHIELD_${codeList.length - 1}@@`;
      });

      // STEP 2: Extract LaTeX Math Formulas
      const mathList = [];
      
      // Match display math: $$...$$ OR \[...\] (including optional multiple backslashes)
      text = text.replace(/(?:\$\$([\s\S]*?)\$\$|\\+\[([\s\S]*?)\\+\])/g, (_, eq1, eq2) => {
        const rawEq = eq1 !== undefined ? eq1 : eq2;
        mathList.push({ type: 'display', eq: cleanKatexEquation(rawEq) });
        return `\n\nKATEXDISPLAYSHIELD_${mathList.length - 1}_\n\n`;
      });
      
      // Match inline math: \(...\) OR $...$
      text = text.replace(/(?:\\+\(([\s\S]*?)\\+\)|(?<!\\)\$(?!\$)([^$\n]+?)(?<!\\)\$)/g, (_, eq1, eq2) => {
        const rawEq = eq1 !== undefined ? eq1 : eq2;
        mathList.push({ type: 'inline', eq: cleanKatexEquation(rawEq) });
        return `KATEXINLINESHIELD_${mathList.length - 1}_`;
      });

      // STEP 3: Restore protected code blocks
      codeList.forEach((codeStr, idx) => {
        text = text.replace(`@@CODE_SHIELD_${idx}@@`, codeStr);
      });
      
      // STEP 4: Parse Markdown with marked.js
      let html = marked.parse(text);
      
      // STEP 5: Re-inject KaTeX Math equations
      // Display Math
      html = html.replace(/(?:<p[^>]*>\s*)?KATEXDISPLAYSHIELD_(\d+)_(?:\s*<\/p>)?/g, (_, idx) => {
        const item = mathList[parseInt(idx, 10)];
        if (!item) return '';
        try {
          return katex.renderToString(item.eq, {
            displayMode: true,
            throwOnError: false,
            trust: true
          });
        } catch (err) {
          console.warn("KaTeX Display Error:", err);
          return `<div class="katex-error text-rose-400 font-mono text-xs my-2 p-2 bg-rose-950/40 rounded border border-rose-800">$$${item.eq}$$</div>`;
        }
      });
      
      // Inline Math
      html = html.replace(/KATEXINLINESHIELD_(\d+)_/g, (_, idx) => {
        const item = mathList[parseInt(idx, 10)];
        if (!item) return '';
        try {
          return katex.renderToString(item.eq, {
            displayMode: false,
            throwOnError: false,
            trust: true
          });
        } catch (err) {
          console.warn("KaTeX Inline Error:", err);
          return `<span class="katex-error text-rose-400 font-mono text-xs">$${item.eq}$</span>`;
        }
      });
      
      // STEP 6: Transform GitHub-style Alert Callouts
      html = html.replace(/<blockquote>\s*<p>\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]([\s\S]*?)<\/blockquote>/gi, (_, type, content) => {
        const t = type.toUpperCase();
        let border = "border-blue-500/40 bg-blue-500/10 text-blue-200";
        let label = "CATATAN";
        
        if (t === "TIP") {
          border = "border-emerald-500/40 bg-emerald-500/10 text-emerald-200";
          label = "TIPS";
        } else if (t === "WARNING" || t === "CAUTION") {
          border = "border-amber-500/40 bg-amber-500/10 text-amber-200";
          label = "PERHATIAN";
        } else if (t === "IMPORTANT") {
          border = "border-purple-500/40 bg-purple-500/10 text-purple-200";
          label = "PENTING";
        }
        
        return `
          <div class="my-4 p-4 rounded-xl border ${border} text-xs sm:text-sm">
            <div class="font-bold mb-1 tracking-wider uppercase text-[11px] opacity-90">${label}</div>
            <div class="leading-relaxed opacity-95">${content}</div>
          </div>
        `;
      });
      
      return html;
    }

    async function openMarkdownViewer(url, title, subtitle, githubUrl, backupUrl) {
      modalTitle.textContent = title;
      modalSub.textContent = subtitle;
      modalGithubLink.href = githubUrl || '#';
      modalToc.style.display = 'none';
      modalToc.innerHTML = '';
      
      // Make modal visible with flex display
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';

      // Retrieve markdown text
      let markdownText = getContentFromRegistry(url, backupUrl);

      if (!markdownText) {
        try {
          let response = await fetch(url);
          if (!response.ok && backupUrl) {
            response = await fetch(backupUrl);
          }
          if (response.ok) {
            markdownText = await response.text();
          }
        } catch (fetchErr) {
          console.warn("Fetch fallback failed:", fetchErr);
        }
      }

      if (markdownText) {
        modalBody.innerHTML = renderMarkdownContent(markdownText);
        
        // Render Mermaid Diagrams
        const mermaidNodes = [];
        modalBody.querySelectorAll('pre code.language-mermaid, pre code.lang-mermaid').forEach((codeEl) => {
          const pre = codeEl.closest('pre');
          const diagramText = codeEl.textContent.trim();
          const container = document.createElement('div');
          container.className = 'mermaid my-6 p-4 rounded-xl bg-slate-950/80 border border-slate-800 flex justify-center overflow-x-auto';
          container.textContent = diagramText;
          pre.parentNode.replaceChild(container, pre);
          mermaidNodes.push(container);
        });
        
        if (mermaidNodes.length > 0) {
          try {
            await mermaid.run({ nodes: mermaidNodes });
          } catch (mErr) {
            console.warn("Mermaid execution error:", mErr);
          }
        }
        
        // Highlight Code Blocks
        modalBody.querySelectorAll('pre code:not(.language-mermaid)').forEach((block) => {
          hljs.highlightElement(block);
        });
        
        // Build Table of Contents
        const headings = modalBody.querySelectorAll('h1, h2, h3');
        if (headings.length > 1) {
          modalToc.innerHTML = '<span class="text-slate-500 font-semibold text-[11px] shrink-0 mr-1">Daftar Isi:</span>';
          headings.forEach((h, idx) => {
            const id = `heading-${idx}`;
            h.id = id;
            const text = h.textContent.replace(/^[0-9\.\s]+/, '').trim();
            if (text && text.length > 2) {
              const pill = document.createElement('a');
              pill.href = `#${id}`;
              pill.className = 'shrink-0 px-2 py-0.5 rounded bg-slate-800/80 hover:bg-indigo-600 text-slate-300 hover:text-white border border-slate-700/80 transition text-[11px] font-medium cursor-pointer';
              pill.textContent = text.length > 32 ? text.slice(0, 32) + '…' : text;
              pill.onclick = (e) => {
                e.preventDefault();
                h.scrollIntoView({ behavior: 'smooth', block: 'start' });
              };
              modalToc.appendChild(pill);
            }
          });
          modalToc.style.display = 'flex';
        }
        
        modalBody.scrollTop = 0;
      } else {
        modalBody.innerHTML = `
          <div class="py-16 px-4 text-center max-w-md mx-auto">
            <h4 class="font-bold text-base text-white">Berkas Kajian Belum Tersedia</h4>
            <p class="text-xs text-slate-400 mt-2 leading-relaxed">
              Berkas kajian dapat diakses langsung melalui repositori GitHub.
            </p>
            <div class="mt-5">
              <a href="${githubUrl}" target="_blank" class="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow transition inline-block">
                Buka di GitHub
              </a>
            </div>
          </div>
        `;
      }
    }

    function closeModal() {
      modal.style.display = 'none';
      document.body.style.overflow = 'auto';
    }

    // Modal click-outside protection: clicking backdrop DOES NOT close modal.
    // Modal is only closed via explicit Close button (X) or Escape key.

    function toggleFullscreenModal() {
      isModalFullscreen = !isModalFullscreen;
      if (isModalFullscreen) {
        modalDialog.className = 'bg-[#0b101b] border-none w-screen h-screen max-w-none max-h-none flex flex-col shadow-2xl overflow-hidden rounded-none';
      } else {
        modalDialog.className = 'bg-[#0b101b] border border-slate-800 rounded-2xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-2xl overflow-hidden';
      }
    }

    function copyCurrentMarkdown() {
      if (!currentRawMarkdown) return;
      navigator.clipboard.writeText(currentRawMarkdown).then(() => {
        const copyBtnText = document.getElementById('copyBtnText');
        copyBtnText.textContent = 'Tersalin!';
        setTimeout(() => { copyBtnText.textContent = 'Salin'; }, 2000);
      }).catch(() => {
        alert("Gagal menyalin otomatis, silakan salin teks manual.");
      });
    }

    // Initial render
    renderCourses();
  </script>
</body>
</html>
"""

# Replace placeholders
final_html = html_template.replace("__DATA_TREE_JSON__", data_tree_json)
final_html = final_html.replace("__SEMESTER_META_JSON__", semester_meta_json)
final_html = final_html.replace("__REGISTRY_JSON__", registry_json)
final_html = final_html.replace("__TOTAL_SUBJECTS__", str(total_subjects))
final_html = final_html.replace("__TOTAL_RK_FILES__", str(total_rk_files))
final_html = final_html.replace("__TOTAL_RAW_FILES__", str(total_raw_files))
final_html = final_html.replace("__TOPICS_BUTTONS__", topic_pills_html)

out_html = os.path.join(base_dir, "index.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated {out_html} successfully ({len(final_html):,} bytes)!")
