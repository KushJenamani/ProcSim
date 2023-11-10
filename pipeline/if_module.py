from pipeline_register import ifid;

class If ():
    def __init__(self, pc, inst_mem, outpipe: ifid):
        self.pc = pc;
        self.inst_mem = inst_mem;
        self.outpipe = outpipe
    
    def input(self, pipe):
        pass

    def output(self):
        print('pc =', self.pc.get())
        self.outpipe.inst = self.inst_mem.getInst(self.pc.get());
        print('instruction is: ', self.outpipe.inst)
        self.pc.set(self.pc.get() + 4);
        
        self.outpipe.end = self.outpipe.inst == '0'*32;       # outpipe inst has been intialized in this function before
        self.outpipe.pc_4 = self.pc.get();
        
    def fetch(self):
        print('fetched ')
        self.output();
