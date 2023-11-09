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
        if (self.idex.signalsObject.memread):
            if (self.ifid.rs == self.idex.rd or self.ifid.rt == self.idex.rd):
                self.stall()
