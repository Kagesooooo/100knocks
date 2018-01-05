from graphviz import Digraph
import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

G = Digraph(format="png")
G.attr("node", shape="circle")

for sen in root.findall('document/sentences/sentence/dependencies[@type="collapsed-dependencies"]')[:1]:
    for dep in sen.findall('dep'):
        if dep.get('type') != 'punct':
            x = dep.find('governor').get('idx')
            y = dep.find('dependent').get('idx')
            G.node(x,dep.find('governor').text)
            G.node(y,dep.find('dependent').text)
            G.edge(x,y)

G.render("output/57")
