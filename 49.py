import func4
import re

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0:
    list0 = []
    for c0 in sen:
        if c0.has_noun():
            x = c0.dst
            list1 = [c0]
            for c1 in sen:
                if x == c1.num:
                    x = c1.dst
                    list1.append(c1)
            if len(list1) == 1:
                break
            list0.append(list1)

    if len(list0) > 1:
        for i, l0 in enumerate(list0):
            for l1 in list0[i+1:]:
                st0 = []
                st1 = []
                flag0 = False
                for v0 in l0:
                    for j,v1 in enumerate(l1):
                        if v0 == v1:
                            x = j
                            flag0 = True
                            break
                        st1.append(v1)
                    if flag0:
                        st = ''
                        stx = ''
                        sty = ''
                        if x == 0:
                            for s in st0:
                                if s == st0[0]:
                                    stx += s.rpl_noun() + ' -> '
                                else:
                                    stx += s.st + ' -> '
                            sty = l1[0].rpl_noun().replace('X','Y')
                            print(stx+sty)
                        else:
                            st = ' | '
                            for m in l1[x:]:
                                st += m.st
                            for s in st0:
                                if s == st0[0]:
                                    stx += s.rpl_noun()
                                else:
                                    stx += ' -> ' + s.st
                            sty += ' | '
                            for s in st1:
                                if s == st1[0]:
                                    sty += s.rpl_noun().replace('X','Y')
                                else:
                                    sty += ' -> ' + s.st
                            print(stx+sty+st)
                        break
                    st0.append(v0)
                    st1 = []
                    flag0 = False
