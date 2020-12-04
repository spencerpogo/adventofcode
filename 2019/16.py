import math
import numpy as np

"""
def calculate_pattern(length, base, repeats):
    patt = []
    for i in base:
        patt += [i] * repeats
    val = (patt * math.ceil(length+1/len(patt)))[1:length+1]
    #print(val)
    return val
"""
def calculate_pattern(length, repeats):
    return np.resize(np.repeat(np.array((0, 1, 0, -1)), repeats), length+1)[1:length+1]


def calculate_phase(inp):
    res = []
    for i, val in enumerate(inp):
        total = 0
        for t1, t2 in zip(inp, calculate_pattern(len(inp), i+1)):
            total += t1 * t2
        res.append(abs(total)%10)
    return res


def part1(data):
    inp = [int(i) for i in list(data)]
    for i in range(100):
        inp = calculate_phase(inp)
    return ''.join(str(i) for i in inp[:8])

def part2(data):
    offset = int(data[:7])
    inp = [int(i) for i in list(data)*10000]
    for i in range(100):
        inp = calculate_phase(inp)
    return ''.join(str(i) for i in inp[offset:offset+8])
