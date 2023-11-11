class Alu:
    #00 be add
    #01 be sub
    #10 be mul
    #11 be div
    #4 be sll

    def f1(a, b): 
        if a < b: 
            return 1 
        else: 
            return 0
    
    def f2(a, b):
        return a * pow(2, b)  # shift left is same as mult by a power of 2

    def intToBin(num:int):
        bin:str = ""
        num2 = num
        while num:
            if (num % 2):
                bin = '1' + bin
            else:
                bin = '0' + bin
            num //= 2

        while (len(bin) < 32):
            bin = '0' + bin
        if num2 > 0:
            return bin
        else:
            return bin
        
    # def binToInt(bin:str):
    #     factor = 1
    #     if (bin[0] == 1):
    #         factor = -1
        
    #     num = 0
    #     for i in range(1, len(bin)):
    #         num = 2 * num + int(bin[i])

    #     return factor * num
    
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
        
    def sll(a, b):
        ans = a << b
        #check if msb of a is 1
        #if it is 1 then interpret it as 2s complement

    exec = {
        '0010': lambda a, b: a + b,
        '0110': lambda a, b: a - b,
        '0000':  lambda a, b: a & b,
        '0001': lambda a, b: a | b,
        '0111': f1, # this is set on less than
        '1111': f2,# this is sll
        '1110': lambda a, b: a * b,
        2: lambda a, b: a * b,
        3: lambda a, b: a // b,
        4: lambda a, b: abs(a << b),
    }

    zero: bool;

    def alu(self, op1, op2, aluop):
        if(type(op1) != type(1)):
            op1 = self.binToInt(op1)
        if(type(op2) != type(1)):
            op2 = self.binToInt(op2)
        res = (self.exec[aluop])(op1, op2);
        print("res:", res, "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        if (res == 0): self.zero = True;
        else: self.zero = False;

        return res;

    def getzero(self):
        return self.zero;

# al = Alu();
# res = al.alu(2, 3, '0010')
# print(res)
# print(al.binToInt('1111111'))
