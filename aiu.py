import func4

list0 = func4.mk_chunk('neko.txt.cabocha')

# for sen in list0:
#     for i in range(len(sen)):
#         if (sen[i].has_verb() and len(sen[i].srcs)>0):
#             for j in range(len(sen)):
#                 if (sen[j].has_noun() and (sen[j].num in sen[i].srcs)):
#                     print(sen[i].st + ' ' + sen[j].st)

for s in list0[4:6]:
    for c in s:
        print(c.rpl_noun())
