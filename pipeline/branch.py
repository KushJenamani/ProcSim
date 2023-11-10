class Branch:
    def __init__(self, pc, ifid, idex):
        self.pc = pc;
        self.ifid = ifid;
        self.idex = idex;

    def branch(self, bta):
        self.pc.set(bta);
        print('bta: ',bta)
        self.ifid.inst = '0' * 32;
        self.idex.signalsObject.flush();