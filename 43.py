import func4

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0:
    for c0 in sen:
        if c0.has_noun():
            for c1 in sen:
                if (c0.num in c1.srcs and c1.has_verb()):
                    print(c0.st + '\t' + c1.st)
