import json
import pickle
from collections import OrderedDict
import math
from scipy import sparse, io
import sklearn.decomposition
import numpy as np

with open('tc.txt', encoding='utf-8') as ftc:
    tc_dic = json.load(ftc)
with open('t.txt')as ft:
    t_dic = json.load(ft)
with open('c.txt')as fc:
    c_dic = json.load(fc)

line = open('output/83.txt').read()
n = int(line[:-1])

index_t = OrderedDict((key, i) for i, key in enumerate(sorted(t_dic.keys())))
index_c = OrderedDict((key, i) for i, key in enumerate(sorted(c_dic.keys())))
len_t = len(index_t)
len_c = len(index_c)
matrix0 = sparse.lil_matrix((len_t,len_c))

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
        matrix0[index_t[t],index_c[c]] = f

io.savemat('chap9_matrix.mat',{'matrix0':matrix0})
with open('chap9_index','wb')as d:
    pickle.dump(index_t,d)
