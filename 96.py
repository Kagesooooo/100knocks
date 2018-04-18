import numpy as np
from scipy import io
import pickle
from collections import OrderedDict

with open('chap10_word2vec.txt', 'rt')as f:
    sens = f.readlines()

with open('nations.txt')as f:
    nations = [nation.strip().replace(' ','_') for nation in f.readlines()]

nation_vecs = []
for sen in sens:
    words = sen.split()
    if words[0] in nations:
        nation_vecs.append(sen.strip())

matrix = np.zeros([len(nation_vecs),300])

index = OrderedDict()
for i,vec in enumerate(nation_vecs):
    st = vec.strip().split()
    index[st[0]] = i
    matrix[i] = st[1:]

io.savemat('chap10_nation_matrix_300', {'matrix_300': matrix})
with open('chap10_nation_index','wb')as f:
    pickle.dump(index,f)
