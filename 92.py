from scipy import io
import pickle
import numpy as np

def cos(x,y):
    ab = np.linalg.norm(x) * np.linalg.norm(y)
    return np.dot(x,y) / ab if ab!=0 else -1

with open('output/91.txt')as f:
    sens = f.readlines()

with open('chap10_index','rb')as f:
    index = pickle.load(f)
keys = [key for key in index.keys()]
matrix_300 = io.loadmat('chap10_matrix_300')['matrix_300']

# with open('chap9_index','rb')as f:
#     index = pickle.load(f)
# keys = [key for key in index.keys()]
# matrix_300 = io.loadmat('chap9_matrix_300')['matrix_300']

with open('output/92.txt','w')as f:
    for sen in sens[1:]:
        words = sen.split()
        top_value = -1
        top_word = ''
        try:
            vec = matrix_300[index[words[1]]]-matrix_300[index[words[0]]]+matrix_300[index[words[2]]]
            for key in keys:
                sim = cos(vec,matrix_300[index[key]])
                if sim > top_value:
                    top_value = sim
                    top_word = key
        except KeyError:
            pass
        f.write(sen.strip()+' '+top_word+' '+str(top_value)+'\n')
