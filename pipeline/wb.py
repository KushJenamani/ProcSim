
class Wb:
    def __init__(self, regfile, inpipe):
        self.regfile = regfile;
        self.inpipe = inpipe;

    def input(self):
        if self.inpipe.signalsObject:
            if (self.inpipe.signalsControl.mem2reg == True):
                self.result = self.inpipe.memres;
            else:
                self.result = self.inpipe.alures;

    def output(self):
        if self.inpipe.signalsObject:
            self.regfile.write(self.inpipe.regdst, self.result);

    def writeBack(self):
        self.input();
        self.output();
        return self.inpipe.end;