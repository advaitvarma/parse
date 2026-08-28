import re
import os

files = ['index.html', 'code.html', 'loading.html', 'stitch_loading.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the config block
    config_match = re.search(r'(<script id="tailwind-config">.*?</script>)', content, re.DOTALL)
    if not config_match:
        print(f"Config block not found in {filepath}")
        continue
        
    config_block = config_match.group(1)
    
    # Remove config block from its current position
    content = content.replace(config_block, '')
    
    # Find tailwind cdn script
    cdn_match = re.search(r'(<script src="https://cdn\.tailwindcss\.com.*?</script>)', content)
    if not cdn_match:
        print(f"CDN block not found in {filepath}")
        continue
        
    cdn_block = cdn_match.group(1)
    
    # Insert config block BEFORE cdn block
    content = content.replace(cdn_block, config_block + '\n    ' + cdn_block)
    
    with open(filepath, 'w') as f:
        f.write(content)
        print(f"Fixed order in {filepath}")

