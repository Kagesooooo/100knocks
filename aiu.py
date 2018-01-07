import xml.etree.ElementTree as ET
import re

pattern = re.compile(r'^\((.*?) (.*?)\)$')

def mk_nplist(str0, list0):
    match = pattern.match(str0)
    key = match.group(1)
    value = match.group(2)
    cnt0 = 0
    cnt1 = 0
    st = ''
    words = []
    for c in value:
        if c == '(':
            st += c
            cnt0 += 1
        elif c == ')':
            st += c
            cnt1 += 1
            if cnt0 == cnt1:
                words.append(mk_nplist(st, list0))
                st = ''
        # elif not (cnt0 == cnt1 and c == ' '):
        elif cnt0 != cnt1 or c != ' ':
            st += c
        else:
            continue
    if st != '':
        words.append(st)
    result = ' '.join(words)
    if key == 'NP':
        list0.append(result)
        print(result)
    return result

root = ET.parse('nlp.txt.xml')

for parse in root.iterfind('./document/sentences/sentence/parse'):
    result = []
    mk_nplist(parse.text[:-1], result)
    # print(result)
