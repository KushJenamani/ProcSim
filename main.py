import control
import pc
import memory
import regfile
import control
from control import SignalsObject 
import alu
from alu import Alu
import os
# note that rs is never used in shift left logical
# note that if we have a binary string with starting bit as 1 then we need to treat it as 2s complement more times than not

filename = 'bytecode.txt'
# instantiate all objects
datamem1  = memory.DataMemory();
instmem1 = memory.InstMemory(filename); # now instruction memory has all the required instuctions
regfile1 = regfile.RegFile();
pc1 = pc.PC(0);
control1 = control.Control();
alu1 = alu.Alu();
alutmp = alu.Alu()

#take inputs (the numbers to sort)

print('Enter the number of elements to be sorted');
n = int(input())
regfile1.inputs(regWrite=True, a1 = 0, a2 = 0, a3 = 9, datain = n)
# n = 4

# inp = [4, 3, 6, 8]
inp = []
out = []
a = 0
print("Enter the starting address for input");
start_addr = int(input())
regfile1.inputs(regWrite = True, a1 = 0, a2 = 0, a3 = 10, datain  = start_addr)
print("Enter the output address");
end_addr = int(input());
regfile1.inputs(regWrite = True, a1 = 0, a2 = 0, a3 = 11, datain  = end_addr)

print("enter the numbers to be sorted\n")
for i in range(n):
    a = int(input());
    inp.append(a);
    # the numbers must also be stored at the starting address
    datamem1.inputs(memRead=False, memWrite=True, address=start_addr+i*4, datain=a)


# now instruction memory has all the instructions 

init = len(instmem1.mem)
# the program will end when pc points to some address value that hasn't been put in the instruction memory's dictionary
pc1.set(4194304)  # initialize pc to the first instruction in codespace


    # branch: bool     --
    # jump: bool       --
    # alusrc: bool     --
    # alucontrol: str  --
    # memread: bool    
    # memwrite: bool   
    # regwrite: bool   
    # regdst: bool     --
    # mem2reg: bool    --

iter = 0
while True:
    print('iter', iter)
    iter+=1
    print('pc is', pc1.get())
    try:
        inst = instmem1.getInst(pc1.get())
        if(pc1.get() > 4194448):
            print(" inst is ", inst)
    except:
        print('broke due to catch')
        break
    
    # print("the fetched instruction is", inst, "hello")
    # now I have the entire instruction in binary
    # let me look at the opcode and figure out what to do
    # i can get all the control signals using control.py
    opcode = inst[0:6]
    rs = inst[6:11]
    rt = inst[11:16]
    rd = inst[16:21]
    shamt = inst[21: 26]
    func = inst[26:32]
    imm = inst[16:32]
    jimm = inst[6:32] ##########################################################################################fetch ends here
    print(rs, rt, rd, imm)
    # so1 = SignalsObject() # signals object
    so1 = control1.decidesignals(inst[0:6], inst[26:32])  ######################################################decode ends here
    # print(so1)
    # I need to figure out based on the control signals what field goes to what port, ignore sll for now
    a3 = 0
    regfile1.inputs(regWrite = False, a1 = alutmp.binToInt(rs), a2 = alutmp.binToInt(rt), a3 = alutmp.binToInt(str(a3)), datain = 0)
    operand1 = regfile1.rd1()
    operand2 = regfile1.rd2()  #operand2 could also be the immidiate field
    if(opcode != '000000' and not so1.branch):
        operand2 = imm  # if it is not r type and it is not a branch then second operand is imm  
    alures = 0
    memout = 0
    regwrdata = 0
    print('operands: ', operand1, operand2)
    if(so1.branch):
        print('branch statement')
        pc1.set(pc1.get() + 4)
        alu2 = Alu()
        res = alu1.alu(operand1, operand2, so1.alucontrol)  # subtract them
        print(operand1, operand2, "----------------------------------------------------------------------------------------")
        if(alu1.getzero() and opcode == '000100'):
            print('beq is  goind to branch!!!')
            # use alu2 to calculate 4 times the immediate value and add it to pc
            reqloc = alu2.alu(op1 = pc1.get(), op2 = alu2.binToInt(imm)*4, aluop='0010')
            pc1.set(reqloc)
            continue
        elif(not alu1.getzero() and opcode == '000101'):
            print('bne is goind to branch!!')
            reqloc = alu2.alu(op1 = pc1.get(), op2 = alu2.binToInt(imm)*4, aluop='0010')
            pc1.set(reqloc)
            continue
        else:
            print("not here===============================================================")
            continue

    elif so1.jump:
        alu2 = Alu()
        reqloc = alu2.binToInt('0000' + jimm + '00')
        pc1.set(reqloc)
        continue
    else:
        if(opcode == '000000' and func == '000000'):
            # it is a sll
            operand1 = regfile1.rd2()
            operand2 = shamt
        elif(so1.alusrc):
            # take data from imm
            operand2 = imm 
            pass
        else:
            # take data from rd2 of register file
            operand2 = regfile1.rd2()
            pass
        if(so1.regdst):
            # dest is rt or rd, rd for add
            # print("a3 is", rd)
            a3 = alutmp.binToInt(rd) # the register file's third input port
            # print("a3 is", a3)
            pass
        else:
            # rt for lw and sw
            # print("a3 is", rt)
            a3 = alutmp.binToInt(rt)# the register file's third input port
            # print("a3 is", a3)
            pass

        
        alures = alu1.alu(operand1, operand2, so1.alucontrol) ################################################################## execute ends here
        datamem1.inputs(memRead=so1.memread, memWrite=so1.memwrite, address=alures, datain=regfile1.rd2())
        # print('so1.memread is', so1.memread)
        memout = datamem1.output() ########################################################################### mem ends here
        if(so1.mem2reg):
            # make the write port of reg equal to output of memory
            regwrdata = memout
            pass
        else:
            # make the write port of the reg equal to output of alu
            regwrdata = alures
            pass
        
        # let's write to the register
        regfile1.inputs(regWrite = so1.regwrite, a1 = rs, a2 = rt, a3 = a3, datain = regwrdata)
        # regfile1.write(so1.regwrite, regwrdata)
        pc1.set(pc1.get() + 4)
        c = 'c'
        # c = input('Enter a random character to continue\n')
        if(c == 'c'):
            os.system('clear')
        elif(c == 'dp'):
            datamem1.printstuff()
        elif(c == 'rp'):
            regfile1.printstuff()
        


datamem1.printstuff()
print()

regfile1.printstuff()


# print(alutmp.binToInt('0' + '11001'))
# print(len(opcode))