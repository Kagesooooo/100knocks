import json
import re

with open('jawiki-country.json', 'r') as f:
    rd = f.readlines()

jdata = []
eng = 0

for i in range(len(rd)):
    jdata.append(json.loads(rd[i]))
    if jdata[i]['title'] == 'イギリス':
        eng = i
text = jdata[eng]['text'].split('\n')

for s in text:
    match = re.search(r'(File|ファイル):(.*?)\|',s)
    if match != None:
        print(match.group(2))


# http://www.yukun.info/blog/2008/08/python-regexp-greedy-reluctant-match.html
