import json
from collections import defaultdict
import math

with open('tc.txt', encoding='utf-8') as ftc:
    tc_dic = json.load(ftc)
with open('t.txt')as ft:
    t_dic = json.load(ft)
with open('c.txt')as fc:
    c_dic = json.load(fc)

line = open('output/83.txt').read()
n = int(line[:-1])

xtc_dic = defaultdict(dict)
for key,value in tc_dic.items():
    if value < 10:
        continue
    t_c = key.split()
    t = t_c[0]
    c = t_c[1]
    f = math.log((n*tc_dic[key])/(t_dic[t]*c_dic[c]))
    if f < 0:
        continue
    else:
        xtc_dic[t][c] = f

json.dump(xtc_dic,open('output/84.txt','w'))
