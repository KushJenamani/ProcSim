class ifid:
    def __init__(self):
        self.pc_4 = 0;
        self.inst = '';

class idex:
    def __init__(self):
        self.signalsObject;
        self.pc_4 = 0;

        self.rd1 = 0;
        self.rd2 = 0;
        self.imm = 0;
        self.shamt = 0;

        self.rs = 0;
        self.rt = 0;
        self.rd = 0;

    

class exmem:
    def __init__(self):
        self.signalsObject;

        self.bta = 0;           # BRANCH TARGET ADDRESS

        self.alures = 0;
        self.aluzero = 0;
        self.rd2 = 0;

        self.rd = 0;
        

class memwb:
    def __init__(self):
        self.signalsControl;
        self.rd = 0;
        self.memres = 0;
        self.alures = 0;