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
    "Sistem_Cerdas": "Kecerdasan Buatan (AI)",
    "Pembelajaran_Mesin": "Kecerdasan Buatan (AI)",
    "Penambangan_Data": "Kecerdasan Buatan (AI)",
    
    # Jaringan & Keamanan
    "Jaringan_Komputer": "Jaringan & Keamanan",
    "Keamanan_dan_Jaminan_Informasi": "Jaringan & Keamanan",
    
    # Humaniora, Kulminasi & Etika
    "Pancasila_dan_Kewarganegaraan": "Pengembangan Diri & Etika",
    "Bahasa_Inggris": "Pengembangan Diri & Etika",
    "Olah_Raga": "Pengembangan Diri & Etika",
    "Bahasa_Indonesia": "Pengembangan Diri & Etika",
    "Pendidikan_Agama": "Pengembangan Diri & Etika",
    "Kewirausahaan": "Pengembangan Diri & Etika",
    "Masyarakat_dan_Etika_Profesi": "Pengembangan Diri & Etika",
    "Metodologi_dan_Penulisan_Ilmiah": "Riset & Karya Ilmiah",
    "Praktik_Kerja_Lapangan": "Kulminasi & Lapangan",
    "Kuliah_Kerja_Nyata": "Kulminasi & Lapangan",
    "Tugas_Akhir": "Kulminasi & Lapangan"
}

SEMESTER_METADATA = {
    1: {
        "title": "Semester 1 • Fondasi Komputasi & Pemrograman Fungsional",
        "badge": "8 Mata Kuliah Wajib",
        "sub": "Dasar Pemrograman, Dasar Sistem, Logika, Diskrit, Mat 1, B.Inggris, PKn, Olahraga",
        "url": "semester1.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/01_Semester_1/RANGKUMAN_SEMESTER_1.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester1.md",
        "desc": "Sintesis komprehensif 8 mata kuliah: paradigma fungsional & rekursi, gerbang logika digital, kuantor logika formal, pembuktian induksi matematika, kalkulus dasar limit-turunan-integral, serta peta relasi antarmata kuliah."
    },
    2: {
        "title": "Semester 2 • Algoritma Prosedural, Sistem Hardware & Aljabar",
        "badge": "7 Mata Kuliah Wajib",
        "sub": "Alpro C, Aljabar Linier, B.Indonesia, IoT, Mat 2, OARK, Agama",
        "url": "semester2.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/02_Semester_2/RANGKUMAN_SEMESTER_2.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester2.md",
        "desc": "Sintesis komprehensif 7 mata kuliah: pointer C & dynamic memory, ruang vektor & dekomposisi matriks, mikrokontroler IoT, siklus instruksi CPU & pipelining, kalkulus multivariabel (gradien, turunan parsial, integral lipat)."
    },
    3: {
        "title": "Semester 3 • Rekayasa Data, Sistem Inti & Komputasi Numerik",
        "badge": "6 Mata Kuliah Wajib",
        "sub": "Basis Data, IMK, Metode Numerik, Sistem Operasi, Statistika, Struktur Data",
        "url": "semester3.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/03_Semester_3/RANGKUMAN_SEMESTER_3.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester3.md",
        "desc": "Sintesis komprehensif 6 mata kuliah: normalisasi BCNF, relasional aljabar, proses OS & deadlock prevention, pohon seimbang AVL, regresi & ANOVA statistika, serta solusi aproksimasi numerik (Newton-Raphson & Runge-Kutta)."
    },
    4: {
        "title": "Semester 4 • Rekayasa Perangkat Lunak, Jaringan & AI Dasar",
        "badge": "6 Mata Kuliah Wajib",
        "sub": "GKV, Jaringan Komputer, MBD, PBO Java, RPL, Sistem Cerdas",
        "url": "semester4.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/04_Semester_4/RANGKUMAN_SEMESTER_4.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester4.md",
        "desc": "Sintesis komprehensif 6 mata kuliah: rendering grafika DDA/Bresenham, subnetting IPv4/VLSM, transaksi ACID & locking concurrency, prinsip OOP SOLID, model Agile/Scrum & diagram UML, serta pencarian A* dan rule-based AI."
    },
    5: {
        "title": "Semester 5 • Keamanan Sistem, Komputasi Skala Besar & Machine Learning",
        "badge": "7 Mata Kuliah Wajib",
        "sub": "KJI, Kewirausahaan, KTP, Pembelajaran Mesin, PBP, Proyek PL, SI",
        "url": "semester5.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/05_Semester_5/RANGKUMAN_SEMESTER_5.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester5.md",
        "desc": "Sintesis komprehensif 7 mata kuliah: kriptografi simetris/asimetris (AES, RSA, SHA), komputasi paralel MPI/OpenMP & Hukum Amdahl, evaluasi Machine Learning (ROC/AUC, F1-Score), web full-stack API, dan tata kelola TI."
    },
    6: {
        "title": "Semester 6 • Analisis Algoritma Kompleks, Manajemen Proyek & Pengujian",
        "badge": "5 Mata Kuliah Wajib",
        "sub": "ASA, Manajemen Proyek, Etika Profesi, PKL, Uji Perangkat Lunak",
        "url": "semester6.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/06_Semester_6/RANGKUMAN_SEMESTER_6.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester6.md",
        "desc": "Sintesis komprehensif 5 mata kuliah: Teorema Master & Dynamic Programming, Earned Value Management (EVM / CPI / SPI), kode etik profesi ACM/IEEE, laporan PKL industri, serta pengujian White Box (Cyclomatic Complexity) & Black Box."
    },
    7: {
        "title": "Semester 7 • Teori Komputasi Lanjut, Data Mining & Metodologi Riset",
        "badge": "3 Mata Kuliah Wajib",
        "sub": "Metodologi Riset, Penambangan Data, Teori Bahasa & Otomata",
        "url": "semester7.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/07_Semester_7/RANGKUMAN_SEMESTER_7.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester7.md",
        "desc": "Sintesis komprehensif 3 mata kuliah: hierarki tata bahasa Chomsky, ekivalensi DFA/NFA/Turing Machine, asosiasi Apriori & clustering k-means, serta formulasi research gap dan sistematika penulisan proposal skripsi."
    },
    8: {
        "title": "Semester 8 • Kulminasi Akademik, Pengabdian Masyarakat & Sidang Tugas Akhir",
        "badge": "2 Mata Kuliah Wajib",
        "sub": "Kuliah Kerja Nyata (KKN), Tugas Akhir / Skripsi Komprehensif",
        "url": "semester8.md",
        "backup_url": "RANGKUMAN_DAN_CONTOH_SOAL/08_Semester_8/RANGKUMAN_SEMESTER_8.md",
        "gh_url": "https://github.com/khairys/BelajarKompre/blob/main/semester8.md",
        "desc": "Sintesis komprehensif 2 mata kuliah puncak: integrasi pengabdian masyarakat partisipatif (PRA), struktur manuskrip skripsi standar IMRaD, serta simulasi dan strategi menghadapi sidang ujian sarjana komprehensif."
    }
}

