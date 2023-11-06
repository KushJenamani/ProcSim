from pipeline_register import idex, exmem;
from alu import Alu;
from mux import Mux;

class Ex:
    def __init__(self, alu, pc_alu, regdst: Mux, rsmux, rtmux, funit, inpipe, outpipe, exmem, memwb):
        self.alu = alu;
        self.pc_alu = pc_alu;
        self.regdst = regdst;
        self.rsmux = rsmux;
        self.rtmux = rtmux;
        self.funit = funit;
        self.inpipe = inpipe;
        self.outpipe = outpipe;
    
        self.exmem = exmem;
        self.memwb = memwb;

    def input(self):
        self.regdst.select(self.inpipe.signalsObject.regdst);   # Select regdst
        self.rsmux.inputs(self.inpipe.rd1, self.exmem.rd, self.memwb.rd);   # inputs to rsmux
        self.rtmux.inputs(self.inpipe.rd2, self.exmem.rd, self.memwb.rd);   # inputs to rtmux


