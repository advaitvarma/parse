import re

# code.html
with open('code.html', 'r') as f:
    content = f.read()

# 1. Update SVG
content = re.sub(
    r'<svg class="h-16 sm:h-20 w-auto text-primary" viewBox="0 0 1280 853"',
    r'<svg class="h-4 sm:h-5 w-auto text-primary" viewBox="295 335 608 168"',
    content
)

# 2. Update Refresh button size
content = re.sub(
    r'<span class="material-symbols-outlined text-\[16px\]">refresh</span>',
    r'<span class="material-symbols-outlined text-[14px]">refresh</span>',
    content
)

with open('code.html', 'w') as f:
    f.write(content)

# index.html
with open('index.html', 'r') as f:
    content = f.read()

# 1. Shadows and transitions for lines
content = re.sub(
    r'class="absolute top-\[11px\] left-\[12\.5%\] h-\[2px\] bg-primary rounded-full transition-all duration-300 ease-out"',
    r'class="absolute top-[11px] left-[12.5%] h-[2px] bg-primary rounded-full transition-all duration-500 ease-out shadow-lg shadow-primary/40"',
    content
)

content = re.sub(
    r'class="absolute left-\[10px\] top-\[11px\] w-\[2px\] bg-primary rounded-full transition-all duration-300 ease-out"',
    r'class="absolute left-[10px] top-[11px] w-[2px] bg-primary rounded-full transition-all duration-500 ease-out shadow-lg shadow-primary/40"',
    content
)

# 2. Section ID and scroll reveal
content = re.sub(
    r'<div class="w-full max-w-4xl mx-auto relative z-10 mb-2xl pt-xl">',
    r'<div id="try-it-section" class="w-full max-w-4xl mx-auto relative z-10 mb-2xl pt-2xl scroll-reveal">',
    content
)

# 3. Drop zone hover styles
content = content.replace(
    'bg-surface-variant/60 backdrop-blur-sm hover:border-primary/50 transition-all group"',
    'bg-surface-variant/60 backdrop-blur-sm hover:border-primary/60 hover:bg-primary/[0.02] transition-all group"'
)

content = content.replace(
    'bg-primary/8 flex items-center justify-center mb-md group-hover:bg-primary/15 transition-colors',
    'bg-primary/8 flex items-center justify-center mb-md group-hover:bg-primary/15 group-hover:scale-110 transition-all'
)

content = content.replace(
    'text-primary text-2xl">upload_file</span>',
    'text-primary text-2xl transition-transform group-hover:-translate-y-0.5">upload_file</span>'
)

content = content.replace(
    'class="text-primary font-medium">browse files</span>.',
    'class="text-primary font-medium underline underline-offset-2">browse files</span>.'
)

# 4. Job desc hover styles
content = content.replace(
    'bg-surface-variant/60 backdrop-blur-sm border border-outline-variant/40 p-lg hover:border-primary/30 transition-all"',
    'bg-surface-variant/60 backdrop-blur-sm border border-outline-variant/40 p-lg hover:border-primary/40 focus-within:border-primary focus-within:shadow-[0_0_0_2px_rgba(82,76,237,0.15)] transition-all"'
)

# 5. Active scale on button
content = content.replace(
    'hover:shadow-primary/30 hover:scale-[1.02] transition-all duration-300"',
    'hover:shadow-primary/30 hover:scale-[1.02] active:scale-[0.98] transition-all duration-300"'
)

# 6. JS Dropzone highlight
content = content.replace(
    "dropZone.classList.add('border-primary', 'bg-primary/5');",
    "dropZone.classList.add('border-primary', 'bg-primary/10', 'scale-[1.01]');"
)

content = content.replace(
    "dropZone.classList.remove('border-primary', 'bg-primary/5');",
    "dropZone.classList.remove('border-primary', 'bg-primary/10', 'scale-[1.01]');"
)

# 7. JS selected size
content = content.replace(
    '`<span class="text-primary font-medium">${file.name}</span> selected`;',
    '`<span class="text-primary font-semibold">${file.name}</span> selected (${Math.round(file.size / 1024)} KB)`;'
)

with open('index.html', 'w') as f:
    f.write(content)

print("Applied theirs")
