import re
with open('assets/index-C4Mep_w2.js', 'r', encoding='utf-8') as f:
    text = f.read()

links = set(re.findall(r'https://pay\.cakto\.com\.br/[a-zA-Z0-9_]+', text))
print("Current links:", links)
