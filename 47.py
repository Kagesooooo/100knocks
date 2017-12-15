import func4

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0:
    for c0 in sen:
        if c0.has_verb():
            flag = False
            st0 = ''
            st1 = ''
            for c1 in sen:
                if (c1.dst == c0.num and c1.has_particle() and c1.has_sahen()):
                    flag = True
                    st0 += c1.right_par() + ' '
                    st1 += c1.st + ' '
            if flag:
                print(c0.left_verb()+'\t'+st0+'\t'+st1)
