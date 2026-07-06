import os
import subprocess

videos = [
    {"id": "1-RrriiuYNUW5qDdDdiKBH8j_ldYsqV1H", "name": "sk_mashup"},
    {"id": "1-IE-qWcdHXnx9k-NTBakWcp-zc3Lpjzc", "name": "new_year_mashup"},
    {"id": "1PDpzrPgMVHCGg4iUAKpOUIO6H7zQ_nKH", "name": "bday_2025"},
    {"id": "1SPYn1eNklDo_OgwghK_JxhSdoycjmsvs", "name": "bday_2026"}
]

os.makedirs("public/videos", exist_ok=True)

for v in videos:
    raw_path = f"public/videos/{v['name']}_raw.mp4"
    out_path = f"public/videos/{v['name']}.webm"
    
    if not os.path.exists(out_path):
        print(f"Downloading {v['name']} from {v['id']}...")
        # use gdown as a module to handle large files and virus warnings automatically
        os.system(f'python -m gdown "{v["id"]}" -O "{raw_path}"')
        
        print(f"Compressing {v['name']}...")
        if os.path.exists(raw_path):
            # Compress to highly optimized muted 30-sec loop
            cmd = [
                "ffmpeg", "-y", "-i", raw_path, 
                "-c:v", "libvpx-vp9", "-crf", "35", "-b:v", "0", 
                "-vf", "scale=-2:720", "-an", "-t", "30",
                out_path
            ]
            subprocess.run(cmd)
            os.remove(raw_path)
            print(f"Done compressing {v['name']}")
        else:
            print(f"Failed to download {v['name']}")

print("All videos processed!")
