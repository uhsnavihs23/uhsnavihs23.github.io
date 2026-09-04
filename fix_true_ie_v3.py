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

consistent_retro_css = """
    /* GO RETRO BETA FEATURE (Consistent Full-Screen IE6) */
    html.retro body {
        font-family: Tahoma, "Microsoft Sans Serif", sans-serif !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        padding-top: 135px !important; /* Room for IE Chrome Top */
        padding-bottom: 25px !important; /* Room for IE Chrome Bottom */
        margin: 0 !important;
    }
    
    /* Hide modern header entirely */
    html.retro header { display: none !important; }
    
    /* Do not mess with main/margins so layouts don't break! */
    html.retro main {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    html.retro footer {
        background: transparent !important;
        border: none !important;
        margin-bottom: 10px !important;
    }
    
    html.retro h1, html.retro h2, html.retro h3, html.retro h4 { font-family: "Times New Roman", Times, serif !important; color: #000000 !important; }
    html.retro p, html.retro span, html.retro div { color: inherit; }
    html.retro a { color: #0000EE !important; text-decoration: underline !important; }
    html.retro a:hover { color: #FF0000 !important; }
    
    html.retro .bg-cardBg, html.retro .bg-white, html.retro [style*="background-color: var(--card-bg)"] {
        background: #ffffff !important;
        border: 1px solid #000000 !important;
        box-shadow: none !important;
        border-radius: 0 !important;
    }
    
    html.retro button {
        background: #ece9d8 !important;
        border: 2px outset #ffffff !important;
        border-right-color: #aca899 !important;
        border-bottom-color: #aca899 !important;
        color: #000000 !important;
        font-family: Tahoma, sans-serif !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }
    html.retro button:active { border-style: inset !important; }
    
    /* Global fixes for relative paths in fake IE nav */
    html.retro #ie-chrome-top a { text-decoration: none !important; color: #000 !important; }
    html.retro #ie-chrome-top a:hover { background: #c1d2ee !important; }
"""

