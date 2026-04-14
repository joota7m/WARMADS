import re

with open('assets/index-C4Mep_w2.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'https://pay.cakto.com.br/bh3e6me_841962'
matches = [m.start() for m in re.finditer(target, text)]

for i, start in enumerate(matches):
    print(f"\n--- Match {i} ---")
    snippet = text[max(0, start - 300): start + len(target) + 300]
    print(snippet)

