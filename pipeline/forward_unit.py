class Funit:
    def __init__(self, idex, exmem, memwb):
        self.idex = idex;
        self.exmem = exmem;
        self.memwb = memwb;

    def _l1_forward(self):
        rd_rs_same = self.exmem.rd == self.idex.rs and (self.exmem.rd != 0 and self.exmem.rd != '00000');
        rd_rt_same = self.exmem.rd == self.idex.rt and (self.exmem.rd != 0 and self.exmem.rd != '00000');
        
        if (self.exmem.signalsObject.regwrite and rd_rs_same):
            self.idex.rd1 = self.exmem.alures;

        if (self.exmem.signalsObject.regwrite and rd_rt_same):
            self.idex.rd2 = self.exmem.alures;

    def _l2_forward(self):
        rd_rs_same = self.memwb.rd == self.idex.rs and (self.memwb.rd != 0 and self.exmem.rd != '00000') and self.memwb.rd != self.exmem.rd;
        rd_rt_same = self.memwb.rd == self.idex.rt and (self.memwb.rd != 0 and self.exmem.rd != '00000') and self.memwb.rd != self.exmem.rd;

        if (self.memwb.signalsObject.regwrite and rd_rs_same):
            self.idex.rd1 = self.memwb.alures;

        if (self.memwb.signalsObject.regwrite and rd_rt_same):
            self.idex.rd2 = self.memwb.alures;

    def forward(self):
        self._l1_forward();
        self._l2_forward();
