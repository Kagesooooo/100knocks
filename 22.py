import json
import re

f = open('jawiki-country.json')

jdata = []
eng = 0
for i, s in enumerate(f.readlines()):
    jdata.append(json.loads(s))
    if jdata[i]['title'] == 'イギリス':
        eng = i
text = jdata[eng]['text'].split('\n')

for s in text:
    match = re.match(r'\[\[Category:(.*)\]\]',s)
    if match != None:
        print(match.group(1))
