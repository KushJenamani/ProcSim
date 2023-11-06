class Funit:
    def __init__(self, ifex, exmem, memwb, rsmux, rtmux):
        self.ifex = ifex;
        self.exmem = exmem;
        self.memwb = memwb;
        self.rsmux = rsmux;
        self.rtmux = rtmux;

    def _l1_forward(self):
        rd_rs_same = self.exmem.rd == self.ifex.rs and self.exmem.rd != 0;
        rd_rt_same = self.exmem.rd == self.ifex.rt and self.exmem.rd != 0;

        if (self.exmem.regwrite and rd_rs_same):
            self.rsmux.select(1);
        else:
            self.rsmux.select(0);

        if (self.exmem.regwrite and rd_rt_same):
            self.rtmux.select(1);
        else:
            self.rtmux.select(0);

    def _l2_forward(self):
        rd_rs_same = self.memwb.rd == self.ifex.rs and self.memwb.rd != 0 and self.memwb.rd != self.exmem.rd;
        rd_rt_same = self.memwb.rd == self.ifex.rt and self.memwb.rd != 0 and self.memwb.rd != self.exmem.rd;

        if (self.memwb.regwrite and rd_rs_same):
            self.rsmux.select(2);
        else:
            self.rsmux.select(0);

        if (self.memwb.regwrite and rd_rt_same):
            self.rtmux.select(2);
        else:
            self.rtmux.select(0);

    def forward(self):
        self._l1_forward();
        self._l2_forward();
