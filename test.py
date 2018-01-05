import re

st = 'Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of humani-computer interaction. Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.'

pat = re.compile(r'([A-Z].+?[\.;:\?!] )')

match = pat.split(st)

print(match)
