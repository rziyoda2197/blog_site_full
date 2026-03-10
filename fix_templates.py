"""Fix remaining split template tags in Django templates."""
import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE, 'templates', 'blog')

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # Pattern 1: {{ variable_name\n                            }}  (closing }} on next line)
    content = re.sub(
        r'\{\{\s*([\w\.\|:\'\"\-]+)\s*\n\s*\}\}',
        r'{{ \1 }}',
        content
    )
    
    # Pattern 2: {{\n                    variable_name }}  (opening {{ on prev line)
    content = re.sub(
        r'\{\{\s*\n\s*([\w\.\|:\'\"\-]+)\s*\}\}',
        r'{{ \1 }}',
        content
    )

    # Fix pagination: %} <a href=  on same line as elif
    content = re.sub(
        r'(%\})\s*<a\s+href="([^"]+)"\s*\n\s*class="page-link">',
        r'\1\n                        <a href="\2" class="page-link">',
        content
    )
    
    # Fix extra indentation on endif/endfor
    content = re.sub(
        r'(\n)\s{28}(\{% endif %\})\s*\n\s{28}(\{% endfor %\})',
        r'\1                        \2\n                        \3',
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'FIXED: {os.path.basename(filepath)}')
    else:
        print(f'NO CHANGE: {os.path.basename(filepath)}')

for fname in ['home.html', 'post_list.html', 'category.html', 'tag.html', 'search.html']:
    fpath = os.path.join(TEMPLATES_DIR, fname)
    if os.path.exists(fpath):
        fix_file(fpath)

print('\n--- Final Verification ---')
for fname in ['home.html', 'post_list.html', 'tag.html', 'search.html']:
    fpath = os.path.join(TEMPLATES_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if 'category.name' in line:
            print(f'{fname}:{i}: {line.rstrip()}')
