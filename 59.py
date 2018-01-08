import xml.etree.ElementTree as ET
import re

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

def mk_nplist(str0,cnt):
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
                list0.append(mk_nplist(st,cnt+1))
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
        listw.append(cnt)
        # print(word,cnt)
    return word

for parse in root.findall('document/sentences/sentence/parse'):
    list1 = []
    list2 = []
    listw = []
    cnt = 0
    mk_nplist(parse.text[:-1],cnt)
    # print(list1)



    for i in range(len(list1[:-1])):
        flag = False
        for j in range(len(list1))[::-1]:
            if list1[i] in list1[j] and list1[i+1] in list1[j]:
                if list1[j] not in list2:
                    if listw[i] > listw[j]:
                        list2.append(list1[j])
            elif list1[i] == list1[j] and i != j:
                flag = True
        if flag:
            list2.append(list1[i])
        if list1[i] not in list2:
            list2.append(list1[i])
    if list1[-1] not in list2:
        list2.append(list1[-1])

    for l in list2:
        print(l)
