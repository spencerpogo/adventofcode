import itertools
import threading
from queue import Queue


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
        #print('m', mode)
        if mode == 0:
            #print(i, val, mode)
            return self.icode[val]
        elif mode == 1:
            #print(i, val, mode, val)
            return val
        else:
            raise ValueError(f"Invalid mode {mode}")

    def iter(self, times):
        for i in range(times):
            yield self[i]


def intcodev3(icode, inpf):
    pos = 0
    inpos = 0
    output = []
    while pos < len(icode):
        mode = str(icode[pos])
        opcode = int(mode[-2:])
        #print(pos, ': ', mode, sep='')
        pmodes = []
        for p in reversed(mode[:-2]):
            pmodes.append(int(p))
        params = Params(icode, pmodes, pos)
        if opcode == 1: # add
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            icode[outloc] = term1 + term2
            pos += 4
        elif opcode == 2: #multiply
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            icode[outloc] = term1 * term2
            pos += 4
        elif opcode == 3: # inp to memory
            outloc = icode[pos + 1]
            try:
                icode[outloc] = inpf()
            except IndexError:
                print(f"icode[{outloc}] = inpar[{inpos}]")
                raise
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
                pos = loc
            else:
                pos += 3
        elif opcode == 7: # less than
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            if term1 < term2:
                icode[outloc] = 1
            else:
                icode[outloc] = 0
            pos += 4
        elif opcode == 8: # equal to
            term1 = params[0]
            term2 = params[1]
            outloc = icode[pos + 3]
            #print(f"{term1} == {term2} => {outloc}")
            if term1 == term2:
                icode[outloc] = 1
            else:
                icode[outloc] = 0
            pos += 4
        elif opcode == 99:
            #print('end program')
            break
        else:
            raise ValueError(f"Invalid opcode {opcode}")
    #print(icode)
    #print(icode[15], icode[16])
    return icode


def runner(ampcode):
    def run(inp):
        icode = ampcode.copy()
        out = None
        for val in intcodev3(icode, inp):
            out = val
        return out
    return run


def amplify(icode, inp):
    run = runner(icode)
    last = 0
    for phase in inp:
        q = Queue()
        q.put(phase)
        q.put(last)
        last = run(q.get)
    return last


def part1(data):
    #return
    ampcode = [int(i) for i in data.split(',') if i]
    best = float('-inf')
    for a, b, c, d, e in itertools.permutations(range(5)):
        last = amplify(ampcode, [a, b, c, d, e])
        if last > best:
            #print(f"{a},{b},{c},{d},{e}: {last}")
            best = last
    return best


def amp_thread(ampcode, inq, outq):
    #print(f"thread start!")
    out = None
    for val in intcodev3(ampcode.copy(), inq.get):
        out = val
        outq.put(val)
    return out


def part2(data):
    ampcode = [int(i) for i in data.split(',') if i]
    best = float('-inf')
    for a, b, c, d, e in itertools.permutations(range(5, 10)):
        queues = [Queue() for _ in range(5)]
        threads = [threading.Thread(target=amp_thread, args=(ampcode,)+args) for args in zip(queues, queues[1:])]
        for phase, q in zip([a, b, c, d, e], queues):
            q.put(phase)
        for t in threads:
            t.start()
        queues[0].put(0)
        #print('running extra')
        out = amp_thread(ampcode, queues[-1], queues[0])
        for t in threads:
            #print('joining')
            t.join()
        if out > best:
            best = out
    return best
