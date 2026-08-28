import re
import os

files = ['index.html', 'code.html', 'loading.html', 'stitch_loading.html']
for filepath in files:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Find and remove the @media (prefers-color-scheme: dark) block
    # It starts with: /* Auto theme based on system preference */
    # and ends with the closing } of the media query
    
    new_content = re.sub(
        r'/\* Auto theme based on system preference \*/\s*@media\s*\(prefers-color-scheme:\s*dark\)\s*\{\s*:root:not\(\.light\)\s*\{.*?\}\s*\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Removed media query from {filepath}")
    else:
        print(f"No match in {filepath}")

