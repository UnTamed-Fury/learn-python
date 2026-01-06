import os

CONTENT_DIR = 'content'

def generate_index(dir_path):
    rel_path = os.path.relpath(dir_path, CONTENT_DIR)
    if rel_path == '.':
        return # Skip root content dir

    items = sorted(os.listdir(dir_path))
    
    # Filter out index.md itself and hidden files
    items = [i for i in items if not i.startswith('.') and i != 'index.md']
    
    if not items:
        return

    title = os.path.basename(dir_path).replace('.', ' ').replace('_', ' ').title()
    
    content = f"# {title}\n\n"
    content += "## Contents\n\n"
    
    for item in items:
        # Nuxt Content links are usually relative to content root, but in markdown file relative links work too.
        # However, Nuxt Content parses filenames.
        name = os.path.splitext(item)[0].replace('_', ' ').title()
        
        # If item is a directory, link to it
        if os.path.isdir(os.path.join(dir_path, item)):
            content += f"- [{name}](./{item})\n"
        else:
             content += f"- [{name}](./{item})\n"
             
    with open(os.path.join(dir_path, 'index.md'), 'w') as f:
        f.write(content)
        print(f"Created index for {dir_path}")

def main():
    for root, dirs, files in os.walk(CONTENT_DIR):
        # Skip if index.md already exists (unless we want to overwrite, but let's be safe)
        # Actually, for the first run, let's create them if missing.
        if 'index.md' not in files:
            generate_index(root)
        else:
            # Check if it's empty or just basic? For now, skip.
            pass

if __name__ == '__main__':
    main()
