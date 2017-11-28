import re
import numpy as np
import matplotlib.pyplot as plt

with open('neko.txt.mecab')as f:
    dic = {}
    wd_dic = {}
    for s in f:
        if re.search('EOS',s):
            break
        line = re.split(r'[\t,]',s[:-1])
        dic['surface'] = line[0]
        if dic['surface'] not in wd_dic:
            wd_dic[dic['surface']] = 1
        else:
            wd_dic[dic['surface']] += 1
i = 0
a = []
b = []
for k, v in sorted(wd_dic.items(), key=lambda x: -x[1]):
    b.append(v)
plt.hist(b, bins=30, range=(1, 30))
plt.show()
