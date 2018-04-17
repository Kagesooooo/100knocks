import pickle
from scipy import io
import numpy as np

# with open('chap9_index', 'rb')as f:
#     index = pickle.load(f)
#
# matrix_300 = io.loadmat('chap9_matrix_300')['matrix_300']

# target0 = 'United_States'
# target1 = 'u.s'
#
# x = matrix_300[index[target0.lower()]]
# y = matrix_300[index[target1.lower()]]


with open('chap10_index', 'rb')as f:
    index = pickle.load(f)

matrix_300 = io.loadmat('chap10_matrix_300')['matrix_300']

target0 = 'United_States'
target1 = 'U.S'
x = matrix_300[index[target0]]
y = matrix_300[index[target1]]

ab = np.linalg.norm(x)*np.linalg.norm(y)

print(np.dot(x,y)/ab) if ab!=0 else print('error')
