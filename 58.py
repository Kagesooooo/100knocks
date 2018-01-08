import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

for sen in root.findall('document/sentences/sentence'):
    dic = {}
    dicn = {}
    dicd = {}
    for dep in sen.findall('dependencies[@type="collapsed-dependencies"]/dep'):
        if dep.get('type') in ['nsubj','dobj']:
            dic[dep.find('governor').get('idx')] = dep.find('governor').text
            if dep.get('type') == 'nsubj':
                dicn[dep.find('governor').get('idx')] = dep.find('dependent').text
            else:
                dicd[dep.find('governor').get('idx')] = dep.find('dependent').text

    for idx in sorted(dic.keys()):
        if idx in dicn.keys() and idx in dicd.keys():
            print(dicn[idx]+'\t'+dic[idx]+'\t'+dicd[idx])
