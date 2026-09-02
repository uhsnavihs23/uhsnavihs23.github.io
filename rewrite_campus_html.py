import re

with open('../scratch/campus_electricity.html', 'r') as f:
    html = f.read()

# 1. Remove Tabs Navigation
html = re.sub(r'<div class="tabs">.*?</div>', '', html, flags=re.DOTALL)

# 2. Remove hidden classes and tab-content wrappers to make it one long scrollable page
html = html.replace('class="tab-content hidden"', 'class="report-section"')
html = html.replace('class="tab-content"', 'class="report-section"')
html = html.replace('id="overview-content"', 'id="overview-content" style="margin-top: 2rem;"')
html = html.replace('id="analysis-content"', 'id="analysis-content" style="margin-top: 4rem;"')
html = html.replace('id="recommendations-content"', 'id="recommendations-content" style="margin-top: 4rem;"')

# 3. Add Narrative Depth to make it "more humanly" and "like a proper research"
narrative_intro = """
        <div class="intro-card" style="margin-top: 2rem; background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <h2 style="font-size: 1.5rem; color: #111827; margin-bottom: 1rem;">Research Context and Objectives</h2>
            <p style="color: #4b5563; line-height: 1.6; margin-bottom: 1rem;">
                IIT Gandhinagar is committed to building a sustainable and energy efficient campus. As part of this sustainability initiative, it was critical to understand the underlying patterns of electricity consumption across academic blocks, housing grids, and research facilities.
            </p>
            <p style="color: #4b5563; line-height: 1.6;">
                This comprehensive research report transitions raw smart meter data into actionable operational insights. The objective is simple: identify baseline consumption behaviors, isolate peak demand triggers, and formulate practical strategies to optimize energy usage without compromising campus operations.
            </p>
        </div>
"""

# Insert narrative_intro before overview-content
html = html.replace('<div class="report-section" id="overview-content"', narrative_intro + '\n<div class="report-section" id="overview-content"')

narrative_analysis = """
            <div style="background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 2rem;">
                <h2 style="font-size: 1.5rem; color: #111827; margin-bottom: 1rem;">Deep Dive: Consumption Patterns</h2>
                <p style="color: #4b5563; line-height: 1.6;">
                    The core of our research involved dissecting 28 months of granular electricity data. We observed clear cyclical trends heavily influenced by academic calendars and seasonal weather changes. By stepping away from abstract data models and looking at operational realities, the graphs below illustrate precisely when and how the campus draws power.
                </p>
            </div>
"""
html = html.replace('<div class="report-section" id="analysis-content" style="margin-top: 4rem;">', '<div class="report-section" id="analysis-content" style="margin-top: 4rem;">\n' + narrative_analysis)

# 4. Remove em dashes (— and –)
html = html.replace('—', ':').replace('–', '-')

# 5. Remove Javascript tabs logic so charts render correctly on load
js_to_remove = """        function initTabs() {
            const tabs = document.querySelectorAll('.tab');
            const contents = document.querySelectorAll('.tab-content');

            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    const targetTab = tab.dataset.tab;

                    tabs.forEach(t => t.classList.remove('active'));
                    contents.forEach(c => c.classList.add('hidden'));

                    tab.classList.add('active');
                    document.getElementById(`${targetTab}-content`).classList.remove('hidden');

                    // Initialize charts when switching to analysis tab
                    if (targetTab === 'analysis') {
                        setTimeout(() => {
                            if (charts.area) charts.area.resize();
                            if (charts.solar) charts.solar.resize();
                            if (charts.forecast) charts.forecast.resize();
                        }, 100);
                    }
                });
            });
        }"""
html = html.replace(js_to_remove, '')
html = html.replace('initTabs();', '')

with open('projects/data-analyst-projects/campus-electricity/index.html', 'w') as f:
    f.write(html)

