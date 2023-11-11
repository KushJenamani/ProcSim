class Funit:
    def __init__(self, idex, exmem, memwb):
        self.idex = idex;
        self.exmem = exmem;
        self.memwb = memwb;

    def _l1_forward(self):
        rd_rs_same = self.exmem.rd == self.idex.rs and (self.exmem.rd != 0 and self.exmem.rd != '00000');
        rd_rt_same = self.exmem.rd == self.idex.rt and (self.exmem.rd != 0 and self.exmem.rd != '00000');
        
        if (self.exmem.signalsObject.regwrite and rd_rs_same):
            print('L1 FORWARD: RS GETS EXMEM_RD');
            self.idex.rd1 = self.exmem.alures;

        if (self.exmem.signalsObject.regwrite and rd_rt_same):
            print('L1 FORWARD: RT GETS EXMEM_RD');
            self.idex.rd2 = self.exmem.alures;

    def _l2_forward(self):
        rd_rs_same = self.memwb.rd == self.idex.rs and (self.memwb.rd != 0 and self.memwb.rd != '00000');
        rd_rt_same = self.memwb.rd == self.idex.rt and (self.memwb.rd != 0 and self.memwb.rd != '00000');

        if (self.memwb.signalsObject.regwrite and rd_rs_same):
            print('L2 FORWARD: RS GETS MEMWB_RD');
            self.idex.rd1 = self.memwb.alures;

        if (self.memwb.signalsObject.regwrite and rd_rt_same):
            print('L2 FORWARD: RT GETS MEMWB_RD');
            self.idex.rd2 = self.memwb.alures;

    def forward(self):
        self._l2_forward();
        self._l1_forward();
