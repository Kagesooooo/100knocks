import re

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def mk_morph():
    with open('neko.txt.cabocha') as f:
        sens = []
        sen_list = []
        for s in f:
            sen = re.split(r'[,\t ]',s[:-1])
            if sen[0] == '*':
                continue
            elif sen[0] == 'EOS':
                if len(sens)>0:
                    sen_list.append(sens)
                    sens = []
                continue
            else:
                morph = Morph(surface=sen[0],base=sen[7],pos=sen[1],pos1=sen[2])
                sens.append(morph)
        return sen_list
