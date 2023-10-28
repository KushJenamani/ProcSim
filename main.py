import control
import pc
import memory
import regfile

#take inputs (the numbers to sort)

print('Enter the number of elements to be sorted');
n = int(input())

inp = []
out = []
a = 0;
print("Enter the starting address for input");
start_addr = int(input());
print("Enter the output address");
end_addr = int(input());


for i in range(n):
    a = int(input());
    inp.append(a);


filename = 'bytecode.txt'
# instantiate all objects
datamem1  = memory.DataMemory();
instmem1 = memory.InstMem(filename); # now instruction memory has all the required instuctions
regfile1 = regfile.Regfile();
pc1 = pc.PC();








