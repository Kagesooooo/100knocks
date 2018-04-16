import pickle
from collections import OrderedDict
from scipy import io
import numpy as np

def cos(x,y):
    ab = np.linalg.norm(x) * np.linalg.norm(y)
    return np.dot(x,y) / ab if ab!=0 else -1

with open('chap9_index', 'rb')as f:
        index = pickle.load(f)
matrix_300 = io.loadmat('chap9_matrix_300')['matrix_300']
target0 = 'Spain'
target1 = 'Madrid'
target2 = 'Athens'
x = matrix_300[index[target0.lower()]]-matrix_300[index[target1.lower()]]+matrix_300[index[target2.lower()]]
distances = [cos(x, matrix_300[i]) for i in range(len(index))]

index_sorted= np.argsort(distances)
keys = list(index.keys())
for index in index_sorted[:-12:-1]:
    print('{}\t{}'.format(keys[index], distances[index]))
