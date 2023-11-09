from pipeline_register import ifid;

class If ():
    def __init__(self, pc, inst_mem):
        self.pc = pc;
        self.inst_mem = inst_mem;
    
    def input(self, pipe):
        pass

    def output(self, pipe: ifid):
        pipe.inst = self.inst_mem.getInst(self.pc);
        self.pc += 4;
        
        pipe.pc_4 = self.pc;
        
    def fetch(self):
        self.output();
