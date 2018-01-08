import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

dic = {}
for coref in root.findall('document/coreference/coreference'):
    for men in coref.findall('mention'):
        if men.get('representative','false') == 'true':
            word = men.find('text').text
            dic[word] = {}
            dic[word]['sentence'] = []
            dic[word]['start'] = []
            dic[word]['end'] = []
        else:
            dic[word]['sentence'].append(int(men.find('sentence').text)-1)
            dic[word]['start'].append(int(men.find('start').text)-1)
            dic[word]['end'].append(int(men.find('end').text)-1)

for i, sens in enumerate(root.findall('document/sentences/sentence')):
    sen = ''
    for j, tok in enumerate(sens.findall('tokens/token')):
        for word in dic:
            for k in range(len(dic[word]['sentence'])):
                if i == dic[word]['sentence'][k]:
                    if j == dic[word]['start'][k]:
                        sen += '[' + word + '('
                    if j == dic[word]['end'][k]:
                        sen = sen[:-1] + ')]' + ' '
        sen += tok.find('word').text + ' '
    print(sen[:-1])
