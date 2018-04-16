import pickle
from collections import OrderedDict
import numpy as np
from scipy import io
import word2vec

word2vec.word2vec(train='enwiki2.txt',output='chap10_word2vec.txt',size=300,threads=4,binary=0)

with open('chap10_word2vec', 'rt')as f:
    work = f.readline().split(' ')
    size_dict = int(work[0])
    size_x = int(work[1])
    index = OrderedDict()
    matrix = np.zeros([size_dict, size_x], dtype=np.float64)
    for i, line in enumerate(f):
        work = line.strip().split(' ')
        index[work[0]] = i
        matrix[i] = work[1:]

io.savemat('chap10_matrix_300', {'matrix_300': matrix})
with open('chap10_index', 'wb')as f:
    pickle.dump(index,f)
