

class Params:
    def __init__(self, icode, modes, pos, rb):
        self.icode = icode
        self.modes = modes
        self.pos = pos
        self.rb = rb
    
    def getmode(self, i):
        try:
            mode = self.modes[i]
        except IndexError:
            mode = 0
        return mode

    def getadr(self, i):
        mode = self.getmode(i)
        val = self.icode[self.pos + i + 1]
        #print('m', mode)
        if mode == 0:
            #print(i, val, mode)
            return val
        elif mode == 1:
            #print(i, val, mode, val)
            return val
        elif mode == 2:
            adr = self.rb + val
            return adr
        else:
            raise ValueError(f"Invalid mode {mode}")
    
    def __getitem__(self, i):
        mode = self.getmode(i)
        val = self.icode[self.pos + i + 1]
        #print('m', mode)
        if mode == 0:
            return self.icode[val] if val < len(self.icode) else 0
            #print(i, val, mode)
            #try:
            #    return self.icode[val]
            #except IndexError:
            #    raise IndexError(f"getting paramater {i} with mode 0: intcode[{self.pos + i + 1}] is {val}, intcode[{val}] out of range")
        elif mode == 1:
            #print(i, val, mode, val)
            return val
        elif mode == 2:
            adr = self.rb + val
            return self.icode[adr]
        else:
            raise ValueError(f"Invalid mode {mode}")

    def iter(self, times):
        for i in range(times):
            yield self[i]


# INTCODE V4!!!!!! ENOUGHT INTCODE ALREADY!!
def intcodev4(icode, inpf):
    icode += [0] * 400
    pos = 0
    rb = 0
    inpos = 0
    output = []
    while pos < len(icode):
        mode = str(icode[pos])
        opcode = int(mode[-2:])
        #print(pos, ": ", mode, sep="")
        #print(pos, ': ', mode, sep='')
        pmodes = []
        for p in reversed(mode[:-2]):
            pmodes.append(int(p))
        params = Params(icode, pmodes, pos, rb)
        if opcode == 1: # add
            term1 = params[0]
            term2 = params[1]
            #outloc = params[2]
            outloc = params.getadr(2)
            icode[outloc] = term1 + term2
            pos += 4
        elif opcode == 2: #multiply
            term1 = params[0]
            term2 = params[1]
            #outloc = params[2]
            outloc = params.getadr(2)
            icode[outloc] = term1 * term2
            pos += 4
        elif opcode == 3: # inp to memory
            #outloc = params[0]
            outloc = params.getadr(2)
            val = inpf()
            if not isinstance(val, int):
                raise TypeError("Input functions should return int, instead got {type(val)!r}: {val}")
            icode[outloc] = val
            #print('i', icode[outloc])
            inpos += 1
            pos += 2
        elif opcode == 4: # memory to out
            val = params[0]
            #print('o', val)
            yield val
            pos += 2
        elif opcode == 5: # jump if true
            val = params[0]
            loc = params[1]
            if val != 0:
                #print(f'jump to {loc}')
                pos = loc
            else:
                pos += 3
        elif opcode == 6: # jump if false
            val = params[0]
            loc = params[1]
            if val == 0:
                #print(f'jump to {loc}')
                pos = loc
            else:
                pos += 3
        elif opcode == 7: # less than
            term1 = params[0]
            term2 = params[1]
            #outloc = params[2]
            outloc = params.getadr(2)
            if term1 < term2:
                icode[outloc] = 1
            else:
                icode[outloc] = 0
            pos += 4
        elif opcode == 8: # equal to
            term1 = params[0]
            term2 = params[1]
            #outloc = params[2]
            outloc = params.getadr(2)
            #print(f"{term1} == {term2} => {outloc}")
            if term1 == term2:
                icode[outloc] = 1
            else:
                icode[outloc] = 0
            pos += 4
        elif opcode == 9: # adjust relative base
            rb += params[0]
            pos += 2
        elif opcode == 99:
            #print('end program')
            break
        else:
            raise ValueError(f"Invalid opcode {opcode}")
    #print(icode)
    #print(icode[15], icode[16])
    #return icode


def part1(data):
    icode = [int(i) for i in data.split(',') if data]
    def inp():
        print("Getting input!")
        return 1
    for val in intcodev4(icode, inp):
        print("Output:", val)

def part2(data):
    icode = [int(i) for i in data.split(',') if data]
    def inp():
        print("Getting input!")
        return 2
    for val in intcodev4(icode, inp):
        print("Output:", val)
