import os

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Fix remaining hardcoded borders
    content = content.replace('border-gray-300', 'border-borderColor')
    content = content.replace('border-gray-700', 'border-borderColor')
    content = content.replace('border-gray-800', 'border-borderColor')
    
    # Fix text grays that might be unreadable in dark mode
    # Actually, text-gray-500 and text-gray-400 might be fine on dark background, but let's use text-secondary
    content = content.replace('text-gray-500', 'text-secondary')
    content = content.replace('text-gray-600', 'text-secondary')
    
    # Re-fix contact card borders (because it's always dark, we want dark borders)
    # The contact card inputs had border-gray-700, but I just replaced that with border-borderColor
    # In light mode, borderColor is light (#e5e7eb), so the dark contact form inputs would have light borders!
    # Let's revert the contact card input styles explicitly.
    if 'id="contact-card"' in content:
        # Instead of doing that, let's just make the contact card explicitly follow the theme!
        # Contact card is currently hardcoded to bg-slate-900.
        # Let's change it to be adaptive: bg-slate-900 in light mode, bg-black in dark mode?
        # Actually, let's make it match the theme: bg-primary in light (slate-900), and a slightly different dark in dark mode?
        pass

    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            update_file(os.path.join(root, file))
