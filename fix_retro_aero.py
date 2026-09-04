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

new_retro_css = """
    /* GO RETRO BETA FEATURE (2010 IE8 / Windows 7 Aero Aesthetic) */
    html.retro body {
        font-family: "Segoe UI", Tahoma, Arial, sans-serif !important;
        background-color: #e8f1f8 !important; /* Windows 7 default background color */
        color: #333333 !important;
    }
    
    /* Aero Glass Header */
    html.retro header {
        background: linear-gradient(to bottom, #e3effa 0%, #c4ddf3 49%, #a5cbf0 50%, #cce0f5 100%) !important;
        border-bottom: 1px solid #7a9ebe !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.8) !important;
        border-radius: 0 0 6px 6px !important;
        backdrop-filter: blur(5px) !important;
    }
    html.retro header a, html.retro header span {
        color: #1e395b !important;
        text-shadow: 0 1px 0 rgba(255,255,255,0.8) !important;
    }
    html.retro header nav a {
        background: transparent !important;
        color: #1e395b !important;
        border: 1px solid transparent !important;
        padding: 4px 10px !important;
        border-radius: 4px !important;
        font-weight: normal !important;
    }
    html.retro header nav a:hover {
        background: linear-gradient(to bottom, #f3f8fd 0%, #e2effa 100%) !important;
        border: 1px solid #b8d6f2 !important;
        box-shadow: inset 0 0 2px #fff !important;
    }
    
    /* Content Area */
    html.retro main {
        background-color: #ffffff !important;
        border: 1px solid #aebac9 !important;
        border-radius: 5px !important;
        box-shadow: 0 0 8px rgba(0,0,0,0.1) !important;
        margin-top: 15px !important;
        padding: 20px !important;
    }
    
    html.retro h1, html.retro h2, html.retro h3, html.retro h4 {
        font-family: "Segoe UI", Tahoma, Arial, sans-serif !important;
        color: #003399 !important; /* Classic IE blue heading */
        font-weight: 600 !important;
        border-bottom: 1px solid #dce4ec !important;
        padding-bottom: 5px !important;
        margin-bottom: 15px !important;
    }
    
    html.retro a {
        color: #0066cc !important;
        text-decoration: none !important;
    }
    html.retro a:hover {
        text-decoration: underline !important;
    }
    
    /* Cards */
    html.retro .bg-cardBg, html.retro .bg-white, html.retro [style*="background-color: var(--card-bg)"] {
        background: linear-gradient(to bottom, #ffffff 0%, #f7f9fc 100%) !important;
        border: 1px solid #c5d2e0 !important;
        border-radius: 4px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
    }
    
    /* Buttons */
    html.retro button {
        background: linear-gradient(to bottom, #f2f6fb 0%, #dbe7f5 49%, #c4d8ed 50%, #dae7f5 100%) !important;
        border: 1px solid #8ca6c2 !important;
        border-radius: 3px !important;
        color: #1e395b !important;
        font-family: "Segoe UI", Tahoma, sans-serif !important;
        padding: 4px 12px !important;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.8), 0 1px 1px rgba(0,0,0,0.1) !important;
    }
    html.retro button:active {
        background: linear-gradient(to bottom, #c4d8ed 0%, #a5cbf0 100%) !important;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.2) !important;
    }
    
    /* The Retro Toggle Button itself */
    html.retro #retroToggle {
        background: linear-gradient(to bottom, #ff9999 0%, #cc0000 100%) !important;
        border: 1px solid #800000 !important;
        color: white !important;
        text-shadow: none !important;
        font-family: "Segoe UI", Tahoma, sans-serif !important;
        border-radius: 4px !important;
    }
    
    /* Ensure dark mode colors don't clash by heavily forcing text/bg inside retro */
    html.retro * {
        scrollbar-color: #c4d8ed #f0f4f9 !important;
    }
    
    /* Force specific text elements */
    html.retro p, html.retro span, html.retro div {
        color: inherit;
    }
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the old retro block and replace it up to </style>
    if '/* GO RETRO BETA FEATURE */' in content:
        content = re.sub(r'/\*\s*GO RETRO BETA FEATURE\s*\*/.*?(?=\s*</style>)', new_retro_css, content, flags=re.DOTALL)
        
        with open(filepath, 'w') as f:
            f.write(content)

print("Aero Retro CSS injected!")
