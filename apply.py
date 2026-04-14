import re
import os

# 1. Update links in JS
js_path = 'assets/index-C4Mep_w2.js'
with open(js_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace START plan (i9nj4to -> htjs7iq)
text = text.replace('https://pay.cakto.com.br/i9nj4to', 'https://pay.cakto.com.br/htjs7iq')

# For bh3e6me_841962, we have 4 matches. Match 0 (Hero CTA) -> m586zfb_848793 (149), 
# Match 1 (SCALE Plan) -> m586zfb_848793 (149),
# Match 2 (TEAM Plan) -> 38m2aqd (499)
# Match 3 (Bottom CTA) -> m586zfb_848793 (149)

# We will just replace Match 2 specifically.
# The context for Match 2: 'extras:["Até 8 usuários na mesma conta","Painel centralizado para toda a equipe"],cta:"Falar com a equipe",href:"https://pay.cakto.com.br/bh3e6me_841962"'
team_context = 'extras:["Até 8 usuários na mesma conta","Painel centralizado para toda a equipe"],cta:"Falar com a equipe",href:"https://pay.cakto.com.br/bh3e6me_841962"'
team_new = 'extras:["Até 8 usuários na mesma conta","Painel centralizado para toda a equipe"],cta:"Falar com a equipe",href:"https://pay.cakto.com.br/38m2aqd"'

if team_context in text:
    text = text.replace(team_context, team_new)
else:
    print("Could not find TEAM context!")

# Now replace all remaining bh3e6me_841962 with m586zfb_848793
text = text.replace('https://pay.cakto.com.br/bh3e6me_841962', 'https://pay.cakto.com.br/m586zfb_848793')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("JS Links Updated.")

# 2. Inject Pixel into HTML
html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

pixel_code = """
    <!-- Meta Pixel Code -->
    <script>
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '1773068683666926');
    fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=1773068683666926&ev=PageView&noscript=1"
    /></noscript>
    <!-- End Meta Pixel Code -->
  </head>
"""

# Only inject if not already there
if "1773068683666926" not in html:
    html = html.replace('</head>', pixel_code)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML Pixel Injected.")

