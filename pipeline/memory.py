class DataMemory:
    mem = {}
    memRead: bool;
    memWrite: bool;
    address: str;

    def __init__(self):
        self.memRead = False;
        self.memWrite = False;
        self.address = 0;

    def inputs(self, memRead, memWrite, address, datain):
        self.memRead = memRead;
        self.memWrite = memWrite;
        self.address = address;
    
        if self.memWrite:
            self.mem[address] = datain;
            print("wrote", datain, "to address", address)
        
    def output(self):
        if self.memRead:
            return self.mem.get(self.address, 1000);
        else:
            # print("Ohhhh yeahhh!!!")
            pass
    
    def printstuff(self):
        for (key, value) in self.mem.items():
            print(str(key)+": "+str(value), end=', ')
        print('----------------')
        

#Start from 4194304
class InstMemory:
    mem = {}
    def __init__(self, filename):
        file = open(filename)
        code = file.readlines()
        for i in range(len(code)):
            self.mem[4194304 + i*4] = code[i];
        # else:
        #     self.mem = "EXEC DONE"
        print('length of inst_mem is; ', len(self.mem))

    def getInst(self, pc):
        if (pc in self.mem):
            return self.mem[pc];
        else:
            return '1' * 32;

    
        
