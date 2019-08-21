import re

r = re.compile(r"(?:\* )(?P<pre>.*?)(?P<eur>(?P<a>[0-9]+)(?:(?:\.|,)(?P<b>-|[0-9]{2}))? ?(?:€|EUR))(?P<post>.*)")
old = re.compile(r'~~.*?~~')

with open('preise.txt') as f:
    data = f.read()

for line in data.splitlines():
    line = old.sub('', line)
    m = r.match(line)
    if m:
        name = '%s %s' % (
            m.group('pre').strip().strip('/').strip(),
            m.group('post').strip().strip('/').strip()
        )
        name = name.strip()
        eura = int(m.group('a'))
        eurb = int(m.group('b')) if m.group('b') and m.group('b').isdigit() else 0
        eur = (eura * 100) + eurb
        print(f''' insert into article (name, amount, active, created, usage_count) values ("{name}", {eur}, true, now(), 0); ''')
