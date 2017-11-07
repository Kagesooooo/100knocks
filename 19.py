# from collections import OrderedDict

with open('hightemp.txt','r') as f:
    rd = f.readlines()

dic = {}
for  s in rd:
    list0 = s[:-1].split('\t')
    if list0[0] not in dic:
        dic[list0[0]] = []
    dic[list0[0]].append(list0[1:])

for t,s in sorted(dic.items(), key=lambda x:len(x[1]), reverse=True):
    print(t,len(s))

 # cut -f1 hightemp.txt | sort | uniq -c | sort --reverse