# --- BUILD EMBEDDED CONTENT REGISTRY (100% Anti-CORS & Instant Load) ---
content_registry = {}

# 1. Semesters (semester1.md s.d. semester8.md)
for i in range(1, 9):
    fn = os.path.join(base_dir, f"semester{i}.md")
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f:
            text = f.read()
            content_registry[f"semester{i}.md"] = text
            content_registry[f"RANGKUMAN_DAN_CONTOH_SOAL/{i:02d}_Semester_{i}/RANGKUMAN_SEMESTER_{i}.md"] = text

# 2. RANGKUMAN_DAN_CONTOH_SOAL (all markdown files)
for root, dirs, files in os.walk(rangkuman_base):
    for f in files:
        if f.endswith(".md"):
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, base_dir).replace("\\", "/")
            with open(fp, "r", encoding="utf-8") as mf:
                content_registry[rel] = mf.read()

registry_json = json.dumps(content_registry, ensure_ascii=False)
# Secure script tags from prematurely closing HTML script tag
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

html_content = f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BelajarKompre • Portal Belajar S1 Informatika Undip</title>
  <meta name="description" content="Katalog 44 mata kuliah wajib dan 88 berkas kajian materi perkuliahan serta bank soal komprehensif S1 Informatika Universitas Diponegoro (Kurikulum 2020). Dilengkapi rangkuman terpadu Semester 1 hingga 8 dengan formula KaTeX.">
  
  <!-- Favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎓</text></svg>">
  
  <!-- Tailwind CSS & Marked.js -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
  <!-- KaTeX for LaTeX Math Formula Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  
  <!-- Mermaid.js for Diagrams & Flowcharts -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  
  <!-- Highlight.js for Code Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark-dimmed.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }},
          colors: {{
            brand: {{
              50: '#eef2ff',
              100: '#e0e7ff',
              400: '#818cf8',
              500: '#6366f1',
              600: '#4f46e5',
              900: '#312e81',
            }}
          }}
        }}
      }}
    }}
  </script>
  
  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: #090d16; }}
    ::-webkit-scrollbar-thumb {{ background: #1e293b; border-radius: 9999px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #334155; }}
    
    /* KaTeX Math Styling */
    .katex {{ font-size: 1.08em; text-rendering: auto; }}
    .katex-display {{
      margin: 1.25rem 0 !important;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 0.75rem 1rem;
      background: rgba(15, 23, 42, 0.75);
      border-radius: 0.75rem;
      border: 1px solid rgba(99, 102, 241, 0.25);
      box-shadow: 0 4px 12px -2px rgba(0, 0, 0, 0.3);
    }}
    .katex-html {{ white-space: normal; }}
    
    /* Markdown Modal Typography */
    .markdown-body {{ line-height: 1.75; font-size: 0.95rem; }}
    .markdown-body h1 {{ font-size: 1.85rem; font-weight: 800; color: #f8fafc; margin-top: 1.75rem; margin-bottom: 0.85rem; border-bottom: 1px solid #334155; padding-bottom: 0.6rem; letter-spacing: -0.02em; }}
    .markdown-body h2 {{ font-size: 1.45rem; font-weight: 700; color: #93c5fd; margin-top: 2rem; margin-bottom: 0.75rem; border-bottom: 1px solid #1e293b; padding-bottom: 0.4rem; letter-spacing: -0.01em; scroll-margin-top: 5.5rem; }}
    .markdown-body h3 {{ font-size: 1.2rem; font-weight: 600; color: #cbd5e1; margin-top: 1.5rem; margin-bottom: 0.6rem; scroll-margin-top: 5.5rem; }}
    .markdown-body h4 {{ font-size: 1.05rem; font-weight: 600; color: #e2e8f0; margin-top: 1.25rem; margin-bottom: 0.4rem; }}
    .markdown-body p {{ margin-bottom: 1rem; line-height: 1.8; color: #cbd5e1; }}
    .markdown-body ul, .markdown-body ol {{ padding-left: 1.5rem; margin-bottom: 1.25rem; color: #cbd5e1; }}
    .markdown-body ul {{ list-style-type: disc; }}
    .markdown-body ol {{ list-style-type: decimal; }}
    .markdown-body li {{ margin-bottom: 0.45rem; line-height: 1.65; }}
    .markdown-body strong {{ color: #ffffff; font-weight: 700; }}
    .markdown-body em {{ color: #94a3b8; font-style: italic; }}
    .markdown-body code {{ font-family: 'JetBrains Mono', monospace; background: #1e293b; color: #fb7185; padding: 0.2rem 0.45rem; border-radius: 0.35rem; font-size: 0.88em; }}
    .markdown-body pre {{ background: #0b101b; border: 1px solid #1e293b; padding: 1.15rem; border-radius: 0.85rem; overflow-x: auto; margin: 1.25rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); }}
    .markdown-body pre code {{ background: transparent; color: #e2e8f0; padding: 0; font-size: 0.88em; }}
    .markdown-body table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.9rem; overflow-x: auto; display: block; }}
    .markdown-body th, .markdown-body td {{ border: 1px solid #334155; padding: 0.75rem 1rem; text-align: left; }}
    .markdown-body th {{ background: #1e293b; color: #f8fafc; font-weight: 600; }}
    .markdown-body tr:nth-child(even) {{ background: rgba(15, 23, 42, 0.45); }}
    .markdown-body hr {{ border: 0; border-top: 1px solid #1e293b; margin: 2rem 0; }}
    
    /* Mermaid SVG Responsive */
    .mermaid svg {{ max-width: 100%; height: auto; }}
  </style>
</head>
<body class="bg-[#090d16] text-slate-100 min-h-screen selection:bg-brand-500/30 selection:text-brand-100 antialiased">

  <!-- Ambient Glow Background -->
  <div class="fixed inset-0 pointer-events-none overflow-hidden -z-10">
    <div class="absolute -top-40 left-1/2 -translate-x-1/2 w-[700px] h-[350px] bg-indigo-600/15 blur-[120px] rounded-full"></div>
    <div class="absolute top-[600px] -left-40 w-[400px] h-[400px] bg-blue-600/10 blur-[140px] rounded-full"></div>
    <div class="absolute bottom-40 -right-40 w-[400px] h-[400px] bg-emerald-600/10 blur-[140px] rounded-full"></div>
  </div>

  <!-- Navbar -->
  <nav class="sticky top-0 z-40 backdrop-blur-xl bg-[#090d16]/90 border-b border-slate-800/80 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="text-2xl">🎓</span>
        <div>
          <a href="#" class="font-extrabold text-lg tracking-tight text-white hover:text-indigo-400 transition flex items-center gap-2">
            BelajarKompre
            <span class="text-[10px] uppercase font-bold tracking-widest px-2 py-0.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400">Undip</span>
          </a>
        </div>
      </div>
      
      <div class="flex items-center gap-2 sm:gap-3">
        <!-- Semester Summary Dropdown Button -->
        <div class="relative group">
          <button class="inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-amber-500/15 hover:bg-amber-500/25 border border-amber-500/30 text-amber-300 transition shadow-sm">
            <span>✨</span> <span class="hidden sm:inline">Rangkuman</span> Semester (1-8)
            <svg class="w-3.5 h-3.5 opacity-70 group-hover:translate-y-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <!-- Dropdown List -->
          <div class="absolute right-0 mt-1 w-64 rounded-xl bg-slate-900 border border-slate-700/80 shadow-2xl p-1.5 hidden group-hover:block z-50 animate-in fade-in duration-100">
            <div class="px-2 py-1 text-[10px] font-bold uppercase tracking-wider text-slate-400 border-b border-slate-800 mb-1">
              Pilih Rangkuman Komprehensif
            </div>
            {"".join([f'''<button onclick="openSemesterSummary({i})" class="w-full text-left px-2.5 py-1.5 rounded-lg hover:bg-indigo-600/20 hover:text-indigo-200 text-xs font-medium text-slate-300 flex items-center justify-between transition">
              <span>Semester {i}</span>
              <span class="text-[10px] text-slate-400">{SEMESTER_METADATA[i]["badge"]}</span>
            </button>''' for i in range(1, 9)])}
          </div>
        </div>

        <a href="https://github.com/khairys/BelajarKompre/blob/main/llms.txt" target="_blank"
           class="hidden md:inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700/80 text-slate-300 hover:text-white transition">
          <span>🤖</span> llms.txt (AI)
        </a>
        <a href="https://github.com/khairys/BelajarKompre" target="_blank"
           class="inline-flex items-center gap-2 text-xs font-semibold px-3.5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/20 transition">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          <span class="hidden sm:inline">GitHub</span> Repo
        </a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <header class="pt-12 pb-6 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto text-center md:text-left">
    <div class="flex flex-col md:flex-row items-center justify-between gap-8">
      <div class="max-w-3xl">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/25 text-emerald-400 text-xs font-semibold mb-4">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>Baseline Kurikulum 2020 • 44 Matkul Wajib Lengkap & 8 Sintesis Semester</span>
        </div>
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-white leading-tight">
          Portal Belajar Komprehensif <br class="hidden sm:inline">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-sky-300 to-emerald-400">
            S1 Informatika Undip
          </span>
        </h1>
        <p class="mt-4 text-slate-400 text-sm sm:text-base leading-relaxed max-w-2xl">
          Repositori kajian akademik mandiri: 44 mata kuliah wajib Semester 1 s/d 8, 8 berkas sintesis semester lengkap, formula KaTeX rendered, diagram alur Mermaid, dan pembahasan komprehensif.
        </p>
      </div>

      <!-- Quick Metrics Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-2 gap-3 w-full md:w-80">
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-amber-400">{total_subjects}</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">Matkul Wajib</div>
        </div>
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-emerald-400">8</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">Sintesis Semester</div>
        </div>
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-blue-400">{total_rk_files}</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">Kajian Materi & Soal</div>
        </div>
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-purple-400">100%</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">KaTeX Rendered</div>
        </div>
      </div>
    </div>
  </header>

  <!-- Interactive Controls Section -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
    <!-- Search Bar -->
    <div class="relative mb-5">
      <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-slate-400">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
      </div>
      <input id="searchInput" type="text" 
             placeholder="Ketik untuk mencari mata kuliah, topik, atau kata kunci (contoh: Algoritma, SQL, Jaringan, AI, Kriptografi)..." 
             class="w-full bg-slate-900/90 border border-slate-800 focus:border-indigo-500 rounded-2xl pl-12 pr-12 py-3.5 text-sm sm:text-base text-white placeholder-slate-500 shadow-xl focus:outline-none focus:ring-2 focus:ring-indigo-500/20 transition-all">
      <div id="clearSearchBtn" class="absolute inset-y-0 right-0 pr-4 flex items-center cursor-pointer text-slate-500 hover:text-slate-300 hidden">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </div>
    </div>

    <!-- Filters Row -->
    <div class="space-y-3">
      <!-- Semester Pills Filter -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-none text-xs font-semibold">
        <span class="text-slate-400 mr-1 hidden sm:inline whitespace-nowrap">Semester:</span>
        <button data-sem="all" class="sem-btn active px-3.5 py-1.5 rounded-full bg-indigo-600 text-white whitespace-nowrap transition shadow-sm">
          Semua (1-8)
        </button>
        {" ".join([f'''<button data-sem="{i}" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem {i} ({SEMESTER_METADATA[i]["badge"].split()[0]})
        </button>''' for i in range(1, 9)])}
      </div>

      <!-- Topic Pills Filter -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-none text-xs">
        <span class="text-slate-400 mr-1 hidden sm:inline whitespace-nowrap font-semibold">Bidang:</span>
        <button data-topic="all" class="topic-btn active px-3 py-1 rounded-lg bg-slate-800 text-slate-100 whitespace-nowrap border border-slate-700 font-medium transition">
          Semua Topik
        </button>
        {' '.join([f'<button data-topic="{t}" class="topic-btn px-3 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-400 border border-slate-800/80 whitespace-nowrap font-medium transition">{t}</button>' for t in sorted_topics])}
      </div>

      <!-- Featured Semester Synthesis Banner (Dynamic & Interactive for Semesters 1-8) -->
      <div id="semesterGptBanner" class="mt-4 p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-indigo-950/80 via-slate-900/95 to-purple-950/80 border border-indigo-500/30 flex flex-col gap-4 backdrop-blur-md shadow-lg shadow-indigo-500/5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div class="flex items-start sm:items-center gap-3.5">
            <div class="w-10 h-10 rounded-xl bg-indigo-500/20 border border-indigo-500/40 flex items-center justify-center text-xl shrink-0">
              ✨
            </div>
            <div>
              <div class="flex flex-wrap items-center gap-2">
                <h3 id="semesterGptTitle" class="font-bold text-sm sm:text-base text-white">Rangkuman Semester 1 • Fondasi Komputasi & Pemrograman Fungsional</h3>
                <span id="semesterGptBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/15 border border-amber-500/30 text-amber-300 uppercase tracking-wider">8 Mata Kuliah Wajib</span>
              </div>
              <p id="semesterGptDesc" class="text-xs text-slate-400 mt-1 leading-relaxed">
                Sintesis komprehensif 8 mata kuliah: paradigma fungsional & rekursi, gerbang logika digital, kuantor logika formal, pembuktian induksi matematika, kalkulus dasar limit-turunan-integral, serta peta relasi antarmata kuliah.
              </p>
            </div>
          </div>
          
          <div class="flex items-center gap-2 shrink-0 self-end sm:self-center">
            <a id="semesterGptGhLink" href="https://github.com/khairys/BelajarKompre/blob/main/semester1.md" target="_blank"
               class="px-3 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white font-medium text-xs border border-slate-700 transition flex items-center gap-1.5" title="Buka di GitHub">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
              <span>GitHub</span>
            </a>
            <button id="semesterGptBtn" onclick="openSemesterSummary(1)" class="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition shadow-md shadow-indigo-600/25 flex items-center justify-center gap-2 active:scale-95">
              <span>📖</span> Buka Rangkuman Semester 1
            </button>
          </div>
        </div>

        <!-- Quick Selector for Semesters 1-8 -->
        <div class="pt-2 border-t border-slate-800/80 flex items-center gap-1.5 overflow-x-auto text-[11px] scrollbar-none">
          <span class="text-slate-400 font-medium shrink-0 mr-1">Pilih Sintesis:</span>
          {"".join([f'''<button onclick="switchSemesterGptBanner({i})" id="semGptTab-{i}" class="sem-gpt-tab {'px-2.5 py-1 rounded-lg font-semibold transition shrink-0 ' + ('bg-indigo-600 text-white shadow-sm' if i == 1 else 'bg-slate-900/90 hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-800')}">
            Sem {i}
          </button>''' for i in range(1, 9)])}
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content Grid -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
    <div class="flex items-center justify-between mb-6">
      <div id="resultCount" class="text-xs sm:text-sm font-medium text-slate-400">
        Menampilkan 44 mata kuliah
      </div>
      <div class="flex items-center gap-2 text-xs text-slate-500">
        <span class="inline-block w-2 h-2 rounded-full bg-indigo-400"></span> Klik Rangkuman / Bank Soal untuk membaca
      </div>
    </div>

    <!-- Cards Grid -->
    <div id="coursesGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      <!-- Generated via JavaScript -->
    </div>

    <!-- Empty State -->
    <div id="emptyState" class="hidden text-center py-20 bg-slate-900/40 border border-slate-800 rounded-3xl p-8">
      <div class="text-5xl mb-4">🔍</div>
      <h3 class="text-lg font-bold text-slate-200">Mata kuliah tidak ditemukan</h3>
      <p class="text-sm text-slate-500 max-w-sm mx-auto mt-1">Coba gunakan kata kunci pencarian lain atau pilih filter "Semua Semester".</p>
      <button onclick="resetFilters()" class="mt-4 px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-semibold text-white transition">
        Reset Pencarian
      </button>
    </div>
  </main>

  <!-- Immersive Markdown Modal Reader (KaTeX + Mermaid + Highlight.js) -->
  <div id="markdownModal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-2 sm:p-5 transition-all">
    <div id="modalDialog" class="bg-[#0b101b] border border-slate-800 rounded-2xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-2xl overflow-hidden transition-all duration-150">
      
      <!-- Modal Top Bar -->
      <div class="px-5 py-3.5 border-b border-slate-800/90 flex items-center justify-between bg-slate-900/80">
        <div class="flex items-center gap-3 min-w-0 pr-4">
          <span id="modalIcon" class="text-xl">📖</span>
          <div class="min-w-0">
            <h2 id="modalTitle" class="text-base sm:text-lg font-bold text-white truncate leading-snug">Judul Dokumen</h2>
            <p id="modalSub" class="text-xs text-slate-400 truncate">Semester & Topik</p>
          </div>
        </div>
        
        <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
          <!-- Copy Markdown Button -->
          <button onclick="copyCurrentMarkdown()" class="p-1.5 sm:px-3 sm:py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium border border-slate-700/80 transition flex items-center gap-1" title="Salin Teks Markdown">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
            <span id="copyBtnText" class="hidden sm:inline">Salin</span>
          </button>
          
          <!-- Fullscreen Toggle Button -->
          <button onclick="toggleFullscreenModal()" class="p-1.5 sm:px-2.5 sm:py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium border border-slate-700/80 transition" title="Layar Penuh (Toggle)">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
          </button>
          
          <!-- Open in GitHub Link -->
          <a id="modalGithubLink" href="#" target="_blank"
             class="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-medium border border-slate-700/80 transition" title="Buka berkas di GitHub">
            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            <span class="hidden md:inline">GitHub</span>
          </a>
          
          <!-- Close Button -->
          <button onclick="closeModal()" class="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition" title="Tutup (Esc)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </div>
      </div>
      
      <!-- Table of Contents Quick Jump Bar -->
      <div id="modalToc" class="px-5 py-2 bg-slate-950/90 border-b border-slate-800/80 flex items-center gap-2 overflow-x-auto text-xs scrollbar-none hidden">
        <!-- Dynamically injected TOC pills -->
      </div>
      
      <!-- Modal Body (Rendered Markdown Container) -->
      <div id="modalBody" class="p-6 sm:p-10 overflow-y-auto markdown-body text-slate-200">
        <!-- Markdown injected here -->
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="mt-20 border-t border-slate-900 bg-[#070a12] py-10 px-4 sm:px-6 lg:px-8 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-2">
        <span class="text-lg">🎓</span>
        <span class="font-bold text-slate-300">BelajarKompre</span>
        <span>• Departemen Informatika Undip</span>
      </div>
      <div class="flex items-center gap-4 text-slate-400">
        <a href="https://github.com/khairys/BelajarKompre" target="_blank" class="hover:text-white transition">GitHub Repo</a>
        <span>•</span>
        <a href="https://github.com/khairys/BelajarKompre/blob/main/INVENTARIS_BERKAS.md" target="_blank" class="hover:text-white transition">Inventaris Berkas</a>
        <span>•</span>
        <a href="https://github.com/khairys/BelajarKompre/blob/main/AGENT_GUIDE.md" target="_blank" class="hover:text-white transition">Agent Guide</a>
      </div>
      <div>
        Baseline Kurikulum 2020 (44 Matkul • 8 Sintesis Semester • 88 Berkas Kajian)
      </div>
    </div>
  </footer>

  <!-- Application Logic -->
  <script>
    // Initialize Mermaid
    mermaid.initialize({{
      startOnLoad: false,
      theme: 'dark',
      themeVariables: {{
        darkMode: true,
        background: '#0b101b',
        primaryColor: '#6366f1',
        primaryBorderColor: '#818cf8',
        primaryTextColor: '#f8fafc',
        lineColor: '#64748b'
      }}
    }});

    const dataTree = {json.dumps(data_tree, ensure_ascii=False)};
    const semesterMeta = {json.dumps(SEMESTER_METADATA, ensure_ascii=False)};
    const contentRegistry = {registry_json};
    
    // Helper to retrieve markdown content from embedded registry (Anti-CORS / 0ms instant)
    function getContentFromRegistry(url, backupUrl) {{
      if (!url) return null;
      if (contentRegistry[url]) return contentRegistry[url];
      if (backupUrl && contentRegistry[backupUrl]) return contentRegistry[backupUrl];
      
      const normUrl = url.replace(/\\\\/g, '/');
      if (contentRegistry[normUrl]) return contentRegistry[normUrl];
      
      const filename = normUrl.split('/').pop();
      if (contentRegistry[filename]) return contentRegistry[filename];
      
      for (const key in contentRegistry) {{
        if (key.endsWith(normUrl) || key.endsWith(filename)) {{
          return contentRegistry[key];
        }}
      }}
      return null;
    }}

    // Flatten subjects
    let allSubjects = [];
    dataTree.forEach(sem => {{
      sem.subjects.forEach(subj => {{
        allSubjects.push({{
          ...subj,
          semester_name: sem.name
        }});
      }});
    }});

    // State
    let currentSemester = 'all';
    let currentTopic = 'all';
    let activeGptSemester = 1;
    let searchQuery = '';
    let currentRawMarkdown = '';
    let isModalFullscreen = false;

    const coursesGrid = document.getElementById('coursesGrid');
    const resultCount = document.getElementById('resultCount');
    const emptyState = document.getElementById('emptyState');
    const searchInput = document.getElementById('searchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');

    // Render Course Cards
    function renderCourses() {{
      const query = searchQuery.toLowerCase().trim();

      const filtered = allSubjects.filter(item => {{
        if (currentSemester !== 'all' && item.semester_num.toString() !== currentSemester) {{
          return false;
        }}
        if (currentTopic !== 'all' && item.topic !== currentTopic) {{
          return false;
        }}
        if (query) {{
          const matchName = item.name.toLowerCase().includes(query);
          const matchFolder = item.folder.toLowerCase().includes(query);
          const matchTopic = item.topic.toLowerCase().includes(query);
          const matchMateri = item.materi_files.some(f => f.toLowerCase().includes(query));
          const matchSoal = item.soal_files.some(f => f.toLowerCase().includes(query));
          return matchName || matchFolder || matchTopic || matchMateri || matchSoal;
        }}
        return true;
      }});

      resultCount.textContent = `Menampilkan ${{filtered.length}} dari ${{allSubjects.length}} mata kuliah`;

      if (filtered.length === 0) {{
        coursesGrid.innerHTML = '';
        emptyState.classList.remove('hidden');
        return;
      }}

      emptyState.classList.add('hidden');

      coursesGrid.innerHTML = filtered.map(item => `
        <div class="group bg-slate-900/60 hover:bg-slate-900/90 border border-slate-800/80 hover:border-indigo-500/40 rounded-2xl p-5 flex flex-col justify-between transition-all duration-200 hover:shadow-xl hover:shadow-indigo-500/5">
          <div>
            <!-- Top Badges -->
            <div class="flex items-center justify-between gap-2 mb-3">
              <span class="px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 font-semibold text-[11px] border border-slate-700/60">
                ${{item.semester_name}}
              </span>
              <span class="text-[11px] font-medium text-slate-400 px-2 py-0.5 rounded-md bg-slate-800/50">
                ${{item.topic}}
              </span>
            </div>

            <!-- Subject Title -->
            <h3 class="font-bold text-lg text-white group-hover:text-indigo-300 transition-colors line-clamp-1 mb-1" title="${{item.name}}">
              ${{item.name}}
            </h3>
            <p class="font-mono text-[11px] text-slate-500 mb-4 truncate">${{item.folder}}</p>
          </div>

          <!-- Action Buttons -->
          <div class="space-y-2 pt-3 border-t border-slate-800/70">
            <div class="grid grid-cols-2 gap-2">
              <button onclick="openMarkdownViewer('${{item.url_rk_materi}}', '📖 Rangkuman: ${{item.name}}', '${{item.semester_name}} • ${{item.topic}}', '${{item.gh_rk_materi}}')"
                      class="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl bg-indigo-500/10 hover:bg-indigo-500/20 border border-indigo-500/30 hover:border-indigo-500/50 text-indigo-300 text-xs font-semibold transition active:scale-[0.98]">
                <span>📖</span> Rangkuman
              </button>
              <button onclick="openMarkdownViewer('${{item.url_rk_soal}}', '📝 Bank Soal: ${{item.name}}', '${{item.semester_name}} • ${{item.topic}}', '${{item.gh_rk_soal}}')"
                      class="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 hover:border-amber-500/50 text-amber-300 text-xs font-semibold transition active:scale-[0.98]">
                <span>📝</span> Bank Soal
              </button>
            </div>

            <!-- Expandable Archive Details Accordion -->
            <details class="text-[11px] text-slate-400 mt-2">
              <summary class="cursor-pointer select-none py-1 hover:text-slate-200 transition flex items-center justify-between">
                <span>Arsip DMW: ${{item.materi_count}} slide, ${{item.soal_count}} soal</span>
                <span class="text-xs">▾</span>
              </summary>
              <div class="mt-2 p-2.5 rounded-xl bg-slate-950/70 border border-slate-800/80 space-y-1.5 max-h-28 overflow-y-auto">
                <div class="font-semibold text-slate-300">File Soal (${{item.soal_count}}):</div>
                ${{item.soal_files.length ? item.soal_files.slice(0, 3).map(f => `<div class="truncate text-[10px] text-amber-400/90 font-mono">📄 ${{f}}</div>`).join('') : '<div class="italic text-slate-600">Tidak ada soal tertulis (proyek/skripsi)</div>'}}
                <div class="font-semibold text-slate-300 pt-1">File Materi (${{item.materi_count}}):</div>
                ${{item.materi_files.length ? item.materi_files.slice(0, 3).map(f => `<div class="truncate text-[10px] text-blue-400/90 font-mono">📑 ${{f}}</div>`).join('') : '<div class="italic text-slate-600">Tidak ada materi tertulis</div>'}}
              </div>
            </details>
          </div>
        </div>
      `).join('');
    }}

    // Filter Events
    document.querySelectorAll('.sem-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.sem-btn').forEach(b => {{
          b.classList.remove('bg-indigo-600', 'text-white');
          b.classList.add('bg-slate-900', 'text-slate-300');
        }});
        btn.classList.remove('bg-slate-900', 'text-slate-300');
        btn.classList.add('bg-indigo-600', 'text-white');
        currentSemester = btn.getAttribute('data-sem');
        
        if (currentSemester !== 'all') {{
          switchSemesterGptBanner(parseInt(currentSemester, 10));
        }}
        renderCourses();
      }});
    }});

    function switchSemesterGptBanner(semNum) {{
      activeGptSemester = semNum;
      const meta = semesterMeta[semNum] || semesterMeta[1];
      
      document.getElementById('semesterGptTitle').textContent = `Rangkuman ${{meta.title}}`;
      document.getElementById('semesterGptBadge').textContent = meta.badge;
      document.getElementById('semesterGptDesc').textContent = meta.desc;
      
      const btn = document.getElementById('semesterGptBtn');
      btn.setAttribute('onclick', `openSemesterSummary(${{semNum}})`);
      btn.innerHTML = `<span>📖</span> Buka Rangkuman Semester ${{semNum}}`;
      
      const ghLink = document.getElementById('semesterGptGhLink');
      ghLink.href = meta.gh_url;
      
      document.querySelectorAll('.sem-gpt-tab').forEach((tab, idx) => {{
        const s = idx + 1;
        if (s === semNum) {{
          tab.className = 'sem-gpt-tab px-2.5 py-1 rounded-lg font-semibold transition shrink-0 bg-indigo-600 text-white shadow-sm';
        }} else {{
          tab.className = 'sem-gpt-tab px-2.5 py-1 rounded-lg font-semibold transition shrink-0 bg-slate-900/90 hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-800';
        }}
      }});
    }}

    function openSemesterSummary(semNum) {{
      const meta = semesterMeta[semNum];
      if (!meta) return;
      openMarkdownViewer(
        meta.url,
        `🎓 Rangkuman Komprehensif: Semester ${{semNum}}`,
        `${{meta.badge}} • ${{meta.sub}}`,
        meta.gh_url,
        meta.backup_url
      );
    }}

    document.querySelectorAll('.topic-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.topic-btn').forEach(b => {{
          b.classList.remove('bg-slate-800', 'text-slate-100', 'border-slate-700');
          b.classList.add('bg-slate-900', 'text-slate-400', 'border-slate-800/80');
        }});
        btn.classList.remove('bg-slate-900', 'text-slate-400', 'border-slate-800/80');
        btn.classList.add('bg-slate-800', 'text-slate-100', 'border-slate-700');
        currentTopic = btn.getAttribute('data-topic');
        renderCourses();
      }});
    }});

    // Search input
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value;
      if (searchQuery) {{
        clearSearchBtn.classList.remove('hidden');
      }} else {{
        clearSearchBtn.classList.add('hidden');
      }}
      renderCourses();
    }});

    clearSearchBtn.addEventListener('click', () => {{
      searchInput.value = '';
      searchQuery = '';
      clearSearchBtn.classList.add('hidden');
      renderCourses();
    }});

    function resetFilters() {{
      searchInput.value = '';
      searchQuery = '';
      clearSearchBtn.classList.add('hidden');
      currentSemester = 'all';
      currentTopic = 'all';
      document.querySelector('.sem-btn[data-sem="all"]').click();
      document.querySelector('.topic-btn[data-topic="all"]').click();
    }}

    // Keyboard shortcut (/)
    window.addEventListener('keydown', (e) => {{
      if (e.key === '/' && document.activeElement !== searchInput) {{
        e.preventDefault();
        searchInput.focus();
      }}
      if (e.key === 'Escape') {{
        closeModal();
      }}
    }});

    // KaTeX Formula Cleaner Function
    function cleanKatexEquation(eq) {{
      if (!eq) return '';
      // Fix markdown escaped underscores inside math e.g. \\_{10} -> _{10}
      let cleaned = eq.replace(/\\\\_([0-9a-zA-Z{{])/g, '_$1');
      cleaned = cleaned.replace(/\\\\_/g, '_');
      // Fix double escaped curly braces
      cleaned = cleaned.replace(/\\\\{{/g, '{{').replace(/\\\\}}/g, '}}');
      return cleaned.trim();
    }}

    // Robust Markdown Parser with Bulletproof KaTeX & GitHub Callouts Support
    function renderMarkdownContent(raw) {{
      currentRawMarkdown = raw;
      
      // STEP 1: Protect code blocks and inline code from KaTeX regex
      const codeList = [];
      let text = raw.replace(/(```[\\s\\S]*?```|`[^`\\n]+?`)/g, (match) => {{
        codeList.push(match);
        return `@@CODE_SHIELD_${{codeList.length - 1}}@@`;
      }});

      // STEP 2: Extract LaTeX Math Formulas
      const mathList = [];
      
      // Match display math: $$...$$ OR \\[...\\] OR \\\\[...\\\\]
      text = text.replace(/(?:\\$\\$([\\s\\S]*?)\\$\\$|(?:\\\\\\\\|\\\\)\\[([\\s\\S]*?)(?:\\\\\\\\|\\\\)\\])/g, (_, eq1, eq2) => {{
        const rawEq = eq1 !== undefined ? eq1 : eq2;
        mathList.push({{ type: 'display', eq: cleanKatexEquation(rawEq) }});
        return `\\n\\nKATEXDISPLAYSHIELD_${{mathList.length - 1}}_\\n\\n`;
      }});
      
      // Match inline math: \\(...\\) OR \\\\(...\\\\) OR $...$
      text = text.replace(/(?:(?:\\\\\\\\|\\\\)\\(([\\s\\S]*?)(?:\\\\\\\\|\\\\)\\)|(?<!\\\\)\\$(?!\\$)([^$\\n]+?)(?<!\\\\)\\$)/g, (_, eq1, eq2) => {{
        const rawEq = eq1 !== undefined ? eq1 : eq2;
        mathList.push({{ type: 'inline', eq: cleanKatexEquation(rawEq) }});
        return `KATEXINLINESHIELD_${{mathList.length - 1}}_`;
      }});

      // STEP 3: Restore protected code blocks
      codeList.forEach((codeStr, idx) => {{
        text = text.replace(`@@CODE_SHIELD_${{idx}}@@`, codeStr);
      }});
      
      // STEP 4: Parse Markdown with marked.js
      let html = marked.parse(text);
      
      // STEP 5: Re-inject and render KaTeX Math equations
      // Display Math
      html = html.replace(/(?:<p>\\s*)?KATEXDISPLAYSHIELD_(\\d+)_(?:\\s*<\\/p>)?/g, (_, idx) => {{
        const item = mathList[parseInt(idx, 10)];
        if (!item) return '';
        try {{
          return katex.renderToString(item.eq, {{
            displayMode: true,
            throwOnError: false,
            trust: true
          }});
        }} catch (err) {{
          console.warn("KaTeX Display Error:", err);
          return `<div class="katex-error text-rose-400 font-mono text-xs my-2 p-2 bg-rose-950/40 rounded border border-rose-800">$$${{item.eq}}$$</div>`;
        }}
      }});
      
      // Inline Math
      html = html.replace(/KATEXINLINESHIELD_(\\d+)_/g, (_, idx) => {{
        const item = mathList[parseInt(idx, 10)];
        if (!item) return '';
        try {{
          return katex.renderToString(item.eq, {{
            displayMode: false,
            throwOnError: false,
            trust: true
          }});
        }} catch (err) {{
          console.warn("KaTeX Inline Error:", err);
          return `<span class="katex-error text-rose-400 font-mono text-xs">$${{item.eq}}$</span>`;
        }}
      }});
      
      // STEP 6: Transform GitHub-style Alert Callouts (> [!NOTE], > [!TIP], > [!WARNING], > [!IMPORTANT])
      html = html.replace(/<blockquote>\\s*<p>\\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\\]([\\s\\S]*?)<\\/blockquote>/gi, (_, type, content) => {{
        const t = type.toUpperCase();
        let border = "border-blue-500/40 bg-blue-500/10 text-blue-200";
        let icon = "ℹ️";
        let label = "CATATAN";
        
        if (t === "TIP") {{
          border = "border-emerald-500/40 bg-emerald-500/10 text-emerald-200";
          icon = "💡";
          label = "TIPS";
        }} else if (t === "WARNING" || t === "CAUTION") {{
          border = "border-amber-500/40 bg-amber-500/10 text-amber-200";
          icon = "⚠️";
          label = "PERHATIAN";
        }} else if (t === "IMPORTANT") {{
          border = "border-purple-500/40 bg-purple-500/10 text-purple-200";
          icon = "📌";
          label = "PENTING";
        }}
        
        return `
          <div class="my-5 p-4 rounded-xl border ${{border}} text-xs sm:text-sm shadow-sm">
            <div class="font-bold flex items-center gap-1.5 mb-1.5 tracking-wider uppercase text-[11px]">
              <span>${{icon}}</span> ${{label}}
            </div>
            <div class="leading-relaxed opacity-95">${{content}}</div>
          </div>
        `;
      }});
      
      return html;
    }}

    // Markdown Modal Viewer (Instant Embedded + Fallback Fetch)
    const modal = document.getElementById('markdownModal');
    const modalDialog = document.getElementById('modalDialog');
    const modalTitle = document.getElementById('modalTitle');
    const modalSub = document.getElementById('modalSub');
    const modalBody = document.getElementById('modalBody');
    const modalToc = document.getElementById('modalToc');
    const modalGithubLink = document.getElementById('modalGithubLink');

    async function openMarkdownViewer(url, title, subtitle, githubUrl, backupUrl) {{
      modalTitle.textContent = title;
      modalSub.textContent = subtitle;
      modalGithubLink.href = githubUrl || '#';
      modalToc.classList.add('hidden');
      modalToc.innerHTML = '';
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';

      // 1. Get markdown from embedded registry (Instant & 100% CORS-proof!)
      let markdownText = getContentFromRegistry(url, backupUrl);

      // 2. Fallback to fetch only if not embedded (for external/new files)
      if (!markdownText) {{
        try {{
          let response = await fetch(url);
          if (!response.ok && backupUrl) {{
            response = await fetch(backupUrl);
          }}
          if (response.ok) {{
            markdownText = await response.text();
          }}
        }} catch (fetchErr) {{
          console.warn("Fetch fallback failed:", fetchErr);
        }}
      }}

      // 3. Render directly if markdown text is available
      if (markdownText) {{
        // Render Markdown with Bulletproof KaTeX
        modalBody.innerHTML = renderMarkdownContent(markdownText);
        
        // Render Mermaid Diagrams
        const mermaidNodes = [];
        modalBody.querySelectorAll('pre code.language-mermaid, pre code.lang-mermaid').forEach((codeEl) => {{
          const pre = codeEl.closest('pre');
          const diagramText = codeEl.textContent.trim();
          const container = document.createElement('div');
          container.className = 'mermaid my-6 p-4 rounded-2xl bg-slate-950/80 border border-slate-800 flex justify-center overflow-x-auto';
          container.textContent = diagramText;
          pre.parentNode.replaceChild(container, pre);
          mermaidNodes.push(container);
        }});
        
        if (mermaidNodes.length > 0) {{
          try {{
            await mermaid.run({{ nodes: mermaidNodes }});
          }} catch (mErr) {{
            console.warn("Mermaid execution error:", mErr);
          }}
        }}
        
        // Highlight Code Blocks
        modalBody.querySelectorAll('pre code:not(.language-mermaid)').forEach((block) => {{
          hljs.highlightElement(block);
        }});
        
        // Build Table of Contents Pills
        const headings = modalBody.querySelectorAll('h1, h2, h3');
        if (headings.length > 1) {{
          modalToc.innerHTML = '<span class="text-slate-400 font-semibold text-[11px] shrink-0 mr-1">Lompat ke:</span>';
          headings.forEach((h, idx) => {{
            const id = `heading-${{idx}}`;
            h.id = id;
            const text = h.textContent.replace(/^[0-9\\.\\s]+/, '').replace(/^🎯\\s*/, '').replace(/^🎓\\s*/, '').trim();
            if (text && text.length > 2) {{
              const pill = document.createElement('a');
              pill.href = `#${{id}}`;
              pill.className = 'shrink-0 px-2.5 py-1 rounded-md bg-slate-900 hover:bg-indigo-600 text-slate-300 hover:text-white border border-slate-800 transition text-[11px] font-medium';
              pill.textContent = text.length > 30 ? text.slice(0, 30) + '…' : text;
              pill.onclick = (e) => {{
                e.preventDefault();
                h.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
              }};
              modalToc.appendChild(pill);
            }}
          }});
          modalToc.classList.remove('hidden');
        }}
        
        modalBody.scrollTop = 0;
      }} else {{
        modalBody.innerHTML = `
          <div class="py-16 px-4 text-center max-w-md mx-auto">
            <div class="text-5xl mb-4">📄</div>
            <h4 class="font-bold text-lg text-white">Berkas Kajian Belum Tersedia</h4>
            <p class="text-xs text-slate-400 mt-2 leading-relaxed">
              Berkas kajian sedang disinkronkan ke dalam repositori lokal.
            </p>
            <div class="mt-6 flex flex-col gap-2.5">
              <a href="${{githubUrl}}" target="_blank" class="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg shadow-indigo-600/20 transition">
                🌐 Buka di GitHub (Tampilan Lengkap)
              </a>
            </div>
          </div>
        `;
      }}
    }}

    function closeModal() {{
      modal.classList.add('hidden');
      document.body.style.overflow = 'auto';
    }}

    function toggleFullscreenModal() {{
      isModalFullscreen = !isModalFullscreen;
      if (isModalFullscreen) {{
        modalDialog.className = 'bg-[#0b101b] border-none w-screen h-screen max-w-none max-h-none flex flex-col shadow-2xl overflow-hidden rounded-none';
      }} else {{
        modalDialog.className = 'bg-[#0b101b] border border-slate-800 rounded-2xl w-full max-w-4xl max-h-[92vh] flex flex-col shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150';
      }}
    }}

    function copyCurrentMarkdown() {{
      if (!currentRawMarkdown) return;
      navigator.clipboard.writeText(currentRawMarkdown).then(() => {{
        const copyBtnText = document.getElementById('copyBtnText');
        copyBtnText.textContent = 'Tersalin!';
        setTimeout(() => {{ copyBtnText.textContent = 'Salin'; }}, 2000);
      }}).catch(() => {{
        alert("Gagal menyalin otomatis, silakan salin manual.");
      }});
    }}

    modal.addEventListener('click', (e) => {{
      if (e.target === modal) {{
        closeModal();
      }}
    }});

    // Initial render
    renderCourses();
  </script>
</body>
</html>
"""

out_html = os.path.join(base_dir, "index.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_html} successfully ({len(html_content):,} bytes)!")
