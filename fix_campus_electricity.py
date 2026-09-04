import re

filepath = "/Users/shivanshusharma/Documents/AGY_Projects/live_site_repo/projects/data-analyst-projects/campus-electricity/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Replace lucide icon with raw SVG in Conclusion & Impact
content = content.replace(
    '<i data-lucide="check-circle" style="color: #059669; width: 1.5rem; height: 1.5rem;"></i>',
    '<svg xmlns="http://www.w3.org/2000/svg" style="color: #059669; width: 1.5rem; height: 1.5rem; margin-right: 0.25rem;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>'
)

# Insert standard header
header_html = """
    <!-- Global Header -->
    <header style="position: sticky; top: 0; z-index: 50; width: 100%; backdrop-filter: blur(12px); background-color: rgba(255, 255, 255, 0.8); border-bottom: 1px solid #e5e7eb;">
        <div style="max-width: 1280px; margin: 0 auto; padding: 0 1.5rem; height: 4rem; display: flex; align-items: center; justify-content: space-between;">
            <a href="../../../index.html" style="font-size: 1.25rem; font-weight: 700; color: #0f172a; text-decoration: none;">Shivanshu Sharma</a>
            <nav style="display: flex; gap: 1.5rem; align-items: center;">
                <a href="../../../index.html" style="font-size: 0.875rem; font-weight: 500; color: #475569; text-decoration: none;">Home</a>
                <a href="../../index.html" style="font-size: 0.875rem; font-weight: 500; color: #3b82f6; text-decoration: none;">Projects</a>
                <a href="../../../about.html" style="font-size: 0.875rem; font-weight: 500; color: #475569; text-decoration: none;">About</a>
            </nav>
        </div>
    </header>
"""

# Replace the old .header
content = re.sub(r'<div class="header">.*?</div>\s*</div>', header_html, content, flags=re.DOTALL)

# Add "Back to Projects" button inside .container
back_btn = """
    <div style="margin-top: 2rem; margin-bottom: 1rem;">
        <a href="../../index.html" style="display: inline-flex; align-items: center; font-size: 0.875rem; font-weight: 500; color: #475569; text-decoration: none; transition: color 0.2s;">
            <svg style="margin-right: 0.5rem; width: 1rem; height: 1rem;" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
            Back to Projects
        </a>
    </div>
"""
content = re.sub(r'(<div class="container">\s*<!-- Overview Tab -->)', r'\1' + back_btn + r'\n        <div style="margin-bottom: 2rem; border-bottom: 1px solid #e5e7eb; padding-bottom: 1rem;">\n            <h1 style="font-size: 2rem; font-weight: bold; color: #111827;">IIT Gandhinagar Campus Energy Dashboard</h1>\n            <p style="color: #6b7280; margin-top: 0.5rem;">An end-to-end analysis of electricity consumption trends and optimization strategies (Oct 2019 - Jan 2022)</p>\n        </div>\n', content)

with open(filepath, 'w') as f:
    f.write(content)

print("campus-electricity updated")
