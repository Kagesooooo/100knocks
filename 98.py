import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

fname_dict_index_t = 'dict_index_country'
fname_matrix_x300 = 'matrix_x300_country'

with open('chap10_nation_index', 'rb')as f:
        index = pickle.load(f)

matrix_300 = io.loadmat('chap10_nation_matrix_300')['matrix_300']

ward = ward(matrix_300)
print(ward)

dendrogram(ward, labels=list(index.keys()), leaf_font_size=8)
plt.show()
