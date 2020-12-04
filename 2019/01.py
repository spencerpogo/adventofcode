def fuel_needed(i):
    return (i // 3) - 2


def part1(data):
    r = 0
    for i in data.split("\n"):
        r += fuel_needed(int(i))
    return r


def part2(data):
    r = 0
    for i in data.split("\n"):
        i = int(i)
        needed = fuel_needed(i)
        while needed > 0:
            r += needed
            needed = fuel_needed(needed)
    return r
