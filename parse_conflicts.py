import re

files = ['code.html', 'index.html']
for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Split by lines
    lines = content.split('\n')
    conflicts = []
    current_conflict = None
    state = 0
    
    for i, line in enumerate(lines):
        if line.startswith('<<<<<<< HEAD'):
            current_conflict = {'start': i, 'ours': [], 'theirs': [], 'end': -1}
            state = 1
        elif line.startswith('======='):
            state = 2
        elif line.startswith('>>>>>>>'):
            current_conflict['end'] = i
            conflicts.append(current_conflict)
            state = 0
        else:
            if state == 1:
                current_conflict['ours'].append(line)
            elif state == 2:
                current_conflict['theirs'].append(line)
                
    print(f"\n--- Conflicts in {filepath} ({len(conflicts)}) ---")
    for i, c in enumerate(conflicts):
        print(f"\nConflict {i+1}:")
        print("OURS:\n" + "\n".join(c['ours']))
        print("THEIRS:\n" + "\n".join(c['theirs']))
