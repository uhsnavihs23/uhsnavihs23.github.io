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

taste_css = """
    /* --- TASTE SKILL ENHANCEMENTS --- */
    /* 1. Micro-interactions (Spring physics on click) */
    button, .btn, a.inline-flex, a.bg-accent, .group {
        transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease, box-shadow 0.2s ease !important;
    }
    button:active:not(:disabled), .btn:active, a.inline-flex:active, a.bg-accent:active {
        transform: scale(0.96) !important;
    }
    
    /* 2. Beautiful Focus Rings (Accessibility) */
    *:focus-visible {
        outline: none !important;
        box-shadow: 0 0 0 2px var(--bg-color), 0 0 0 4px var(--accent-color) !important;
        border-radius: inherit;
    }
    
    /* 3. Typography Polish (Balance & Kerning) */
    h1, h2, h3, h4 {
        text-wrap: balance !important;
        line-height: 1.15 !important;
        letter-spacing: -0.02em !important;
    }
    p {
        text-wrap: pretty !important;
    }
    
    /* 4. Elegant Text Selection */
    ::selection {
        background-color: rgba(0, 112, 243, 0.2) !important;
        color: inherit;
    }
    html.dark ::selection {
        background-color: rgba(50, 145, 255, 0.3) !important;
    }
    
    /* 5. Glassmorphism for sticky navigation */
    header {
        backdrop-filter: blur(12px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(12px) saturate(180%) !important;
    }
"""

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Inject right before the FIRST </style> tag to avoid duplication
    content = content.replace("</style>", taste_css + "\n</style>", 1)

    with open(filepath, 'w') as f:
        f.write(content)

print("Taste Skill globally injected properly!")
