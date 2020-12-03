
def intcode(icode):
    pos = 0
    #print(icode)
    while pos < len(icode):
        opcode = icode[pos]
        if opcode == 1:
            tloc1 = icode[pos + 1]
            term1 = icode[tloc1]
            tloc2 = icode[pos + 2]
            term2 = icode[tloc2]
            outloc = icode[pos + 3]
            icode[outloc] = term1 + term2
            pos += 4
        elif opcode == 2:
            term1 = icode[icode[pos + 1]]
            term2 = icode[icode[pos + 2]]
            outloc = icode[pos + 3]
            icode[outloc] = term1 * term2
            pos += 4
        elif opcode == 99:
            break
        else:
            raise ValueError(f"Invalid opcode {opcode}")
    #print(icode)
    return icode


def part1(data):
    icode = [int(i) for i in data.split(",") if i]
    icode[1] = 12
    icode[2] = 2

    icode = intcode(icode)
    return icode[0]

def part2(data):
    data = [int(i) for i in data.split(",") if i]
    for noun in range(100):
        for verb in range(100):
            icode = data.copy()
            icode[1] = noun
            icode[2] = verb
            out = intcode(icode)[0]
            if out == 19690720:
                return 100 * noun + verb
    raise ValueError("not found")
    
    
