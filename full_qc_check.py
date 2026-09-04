import os
import re

base_path = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo"
html_files = []
for root, dirs, files in os.walk(base_path):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

issues = []
print(f"Starting QC on {len(html_files)} HTML files...")

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
        
    rel_path = os.path.relpath(filepath, base_path)
    
    with open(filepath, 'r') as f:
        content = f.read()
        
    # 1. Dark Mode is forbidden in Retro
    if "html.classList.contains('dark')" not in content or "window.setTheme(false)" not in content:
        issues.append(f"{rel_path}: Dark Mode strict disable logic missing in Retro JS.")
        
    # 2. Absolute Paths in IE Nav
    if "href=\"/projects/index.html\"" not in content:
        issues.append(f"{rel_path}: Missing absolute path /projects/index.html in Retro nav.")
        
    # 3. GoatCounter tracking pixel
    if "23022000.goatcounter.com" not in content:
        issues.append(f"{rel_path}: Missing GoatCounter script.")
        
    # 4. Retro Toggle Button
    if "retroToggle" not in content:
        issues.append(f"{rel_path}: Missing retroToggle button.")
        
    # 5. Contact Card Override
    if "html.retro #contact-card" not in content:
        issues.append(f"{rel_path}: Missing Contact Card light-theme CSS override.")
        
    # 6. Unicode Arrows
    if "&larr;" not in content or "&rarr;" not in content:
        issues.append(f"{rel_path}: Missing standard HTML arrows (&larr; / &rarr;) in IE chrome.")
        
if len(issues) == 0:
    print("QC PASSED: 100% consistency verified across all files.")
else:
    print("QC FAILED: Found the following issues:")
    for issue in issues:
        print(f" - {issue}")
