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
            if (self.inpipe.signalsObject.alucontrol == "1111"):
                self.rd1 = self.rd2;
                self.rd2 = self.inpipe.shamt;
            
            # WHEN IMM FIELD IS TO BE USED
            if (self.inpipe.signalsObject.alusrc):
                self.rd2 = self.inpipe.imm;
            
            # ALU ACTION
            self.res = self.alu.alu(self.rd1, self.rd2, self.inpipe.signalsObject.alucontrol);
            self.zero = self.alu.getzero();

            # PC ALU ACTION
            print('HERE IS YOUR IMM \n \n' + self.inpipe.imm);
            print('we passed to the alu: ', self.inpipe.pc_4, self.inpipe.imm * 4)
            self.pc_res = self.pc_alu.alu(self.inpipe.pc_4, self.inpipe.imm * 4, '0010');
        
            if (self.inpipe.signalsObject.regdst == True):
                self.rd = self.inpipe.rd;
            else:
                self.rd = self.inpipe.rt;

        

    def output(self):
        if self.inpipe.signalsObject:
            self.outpipe.signalsObject = self.inpipe.signalsObject;

            self.outpipe.bta = self.pc_res;

            self.outpipe.alures = self.res;
            self.outpipe.aluzero = self.zero;
            self.outpipe.rd2 = self.inpipe.rd2; # NOT self.rd2, IT CAN BE OVERWRITTEN WITH IMM OR SHAMT..

            self.outpipe.rd = self.rd;
        
            self.outpipe.end = self.inpipe.end;
            print('ex done for', self.inpipe)
            self.outpipe.inst = self.inpipe.inst

    def execute(self):
        self.input();
        self.output();



        