true_ie_js = """
        const retroToggle = document.getElementById('retroToggle');
        function setRetro(isRetro) {
            if (isRetro) {
                html.classList.add('retro');
                localStorage.setItem('retro', 'true');
                if (!document.getElementById('ie-chrome-top')) {
                    // Calculate root path for absolute links
                    const rootPath = window.location.pathname.includes('/projects/') ? 
                        (window.location.pathname.includes('/data-analyst-projects/') ? '../../' : '../') : './';
                        
                    const chromeTop = document.createElement('div');
                    chromeTop.id = 'ie-chrome-top';
                    chromeTop.style.cssText = 'position: fixed; top: 0; left: 0; right: 0; z-index: 999999; font-family: Tahoma, sans-serif; background: #ece9d8; border-bottom: 2px solid #aca899;';
                    chromeTop.innerHTML = `
                        <div style="background: linear-gradient(to right, #0058e6 0%, #3a93ff 100%); padding: 3px 4px; display: flex; justify-content: space-between; align-items: center;">
                            <div style="color: white; font-size: 13px; font-weight: bold; text-shadow: 1px 1px 1px #00138c; display: flex; align-items: center;">
                                <img src="https://win98icons.alexmeub.com/icons/png/msie1-2.png" width="16" height="16" style="margin-right: 5px;" alt="IE">
                                Shivanshu Sharma - Microsoft Internet Explorer
                            </div>
                            <div style="display:flex; gap:2px;">
                                <button style="background:#ece9d8; border: 1px outset #fff; font-size: 10px; width:16px; height:16px; cursor:pointer; color:#000; padding:0; line-height:10px;">_</button>
                                <button style="background:#ece9d8; border: 1px outset #fff; font-size: 10px; width:16px; height:16px; cursor:pointer; color:#000; padding:0; line-height:10px;">□</button>
                                <button onclick="document.getElementById('retroToggle').click()" style="background:#e81123; border: 1px outset #fff; font-size: 10px; font-weight:bold; width:16px; height:16px; cursor:pointer; color:white; padding:0; line-height:10px;">X</button>
                            </div>
                        </div>
                        <div style="padding: 2px 5px; font-size: 11px; color: #000; display: flex; gap: 10px; align-items: center; border-bottom: 1px solid #aca899;">
                            <span style="cursor:pointer;"><u>F</u>ile</span>
                            <span style="cursor:pointer;"><u>E</u>dit</span>
                            <span style="cursor:pointer;"><u>V</u>iew</span>
                            <span style="cursor:pointer;"><u>F</u>avorites</span>
                            <span style="cursor:pointer;"><u>T</u>ools</span>
                            <span style="cursor:pointer;"><u>H</u>elp</span>
                            <div style="width: 1px; height: 12px; background: #aca899; margin: 0 5px;"></div>
                            <a href="/index.html" style="padding: 0 4px;">Home</a>
                            <a href="/projects/index.html" style="padding: 0 4px;">Projects</a>
                            <a href="/about.html" style="padding: 0 4px;">About</a>
                            <span onclick="document.getElementById('themeToggle').click()" style="cursor:pointer; color: #000; font-weight: bold; margin-left: 10px; border: 1px outset #fff; padding: 0 4px; background: #ece9d8;">Toggle Theme</span>
                        </div>
                        <div style="padding: 2px 5px; border-top: 1px solid #fff; border-bottom: 1px solid #aca899; display: flex; align-items: center; gap: 2px;">
                            <button onclick="history.back()" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:3px; cursor:pointer; padding:2px 4px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                <img src="https://win98icons.alexmeub.com/icons/png/back-0.png" width="24" height="24"> Back
                            </button>
                            <button onclick="history.forward()" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:3px; cursor:pointer; padding:2px 4px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                <img src="https://win98icons.alexmeub.com/icons/png/forward-0.png" width="24" height="24">
                            </button>
                            <button onclick="location.reload()" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:3px; cursor:pointer; padding:2px 4px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                <img src="https://win98icons.alexmeub.com/icons/png/refresh-0.png" width="22" height="22">
                            </button>
                            <button onclick="location.href='/index.html'" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:3px; cursor:pointer; padding:2px 4px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                <img src="https://win98icons.alexmeub.com/icons/png/home-0.png" width="22" height="22">
                            </button>
                        </div>
                        <div style="padding: 2px 5px; border-top: 1px solid #fff; display: flex; align-items: center; gap: 4px;">
                            <span style="font-size: 11px; color: #000; padding-left: 2px;">Address</span>
                            <div style="flex:1; display:flex; border: 2px inset #fff; background: #fff; height: 20px; align-items:center; padding:0 2px;">
                                <img src="https://win98icons.alexmeub.com/icons/png/msie1-2.png" width="14" height="14" style="margin-right:3px;">
                                <input type="text" value="${window.location.href}" readonly style="flex:1; border:none; outline:none; font-family: Tahoma, sans-serif; font-size: 11px; color:#000; background:transparent;">
                            </div>
                            <button style="font-size: 11px; border: 1px outset #fff; background: #ece9d8; color: #000; padding: 1px 6px; cursor:pointer; height:20px; display:flex; align-items:center; gap:2px; box-shadow:none;">
                                <img src="https://win98icons.alexmeub.com/icons/png/search_web-0.png" width="14" height="14"> Go
                            </button>
                        </div>
                        <div style="background: #ffffe1; border-top: 1px solid #000; padding: 3px 10px; font-size: 11px; color: #000;">
                            ⚠️ <strong>Retro Mode Active:</strong> IE6 emulation running. <a href="javascript:void(0)" onclick="document.getElementById('retroToggle').click()" style="color:#0000ee; text-decoration:underline;">Click here to exit</a>.
                        </div>
                    `;
                    document.body.insertBefore(chromeTop, document.body.firstChild);
                    
                    const chromeBottom = document.createElement('div');
                    chromeBottom.id = 'ie-chrome-bottom';
                    chromeBottom.style.cssText = 'position: fixed; bottom: 0; left: 0; right: 0; z-index: 999999; font-family: Tahoma, sans-serif; background: #ece9d8; border-top: 2px outset #fff; padding: 2px 5px; display: flex; justify-content: space-between; font-size: 11px; color: #000;';
                    chromeBottom.innerHTML = `
                        <div style="display:flex; align-items:center; gap:5px; border: 1px inset #fff; padding: 1px 5px; flex:1; max-width: 300px;">
                            <img src="https://win98icons.alexmeub.com/icons/png/msie1-2.png" width="14" height="14"> Done
                        </div>
                        <div style="display:flex; align-items:center; gap:5px; border: 1px inset #fff; padding: 1px 5px; width: 150px;">
                            <img src="https://win98icons.alexmeub.com/icons/png/world-0.png" width="14" height="14"> Internet
                        </div>
                    `;
                    document.body.appendChild(chromeBottom);
                }
            } else {
                html.classList.remove('retro');
                localStorage.setItem('retro', 'false');
                const chromeTop = document.getElementById('ie-chrome-top');
                if (chromeTop) chromeTop.remove();
                const chromeBottom = document.getElementById('ie-chrome-bottom');
                if (chromeBottom) chromeBottom.remove();
            }
        }
        if (localStorage.getItem('retro') === 'true') { setRetro(true); } else { setRetro(false); }
        if (retroToggle) { retroToggle.addEventListener('click', () => { setRetro(!html.classList.contains('retro')); }); }
"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Replace the CSS
    if '/* GO RETRO' in content:
        content = re.sub(r'/\*\s*GO RETRO.*?(?=\s*</style>)', consistent_retro_css, content, flags=re.DOTALL)
    
    # 2. Replace the JS
    if 'const retroToggle = document.getElementById(\'retroToggle\');' in content:
        content = re.sub(r"const retroToggle = document.getElementById\('retroToggle'\);.*?if \(retroToggle\) \{ retroToggle\.addEventListener\('click', \(\) => \{ setRetro\(!html\.classList\.contains\('retro'\)\); \}\); \}", true_ie_js, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

print("Consistent True IE injected!")
