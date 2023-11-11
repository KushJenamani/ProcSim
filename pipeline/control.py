# take in the func field and the opcode and then decide the control signals
class SignalsObject:
    branch: bool
    jump: bool
    alusrc: bool
    alucontrol: str
    memread: bool
    memwrite: bool
    regwrite: bool
    regdst: bool
    mem2reg: bool

    def __init__():
        pass
    def __init__(self, branch, jump, alusrc, alucontrol, memread, memwrite, regwrite, regdst, mem2reg):
        self.branch = branch
        self.jump = jump
        self.alucontrol = alucontrol
        self.alusrc = alusrc
        self.memread = memread
        self.memwrite = memwrite
        self.regdst = regdst
        self.regwrite = regwrite
        self.mem2reg = mem2reg

    def flush(self):
        self.branch = False;
        self.jump = False;
        self.alusrc = False;
        self.alucontrol = '0000';
        self.memread = False;
        self.memwrite = False;
        self.regwrite = False;
        self.regdst = False;
        self.mem2reg = False;


class Control:
    opcode: str;
    func: str;
    def __init__(self):
        pass
    def decidesignals(self, opcode: str, func: str):  # let's make this function return an object of type control with which I can use . to get the required signal
        if(opcode == '000000'):
            #it is r type look at func field
            match func:
                case '000000':
                    # it is a sll
                    print('sll')
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='1111', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '100000':
                    #it is an add instruction
                    print('add')
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='0010', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '100010':
                    #it is a subtract instruction
                    print('sub')
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='0110', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '100100':
                    # it is an and instruction
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='0000', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '100101':
                    # it is an or instructiion
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='0001', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '101010':
                    # it is a slt instruction
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='0111', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '100111':
                    # it is a nor
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='1100', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case _:
                    print("wtf do you thing too much animosity")
                    exit(0)
        else:
            #it is not r type:
            match opcode:
                case '011100':
                    # it is mul
                    print('mul')
                    return SignalsObject(regdst=True, regwrite= True, alusrc=False, alucontrol='1110', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '001000':
                    # it is addi
                    print('addi')
                    return SignalsObject(regdst=False, regwrite= True, alusrc=True, alucontrol='0010', mem2reg=False, memread=False, memwrite=False, jump=False, branch=False)
                case '100011':
                    # it is lw
                    print('lw')
                    return SignalsObject(regdst=False, regwrite= True, alusrc=True, alucontrol='0010', mem2reg=True, memread=True, memwrite=False, jump=False, branch=False)
                case '101011':
                    # it is a sw
                    print('sw')
                    return SignalsObject(regdst=False, regwrite= False, alusrc=True, alucontrol='0010', mem2reg=False, memread=False, memwrite=True, jump=False, branch=False)
                case '000100':
                    # it is a beq
                    print('it is beq')
                    return SignalsObject(regdst=False, regwrite= False, alusrc=False, alucontrol='0110', mem2reg=False, memread=False, memwrite=False, jump=False, branch=True)
                case '000101':
                    # it is a bne
                    print('it is bne')
                    return SignalsObject(regdst=False, regwrite= False, alusrc=False, alucontrol='0110', mem2reg=False, memread=False, memwrite=False, jump=False, branch=True)
                case '000010':
                    # it is a j
                    return SignalsObject(regdst=False, regwrite=False, alusrc=False, alucontrol='0111', mem2reg=False, memread=False, memwrite=False, jump=True, branch=False)
                case _:
                    print('that instruction does not exist')
                    print('opcode: ', opcode, 'func: ', func)
                    # exit(0)
# 0000	and
# 0001	or
# 0010	add
# 0110	sub
# 0111	slt
# 1100	nor


#00001000000100000000000000000001