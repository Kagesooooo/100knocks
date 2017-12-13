import re

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def __str__(self):
        return '{}'.format(self.surface)

class Chunk:
    def __init__(self,morphs,dst,srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
    def __str__(self):
        return 'morphs: {}, dst: {}, srcs: {}'.format([str(v) for v in self.morphs],self.dst,self.srcs)

def mk_chunk(file_name):
    with open(file_name) as f:
        sens = []
        sen_list = []
        morphs0 = []
        for s in f:
            sen = re.split(r'[,\t ]',s[:-1])
            if sen[0] == '*':
                if len(morphs0) > 0:
                    chunk = Chunk(morphs=morphs0,dst=dst0,srcs=srcs0)
                    morphs0 = []
                    sens.append(chunk)
                dst0 = sen[2][:-1]
                srcs0 = sen[1]
                continue
            elif sen[0] == 'EOS':
                if len(morphs0) > 0:
                    chunk = Chunk(morphs=morphs0,dst=dst0,srcs=srcs0)
                    morphs0 = []
                    sens.append(chunk)
                if len(sens)>0:
                    sen_list.append(sens)
                    sens = []
                continue
            else:
                morph = Morph(surface=sen[0],base=sen[7],pos=sen[1],pos1=sen[2])
                morphs0.append(morph)
        return sen_list
