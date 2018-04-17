import pickle
from scipy import io
import numpy as np

with open('combined.tab')as f:
    sens = f.readlines()

with open('chap10_index','rb')as f:
    index = pickle.load(f)
matrix_300 = io.loadmat('chap10_matrix_300')['matrix_300']

def cos(x,y):
    ab = np.linalg.norm(x) * np.linalg.norm(y)
    return np.dot(x,y) / ab if ab!=0 else -1

with open('output/94.txt','w')as f:
    for sen in sens[1:]:
        words = sen.split('\t')
        try:
            sim = cos(matrix_300[index[words[0]]],matrix_300[index[words[1]]])
            # print(sen.strip()+' '+str(sim))
            f.write(sen.strip()+'\t'+str(sim)+'\n')
        except:
            pass
