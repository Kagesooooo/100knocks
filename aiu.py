import xml.etree.ElementTree as ET
import re

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

# def mk_nplist(str0):
#     cnt0 = 0
#     cnt1 = 0
#     st = ''
#     list0 = []
#     match = re.match(r'^\((.*?) (.*?)\)$',str0)
#     for char in match.group(2):
#         if char == '(':
#             st += char
#             cnt0 += 1
#         elif char == ')':
#             st += char
#             cnt1 += 1
#             if cnt0 == cnt1:
#                 list0.append(mk_nplist(st))
#                 st = ''
#         elif cnt0 != cnt1 or char != ' ':
#             st += char
#         else:
#             continue
#     if st != '':
#         list0.append(st)
#     word = ' '.join(list0)
#     if match.group(1) == 'NP':
#         print(word)
#     return word


def mk_nplist(st):
    cnt0 = 0
    cnt1 = 0
    st = ''
    flag = False
    for char in st:
        if char == '(':
            cnt0 += 1
            if cnt0 == 2:
                flag = True
        elif char == ')':
            cnt1 += 1
            st += char
            if cnt0 == cnt1:
                mk_nplist(st)
        else:
            if flag:
                st += char
    print(st)


for parse in root.findall('document/sentences/sentence/parse')[:1]:
    mk_nplist(parse.text[:-1])
