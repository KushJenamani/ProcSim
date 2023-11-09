from pipeline_register import exmem, memwb;
from memory import DataMemory;


class Mem:
    def __init__(self, mem: DataMemory, branchModule, inpipe: exmem, outpipe: memwb):
        self.mem = mem;
        self.exmem = exmem;
        self.memwb = memwb;
        self.branchModule = branchModule;

    def input(self):
        self.mem.inputs(self.inpipe.signalsObject.memread,
                        self.inpipe.signalsObject.memwrite,
                        self.inpipe.alures,
                        self.inpipe.rd2);
    
        self.memres = self.mem.output();

        # Branch
        if (self.inpipe.aluzero and self.inpipe.signalsObject.branch):
            self.branchModule.branch(self.inpipe.bta);
        

    def output(self):
        self.outpipe.memres = self.memres;
        self.outpipe.rd = self.inpipe.rd;
        self.outpipe.alures = self.inpipe.alures;