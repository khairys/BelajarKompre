import json
import os
import re
import sys
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

base_dir = r"D:\Gathan\My Project\BelajarKompre"

with open(r"C:\Users\agath\.gemini\antigravity\brain\2b536463-8539-48b8-94a5-d4226c715bfe\scratch\planned_downloads.json", "r", encoding="utf-8") as f:
    planned_items = json.load(f)

with open(r"C:\Users\agath\.gemini\antigravity\plugin_data\gdrive\token.json", "r", encoding="utf-8") as f:
    token_data = json.load(f)

access_token = token_data['token']['access_token']
refresh_token = token_data['token']['refresh_token']
client_id = token_data.get('client_id')
client_secret = token_data.get('client_secret')

def refresh_token():
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
            return access_token
    except Exception as e:
        print("Token refresh error:", e)
        return access_token

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '_', name)
    return name.strip()

def download_one(item):
    f_info, (sem_folder, subj_folder, cat) = item
    dest_dir = os.path.join(base_dir, sem_folder, subj_folder, cat)
    os.makedirs(dest_dir, exist_ok=True)
    
    file_id = f_info['id']
    fname = sanitize_filename(f_info['name'])
    out_path = os.path.join(dest_dir, fname)
    
    # Skip if exists and not empty
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100:
        return ("ALREADY_EXISTS", fname, out_path)
    
    # Download URL
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&supportsAllDrives=true"
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {access_token}'})
    
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                content = resp.read()
                if len(content) == 0:
                    return ("ZERO_BYTE", fname, 0)
                with open(out_path, 'wb') as f_out:
                    f_out.write(content)
                return ("SUCCESS", fname, len(content))
        except urllib.error.HTTPError as e:
            if e.code == 401 and attempt == 0:
                new_tok = refresh_token()
                req = urllib.request.Request(url, headers={'Authorization': f'Bearer {new_tok}'})
                continue
            return (f"HTTP_{e.code}", fname, str(e.reason))
        except Exception as e:
            return ("ERROR", fname, str(e))

def run_sync(target_sem=None, max_workers=12):
    if target_sem and target_sem != "all":
        items = [p for p in planned_items if p[1][0] == target_sem]
    else:
        items = planned_items
        
    print(f"=== Starting High-Throughput Sync ({max_workers} Workers) ===")
    print(f"Target: {target_sem or 'ALL'} | Total Items: {len(items)}")
    
    downloaded = 0
    already_existed = 0
    errors = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_one, item): item for item in items}
        for future in as_completed(futures):
            status, fname, extra = future.result()
            if status == "SUCCESS":
                downloaded += 1
                if downloaded % 25 == 0 or downloaded == len(items):
                    print(f"  [+] Downloaded: {downloaded} files... (Latest: {fname[:40]} - {extra} bytes)")
            elif status == "ALREADY_EXISTS":
                already_existed += 1
            else:
                errors += 1
                
    print(f"\n=== SYNC SUMMARY ===")
    print(f"  Total Processed: {len(items)}")
    print(f"  Success Downloaded: {downloaded}")
    print(f"  Already Existed: {already_existed}")
    print(f"  Errors / Skipped: {errors}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    run_sync(target, max_workers=workers)
