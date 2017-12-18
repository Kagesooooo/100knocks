import re

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def is_noun(self):
        return self.pos=='名詞'
    def is_verb(self):
        return self.pos=='動詞'
    def is_par(self):
        return self.pos=='助詞'
    def __str__(self):
        return '{}'.format(self.surface)

class Chunk:
    def __init__(self,morphs,dst,num,srcs):
        self.morphs = morphs
        self.dst = dst
        self.num = num
        self.st = ''
        self.srcs = srcs
        for v in self.morphs:
            self.st += str(v)
    def has_noun(self):
        flag = False
        for m in self.morphs:
            if m.is_noun():
                flag = True
                break
        return flag
    def has_verb(self):
        flag = False
        for v in self.morphs:
            if v.is_verb():
                flag =  True
                break
        return flag
    def has_particle(self):
        flag = False
        for p in self.morphs:
            if p.is_par():
                flag = True
                break
        return flag
    def has_sahen(self):
        flag = False
        for s in self.morphs:
            if s.pos1 == 'サ変接続':
                flag = True
                break
        return flag
    def right_par(self):
        for p in self.morphs:
            if p.is_par():
                return p.base
    def left_verb(self):
        for v in self.morphs:
            if v.is_verb():
                return v.base
    def rpl_noun(self):
        st = ''
        flag = False
        for v in self.morphs:
            if v.pos == '名詞':
                if flag:
                    continue
                else:
                    st += 'X'
                    flag = True
            else:
                st += v.surface
        return st
    def __str__(self):
        return 'morphs: {}, dst: {}, srcs: {}'.format(self.st,self.dst,self.srcs)

def mk_chunk(file_name):
    with open(file_name) as f:
        sens = []
        sen_list = []
        morphs0 = []
        for s in f:
            sen = re.split(r'[,\t ]',s[:-1])
            if sen[0] == '*':
                if len(morphs0) > 0:
                    srcs0 = []
                    for s in sens:
                        if num0 == s.dst:
                            srcs0.append(int(s.num))
                    chunk = Chunk(morphs=morphs0,dst=dst0,num=num0,srcs=srcs0)
                    morphs0 = []
                    sens.append(chunk)
                dst0 = int(sen[2][:-1])
                num0 = int(sen[1])
                continue
            elif sen[0] == 'EOS':
                if len(morphs0) > 0:
                    srcs0 = []
                    for s in sens:
                        if num0 == s.dst:
                            srcs0.append(int(s.num))
                    chunk = Chunk(morphs=morphs0,dst=dst0,num=num0,srcs=srcs0)
                    morphs0 = []
                    sens.append(chunk)
                if len(sens)>0:
                    sen_list.append(sens)
                    sens = []
                continue
            else:
                if sen[1] == '記号':
                    continue
                morph = Morph(surface=sen[0],base=sen[7],pos=sen[1],pos1=sen[2])
                morphs0.append(morph)
        return sen_list
