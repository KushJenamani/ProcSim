from pipeline_register import ifid, idex;
from regfile import RegFile;
from alu import Alu;
from control import Control;

class Id:
    def __init__(self, regfile, inpipe: ifid, outpipe: idex):
        self.regfile = regfile;
        self._control = Control();
        self.inpipe = inpipe;
        self.outpipe = outpipe;

    def input(self):
        inst = self.inpipe.inst;

        opcode = inst[0:6];
        rs = inst[6:11];
        rt = inst[11:16];
        rd = inst[16:21];
        shamt = inst[21: 26];
        func = inst[26:32];
        imm = inst[16:32];
        jimm = inst[6:32];
    
        self.signalsObject = self._control.decidesignals(opcode, func);
        self.rs = rs;
        self.rt = rt;
        self.rd = rd;
