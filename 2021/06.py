from collections import deque

def solve(inp, days):
    timers = deque([0] * 9)
    for n in inp.split(","):
        timers[int(n)] += 1

    for _ in range(days):
        timers.rotate(-1)
        timers[6] += timers[8]
    
    return sum(timers)


def part1(inp):
    return solve(inp, 80)

def part2(inp):
    return solve(inp, 256)
