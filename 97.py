import pickle
from collections import OrderedDict
from scipy import io
import numpy as np
from sklearn.cluster import KMeans

with open('chap10_nation_index', 'rb')as f:
        index = pickle.load(f)
keys = [key for key in index.keys()]
matrix_300 = io.loadmat('chap10_nation_matrix_300')['matrix_300']

k = KMeans(n_clusters=5).fit_predict(matrix_300)
zipp = zip(keys,k)

for country, category in sorted(zipp, key=lambda x: x[1]):
    print(str(category)+'\t'+country)
