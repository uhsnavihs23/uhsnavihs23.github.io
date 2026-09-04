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

xp_retro_css = """
    /* GO RETRO BETA FEATURE (2005 Windows XP / Internet Explorer 6 Aesthetic) */
    html.retro body {
        font-family: Tahoma, "Microsoft Sans Serif", sans-serif !important;
        background-color: #004e98 !important; /* XP Desktop Blue */
        color: #000000 !important;
        padding: 2% !important; /* Give desktop space */
    }
    
    /* Browser Window Chrome */
    html.retro header {
        background: linear-gradient(to bottom, #0058e6 0%, #3a93ff 100%) !important;
        border: 1px solid #00138c !important;
        border-radius: 8px 8px 0 0 !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5) !important;
        padding: 0 !important;
        display: block !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
        backdrop-filter: none !important;
    }
    
    html.retro header > div {
        display: block !important;
        padding: 0 !important;
        height: auto !important;
    }
    
    /* Title Bar Text (Site Name) */
    html.retro header a.text-xl {
        color: #ffffff !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 2px #00138c !important;
        font-size: 13px !important;
        font-family: "Trebuchet MS", sans-serif !important;
        display: block !important;
        padding: 4px 10px !important;
    }
    
    /* IE6 Toolbar (Menu Bar) */
    html.retro header nav {
        background-color: #ece9d8 !important; /* XP Luna Window Color */
        border-top: 1px solid #ffffff !important;
        border-bottom: 1px solid #aca899 !important;
        padding: 4px 8px !important;
        display: flex !important;
        gap: 2px !important;
        align-items: center !important;
    }
    
    html.retro header nav a {
        background: transparent !important;
        color: #000000 !important;
        border: 1px solid transparent !important;
        border-radius: 0 !important;
        font-size: 12px !important;
        padding: 3px 8px !important;
        font-family: Tahoma, sans-serif !important;
        text-shadow: none !important;
        margin: 0 !important;
    }
    
    html.retro header nav a:hover {
        border-color: #316ac5 !important;
        background-color: #c1d2ee !important;
        box-shadow: none !important;
    }
    
    /* Main Content (The "Webpage") */
    html.retro main {
        background-color: #ffffff !important;
        border: 3px inset #d4d0c8 !important;
        border-top: none !important;
        border-radius: 0 !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5) !important;
        margin: 0 auto !important;
        max-width: 1200px !important;
        padding: 20px !important;
        min-height: 80vh !important;
    }
    
    /* Headings */
    html.retro h1, html.retro h2, html.retro h3, html.retro h4 {
        font-family: "Times New Roman", Times, serif !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-bottom: none !important;
    }
    
    html.retro p, html.retro span, html.retro div {
        color: inherit;
    }
    
    html.retro a {
        color: #0000EE !important;
        text-decoration: underline !important;
    }
    html.retro a:hover {
        color: #FF0000 !important; /* Classic IE hover color */
    }
    
    /* Cards and Elements inside */
    html.retro .bg-cardBg, html.retro .bg-white, html.retro [style*="background-color: var(--card-bg)"] {
        background: #ffffff !important;
        border: 1px solid #000000 !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }
    
    /* Buttons */
    html.retro button {
        background: #ece9d8 !important;
        border: 2px outset #ffffff !important;
        border-right-color: #aca899 !important;
        border-bottom-color: #aca899 !important;
        border-radius: 0 !important;
        color: #000000 !important;
        font-family: Tahoma, sans-serif !important;
        padding: 2px 10px !important;
        box-shadow: none !important;
        text-shadow: none !important;
    }
    html.retro button:active {
        border-style: inset !important;
    }
    
    /* Retro Button Specific */
    html.retro #retroToggle {
        margin-left: auto !important;
        background: #ece9d8 !important;
        color: #000000 !important;
    }
    
    /* Remove SVG Theme Icons in retro mode, rely on text */
    html.retro #themeToggle svg {
        display: none !important;
    }
    html.retro #themeToggle::after {
        content: "Theme";
        font-size: 11px;
    }
    
    /* FOOTER */
    html.retro footer {
        max-width: 1200px !important;
        margin: 0 auto !important;
        background: #ece9d8 !important;
        border: 2px outset #ffffff !important;
        border-top-color: #aca899 !important;
        padding: 5px !important;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5) !important;
    }
    
    /* ========================================================= */
    /* DARK MODE RETRO -> WINDOWS HIGH CONTRAST BLACK AESTHETIC  */
    /* ========================================================= */
    html.dark.retro body { background-color: #000000 !important; color: #FFFFFF !important; }
    html.dark.retro header { background: #000000 !important; border: 2px solid #FFFFFF !important; border-radius: 0 !important; box-shadow: none !important; }
    html.dark.retro header a.text-xl { color: #FFFFFF !important; text-shadow: none !important; }
    html.dark.retro header nav { background-color: #000000 !important; border-top: 2px solid #FFFFFF !important; border-bottom: 2px solid #FFFFFF !important; }
    html.dark.retro header nav a { color: #FFFFFF !important; }
    html.dark.retro header nav a:hover { background-color: #FFFFFF !important; color: #000000 !important; }
    html.dark.retro main { background-color: #000000 !important; border: 2px solid #FFFFFF !important; border-top: none !important; box-shadow: none !important; color: #FFFFFF !important; }
    html.dark.retro h1, html.dark.retro h2, html.dark.retro h3, html.dark.retro h4 { color: #00FF00 !important; } /* Lime green headers */
    html.dark.retro a { color: #FFFF00 !important; } /* Yellow links */
    html.dark.retro a:hover { color: #FF0000 !important; }
    html.dark.retro .bg-cardBg, html.dark.retro .bg-white, html.dark.retro [style*="background-color: var(--card-bg)"] { background: #000000 !important; border: 1px solid #FFFFFF !important; }
    html.dark.retro button { background: #000000 !important; border: 2px solid #FFFFFF !important; color: #FFFFFF !important; }
    html.dark.retro button:active { background: #FFFFFF !important; color: #000000 !important; }
    html.dark.retro footer { background: #000000 !important; border: 2px solid #FFFFFF !important; }
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Regex to find everything from /* GO RETRO to the end of the style block
    if '/* GO RETRO' in content:
        # Match from /* GO RETRO up to just before </style>
        content = re.sub(r'/\*\s*GO RETRO.*?(?=\s*</style>)', xp_retro_css, content, flags=re.DOTALL)
        
        with open(filepath, 'w') as f:
            f.write(content)

print("Windows XP / IE6 CSS successfully injected into all files!")
