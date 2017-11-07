from collections import OrderedDict

with open('hightemp.txt','r') as f:
    rd = f.readlines()

dic = {}
for  s in rd:
    list0 = s[:-1].split('\t')
    if list0[0] not in dic:
        dic[list0[0]] = []
    dic[list0[0]].append(list0[1:])

wd = ''
for t in OrderedDict(sorted(dic.items(), key=lambda x:len(x[1]), reverse=True)):
    for list1 in dic[t]:
        wd += t + '\t' + '\t'.join([st for i,st in enumerate(list1)]) + '\n'

print(wd[:-1])
