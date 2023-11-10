from pipeline_register import idex, ifid;
import pc;

class Hazard:
    def __init__(self, pc: pc, ifid: ifid, idex: idex):
        self.pc = pc;
        self.ifid = ifid;
        self.idex = idex;

    def stall(self):
        self.pc.set(self.pc.get() - 4);
        self.idex.signalsObject.flush();

    def detect(self):
        if (self.idex.signalsObject and self.idex.signalsObject.memread):
            if (self.ifid.inst[6:11] == self.idex.rd or self.ifid.inst[11:16] == self.idex.rd):
                self.stall()
