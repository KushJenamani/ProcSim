from pipeline_register import idex, exmem;
from alu import Alu;
from mux import Mux;
from forward_unit import Funit;

class Ex:
    def __init__(self, alu: Alu, pc_alu: Alu, funit: Funit, inpipe:idex, outpipe:exmem):
        self.alu = alu;
        self.pc_alu = pc_alu;
        self.funit = funit;
        self.inpipe = inpipe;
        self.outpipe = outpipe;

    def input(self):
        if self.inpipe.signalsObject:
            self.funit.forward();

            self.rd1 = self.inpipe.rd1;
            self.rd2 = self.inpipe.rd2;

            # IF WE ENCOUNTER SLL
            if (self.inpipe.signalsControl.aluop == "1111"):
                self.rd1 = self.rd2;
                self.rd2 = self.inpipe.shamt;
            
            # WHEN IMM FIELD IS TO BE USED
            if (self.inpipe.signalsControl.aluSrc):
                self.rd2 = self.inpipe.imm;
            
            # ALU ACTION
            self.res = self.alu(self.rd1, self.rd2, self.inpipe.signalsControl.aluSrc);
            self.zero = self.alu.getzero();

            # PC ALU ACTION
            self.pc_res = self.pc_alu(self.pc, self.imm + '00', '0010');
        
            if (self.signalsObject.regdst == True):
                self.rd = self.inpipe.rd;
            else:
                self.rd = self.inpipe.rt;

        

    def output(self):
        if self.inpipe.signalsObject:
            self.outpipe.signalsObject = self.signalsObject;

            self.outpipe.bta = self.res;

            self.outpipe.alures = self.res;
            self.outpipe.aluzero = self.zero;
            self.outpipe.rd2 = self.inpipe.rd2; # NOT self.rd2, IT CAN BE OVERWRITTEN WITH IMM OR SHAMT..

            self.outpipe.rd = self.rd;
        
            self.outpipe.end = self.inpipe.end;

    def execute(self):
        self.input();
        self.output();



        



