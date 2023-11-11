

'''     CRITICAL CHANGE      '''

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
        self.alu = alu.Alu()
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.regWrite = False

    def inputs(self, regWrite, a1, a2, a3, datain  = 0): # a1, a2 and a3 need to be integers after they come here
        self.a1 = a1;
        self.a2 = a2;
        self.a3 = a2;
        self.regWrite = regWrite;
        if(type(a1) != type(1)):
            self.a1 = self.alu.binToInt(a1);
        if(type(a2) != type(1)):
            self.a2 = self.alu.binToInt(a2);
        if(type(a3) != type(1)):
            self.a3 = self.alu.binToInt(a3);
    
        if self.regWrite and self.a3 != 0:
            self.reg[self.a3] = datain
            print("wrote", datain,"to", self.a3)

        
    def rd1(self):
        return self.reg[self.a1];

    def rd2(self):
        return self.reg[self.a2];

    def write(self, regWrite, datain, a3 = 0):
        self.regWrite = regWrite;       ## MADE A CRUCIAL CHANGE HERE, CONFIRM WITH PRAT

        if (type(a3) != type(1)):
            a3 = self.alu.binToInt(a3);
        
        if self.regWrite and a3 != 0:
            self.reg[a3] = datain
            print("wrote", datain,"to", a3)
    
    # def write(self, regWrite, datain):
    #     self.regWrite = regWrite;       ## MADE A CRUCIAL CHANGE HERE, CONFIRM WITH PRAT

    #     if self.regWrite:
    #         self.reg[self.a3] = datain
    #         print("wrote", datain,"to", self.a3)

    def printstuff(self):
        for (key, value) in self.reg.items():
            print(str(key)+": "+str(value), end=', ')
        print('----------------')