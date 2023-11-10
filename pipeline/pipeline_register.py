from control import SignalsObject

default_object = SignalsObject(regdst=False, regwrite= False, alusrc=False, alucontrol='0000', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
class ifid:
    def __init__(self):
        self.pc_4 = 0;
        self.inst = '0' * 32;
        

        self.end = False;

class idex:
    def __init__(self):
        self.signalsObject = default_object;
        self.pc_4 = 0;
        self.inst = '0' * 32;

        self.rd1 = 0;
        self.rd2 = 0;
        self.imm = '0000000000000000';
        self.shamt = 0;

        self.rs = 0;
        self.rt = 0;
        self.rd = 0;

        self.end = False;

    

class exmem:
    def __init__(self):
        self.signalsObject = default_object;
        self.inst = '0' * 32;
        self.bta = 0;           # BRANCH TARGET ADDRESS

        self.alures = 0;
        self.aluzero = 0;
        self.rd2 = 0;

        self.rd = 0;

        self.end = False;
        

class memwb:
    def __init__(self):
        self.signalsObject = default_object;
        self.inst = '0' * 32;
        self.rd = 0;
        self.inst = ''
        self.memres = 0;
        self.alures = 0;

        self.end = False;