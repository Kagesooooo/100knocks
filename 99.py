import pickle
from scipy import io
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

with open('chap10_nation_index', 'rb')as f:
    index = pickle.load(f)

matrix_300 = io.loadmat('chap10_nation_matrix_300')['matrix_300']

t = TSNE().fit_transform(matrix_300)

predicts = KMeans(n_clusters=5).fit_predict(matrix_300)

fig, ax = plt.subplots()
cmap = plt.get_cmap('Set1')
for index, label in enumerate(index.keys()):
    cval = cmap(predicts[index] / 4)
    ax.scatter(t[index, 0], t[index, 1], marker='.', color=cval)
    ax.annotate(label, xy=(t[index, 0], t[index, 1]), color=cval)
plt.show()
