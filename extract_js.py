from bs4 import BeautifulSoup
import sys

with open('projects/policy-brief-generator/index.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

scripts = soup.find_all('script')
# The last script is the logic
logic = scripts[-1].string
if logic:
    with open('test_logic.js', 'w') as f:
        f.write(logic)
