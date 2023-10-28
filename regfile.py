import random

class RegFile: 
    reg = {0:0, 31:0}
    regWrite:bool;
    a1:int;
    a2:int;
    a3:int;

    def __init__(self):
        for i in range(1, 31):
            self.reg[i] = random.randint(-100, 100)

    def inputs(self, regWrite, a1, a2, a3, datain):
        self.regWrite = regWrite;
        self.a1 = a1;
        self.a2 = a2;
        self.a3 = a3;
    
        if self.memWrite:
            self.reg[a3] = datain;
        
    def rd1(self):
        return self.reg[self.a1];

    def rd2(self):
        return self.reg[self.a2];