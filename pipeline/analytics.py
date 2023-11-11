class Analytics:
    regmap = {
        0: '$zero',
        1: 'at',
        2: 'v0',
        3: 'v1',
        4: 'a0',
        5: 'a1',
        6: 'a2',
        7: 'a3',
        8: 't0',
        9: 't1',
        10: 't2',
        11: 't3',
        12: 't4',
        13: 't5',
        14: 't6',
        15: 't7',
        16: 's0',
        17: 's1',
        18: 's2',
        19: 's3',
        20: 's4',
        21: 's5',
        22: 's6',
        23: 's7',
        24: 't8',
        25: 't9',
        26: 'k0',
        27: 'k1',
        28: 'gp',
        29: 'sp',
        30: 'fp',
        31: 'ra',
        '---': ''
    }

    def __init__(self, if_mod, id, ex, mem, wb, ifid, idex, exmem, memwb):
        self.if_mod = if_mod;
        self.id = id;
        self.ex = ex;
        self.mem = mem;
        self.wb = wb;
        self.ifid = ifid;
        self.idex = idex;
        self.exmem = exmem;
        self.memwb = memwb;    

    def binToInt(self, bin:str):
        factor = 1
        #treat all immidiates as signed 2s complement and opcodes and other stuff as unsigned
        
        if (bin[0] != '1' or len(bin) < 16):
            factor = +1  # changes made here
            num = 0
            for i in range(0, len(bin)):
                num = 2 * num + int(bin[i])  # changes made here

            return factor * num
        else:
            # print('here')
            num = 0
            for i in range(0, len(bin)-1):
                num = 2 * num + int(bin[i])
            num -= pow(2, len(bin)-1)
            return num
        

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
                case _:
                    print('that instruction does not exist')
                    print('opcode: ', opcode, 'func: ', func)

        operation['rs'] = str(operation['rs']) + ' = ' + self.regmap[operation['rs']];
        operation['rt'] = str(operation['rt']) + ' = ' + self.regmap[operation['rt']];
        operation['rd'] = str(operation['rd']) + ' = ' + self.regmap[operation['rd']];
            
        return operation
        

    def dumpPipes(self):
        ifidop = self.getOp(self.ifid.inst, 'ifid');
        idexop = self.getOp(self.idex.inst, 'idex');
        exmemop = self.getOp(self.exmem.inst, 'exmem');
        memwbop = self.getOp(self.memwb.inst, 'memwb');

        ops = {
            'ifidop':ifidop,
            'idexop':idexop,
            'exmemop':exmemop,
            'memwbop':memwbop
        }
        fields = ['name', 'rs', 'rt', 'rd', 'imm', 'jimm', 'shamt'];


        for i in range(7):
            print(f"{fields[i]:<{7}} : ", end='');
            for k, v in ops.items():
                string = str(v[fields[i]]);
                if (fields[i] == 'rs' or fields[i] == 'rt' or fields[i] == 'rd'):
                    print(f"{string:<{10}} | ", end="");
                else:
                    print(f"{string:<{10}} | ", end="");
            print();
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n');

        pipes = [self.ifid, self.idex, self.exmem, self.memwb];
        wish = ['rd1', 'rd2', 'alures', 'aluzero', 'imm', 'bta']

        for w in wish:
            print(f"{w:<{7}} : ", end='');
            for p in pipes:
                if hasattr(p, w):
                    if (w == 'imm'):
                        print(f"{str(self.binToInt(getattr(p, w))):<{10}} | ", end="");
                    else:
                        print(f"{str(getattr(p, w)):<{10}} | ", end='');
                else:
                    print(f"{'---':<{10}} | ", end="");
            print();
        print('\n');

        
