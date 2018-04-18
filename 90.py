import pickle
from collections import OrderedDict
import numpy as np
from scipy import io
import word2vec

word2vec.word2vec(train='enwiki2.txt',output='chap10_word2vec.txt',size=300)

with open('chap10_word2vec.txt', 'rt')as f:
    sen = f.readlines()

nums = sen[0].split()
matrix = np.zeros([int(nums[0]),300])

index = OrderedDict()
for i,l in enumerate(sen[1:]):
    st = l.strip().split()
    index[st[0]] = i
    matrix[i] = st[1:]

io.savemat('chap10_matrix_300', {'matrix_300': matrix})
with open('chap10_index','wb')as f:
    pickle.dump(index,f)
