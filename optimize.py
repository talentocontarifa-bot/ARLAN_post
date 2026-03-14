import os
import urllib.request
from PIL import Image

src_dir = r"C:\Users\rufin\OneDrive\Documentos\Talento_con_Tarifa\Trabajos\ARLAN\Arlan\selecion_IA"
dest_dir = r"c:\Users\rufin\.gemini\antigravity\playground\baryonic-einstein\ARLAN_post\public\recursos"
os.makedirs(dest_dir, exist_ok=True)

files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])[:8]

for i, f in enumerate(files):
    img_path = os.path.join(src_dir, f)
    img = Image.open(img_path)
    img.thumbnail((1920, 1920), Image.Resampling.LANCZOS)
    dest_path = os.path.join(dest_dir, f"fondo_{i+1}.jpg")
    if img.mode in ("RGBA", "P"): img = img.convert("RGB")
    img.save(dest_path, "JPEG", quality=80, optimize=True)
    print(f"Saved {dest_path}")

# Download Logo
logo_url = "https://firebasestorage.googleapis.com/v0/b/dreamcrafter-2946b.firebasestorage.app/o/logos%2FARLAN%2FARLAN_full_logo_1.svg?alt=media&token=b9fe1712-47c0-4165-858e-67eb226b681c"
logo_path = os.path.join(dest_dir, "ARLAN_full_logo_1.svg")
urllib.request.urlretrieve(logo_url, logo_path)
print("Logo downloaded")
