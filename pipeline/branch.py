class Branch:
    def __init__(self, pc, ifid, idex):
        self.pc = pc;
        self.ifid = ifid;
        self.idex = idex;

    def branch(self, bta):
        self.pc.set(bta);
        self.ifid.signalsObject.flush();
        self.idex.signalsObject.flush();