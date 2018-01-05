import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

for child in root.iter('token'):
    print(child.find('word').text+'\t'+child.find('lemma').text+'\t'+child.find('POS').text)
