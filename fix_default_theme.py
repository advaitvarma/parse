import re
import os

files = ['index.html', 'code.html', 'loading.html', 'stitch_loading.html']
for filepath in files:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace the matchMedia logic
    old_line = "if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {"
    new_line = "if (savedTheme === 'dark') {"
    
    if old_line in content:
        content = content.replace(old_line, new_line)
        with open(filepath, 'w') as f:
            f.write(content)
            print(f"Updated {filepath}")
    else:
        print(f"Could not find exact line in {filepath}")

