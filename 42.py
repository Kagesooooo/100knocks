import func4

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0:
    for i in range(len(sen)):
        x = sen[i].dst
        for j in range(len(sen)):
            if sen[j].srcs == x:
                print(sen[i].st + ' ' + sen[j].st)
