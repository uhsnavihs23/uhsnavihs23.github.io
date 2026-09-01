import glob
import re

def clean_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove ALL Navbar blocks
    content = re.sub(r'\s*<!-- Navbar -->\s*<header.*?</header>\s*', '\n', content, flags=re.DOTALL)
    
    # Remove ALL Footer blocks
    content = re.sub(r'\s*<!-- Footer -->\s*<footer.*?</footer>\s*', '\n', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)

for filepath in glob.glob('./**/*.html', recursive=True):
    if 'ambient-noise' in filepath or 'budget-visualizer' in filepath or 'pomodoro-timer' in filepath or 'color-palette' in filepath or 'breathing-room' in filepath:
        continue # I manually built these correctly
    if filepath in ['./index.html', './about.html', './projects/index.html']:
        continue # these are handled cleanly by their own scripts
    
    clean_file(filepath)

print("Removed duplicates.")
