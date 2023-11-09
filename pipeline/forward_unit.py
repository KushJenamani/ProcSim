class Funit:
    def __init__(self, idex, exmem, memwb):
        self.idex = idex;
        self.exmem = exmem;
        self.memwb = memwb;

    def _l1_forward(self):
        rd_rs_same = self.exmem.rd == self.idex.rs and self.exmem.rd != 0;
        rd_rt_same = self.exmem.rd == self.idex.rt and self.exmem.rd != 0;

        if (self.exmem.regwrite and rd_rs_same):
            self.idex.rs = self.exmem.rd;

        if (self.exmem.regwrite and rd_rt_same):
            self.idex.rt = self.exmem.rd;

    def _l2_forward(self):
        rd_rs_same = self.memwb.rd == self.idex.rs and self.memwb.rd != 0 and self.memwb.rd != self.exmem.rd;
        rd_rt_same = self.memwb.rd == self.idex.rt and self.memwb.rd != 0 and self.memwb.rd != self.exmem.rd;

        if (self.memwb.regwrite and rd_rs_same):
            self.idex.rs = self.memwb.rd;

        if (self.memwb.regwrite and rd_rt_same):
            self.idex.rt = self.memwb.rd;

    def forward(self):
        self._l1_forward();
        self._l2_forward();
