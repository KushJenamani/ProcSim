from pipeline_register import exmem, memwb;
from memory import DataMemory;


class Mem:
    def __init__(self, mem: DataMemory, branchModule, inpipe: exmem, outpipe: memwb):
        self.mem = mem;
        self.exmem = inpipe;
        self.memwb = outpipe;
        self.inpipe = inpipe;
        self.outpipe = outpipe;
        self.branchModule = branchModule;

    def input(self):
        
        if self.inpipe.signalsObject:
            self.mem.inputs(self.inpipe.signalsObject.memread,
                            self.inpipe.signalsObject.memwrite,
                            self.inpipe.alures,
                            self.inpipe.rd2);
        
            self.memres = self.mem.output();

            # Branch
            if (self.inpipe.aluzero and self.inpipe.signalsObject.branch):
                self.branchModule.branch(self.inpipe.bta);
            

    def output(self):
        
        if self.inpipe.signalsObject:
            self.outpipe.signalsObject = self.inpipe.signalsObject;
            self.outpipe.memres = self.memres;
            self.outpipe.rd = self.inpipe.rd;
            self.outpipe.alures = self.inpipe.alures;
        
            self.outpipe.end = self.inpipe.end;
            self.outpipe.inst = self.inpipe.inst
        print('mem done for', self.inpipe.inst)

    def access(self):
        self.input();
        self.output();