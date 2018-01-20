# import random
#
# fp = open('rt-polaritydata/rt-polaritydata/rt-polarity.pos',encoding='latin-1')
# fn = open('rt-polaritydata/rt-polaritydata/rt-polarity.neg',encoding='latin-1')
#
# list0 = []
#
# for l in fp:
#     list0.append('+1 '+l[:-1])
# fp.close()
#
# for l in fn:
#     list0.append('-1 '+l[:-1])
# fn.close()
#
# random.shuffle(list0)
# with open('sentiment.txt','w')as fo:
#     for l in list0:
#         fo.write(l+'\n')

cntp = 0
cntn = 0
with open('sentiment.txt',encoding='latin-1')as f:
    for l in f:
        if l[:2]=='+1':
            cntp += 1
        elif l[:2]=='-1':
            cntn += 1
        else:
            continue

print(cntp,cntn)
