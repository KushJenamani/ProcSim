class Alu:
    #00 be add
    #01 be sub
    #10 be mul
    #11 be div
    #4 be sll

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
        
    
    def binToInt(bin:str):
        factor = 1
        if (bin[0] == 1):
            factor = -1
        
        num = 0
        for i in range(1, 32):
            num = 2 * num + int(bin[i])

        return factor * num

    def sll(a, b):
        ans = a << b
        #check if msb of a is 1
        #if it is 1 then interpret it as 2s complement

    exec = {
        0: lambda a, b: a + b,
        1: lambda a, b: a - b,
        2: lambda a, b: a * b,
        3: lambda a, b: a // b,
        4: lambda a, b: abs(a << b) \
            ,
    }

    zero: bool;

    def alu(self, op1, op2, aluop):
        res = (self.exec[aluop])(op1, op2);

        if (res == 0): self.zero = True;
        else: self.zero = False;

        return res;

    def zero(self):
        return self.zero;

al = Alu();
res = al.alu(2, 3, 0)
print(res)
