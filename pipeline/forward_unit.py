class Funit:
    def __init__(self, idex, exmem, memwb):
        self.idex = idex;
        self.exmem = exmem;
        self.memwb = memwb;
    
    def getOp(self, inst, tag):
        opcode = inst[0:6];
        func = inst[26:32]

        operation = {
            'name':'---',
            'rs':'---',
            'rt':'---',
            'rd':'---',
            'imm': '---',
            'jimm': '---',
            'shamt':'---',
        }

        if(opcode == '000000'):
            #it is r type look at func field
            match func:
                case '000000':
                    # it is a sll
                    # print('sll')
                    operation['name'] = 'sll';
                case '100000':
                    #it is an add instruction
                    # print('add')
                    operation['name'] = 'add';
                case '100010':
                    #it is a subtract instruction
                    # print('sub')
                    operation['name'] = 'sub';
                case '100100':
                    # it is an and instruction
                    operation['name'] = 'and';
                case '100101':
                    # it is an or instructiion
                    operation['name'] = 'or';
                case '101010':
                    # it is a slt instruction
                    operation['name'] = 'slt';
                case '100111':
                    # it is a nor
                    operation['name'] = 'nor';
                case _:
                    print("wtf do you thing too much animosity")
                    exit('---')
            operation['rs'] = self.binToInt(inst[6:11]);
            operation['rt'] = self.binToInt(inst[11:16]);
            operation['rd'] = self.binToInt(inst[16:21]);
            operation['shamt'] = self.binToInt(inst[21:26]);
        else:         
            operation['rs'] = self.binToInt(inst[6:11]);
            operation['rt'] = self.binToInt(inst[11:16]);
            operation['imm'] = self.binToInt(inst[16:32]);
            #it is not r type:
            match opcode:
                case '001000':
                    # it is addi
                    # print('addi')
                    operation['name'] = 'addi';
                case '100011':
                    # it is lw
                    # print('lw')
                    operation['name'] = 'lw';
                case '101011':
                    # it is a sw
                    # print('sw')
                    operation['name'] = 'sw';
                case '000100':
                    # it is a beq
                    operation['name'] = 'beq';
                case '000101':
                    # it is a bne
                    operation['name'] = 'bne';
                case '000010':
                    # it is a j
                    operation['name'] = 'j';
                    operation['rt'] = '---';
                    operation['rs'] = '---';
                    operation['jimm'] = self.binToInt(inst[6:32]);
                case '011100':
                    operation['name'] = 'mul';
                    operation['rd'] = self.binToInt(inst[16:21]);
                case _:
                    print('that instruction does not exist')
                    print('opcode: ', opcode, 'func: ', func)

        operation['rs'] = str(operation['rs']) + ' = ' + self.regmap[operation['rs']];
        operation['rt'] = str(operation['rt']) + ' = ' + self.regmap[operation['rt']];
        operation['rd'] = str(operation['rd']) + ' = ' + self.regmap[operation['rd']];
            
        return operation
        

    def _l1_forward(self):
        rd_rs_same = self.exmem.rd == self.idex.rs and (self.exmem.rd != 0 and self.exmem.rd != '00000');
        rd_rt_same = self.exmem.rd == self.idex.rt and (self.exmem.rd != 0 and self.exmem.rd != '00000');
        
        if (self.exmem.signalsObject.regwrite and rd_rs_same):
            print('')
            print('L1 FORWARD: RS GETS EXMEM_RD');
            self.idex.rd1 = self.exmem.alures;

        if (self.exmem.signalsObject.regwrite and rd_rt_same):
            print('L1 FORWARD: RT GETS EXMEM_RD');
            self.idex.rd2 = self.exmem.alures;

    def _l2_forward(self):
        rd_rs_same = self.memwb.rd == self.idex.rs and (self.memwb.rd != 0 and self.memwb.rd != '00000');
        rd_rt_same = self.memwb.rd == self.idex.rt and (self.memwb.rd != 0 and self.memwb.rd != '00000');

        if (self.memwb.signalsObject.regwrite and rd_rs_same):
            print('')
            print('L2 FORWARD: RS GETS MEMWB_RD');
            self.idex.rd1 = self.memwb.alures;
            if(self.memwb.signalsObject.memread):
                self.idex.rd1 = self.memwb.memres;

        if (self.memwb.signalsObject.regwrite and rd_rt_same):
            print('L2 FORWARD: RT GETS MEMWB_RD');
            self.idex.rd2 = self.memwb.alures;
            if(self.memwb.signalsObject.memread):
                self.idex.rd2 = self.memwb.memres;

    def forward(self):
        self._l2_forward();
        self._l1_forward();
