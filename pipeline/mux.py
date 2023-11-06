class Mux:
    def __init__(self, *inputs):
        self.inputs = inputs;
    
    def inputs(self, *inputs):
        self.inputs = inputs;

    def select(self, sel):
        self.sel = sel;

    def output(self):
        return self.inputs[self.sel];