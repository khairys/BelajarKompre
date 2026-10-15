import json
import os
import re
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

base_dir = r"D:\Gathan\My Project\BelajarKompre"

with open(os.path.join(base_dir, "katalog_dmw.json"), "r", encoding="utf-8") as f:
    dmw_data = json.load(f)

with open(r"C:\Users\agath\.gemini\antigravity\plugin_data\gdrive\token.json", "r", encoding="utf-8") as f:
    token_data = json.load(f)

access_token = token_data['token']['access_token']
refresh_token = token_data['token']['refresh_token']
client_id = token_data.get('client_id')
client_secret = token_data.get('client_secret')

def refresh_access_token():
    global access_token
    url = "https://oauth2.googleapis.com/token"
    data = urllib.parse.urlencode({
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            access_token = res['access_token']
            print("Access token refreshed successfully.")
            return access_token
    except Exception as e:
        print("Error refreshing token:", e)
        return access_token

# Mapping from DMW matkul name -> (semester_folder, subject_folder)
mapping = {
    # Semester 1
    "dasar sistem": ("01_Semester_1", "Dasar_Sistem"),
    "dasar pemrograman": ("01_Semester_1", "Dasar_Pemrograman"),
    "struktur diskret": ("01_Semester_1", "Struktur_Diskrit"),
    "struktur diskrit": ("01_Semester_1", "Struktur_Diskrit"),
    "matematika i": ("01_Semester_1", "Matematika_I"),
    "logika informatika": ("01_Semester_1", "Logika_Informatika"),
    "pancasila": ("01_Semester_1", "Pancasila_dan_Kewarganegaraan"),
    "kewarganegaraan": ("01_Semester_1", "Pancasila_dan_Kewarganegaraan"),
    "bahasa inggris i": ("01_Semester_1", "Bahasa_Inggris"),
    "bahasa inggris ii": ("01_Semester_1", "Bahasa_Inggris"),
    "bahasa inggris iii": ("01_Semester_1", "Bahasa_Inggris"),
    "bahasa inggris": ("01_Semester_1", "Bahasa_Inggris"),
    
    # Semester 2
    "organisasi dan arsitektur komputer": ("02_Semester_2", "Organisasi_dan_Arsitektur_Komputer"),
    "algoritma dan pemrograman": ("02_Semester_2", "Algoritma_dan_Pemrograman"),
    "bahasa indonesia": ("02_Semester_2", "Bahasa_Indonesia"),
    "internet of things": ("02_Semester_2", "Internet_of_Things"),
    "matematika ii": ("02_Semester_2", "Matematika_II"),
    "aljabar linier": ("02_Semester_2", "Aljabar_Linier"),
    "aljabar linear": ("02_Semester_2", "Aljabar_Linier"),
    
    # Semester 3
    "sistem operasi": ("03_Semester_3", "Sistem_Operasi"),
    "struktur data": ("03_Semester_3", "Struktur_Data"),
    "interaksi manusia komputer": ("03_Semester_3", "Interaksi_Manusia_Komputer"),
    "interaksi manusia-komputer": ("03_Semester_3", "Interaksi_Manusia_Komputer"),
    "basis data": ("03_Semester_3", "Basis_Data"),
    "metode numerik": ("03_Semester_3", "Metode_Numerik"),
    "statistika": ("03_Semester_3", "Statistika"),
    
    # Semester 4
    "jaringan komputer": ("04_Semester_4", "Jaringan_Komputer"),
    "pemrograman berorientasi objek": ("04_Semester_4", "Pemrograman_Berorientasi_Objek"),
    "rekayasa perangkat lunak": ("04_Semester_4", "Rekayasa_Perangkat_Lunak"),
    "manajemen basis data": ("04_Semester_4", "Manajemen_Basis_Data"),
    "grafik dan teknik interaktif": ("04_Semester_4", "Grafika_dan_Komputasi_Visual"),
    "grafika dan komputasi visual": ("04_Semester_4", "Grafika_dan_Komputasi_Visual"),
    "kecerdasan buatan": ("04_Semester_4", "Sistem_Cerdas"),
    "sistem cerdas": ("04_Semester_4", "Sistem_Cerdas"),
    
    # Semester 5
    "komputasi tersebar dan paralel": ("05_Semester_5", "Komputasi_Tersebar_dan_Paralel"),
    "pengembangan platform khusus": ("05_Semester_5", "Pengembangan_Berbasis_Platform"),
    "pengembangan berbasis platform": ("05_Semester_5", "Pengembangan_Berbasis_Platform"),
    "proyek perangkat lunak": ("05_Semester_5", "Proyek_Perangkat_Lunak"),
    "sistem informasi": ("05_Semester_5", "Sistem_Informasi"),
    "keamanan dan jaminan informasi": ("05_Semester_5", "Keamanan_dan_Jaminan_Informasi"),
    "pembelajaran mesin": ("05_Semester_5", "Pembelajaran_Mesin"),
    "kewirausahaan": ("05_Semester_5", "Kewirausahaan"),
    
    # Semester 6
    "praktik kerja lapangan": ("06_Semester_6", "Praktik_Kerja_Lapangan"),
    "analisis dan strategi algoritma": ("06_Semester_6", "Analisis_dan_Strategi_Algoritma"),
    "uji perangkat lunak": ("06_Semester_6", "Uji_Perangkat_Lunak"),
    "manajemen proyek": ("06_Semester_6", "Manajemen_Proyek"),
    "masyarakat dan etika profesi": ("06_Semester_6", "Masyarakat_dan_Etika_Profesi"),
    
    # Semester 7
    "metodologi dan penulisan ilmiah": ("07_Semester_7", "Metodologi_dan_Penulisan_Ilmiah"),
    "teori bahasa dan otomata": ("07_Semester_7", "Teori_Bahasa_dan_Otomata"),
    "penambangan data": ("07_Semester_7", "Penambangan_Data"),
    
    # Semester 8
    "tugas akhir": ("08_Semester_8", "Tugas_Akhir"),
    "kuliah kerja nyata": ("08_Semester_8", "Kuliah_Kerja_Nyata")
}

def extract_file_id(url):
    m = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    if m:
        return m.group(1)
    m = re.search(r'id=([a-zA-Z0-9_-]+)', url)
    if m:
        return m.group(1)
    return None

def sanitize_filename(name):
    # Remove invalid Windows characters
    name = re.sub(r'[\\/*?:"<>|]', '_', name)
    name = name.strip()
    if len(name) > 120:
        name = name[:120]
    return name

def download_file(item, category, target_semester_filter=None):
    # category: 'soal', 'pembahasan', 'modul'
    matkul_info = item.get('matkul', {})
    matkul_name = matkul_info.get('nama', '').lower().strip()
    
    if matkul_name not in mapping:
        return ("SKIPPED_UNMAPPED", matkul_name, None)
    
    sem_folder, subj_folder = mapping[matkul_name]
    
    if target_semester_filter and sem_folder != target_semester_filter:
        return ("SKIPPED_FILTER", matkul_name, None)
    
    sub_dir = "bank_soal" if category in ['soal', 'pembahasan'] else "materi"
    dest_dir = os.path.join(base_dir, sem_folder, subj_folder, sub_dir)
    os.makedirs(dest_dir, exist_ok=True)
    
    url = item.get('url', '')
    file_id = extract_file_id(url)
    if not file_id:
        return ("NO_FILE_ID", url, None)
    
    # Determine title
    if category == 'soal':
        title = item.get('judulSoal', f"Soal_{item.get('tipe', 'UTS')}_{item.get('tahun', '')}")
    elif category == 'pembahasan':
        title = item.get('judulPembahasan', f"Pembahasan_{item.get('tipe', 'UTS')}_{item.get('tahun', '')}")
    else:
        title = item.get('judulModul', 'Modul_Materi')
    
    title = sanitize_filename(title)
    if not any(title.lower().endswith(ext) for ext in ['.pdf', '.docx', '.doc', '.pptx', '.ppt', '.xlsx', '.xls', '.ipynb', '.zip']):
        title += ".pdf"
        
    out_path = os.path.join(dest_dir, title)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
        return ("ALREADY_EXISTS", title, out_path)
    
    # Download
    download_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&supportsAllDrives=true"
    req = urllib.request.Request(download_url, headers={'Authorization': f'Bearer {access_token}'})
    
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                content = resp.read()
                with open(out_path, 'wb') as f_out:
                    f_out.write(content)
                return ("SUCCESS", title, len(content))
        except urllib.error.HTTPError as e:
            if e.code == 401 and attempt == 0:
                new_tok = refresh_access_token()
                req = urllib.request.Request(download_url, headers={'Authorization': f'Bearer {new_tok}'})
                continue
            elif e.code == 403:
                # Might be restricted or Google Doc requiring export
                return (f"HTTP_{e.code}", title, str(e.reason))
            else:
                return (f"HTTP_{e.code}", title, str(e.reason))
        except Exception as e:
            return ("ERROR", title, str(e))

def run_download_batch(semester_filter=None, max_workers=6):
    tasks = []
    for s in dmw_data['soals']:
        tasks.append((s, 'soal'))
    for p in dmw_data['pembahasans']:
        tasks.append((p, 'pembahasan'))
    for m in dmw_data['moduls']:
        tasks.append((m, 'modul'))
        
    print(f"Total tasks available: {len(tasks)}")
    
    downloaded = 0
    already_existed = 0
    skipped = 0
    errors = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_file, item, cat, semester_filter): (item, cat) for item, cat in tasks}
        for future in as_completed(futures):
            res, title, extra = future.result()
            if res == "SUCCESS":
                downloaded += 1
                if downloaded % 10 == 0:
                    print(f"  [+] Downloaded: {downloaded} files... (Latest: {title} - {extra} bytes)")
            elif res == "ALREADY_EXISTS":
                already_existed += 1
            elif res.startswith("SKIPPED"):
                skipped += 1
            else:
                errors += 1
                print(f"  [!] Failed ({res}): {title} - {extra}")
                
    print(f"\n--- BATCH SUMMARY ({semester_filter or 'ALL'}) ---")
    print(f"  Downloaded: {downloaded}")
    print(f"  Already existed: {already_existed}")
    print(f"  Skipped (filter/unmapped): {skipped}")
    print(f"  Errors/Restricted: {errors}")

if __name__ == "__main__":
    import sys
    sem = sys.argv[1] if len(sys.argv) > 1 else None
    run_download_batch(sem, max_workers=6)
