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

true_retro_css = """
    /* GO RETRO BETA FEATURE (True Internet Explorer Emulator) */
    html.retro {
        background: #004e98 !important; /* Windows XP Desktop */
    }
    html.retro body {
        font-family: Tahoma, "Microsoft Sans Serif", sans-serif !important;
        background-color: transparent !important;
        color: #000000 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Hide modern header entirely in retro mode */
    html.retro header { display: none !important; }
    
    html.retro main {
        margin: 110px 20px 20px 20px !important;
        background-color: #ffffff !important;
        border: 3px inset #d4d0c8 !important;
        border-radius: 0 !important;
        padding: 20px !important;
        min-height: calc(100vh - 160px) !important;
    }
    
    html.retro footer {
        margin: 0 20px 20px 20px !important;
        background: #ece9d8 !important;
        border: 2px outset #ffffff !important;
        border-top-color: #aca899 !important;
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
"""

true_retro_js = """
        const retroToggle = document.getElementById('retroToggle');
        function setRetro(isRetro) {
            if (isRetro) {
                html.classList.add('retro');
                localStorage.setItem('retro', 'true');
                if (!document.getElementById('ie-chrome')) {
                    const chrome = document.createElement('div');
                    chrome.id = 'ie-chrome';
                    chrome.style.cssText = 'position: fixed; top: 0; left: 0; right: 0; z-index: 999999; font-family: Tahoma, sans-serif;';
                    chrome.innerHTML = `
                        <div style="background: linear-gradient(to right, #0058e6 0%, #3a93ff 100%); padding: 4px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #00138c;">
                            <div style="color: white; font-size: 13px; font-weight: bold; text-shadow: 1px 1px 1px #00138c; display: flex; align-items: center;">
                                <img src="https://win98icons.alexmeub.com/icons/png/msie1-2.png" width="16" height="16" style="margin-right: 5px;" alt="IE">
                                Microsoft Internet Explorer
                            </div>
                            <div style="display:flex; gap:2px;">
                                <button style="background:#ece9d8; border: 1px outset #fff; font-size: 10px; width:20px; height:20px; cursor:pointer; color:#000; padding:0; line-height:10px;">_</button>
                                <button style="background:#ece9d8; border: 1px outset #fff; font-size: 10px; width:20px; height:20px; cursor:pointer; color:#000; padding:0; line-height:10px;">□</button>
                                <button onclick="document.getElementById('retroToggle').click()" style="background:#e81123; border: 1px outset #fff; font-size: 10px; font-weight:bold; width:20px; height:20px; cursor:pointer; color:white; padding:0; line-height:10px;">X</button>
                            </div>
                        </div>
                        <div style="background: #ece9d8; padding: 2px 5px; border-bottom: 1px solid #aca899; font-size: 11px; color: #000;">
                            <span style="margin-right:10px; cursor:pointer;"><u>F</u>ile</span><span style="margin-right:10px; cursor:pointer;"><u>E</u>dit</span><span style="margin-right:10px; cursor:pointer;"><u>V</u>iew</span><span style="margin-right:10px; cursor:pointer;"><u>F</u>avorites</span><span style="margin-right:10px; cursor:pointer;"><u>T</u>ools</span><span style="cursor:pointer;"><u>H</u>elp</span>
                        </div>
                        <div style="background: #ece9d8; padding: 4px 5px; border-bottom: 1px solid #aca899; display: flex; align-items: center; gap: 4px;">
                            <button style="background:transparent; border:none; color: #888; font-size:11px; display:flex; flex-direction:row; align-items:center; gap:2px; box-shadow:none;"><span style="font-size:16px;">⇦</span> Back</button>
                            <button style="background:transparent; border:none; color: #888; font-size:11px; display:flex; flex-direction:row; align-items:center; gap:2px; box-shadow:none;"><span style="font-size:16px;">⇨</span></button>
                            <button style="background:transparent; border:none; color: #000; font-size:11px; display:flex; flex-direction:row; align-items:center; gap:2px; box-shadow:none; cursor:pointer;"><span style="font-size:16px;">✖</span></button>
                            <button style="background:transparent; border:none; color: #000; font-size:11px; display:flex; flex-direction:row; align-items:center; gap:2px; box-shadow:none; cursor:pointer;" onclick="location.reload()"><span style="font-size:16px;">⟳</span></button>
                            <div style="height: 20px; width: 1px; background: #aca899; margin: 0 5px;"></div>
                            <span style="font-size: 11px; color: #000;">Address</span>
                            <input type="text" value="${window.location.href}" readonly style="flex:1; border: 2px inset #fff; padding: 2px; font-size: 11px; color:#000; background:#fff; height:18px;">
                            <button style="font-size: 11px; border: 1px outset #fff; background: #ece9d8; color: #000; padding: 2px 6px; cursor:pointer; height:22px;">Go</button>
                        </div>
                        <div style="background: #ffffe1; border-bottom: 1px solid #000; padding: 5px; font-size: 12px; color: #000; display:flex; justify-content:space-between; align-items:center;">
                            <span>⚠️ <strong>Disclaimer:</strong> You are viewing this site in Retro Mode, emulating Microsoft Internet Explorer (circa 2005). Layouts and colors have intentionally been altered.</span>
                            <button onclick="document.getElementById('retroToggle').click()" style="font-size:11px; padding:2px 8px; font-weight:bold;">Exit Retro Mode</button>
                        </div>
                    `;
                    document.body.insertBefore(chrome, document.body.firstChild);
                }
            } else {
                html.classList.remove('retro');
                localStorage.setItem('retro', 'false');
                const chrome = document.getElementById('ie-chrome');
                if (chrome) chrome.remove();
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
        content = re.sub(r'/\*\s*GO RETRO.*?(?=\s*</style>)', true_retro_css, content, flags=re.DOTALL)
    
    # 2. Replace the JS
    if 'const retroToggle = document.getElementById(\'retroToggle\');' in content:
        content = re.sub(r"const retroToggle = document.getElementById\('retroToggle'\);.*?if \(retroToggle\) \{ retroToggle\.addEventListener\('click', \(\) => \{ setRetro\(!html\.classList\.contains\('retro'\)\); \}\); \}", true_retro_js, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)

print("True IE overlay logic injected!")
