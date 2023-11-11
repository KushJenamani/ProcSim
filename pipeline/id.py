from pipeline_register import ifid, idex;
from regfile import RegFile;
from alu import Alu;
from control import Control;

class Id:
    def __init__(self, regfile, hazard_unit, inpipe: ifid, outpipe: idex):
        self.regfile = regfile;
        self._control = Control();
        self.hazard_unit = hazard_unit;
        self.inpipe = inpipe;
        self.outpipe = outpipe;

    def input(self):
        if (self.inpipe.inst):
            inst = self.inpipe.inst;

            opcode = inst[0:6];
            rs = inst[6:11];
            rt = inst[11:16];
            rd = inst[16:21];
            shamt = inst[21: 26];
            func = inst[26:32];
            imm = inst[16:32];
            jimm = inst[6:32];

            self.pc_4 = self.inpipe.pc_4;
        
            self.signalsObject = self._control.decidesignals(opcode, func);
            self.rs = rs;
            self.rt = rt;
            self.rd = rd;
            self.shamt = shamt;
            self.imm = imm;
        

    def output(self):
        if self.inpipe.inst:
            self.outpipe.signalsObject = self.signalsObject;
            self.outpipe.pc_4 = self.pc_4;

            self.outpipe.rs = self.rs;
            self.outpipe.rt = self.rt;
            self.outpipe.rd = self.rd;
            
            self.outpipe.imm = self.imm;
            self.outpipe.shamt = self.shamt;

            self.outpipe.rd1 = self.rd1;
            self.outpipe.rd2 = self.rd2;
        
            self.outpipe.end = self.inpipe.end;
            self.outpipe.inst = self.inpipe.inst

    def decode(self):
        self.input();

        
        if self.inpipe.inst:
            self.regfile.inputs(False, self.rs, self.rt, self.rd);
            self.rd1 = self.regfile.rd1();
            self.rd2 = self.regfile.rd2();

        self.output();