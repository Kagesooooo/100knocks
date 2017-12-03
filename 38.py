import re
import numpy as np
import matplotlib.pyplot as plt

with open('neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    wd_dic = {}
    for s in f:
        match = pattern.match(s)
        if match == None:
            break
        sur = match.group(1)
        if sur not in wd_dic:
            wd_dic[sur] = 1
        else:
            wd_dic[sur] += 1
i = 0
a = []
b = []
for k, v in sorted(wd_dic.items(), key=lambda x: -x[1]):
    b.append(v)
plt.hist(b, bins=30, range=(1, 30))
plt.show()
