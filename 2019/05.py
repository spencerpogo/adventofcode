import traceback


class Params:
    def __init__(self, icode, modes, pos):
        self.icode = icode
        self.modes = modes
        self.pos = pos

    def getmode(self, i):
        try:
            mode = self.modes[i]
        except IndexError:
            mode = 0
        return mode

    def __getitem__(self, i):
        mode = self.getmode(i)
        val = self.icode[self.pos + i + 1]
        # print('m', mode)
        if mode == 0:
            # print(i, val, mode)
            return self.icode[val]
        elif mode == 1:
            # print(i, val, mode, val)
            return val
        else:
            raise ValueError(f"Invalid mode {mode}")

    def iter(self, times):
        for i in range(times):
            yield self[i]


icode = None


def intcodev2(icode, inp):
    pos = 0
    while pos < len(icode):
        mode = str(icode[pos])
        opcode = int(mode[-2:])
        # print(pos, ': ', mode, sep='')
        pmodes = []
        for p in reversed(mode[:-2]):
            pmodes.append(int(p))
        params = Params(icode, pmodes, pos)
        if opcode == 1:  # add
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            icode[outloc] = term1 + term2
            pos += 4
        elif opcode == 2:  # multiply
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            icode[outloc] = term1 * term2
            pos += 4
        elif opcode == 3:  # inp to memory
            outloc = icode[pos + 1]
            icode[outloc] = inp
            pos += 2
        elif opcode == 4:  # memory to inp
            val = params[0]
            inp = val
            pos += 2
        elif opcode == 5:  # jump if true
            val = params[0]
            loc = params[1]
            if val != 0:
                # print(f'jump to {loc}')
                pos = loc
            else:
                pos += 3
        elif opcode == 6:  # jump if false
            val = params[0]
            loc = params[1]
            if val == 0:
                pos = loc
            else:
                pos += 3
        elif opcode == 7:  # less than
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            if term1 < term2:
                icode[outloc] = 1
            else:
                icode[outloc] = 0
            pos += 4
        elif opcode == 8:  # equal to
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            # print(f"{term1} == {term2} => {outloc}")
            if term1 == term2:
                icode[outloc] = 1
            else:
                icode[outloc] = 0
            pos += 4
        elif opcode == 99:
            # print('end program')
            break
        else:
            raise ValueError(f"Invalid opcode {opcode}")
    # print(icode)
    return icode, inp


def part1(data):
    inp = [int(i) for i in data.split(",") if i]
    print(len(inp))
    _, out = intcodev2(inp, 8)
    return out


def part2(data):
    global icode
    inp = [int(i) for i in data.split(",") if i]
    # print(len(inp))]
    _, out = intcodev2(inp, 5)
    return out
