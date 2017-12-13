import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc')

with open('neko.txt.mecab')as f:
    pattern = re.compile(r'^(.+?)\t(.+?),(.+?),(.+?),(.+?),(.+?),(.+?),(.+?)$')
    wd_dic = {}
    for s in f:
        match = pattern.match(s)
        if match == None:
            continue
        sur = match.group(1)
        if sur not in wd_dic:
            wd_dic[sur] = 1
        else:
            wd_dic[sur] += 1

i = 0
a = []
b = []
for k, v in sorted(wd_dic.items(), key=lambda x: -x[1]):
    a.append(k)
    b.append(v)
    i += 1
    if(i==10):
        break
plt.xticks(range(len(a)), a, fontproperties=fp)
plt.bar(range(len(b)), b, align='center')
plt.show()
