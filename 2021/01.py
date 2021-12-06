def part1(data):
    inp = list(map(int, data.split("\n")))
    return sum(1 if b > a else 0 for a, b in zip(inp, inp[1:]))


def part2(data):
    inp = list(map(int, data.split("\n")))
    total = 0
    for i in range(len(list(inp)) - 3):
        a = sum(inp[i : i + 3])
        b = sum(inp[i + 1 : i + 4])
        total += 1 if b > a else 0
    return total
