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

goatcounter_script = '<script data-goatcounter="https://23022000.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'

unified_js = """
    <script>
        // --- RETRO MODE GLOBAL SCRIPT ---
        function initRetroMode() {
            const html = document.documentElement;
            let retroBtn = document.getElementById('retroToggle');
            
            window.setRetro = function(isRetro) {
                if (isRetro) {
                    html.classList.add('retro');
                    localStorage.setItem('retro', 'true');
                    
                    // Force Light Theme (Retro and Dark mode clash too much)
                    if (html.classList.contains('dark') && typeof window.setTheme === 'function') {
                        window.setTheme(false);
                    } else {
                        html.classList.remove('dark');
                        localStorage.setItem('theme', 'light');
                        const themeIconLight = document.getElementById('themeIconLight');
                        const themeIconDark = document.getElementById('themeIconDark');
                        if(themeIconLight) themeIconLight.classList.add('hidden');
                        if(themeIconDark) themeIconDark.classList.remove('hidden');
                    }
                    
                    if (!document.getElementById('ie-chrome-top')) {
                        const chromeTop = document.createElement('div');
                        chromeTop.id = 'ie-chrome-top';
                        chromeTop.style.cssText = 'position: fixed; top: 0; left: 0; right: 0; z-index: 999999; font-family: Tahoma, sans-serif; background: #ece9d8; border-bottom: 2px solid #aca899;';
                        
                        const isProj = window.location.pathname.includes('/projects/');
                        const isSubProj = window.location.pathname.includes('/data-analyst-projects/');
                        const prefix = isSubProj ? '../../' : (isProj ? '../' : './');
                        
                        chromeTop.innerHTML = `
                            <div style="background: linear-gradient(to right, #0058e6 0%, #3a93ff 100%); padding: 3px 4px; display: flex; justify-content: space-between; align-items: center;">
                                <div style="color: white; font-size: 13px; font-weight: bold; text-shadow: 1px 1px 1px #00138c; display: flex; align-items: center;">
                                    <span style="font-size:16px; margin-right:5px; color:#cce0ff;">e</span>
                                    Shivanshu Sharma - Microsoft Internet Explorer
                                </div>
                                <div style="display:flex; gap:2px;">
                                    <button style="background:#ece9d8; border: 1px outset #fff; font-size: 10px; width:16px; height:16px; cursor:pointer; color:#000; padding:0; line-height:10px; box-shadow:none;">_</button>
                                    <button style="background:#ece9d8; border: 1px outset #fff; font-size: 10px; width:16px; height:16px; cursor:pointer; color:#000; padding:0; line-height:10px; box-shadow:none;">□</button>
                                    <button onclick="window.setRetro(false)" style="background:#e81123; border: 1px outset #fff; font-size: 10px; font-weight:bold; width:16px; height:16px; cursor:pointer; color:white; padding:0; line-height:10px; box-shadow:none;">X</button>
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
                                <a href="` + prefix + `index.html" style="padding: 0 4px; text-decoration:none; color:#000;">Home</a>
                                <a href="` + prefix + `projects/index.html" style="padding: 0 4px; text-decoration:none; color:#000;">Projects</a>
                                <a href="` + prefix + `about.html" style="padding: 0 4px; text-decoration:none; color:#000;">About</a>
                                <span onclick="alert('Dark Mode is disabled while Retro IE6 is active. Exit Retro Mode first to use Dark Mode.');" style="cursor:pointer; color: #666; font-weight: bold; margin-left: 10px; border: 1px solid #aca899; padding: 0 4px; background: #ece9d8;">Dark Mode (Disabled)</span>
                            </div>
                            <div style="padding: 2px 5px; border-top: 1px solid #fff; border-bottom: 1px solid #aca899; display: flex; align-items: center; gap: 2px;">
                                <button onclick="history.back()" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:4px; cursor:pointer; padding:2px 6px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                    <span style="font-size:18px; color:#1a8c44;">&#11164;</span> Back
                                </button>
                                <button onclick="history.forward()" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:4px; cursor:pointer; padding:2px 6px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                    <span style="font-size:18px; color:#1a8c44;">&#11166;</span>
                                </button>
                                <button onclick="location.reload()" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:4px; cursor:pointer; padding:2px 6px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                    <span style="font-size:18px; color:#e81123;">&#10006;</span> Stop
                                </button>
                                <button onclick="location.reload()" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:4px; cursor:pointer; padding:2px 6px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                    <span style="font-size:18px; color:#3a93ff;">&#10227;</span> Refresh
                                </button>
                                <button onclick="location.href='` + prefix + `index.html'" style="background:transparent; border:1px solid transparent; color: #000; font-size:11px; display:flex; align-items:center; gap:4px; cursor:pointer; padding:2px 6px; box-shadow:none;" onmouseover="this.style.border='1px outset #fff'" onmouseout="this.style.border='1px solid transparent'">
                                    <span style="font-size:18px; color:#b58900;">&#8962;</span> Home
                                </button>
                            </div>
                            <div style="padding: 2px 5px; border-top: 1px solid #fff; display: flex; align-items: center; gap: 4px;">
                                <span style="font-size: 11px; color: #000; padding-left: 2px;">Address</span>
                                <div style="flex:1; display:flex; border: 2px inset #fff; background: #fff; height: 20px; align-items:center; padding:0 2px;">
                                    <span style="font-size:14px; margin-right:4px; color:#0058e6;">e</span>
                                    <input type="text" value="${window.location.href}" readonly style="flex:1; border:none; outline:none; font-family: Tahoma, sans-serif; font-size: 11px; color:#000; background:transparent;">
                                </div>
                                <button style="font-size: 11px; border: 1px outset #fff; background: #ece9d8; color: #000; padding: 1px 6px; cursor:pointer; height:20px; display:flex; align-items:center; gap:2px; box-shadow:none;">
                                    <span style="font-size:14px; color:#0058e6;">&#10140;</span> Go
                                </button>
                            </div>
                            <div style="background: #ffffe1; border-top: 1px solid #000; padding: 3px 10px; font-size: 11px; color: #000;">
                                ⚠️ <strong>Retro Mode Active:</strong> IE6 emulation running. Layouts and Dark Mode are overridden. <a href="javascript:void(0)" onclick="window.setRetro(false)" style="color:#0000ee; text-decoration:underline;">Click here to exit</a>.
                            </div>
                        `;
                        document.body.insertBefore(chromeTop, document.body.firstChild);
                        
                        const chromeBottom = document.createElement('div');
                        chromeBottom.id = 'ie-chrome-bottom';
                        chromeBottom.style.cssText = 'position: fixed; bottom: 0; left: 0; right: 0; z-index: 999999; font-family: Tahoma, sans-serif; background: #ece9d8; border-top: 2px outset #fff; padding: 2px 5px; display: flex; justify-content: space-between; font-size: 11px; color: #000;';
                        chromeBottom.innerHTML = `
                            <div style="display:flex; align-items:center; gap:5px; border: 1px inset #fff; padding: 1px 5px; flex:1; max-width: 300px;">
                                <span style="font-size:14px; color:#0058e6;">e</span> Done
                            </div>
                            <div style="display:flex; align-items:center; gap:5px; border: 1px inset #fff; padding: 1px 5px; width: 150px;">
                                <span style="font-size:14px; color:#3a93ff;">&#127760;</span> Internet
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
            
            if (localStorage.getItem('retro') === 'true') { window.setRetro(true); }
            
            document.body.addEventListener('click', function(e) {
                if (e.target && e.target.id === 'retroToggle') {
                    window.setRetro(!html.classList.contains('retro'));
                }
            });
        }
        
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initRetroMode);
        } else {
            initRetroMode();
        }
    </script>
</body>
"""

for filepath in html_files:
    if "test_js.html" in filepath:
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Fix missing </body>
    if '</body>' not in content and '</main>' in content:
        content = content.replace('</main>', '</main>\n</body>')
    
    # 2. Inject GoatCounter if missing
    if "goatcounter.com/count" not in content:
        if '</body>' in content:
            content = content.replace('</body>', goatcounter_script + '\n</body>')

    # 3. Inject Retro JS if missing or replace it
    content = re.sub(r"<!-- --- RETRO MODE GLOBAL SCRIPT --- -->.*</body>", "</body>", content, flags=re.DOTALL)
    content = re.sub(r"<script>\s*// --- RETRO MODE GLOBAL SCRIPT ---.*?</body>", "</body>", content, flags=re.DOTALL)
    content = content.replace("</body>", unified_js)

    with open(filepath, 'w') as f:
        f.write(content)

print("Remaining issues fixed!")
