l = open('input.txt').read().split('\n')
del l[-1]

for i, n in enumerate(l):
    opcode, operand = n.split()
    l[i] = [opcode, int(operand)]

acc = 0
nip = 0
executed = []

while nip not in executed:
    executed.append(nip)
    if l[nip][0] == 'acc':
        acc += l[nip][1]
        nip += 1
    
    elif l[nip][0] == 'nop':
        nip += 1

    elif l[nip][0] == 'jmp':
        nip += l[nip][1]

print(f'Part 1: {acc}')

acc = 0
nip = 0

def run(c):
    program = l[:]
    acc = 0
    nip = 0
    executed = []
    nop_jmp_counter = 0

    while nip not in executed:
        if nip >= len(program):
                break
        executed.append(nip)

        if program[nip][0] == 'acc':
            acc += program[nip][1]
            nip += 1
    
        elif program[nip][0] == 'nop':
            if nop_jmp_counter + 1 == c:
                nip += program[nip][1]
            else:
                nip += 1
            nop_jmp_counter += 1

        elif program[nip][0] == 'jmp':
            if nop_jmp_counter + 1 == c:
                nip += 1
            else:
                nip += program[nip][1]
            nop_jmp_counter += 1


    if nip == len(l):
        print(f'Part 2: {acc}')
    else:
        pass


for i in range(1000):
    run(i)
