import pickle
from scipy import io
import numpy as np

# with open('chap9_index', 'rb') as f:
#     index = pickle.load(f)
# matrix_300 = io.loadmat('chap9_matrix_300')['matrix_300']
# search_word = 'france'
# print(matrix_300[index[search_word.lower()]])

with open('chap10_index', 'rb') as f:
    index = pickle.load(f)
matrix_300 = io.loadmat('chap10_matrix_300')['matrix_300']
search_word = 'United_States'
print(matrix_300[index[search_word]])
