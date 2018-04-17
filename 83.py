
from collections import defaultdict
import json

tc_dic = defaultdict(int)
t_dic = defaultdict(int)
c_dic = defaultdict(int)

ftc = open('tc.txt','w')
ft = open('t.txt','w')
fc = open('c.txt','w')
cnt = 0
with open('output/82.txt')as f:
    for words in f:
        cnt += 1
        t_c = words[:-1].split('\t')
        t = t_c[0]
        c = t_c[1]
        tc_dic[t+" "+c] += 1
        t_dic[t] += 1
        c_dic[c] += 1
    json.dump(tc_dic, ftc)
    json.dump(t_dic, ft)
    json.dump(c_dic, fc)
    print(cnt)
