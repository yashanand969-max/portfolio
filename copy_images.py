import shutil
import os

brain_dir = os.path.join(os.environ['USERPROFILE'], '.gemini', 'antigravity', 'brain', 'e1c09027-fe2c-465b-b9a4-d13e84f05afe')

files = {
    'media__1778011147763.png': 'hero.png',
    'media__1778011147682.png': 'i4u-1.png',
    'media__1778011147725.png': 'i4u-2.png',
    'media__1778011147781.png': 'i4u-3.png'
}

for src, dst in files.items():
    src_path = os.path.join(brain_dir, src)
    if os.path.exists(src_path):
        shutil.copy(src_path, dst)
        print(f"Copied {src} to {dst}")
    else:
        print(f"Missing {src_path}")
