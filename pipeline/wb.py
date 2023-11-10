
class Wb:
    def __init__(self, regfile, inpipe):
        self.regfile = regfile;
        self.inpipe = inpipe;

    def input(self):
        if self.inpipe.signalsObject:
            if (self.inpipe.signalsObject.mem2reg == True):
                self.result = self.inpipe.memres;
            else:
                self.result = self.inpipe.alures;

    def output(self):
        if self.inpipe.signalsObject and self.inpipe.rd != 0:
            self.regfile.write(self.inpipe.signalsObject.regdst, self.result, self.inpipe.rd);

    def writeBack(self):
        self.input();
        self.output();
        return self.inpipe.end;