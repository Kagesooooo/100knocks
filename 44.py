import func4
from graphviz import Digraph

G = Digraph(format="png")
G.attr("node", shape="circle")

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0[2:5]:
    for i in range(len(sen)):
        x = sen[i].dst
        for j in range(len(sen)):
            if sen[j].srcs == x:
                print(sen[i].st + ' ' + sen[j].st)
                G.edge(sen[i].st,sen[j].st)
G.render("output/44")
