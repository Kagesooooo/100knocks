import func4

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0[:5]:
    for c0 in sen:
        if c0.has_noun():
            x = c0.dst
            st = c0.st
            for c1 in sen:
                flag = True
                if x == c1.num:
                    st += ' -> ' + c1.st
                    x = c1.dst
                    flag = False
            if flag:
                    break
            print(st)
