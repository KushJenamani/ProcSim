class DataMemory:
    mem = {}
    memRead: bool;
    memWrite: bool;
    address;

    def __init__(self, memRead, memWrite):
        self.memRead = memRead;
        self.memWrite = memWrite;
        self.address = 0;

    def inputs(self, memRead, memWrite, address, datain):
        self.memRead = memRead;
        self.memWrite = memWrite;
        self.address = address;
    
        if self.memWrite:
            self.mem[address] = datain;
        
    def output(self):
        if self.memRead:
            return self.mem.get(self.address, 0);
        else:
            raise("FileNotFoundError");


#Start from 4194304
class InstMemory:
    mem = {}
    def __init__(self, filename):
        file = open(filename)
        code = file.readlines()
        for i in range(len(code)):
            self.mem[4194304 + i*4] = code[i];


    def getInst(self, pc):
        return self.mem[pc];

    
        
