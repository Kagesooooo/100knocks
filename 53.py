import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

for child in tree.iter('word'):
    print(child.text)
