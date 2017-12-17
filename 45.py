import func4
# from collections import defaultdict

list0 = func4.mk_chunk('neko.txt.cabocha')

# dic = {}

for sen in list0:
    for c0 in sen:
        st0 = ''
        flag = False
        if c0.has_verb():
            list1 = []
            # if c0.left_verb() not in dic:
                # dic[c0.left_verb()] = defaultdict(int)
            for c1 in sen:
                if (c1.dst == c0.num and c1.has_particle()):
                    flag = True
                    list1.append(c1.right_par())
                    # dic[c0.left_verb()][c1.right_par()] += 1
            for s in  sorted(list1):
                st0 += s + ' '
            if flag:
                print(c0.left_verb() + '\t' + st0)

# print(dic['与える'])
