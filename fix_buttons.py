import os

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Fix 'Contact Me' button in about.html (was bg-slate-900)
    # Let's make it the Accent color so it pops in both light and dark mode!
    content = content.replace('class="px-6 py-3 bg-slate-900 text-white font-medium rounded-xl hover:bg-gray-800 transition-colors shadow-sm"', 
                              'class="px-6 py-3 bg-accent text-white font-bold rounded-xl hover:opacity-90 transition-opacity shadow-md"')
    
    # Fix GitHub / LinkedIn buttons in about.html
    # Currently: bg-cardBg border border-borderColor text-primary hover:bg-bgColor
    # Change to: bg-bgColor text-primary border border-borderColor hover:opacity-80
    content = content.replace('class="px-6 py-3 bg-cardBg border border-borderColor text-primary font-medium rounded-xl hover:bg-bgColor transition-colors shadow-sm flex items-center gap-2"',
                              'class="px-6 py-3 bg-bgColor border border-borderColor text-primary font-medium rounded-xl hover:brightness-95 dark:hover:brightness-110 transition-all shadow-sm flex items-center gap-2"')

    # The contact card itself was set to bg-slate-900.
    # In dark mode, having a massive slate-900 block is fine, but maybe it should just be bg-cardBg?
    # No, it's a special highlighted section. Let's make it bg-slate-900 in light mode, and a rich Teal/Zinc gradient in dark mode!
    content = content.replace('class="bg-slate-900 text-white rounded-xl p-8 sm:p-12 shadow-md relative overflow-hidden mt-12"',
                              'class="bg-slate-900 dark:bg-zinc-900 border dark:border-zinc-800 text-white rounded-xl p-8 sm:p-12 shadow-md relative overflow-hidden mt-12"')

    # Fix project cards in projects/index.html and index.html
    # They are `bg-cardBg p-6 rounded-xl border border-borderColor shadow-sm hover:shadow-md transition-shadow`
    # This is fine. But what about the "View Project ->" text?
    # It's `text-accent`. In dark mode, teal-400 on zinc-800 is highly visible.
    
    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            update_file(os.path.join(root, file))
