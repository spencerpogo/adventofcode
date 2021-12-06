def part1(inp):
    h = 0
    d = 0
    for l in inp.split("\n"):
        cmd, arg = l.split(" ")
        a = int(arg)
        if cmd == "forward":
            h += a
        elif cmd == "down":
            d += a
        elif cmd == "up":
            d -= a
        else:
            raise ValueError(f"bad cmd {cmd}")
    return h * d


def part2(inp):
    h = 0
    d = 0
    aim = 0
    for l in inp.split("\n"):
        cmd, val = l.split(" ")
        v = int(val)
        if cmd == "forward":
            h += v
            d += aim * v
        elif cmd == "down":
            aim += v
        elif cmd == "up":
            aim -= v
        else:
            raise ValueError(f"bad cmd {cmd}")
    return h * d
