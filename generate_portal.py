import os
import json

base_dir = r"D:\Gathan\My Project\BelajarKompre"
rangkuman_base = os.path.join(base_dir, "RANGKUMAN_DAN_CONTOH_SOAL")

sem_dirs = sorted([d for d in os.listdir(base_dir) if d.startswith("0") and os.path.isdir(os.path.join(base_dir, d))])

data_tree = []
total_raw_materi = 0
total_raw_soal = 0
total_rk_materi = 0
total_rk_soal = 0
total_subjects = 0

for sem in sem_dirs:
    sem_path = os.path.join(base_dir, sem)
    subjs = sorted([s for s in os.listdir(sem_path) if os.path.isdir(os.path.join(sem_path, s))])
    
    sem_obj = {
        "semester": sem,
        "name": sem.replace("_", " ").title(),
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
        
        # Check rangkuman
        rk_subj_path = os.path.join(rangkuman_base, sem, subj)
        rel_rk_materi = f"RANGKUMAN_DAN_CONTOH_SOAL/{sem}/{subj}/RANGKUMAN_MATERI.md"
        rel_rk_soal = f"RANGKUMAN_DAN_CONTOH_SOAL/{sem}/{subj}/CONTOH_SOAL_DAN_PEMBAHASAN.md"
        
        has_rk_m = os.path.exists(os.path.join(rk_subj_path, "RANGKUMAN_MATERI.md"))
        has_rk_s = os.path.exists(os.path.join(rk_subj_path, "CONTOH_SOAL_DAN_PEMBAHASAN.md"))
        
        if has_rk_m: total_rk_materi += 1
        if has_rk_s: total_rk_soal += 1
        
        sem_obj["subjects"].append({
            "name": subj.replace("_", " "),
            "folder": subj,
            "materi_count": len(materi_files),
            "soal_count": len(soal_files),
            "materi_files": materi_files,
            "soal_files": soal_files,
            "has_rk_materi": has_rk_m,
            "has_rk_soal": has_rk_s,
            "url_rk_materi": rel_rk_materi,
            "url_rk_soal": rel_rk_soal
        })
    data_tree.append(sem_obj)

total_raw_files = total_raw_materi + total_raw_soal
total_rk_files = total_rk_materi + total_rk_soal

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portal Belajar Komprehensif S1 Informatika Undip</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    .badge {{ font-size: 0.72rem; padding: 2px 8px; border-radius: 9999px; }}
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: #0f172a; }}
    ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #475569; }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen">
  <div class="max-w-7xl mx-auto px-4 py-8">
    <!-- Header -->
    <header class="mb-8 border-b border-slate-800 pb-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold mb-2">
          <span>🎓 Kurikulum 2020 Baseline</span> • <span>DMW Informatika Undip</span> • <span class="text-white">Status: 100% Tuntas</span>
        </div>
        <h1 class="text-3xl font-extrabold tracking-tight text-white flex items-center gap-3">
          <span>Portal Belajar Komprehensif</span>
          <span class="text-sm px-2.5 py-0.5 rounded-lg bg-blue-500/20 text-blue-400 border border-blue-500/30 font-medium">S1 Informatika</span>
        </h1>
        <p class="text-slate-400 text-sm mt-1">Repositori materi perkuliahan lengkap, rangkuman 14 pertemuan, dan bank contoh soal ujian komprehensif Semester 1 s/d 8</p>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3 w-full md:w-auto">
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 text-center">
          <div class="text-xs text-slate-400 font-medium">Mata Kuliah</div>
          <div class="text-xl font-bold text-amber-400">{total_subjects} Wajib</div>
        </div>
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 text-center">
          <div class="text-xs text-slate-400 font-medium">Rangkuman & Soal</div>
          <div class="text-xl font-bold text-emerald-400">{total_rk_files} Berkas (100%)</div>
        </div>
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 text-center">
          <div class="text-xs text-slate-400 font-medium">Arsip Mentah DMW</div>
          <div class="text-xl font-bold text-blue-400">{total_raw_files} Berkas</div>
        </div>
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 text-center">
          <div class="text-xs text-slate-400 font-medium">Total Kapasitas</div>
          <div class="text-xl font-bold text-purple-400">~2,85 GB</div>
        </div>
      </div>
    </header>

    <!-- Controls -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      <div class="md:col-span-2 relative">
        <input id="searchInput" type="text" placeholder="🔍 Cari nama mata kuliah, topik, atau kata kunci..." 
               class="w-full bg-slate-900/80 border border-slate-800 rounded-xl px-4 py-3 pl-11 text-sm focus:outline-none focus:border-blue-500 text-white placeholder-slate-500 transition">
        <span class="absolute left-4 top-3.5 text-slate-500">🔍</span>
      </div>
      <div>
        <select id="semesterFilter" class="w-full bg-slate-900/80 border border-slate-800 rounded-xl px-4 py-3 text-sm focus:outline-none focus:border-blue-500 text-white transition">
          <option value="all">Semua Semester (1 s/d 8)</option>
          <option value="01_Semester_1">Semester 1 (8 Mata Kuliah)</option>
          <option value="02_Semester_2">Semester 2 (7 Mata Kuliah)</option>
          <option value="03_Semester_3">Semester 3 (6 Mata Kuliah)</option>
          <option value="04_Semester_4">Semester 4 (6 Mata Kuliah)</option>
          <option value="05_Semester_5">Semester 5 (7 Mata Kuliah)</option>
          <option value="06_Semester_6">Semester 6 (5 Mata Kuliah)</option>
          <option value="07_Semester_7">Semester 7 (3 Mata Kuliah)</option>
          <option value="08_Semester_8">Semester 8 (2 Mata Kuliah: KKN & Tugas Akhir)</option>
        </select>
      </div>
    </div>

    <!-- Container -->
    <div id="contentGrid" class="space-y-8"></div>
  </div>

  <script>
    const data = {json.dumps(data_tree, ensure_ascii=False)};
    const container = document.getElementById('contentGrid');
    const searchInput = document.getElementById('searchInput');
    const semesterFilter = document.getElementById('semesterFilter');

    function render() {{
      const query = searchInput.value.toLowerCase().trim();
      const semFilter = semesterFilter.value;
      container.innerHTML = '';

      let matchedSemesters = 0;

      data.forEach(sem => {{
        if (semFilter !== 'all' && sem.semester !== semFilter) return;

        const filteredSubjs = sem.subjects.filter(subj => {{
          if (!query) return true;
          if (subj.name.toLowerCase().includes(query)) return true;
          if (subj.materi_files.some(f => f.toLowerCase().includes(query))) return true;
          if (subj.soal_files.some(f => f.toLowerCase().includes(query))) return true;
          return false;
        }});

        if (filteredSubjs.length === 0) return;
        matchedSemesters++;

        const semCard = document.createElement('div');
        semCard.className = 'bg-slate-900/50 border border-slate-800/80 rounded-2xl p-6';

        let subjsHtml = filteredSubjs.map((s, idx) => `
          <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-5 transition hover:border-slate-700 shadow-sm">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 mb-4">
              <div>
                <h3 class="font-bold text-lg text-white flex items-center gap-2">
                  <span>📘</span> ${{s.name}}
                </h3>
                <div class="flex items-center gap-2 mt-1">
                  <span class="badge bg-slate-800 text-slate-300 font-mono text-[10px]">${{s.folder}}</span>
                </div>
              </div>
              
              <!-- Quick Access Action Buttons -->
              <div class="flex flex-wrap items-center gap-2">
                <a href="${{s.url_rk_materi}}" target="_blank" 
                   class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 text-xs font-semibold transition">
                  <span>📖</span> Rangkuman Materi
                </a>
                <a href="${{s.url_rk_soal}}" target="_blank" 
                   class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 text-amber-400 text-xs font-semibold transition">
                  <span>📝</span> Contoh Soal & Kompre
                </a>
              </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs mt-3 pt-4 border-t border-slate-800/80">
              <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800/60">
                <div class="font-semibold text-amber-400 mb-2 flex items-center justify-between">
                  <span>📂 Bank Soal Arsip DMW (${{s.soal_count}} berkas)</span>
                  <span class="badge bg-amber-500/10 border border-amber-500/20 text-amber-400">${{s.soal_count}}</span>
                </div>
                <div class="max-h-28 overflow-y-auto pr-1 space-y-1">
                  ${{s.soal_files.length ? s.soal_files.map(f => `<div class="p-1.5 rounded bg-slate-950 border border-slate-800/70 text-slate-300 truncate font-mono text-[11px]" title="${{f}}">📄 ${{f}}</div>`).join('') : '<span class="text-slate-500 italic">Tidak ada berkas tertulis (Proyek/Riset Mandiri)</span>'}}
                </div>
              </div>
              <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800/60">
                <div class="font-semibold text-blue-400 mb-2 flex items-center justify-between">
                  <span>📚 Slide & Modul Arsip DMW (${{s.materi_count}} berkas)</span>
                  <span class="badge bg-blue-500/10 border border-blue-500/20 text-blue-400">${{s.materi_count}}</span>
                </div>
                <div class="max-h-28 overflow-y-auto pr-1 space-y-1">
                  ${{s.materi_files.length ? s.materi_files.map(f => `<div class="p-1.5 rounded bg-slate-950 border border-slate-800/70 text-slate-300 truncate font-mono text-[11px]" title="${{f}}">📑 ${{f}}</div>`).join('') : '<span class="text-slate-500 italic">Tidak ada berkas tertulis (Proyek/Riset Mandiri)</span>'}}
                </div>
              </div>
            </div>
          </div>
        `).join('');

        semCard.innerHTML = `
          <div class="flex items-center justify-between mb-4 border-b border-slate-800 pb-3">
            <h2 class="text-xl font-bold text-blue-300 flex items-center gap-2">
              <span>📁</span> ${{sem.name}}
            </h2>
            <div class="flex items-center gap-2">
              <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800 text-slate-300">
                ${{filteredSubjs.length}} Mata Kuliah
              </span>
              <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400">
                ✅ Rangkuman 100%
              </span>
            </div>
          </div>
          <div class="grid grid-cols-1 gap-4">
            ${{subjsHtml}}
          </div>
        `;
        container.appendChild(semCard);
      }});

      if (matchedSemesters === 0) {{
        container.innerHTML = `
          <div class="text-center py-16 bg-slate-900/30 border border-slate-800 rounded-2xl">
            <div class="text-4xl mb-3">🔍</div>
            <h3 class="text-lg font-bold text-slate-300">Tidak ada mata kuliah atau berkas yang cocok</h3>
            <p class="text-sm text-slate-500 mt-1">Coba gunakan kata kunci pencarian yang lain.</p>
          </div>
        `;
      }}
    }}

    searchInput.addEventListener('input', render);
    semesterFilter.addEventListener('change', render);
    render();
  </script>
</body>
</html>
"""

out_html = os.path.join(base_dir, "index.html")
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_html} successfully!")
