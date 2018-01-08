import xml.etree.ElementTree as ET
import re

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

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
        elif cnt0 != cnt1 or char != ' ':
            st += char
        else:
            continue
    if st != '':
        list0.append(st)
    word = ' '.join(list0)
    if match.group(1) == 'NP':
        list1.append(word)
    return word

for parse in root.findall('document/sentences/sentence/parse'):
    list1 = []
    list2 = []
    mk_nplist(parse.text[:-1])
    for i in range(len(list1[:-1])):
        for st in list1[::-1]:
            if list1[i] in st and list1[i+1] in st:
                if st not in list2:
                    list2.append(st)
                    print(st)
        if list1[i] not in list2:
            list2.append(list1[i])
            print(list1[i])
