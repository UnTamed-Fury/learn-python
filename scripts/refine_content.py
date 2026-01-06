import os
import json

CONTENT_DIR = 'content'

def convert_ipynb_to_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding JSON: {file_path}")
            return

    md_content = ""
    
    # Handle metadata if needed, but usually we just want cells
    cells = data.get('cells', [])
    
    for cell in cells:
        cell_type = cell.get('cell_type')
        source = cell.get('source', [])
        if isinstance(source, str):
            source = [source]
        
        text = "".join(source)
        
        if cell_type == 'markdown':
            md_content += f"{text}\n\n"
        elif cell_type == 'code':
            md_content += "```python\n"
            md_content += f"{text}\n"
            md_content += "```\n\n"
            
            # Optional: Include output? For docs, maybe not necessary or too complex to render images manually.
            # We skip outputs for cleaner text-based docs.

    # Save as .md
    new_path = file_path.replace('.ipynb', '.md')
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Converted: {file_path} -> {new_path}")
    # Remove original to clean up? Or keep it? Let's keep it but Nuxt ignores it.
    # Actually, let's remove it to avoid confusion in file tree if user looks there.
    # os.remove(file_path) 

def wrap_py_in_md(file_path):
    # Only wrap if a corresponding .md doesn't already exist (to avoid overwriting manual docs)
    # But for this repo, the .py files are the content in "Advance" section.
    
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    name_no_ext = os.path.splitext(base_name)[0]
    new_md_path = os.path.join(dir_name, f"{name_no_ext}.md")
    
    # Skip if __init__.py
    if base_name == "__init__.py":
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    md_content = f"# {name_no_ext.replace('_', ' ').title()}\n\n"
    md_content += f"Source: `{base_name}`\n\n"
    md_content += "```python\n"
    md_content += code
    md_content += "\n```\n"

    with open(new_md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Wrapped: {file_path} -> {new_md_path}")

def main():
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            
            if file.endswith('.ipynb'):
                convert_ipynb_to_md(file_path)
            
            elif file.endswith('.py'):
                # We check if this .py file is inside a "content" structure that needs wrapping
                # avoiding scripts/ or app/ which are not in CONTENT_DIR
                wrap_py_in_md(file_path)

if __name__ == '__main__':
    main()
