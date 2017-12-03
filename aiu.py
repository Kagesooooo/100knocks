import re
import func3

dic = {}
i = 0
list0 = [[]]
pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
for s in func3.file_in():
    match = pattern.match(s)
    if match == None:
        break
    dic['surface'] = match.group(1)
    dic['base'] = match.group(8)
    dic['pos'] = match.group(2)
    dic['pos1'] = match.group(3)
    list0[i].append(dic.copy())
    if dic['pos'] == '記号':
        i += 1
        list0.append([])
print(list0)
