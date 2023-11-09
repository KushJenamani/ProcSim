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

pc = PC();
regfile = RegFile();
alu = Alu();
dataMem = DataMemory();
instMem = InstMemory(filename);

forward_unit = Funit(idEx, exMem, memWb);
hazard_unit = Hazard(pc, ifId, idex);
branch_unit = Branch(pc, ifId, idEx);




#create modules
if_mod = If(pc, instMem);
id = Id(regfile, hazard_unit, ifId, idEx);
ex = Ex(alu, forward_unit, idEx, exMem);
mem = Mem(dataMem, branch_unit, exMem, memWb);
wb = Wb(regfile, memWb);


# EXECUTE
while (True):
    end = wb.writeBack();
    mem.access();
    ex.execute();
    id.decode();
    if_mod.fetch();

    if (end):
        break;
