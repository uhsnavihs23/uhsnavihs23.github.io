with open('projects/index.html', 'r') as f:
    content = f.read()

new_cards = """
                <div class="bg-cardBg p-6 rounded-xl border border-borderColor shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">ESG Reporting as a Strategic Advantage</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Transforming compliance mandates into long-term corporate value and risk mitigation.</p>
                    <a href="./esg-strategic-advantage.html" class="text-accent font-medium hover:underline mt-auto">Read Whitepaper &rarr;</a>
                </div>

                <div class="bg-cardBg p-6 rounded-xl border border-borderColor shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">Healthcare Infrastructure Stress Testing</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Analyzing urban vulnerability and hospital bed capacity using demographic density mapping.</p>
                    <a href="./healthcare-infrastructure-stress.html" class="text-accent font-medium hover:underline mt-auto">Read Analysis &rarr;</a>
                </div>

                <div class="bg-cardBg p-6 rounded-xl border border-borderColor shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">The Urban Mobility Divide</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">How unequal access to public transit restricts economic mobility in metropolitan areas.</p>
                    <a href="./urban-mobility-divide.html" class="text-accent font-medium hover:underline mt-auto">Read Essay &rarr;</a>
                </div>

                <div class="bg-cardBg p-6 rounded-xl border border-borderColor shadow-sm hover:shadow-md transition-shadow flex flex-col">
                    <h3 class="text-xl font-bold text-primary mb-2">The Economics of Renewable Subsidies</h3>
                    <p class="text-secondary text-sm mb-4 flex-grow">Evaluating the efficacy of government incentives in driving solar adoption and market parity.</p>
                    <a href="./renewable-subsidies.html" class="text-accent font-medium hover:underline mt-auto">Read Whitepaper &rarr;</a>
                </div>
"""

# Insert right after the Policy Brief Generator card ends
content = content.replace(
    '<a href="./policy-brief-generator/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>\n                </div>', 
    '<a href="./policy-brief-generator/index.html" class="text-accent font-medium hover:underline mt-auto">View App &rarr;</a>\n                </div>\n' + new_cards
)

with open('projects/index.html', 'w') as f:
    f.write(content)

