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
  <meta name="description" content="Katalog 44 mata kuliah wajib dan 88 berkas kajian materi perkuliahan serta bank soal komprehensif S1 Informatika Universitas Diponegoro (Kurikulum 2020).">
  
  <!-- Favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎓</text></svg>">
  
  <!-- Tailwind CSS & Marked.js -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
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
    
    /* Markdown Modal Typography */
    .markdown-body h1 {{ font-size: 1.75rem; font-weight: 800; color: #f8fafc; margin-top: 1.5rem; margin-bottom: 0.75rem; border-bottom: 1px solid #334155; padding-bottom: 0.5rem; }}
    .markdown-body h2 {{ font-size: 1.35rem; font-weight: 700; color: #93c5fd; margin-top: 1.5rem; margin-bottom: 0.6rem; border-bottom: 1px solid #1e293b; padding-bottom: 0.3rem; }}
    .markdown-body h3 {{ font-size: 1.15rem; font-weight: 600; color: #cbd5e1; margin-top: 1.25rem; margin-bottom: 0.5rem; }}
    .markdown-body p {{ margin-bottom: 0.9rem; line-height: 1.65; color: #cbd5e1; }}
    .markdown-body ul, .markdown-body ol {{ padding-left: 1.5rem; margin-bottom: 1rem; color: #cbd5e1; }}
    .markdown-body ul {{ list-style-type: disc; }}
    .markdown-body ol {{ list-style-type: decimal; }}
    .markdown-body li {{ margin-bottom: 0.35rem; }}
    .markdown-body blockquote {{ border-left: 4px solid #6366f1; background: rgba(99, 102, 241, 0.08); padding: 0.75rem 1rem; border-radius: 0.5rem; margin: 1rem 0; color: #e2e8f0; }}
    .markdown-body code {{ font-family: 'JetBrains Mono', monospace; background: #1e293b; color: #f43f5e; padding: 0.15rem 0.4rem; border-radius: 0.3rem; font-size: 0.88em; }}
    .markdown-body pre {{ background: #0f172a; border: 1px solid #1e293b; padding: 1rem; border-radius: 0.75rem; overflow-x: auto; margin: 1rem 0; }}
    .markdown-body pre code {{ background: transparent; color: #e2e8f0; padding: 0; }}
    .markdown-body table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.88rem; }}
    .markdown-body th, .markdown-body td {{ border: 1px solid #334155; padding: 0.6rem 0.85rem; text-align: left; }}
    .markdown-body th {{ background: #1e293b; color: #f8fafc; font-weight: 600; }}
    .markdown-body tr:nth-child(even) {{ background: rgba(15, 23, 42, 0.5); }}
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
  <nav class="sticky top-0 z-40 backdrop-blur-xl bg-[#090d16]/80 border-b border-slate-800/80 transition-all">
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
      
      <div class="flex items-center gap-3">
        <a href="https://github.com/khairys/BelajarKompre/blob/main/llms.txt" target="_blank"
           class="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700/80 text-slate-300 hover:text-white transition">
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
  <header class="pt-12 pb-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto text-center md:text-left">
    <div class="flex flex-col md:flex-row items-center justify-between gap-8">
      <div class="max-w-3xl">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/25 text-emerald-400 text-xs font-semibold mb-4">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>Baseline Kurikulum 2020 • 100% Selesai & Terverifikasi</span>
        </div>
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-white leading-tight">
          Portal Belajar Komprehensif <br class="hidden sm:inline">
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-sky-300 to-emerald-400">
            S1 Informatika Undip
          </span>
        </h1>
        <p class="mt-4 text-slate-400 text-sm sm:text-base leading-relaxed max-w-2xl">
          Repositori mandiri 44 mata kuliah wajib lengkap Semester 1 s/d 8. Menyediakan rangkuman 14 pertemuan, peta konsep, bank soal ujian nyata (UTS/UAS), dan simulasi ujian lisan sidang komprehensif.
        </p>
      </div>

      <!-- Quick Metrics Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-2 gap-3 w-full md:w-80">
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-amber-400">{total_subjects}</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">Matkul Wajib</div>
        </div>
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-emerald-400">{total_rk_files}</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">Kajian Lengkap</div>
        </div>
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-blue-400">{total_raw_files}</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">Arsip Asli DMW</div>
        </div>
        <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-4 text-center backdrop-blur-sm">
          <div class="text-2xl font-black text-purple-400">100%</div>
          <div class="text-[11px] font-medium text-slate-400 mt-0.5">AI Ready</div>
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
             placeholder="Ketik untuk mencari mata kuliah, topik, atau kata kunci (contoh: Algoritma, SQL, Jaringan, AI)..." 
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
        <button data-sem="1" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 1 (8)
        </button>
        <button data-sem="2" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 2 (7)
        </button>
        <button data-sem="3" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 3 (6)
        </button>
        <button data-sem="4" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 4 (6)
        </button>
        <button data-sem="5" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 5 (7)
        </button>
        <button data-sem="6" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 6 (5)
        </button>
        <button data-sem="7" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 7 (3)
        </button>
        <button data-sem="8" class="sem-btn px-3.5 py-1.5 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 whitespace-nowrap transition">
          Sem 8 (2)
        </button>
      </div>

      <!-- Topic Pills Filter -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-none text-xs">
        <span class="text-slate-400 mr-1 hidden sm:inline whitespace-nowrap font-semibold">Bidang:</span>
        <button data-topic="all" class="topic-btn active px-3 py-1 rounded-lg bg-slate-800 text-slate-100 whitespace-nowrap border border-slate-700 font-medium transition">
          Semua Topik
        </button>
        {' '.join([f'<button data-topic="{t}" class="topic-btn px-3 py-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-400 border border-slate-800/80 whitespace-nowrap font-medium transition">{t}</button>' for t in sorted_topics])}
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
        <span class="inline-block w-2 h-2 rounded-full bg-indigo-400"></span> Klik judul untuk baca langsung
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

  <!-- Markdown Modal Viewer -->
  <div id="markdownModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden flex items-center justify-center p-3 sm:p-6 transition-opacity">
    <div class="bg-[#0b101b] border border-slate-800 rounded-2xl w-full max-w-4xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150">
      
      <!-- Modal Header -->
      <div class="px-5 py-4 border-b border-slate-800 flex items-center justify-between bg-slate-900/60">
        <div class="flex items-center gap-2.5 min-w-0 pr-4">
          <span id="modalIcon" class="text-xl">📖</span>
          <div class="min-w-0">
            <h2 id="modalTitle" class="text-base font-bold text-white truncate leading-snug">Judul Dokumen</h2>
            <p id="modalSub" class="text-xs text-slate-400 truncate">Semester & Topik</p>
          </div>
        </div>
        <div class="flex items-center gap-2 shrink-0">
          <a id="modalGithubLink" href="#" target="_blank"
             class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium border border-slate-700 transition" title="Buka berkas di GitHub">
            <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            <span class="hidden sm:inline">GitHub</span>
          </a>
          <button onclick="closeModal()" class="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition" title="Tutup (Esc)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
          </button>
        </div>
      </div>
      
      <!-- Modal Body (Markdown Container) -->
      <div id="modalBody" class="p-6 sm:p-8 overflow-y-auto markdown-body text-slate-200">
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
        Baseline Kurikulum 2020 (44 Matkul / 88 Kajian Komprehensif)
      </div>
    </div>
  </footer>

  <!-- Application Logic -->
  <script>
    const dataTree = {json.dumps(data_tree, ensure_ascii=False)};
    
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
    let searchQuery = '';

    const coursesGrid = document.getElementById('coursesGrid');
    const resultCount = document.getElementById('resultCount');
    const emptyState = document.getElementById('emptyState');
    const searchInput = document.getElementById('searchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');

    // Render Course Cards
    function renderCourses() {{
      const query = searchQuery.toLowerCase().trim();

      const filtered = allSubjects.filter(item => {{
        // Semester Filter
        if (currentSemester !== 'all' && item.semester_num.toString() !== currentSemester) {{
          return false;
        }}
        // Topic Filter
        if (currentTopic !== 'all' && item.topic !== currentTopic) {{
          return false;
        }}
        // Search Query
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
        renderCourses();
      }});
    }});

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

    // Markdown Modal Viewer
    const modal = document.getElementById('markdownModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalSub = document.getElementById('modalSub');
    const modalBody = document.getElementById('modalBody');
    const modalGithubLink = document.getElementById('modalGithubLink');

    async function openMarkdownViewer(url, title, subtitle, githubUrl) {{
      modalTitle.textContent = title;
      modalSub.textContent = subtitle;
      modalGithubLink.href = githubUrl;
      modalBody.innerHTML = `
        <div class="py-16 text-center text-slate-400 animate-pulse">
          <div class="text-3xl mb-2">⏳</div>
          <div class="text-sm font-medium">Memuat berkas kajian...</div>
        </div>
      `;
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';

      try {{
        const response = await fetch(url);
        if (!response.ok) throw new Error('Network response was not ok');
        const markdownText = await response.text();
        modalBody.innerHTML = marked.parse(markdownText);
      }} catch (err) {{
        modalBody.innerHTML = `
          <div class="py-12 px-4 text-center max-w-md mx-auto">
            <div class="text-4xl mb-3">📄</div>
            <h4 class="font-bold text-base text-white">Pratinjau Langsung Terkendala</h4>
            <p class="text-xs text-slate-400 mt-2 leading-relaxed">
              Jika Anda membuka berkas ini via protokol lokal (<code class="text-rose-400">file:///</code>), peramban membatasi permintaan fetch antar berkas karena keamanan CORS.
            </p>
            <div class="mt-5 flex flex-col gap-2">
              <a href="${{githubUrl}}" target="_blank" class="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold transition">
                🌐 Buka di GitHub (Tampilan Lengkap)
              </a>
              <a href="${{url}}" target="_blank" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition">
                📥 Buka Berkas Markdown Asli
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

print(f"Generated {out_html} successfully!")
