import os
import shutil

CONTENT_DIR = 'content/1.beginner' # Focus on beginner for now as 30-days is structured this way

def fix_structure(dir_path):
    files = os.listdir(dir_path)
    md_files = [f for f in files if f.endswith('.md') and f != 'index.md']
    
    if len(md_files) == 1:
        # If there's exactly one other MD file, it's likely the content.
        src = os.path.join(dir_path, md_files[0])
        dst = os.path.join(dir_path, 'index.md')
        print(f"Renaming {md_files[0]} to index.md in {dir_path}")
        shutil.move(src, dst)

def main():
    for root, dirs, files in os.walk(CONTENT_DIR):
        fix_structure(root)

if __name__ == '__main__':
    main()
