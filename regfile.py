import random
import alu
class RegFile: 
    reg = {0:0, 31:0}
    regWrite:bool;
    a1:int;
    a2:int;
    a3:int;
    
    def __init__(self):
        for i in range(1, 31):
            self.reg[i] = -1

    def inputs(self, regWrite, a1, a2, a3, datain  = 0):
        self.regWrite = regWrite;
        self.a1 = a1;
        self.a2 = a2;
        self.a3 = a3;
    
        if self.regWrite:
            self.reg[a3] = datain
            print("wrote", datain,"to", self.a3)

    def getreg(self, val):
        return self.reg[val]
    def rd1(self):
        return self.reg[self.a1];

    def rd2(self):
        return self.reg[self.a2];

    def write(self, regWrite, datain):
        if self.regWrite:
            self.reg[self.a3] = datain
            print("wrote", datain,"to", self.a3)

    def printstuff(self):
        for (key, value) in self.reg.items():
            print(str(key)+": "+str(value))
        print('----------------')