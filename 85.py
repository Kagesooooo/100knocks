from scipy import io
import pickle
import sklearn.decomposition

with open('chap9_index', 'rb') as f:
    index = pickle.load(f)

matrix0 = io.loadmat('chap9_matrix.mat')['matrix0']

# print(matrix0[index['france']])

clf = sklearn.decomposition.TruncatedSVD(300)
matrix_300 = clf.fit_transform(matrix0)
io.savemat('chap9_matrix_300',{'matrix_300':matrix_300})
