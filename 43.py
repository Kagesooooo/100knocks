import func4

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0:
    for i in range(len(sen)):
        x = sen[i].dst
        for k in sen[i].morphs:
            if k.is_noun():
                for j in range(len(sen)):
                    if sen[j].srcs == x:
                        for l in sen[j].morphs:
                            if l.is_verb():
                                print(sen[i].st + ' ' + sen[j].st)
                                break
                break
