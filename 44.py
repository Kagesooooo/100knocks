import func4
from graphviz import Digraph

G = Digraph(format="png")
G.attr("node", shape="circle")

list0 = func4.mk_chunk('neko.txt.cabocha')

for sen in list0[:5]:
    for c0 in sen:
        for c1 in sen:
            if c1.num in c0.srcs:
                G.edge(c1.st,c0.st)


G.render("output/44")
