from pipeline_register import ifid;

class If ():
    def __init__(self, pc, inst_mem, outpipe: ifid):
        self.pc = pc;
        self.inst_mem = inst_mem;
        self.outpipe = outpipe
    
    def binToInt(self, bin:str):
        factor = 1
        #treat all immidiates as signed 2s complement and opcodes and other stuff as unsigned
        if (type(bin) == type(1)):
            print("bin to int got an integer");
            return bin;
        
        if (bin[0] != '1' or len(bin) < 16):
            factor = +1  # changes made here
            num = 0
            for i in range(0, len(bin)):
                num = 2 * num + int(bin[i])  # changes made here

            return factor * num
        else:
            # print('here')
            num = 0
            for i in range(0, len(bin)-1):
                num = 2 * num + int(bin[i])
            num -= pow(2, len(bin)-1)
            return num
        
    def input(self):
        pass

    def output(self):
        print('pc =', self.pc.get())
        
        self.outpipe.inst = self.inst_mem.getInst(self.pc.get());
        print('instruction is: ', self.outpipe.inst)
        self.pc.set(self.pc.get() + 4);
        
        self.outpipe.end = self.outpipe.inst;       # outpipe inst has been intialized in this function before
        self.outpipe.pc_4 = self.pc.get();
    
        if (self.outpipe.inst[0:6] == '000010'):
            self.pc.set(self.binToInt(self.outpipe.inst[6:32] + '00'));
        
    def fetch(self):
        print('fetched ')
        self.output();
