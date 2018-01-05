import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

for child in root.iter('token'):
    if child.find('NER').text == 'PERSON':
        print(child.find('word').text)
