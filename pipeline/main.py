import sys;

sys.path.insert(0, 'C:\\Users\\HP\\Documents\\iiitb\\\'New Folder\'\\CPU_coa\\');
from if_module import If;
from id import Id;
from ex import Ex;
from mem import Mem;
from wb import Wb;

from pipeline_register import *;

from memory import *;
from pc import PC;
from alu import Alu;
from regfile import RegFile;

from forward_unit import Funit;
from mem_hazard import Hazard;
from branch import Branch;



# create pipeline registers
ifId = ifid();
idEx = idex();
exMem = exmem();
memWb = memwb();

# create modules internals

filename = 'bytecode.txt'

pc = PC(0);
regfile = RegFile();
alu = Alu();
pc_alu = Alu();
dataMem = DataMemory();
instMem = InstMemory(filename);

forward_unit = Funit(idEx, exMem, memWb);
hazard_unit = Hazard(pc, ifId, idEx);
branch_unit = Branch(pc, ifId, idEx);




#create modules
if_mod = If(pc, instMem);
id = Id(regfile, hazard_unit, ifId, idEx);
ex = Ex(alu, pc_alu, forward_unit, idEx, exMem);
mem = Mem(dataMem, branch_unit, exMem, memWb);
wb = Wb(regfile, memWb);






# TAKE INPUTS
print('Enter the number of elements to be sorted');
# n = int(input())
n = 2
regfile.inputs(regWrite=True, a1 = 0, a2 = 0, a3 = 9, datain = n)
# n = 4

# inp = [4, 3, 6, 8]
inp = []
out = []
a = 0
print("Enter the starting address for input");
# start_addr = int(input())
start_addr = 4
regfile.inputs(regWrite = True, a1 = 0, a2 = 0, a3 = 10, datain  = start_addr)
print("Enter the output address");
# end_addr = int(input());
end_addr = 24
regfile.inputs(regWrite = True, a1 = 0, a2 = 0, a3 = 11, datain  = end_addr)

print("enter the numbers to be sorted\n")
for i in range(n):
    a = int(input());
    inp.append(a);
    # the numbers must also be stored at the starting address
    dataMem.inputs(memRead=False, memWrite=True, address=start_addr+i*4, datain=a)


# now instruction memory has all the instructions 

init = len(instMem.mem)
# the program will end when pc points to some address value that hasn't been put in the instruction memory's dictionary
pc.set(4194304)  # initialize pc to the first instruction in codespace











# EXECUTE
while (True):
    print('Something vro')
    end = wb.writeBack();
    mem.access();
    ex.execute();
    id.decode();
    try:
        if_mod.fetch();
    except:
        pass

    if (end):
        break;
