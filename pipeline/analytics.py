class Analytics:
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
            'shamt':'---'
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
                case _:
                    print('that instruction does not exist')
                    print('opcode: ', opcode, 'func: ', func)
            
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
            print(f"{fields[i]:<{6}} : ", end='');
            for k, v in ops.items():
                string = str(v[fields[i]]);
                if (fields[i] == 'rs' or fields[i] == 'rt' or fields[i] == 'rd'):
                    print(f"{string:<{10}} | ", end="");
                else:
                    print(f"{string:<{10}} | ", end="");
            print();

        print('\n');

        
