import json
with open("output/84.txt")as f:
    xtc_dic = json.load(f)

dic = {}
cnt = 0
for t in xtc_dic.keys():
    for c in xtc_dic[t].keys():
        if c in dic:
            continue
        else:
            dic[c] = cnt
            cnt += 1
        if t in dic:
            continue
        else:
            dic[t] = cnt
            cnt += 1

xtc_list = []
for i in range(cnt+1):
    li = [0]*cnt
    for j in range(cnt+1):
        if
