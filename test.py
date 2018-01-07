import xml.etree.ElementTree as ET
import re

def mk_nplist(str0):
    cnt0 = 0
    cnt1 = 0
    st = ''
    list0 = []
    match = re.match(r'^\((.*?) (.*?)\)$',str0)
    for char in match.group(2):
        if char == '(':
            st += char
            cnt0 += 1
        elif char == ')':
            st += char
            cnt1 += 1
            if cnt0 == cnt1:
                list0.append(mk_nplist(st))
                st = ''
        elif not (cnt0 == cnt1 and char == ' '):
            st += char
        else:
            continue
    if st != '':
        list0.append(st)
    word = ' '.join(list0)
    if match.group(1) == 'NP':
        print(word)
    return word

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

for parse in root.findall('document/sentences/sentence/parse'):
    mk_nplist(parse.text[:-1])
