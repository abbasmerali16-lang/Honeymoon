import json, re, html
for k in ['wales', 'mru']:
    s = open(k + '.html', encoding='utf-8').read()
    out = []
    def walk(x):
        if isinstance(x, dict):
            for v in x.values(): walk(v)
        elif isinstance(x, list):
            for v in x: walk(v)
        elif isinstance(x, str) and len(x) > 3 and not x.startswith('http') and not re.fullmatch(r'[A-Za-z0-9_:=+/.-]+', x):
            out.append(x)
    for m in re.finditer(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', s, re.S):
        try: walk(json.loads(m.group(1)))
        except Exception: pass
    seen = set()
    print('=====', k, len(s))
    for x in out:
        x = re.sub(r'\s+', ' ', x).strip()
        if x in seen: continue
        seen.add(x); print('>>', x[:700])
