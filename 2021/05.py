from collections import defaultdict
from itertools import product

def parse_point(p):
    x, _, y = p.partition(",")
    return int(x), int(y)

def parse_line(inp):
    l, _, r = inp.partition(" -> ")
    return (parse_point(l), parse_point(r))

def parse_inp(inp):
    return list(map(parse_line, inp.split("\n")))

def get_line_points(s, e):
    sx, sy = s
    ex, ey = e
    xstep = -1 if sx > ex else 1
    ystep = -1 if sy > ey else 1
    xs = range(sx, ex + xstep, xstep)
    ys = range(sy, ey + ystep, ystep)
    if sx == ex or sy == ey:
        return product(xs, ys), True
    else:
        return zip(xs, ys), False

def dbg(points):
    for y in range(10):
        for x in range(10):
            val = points.get((x, y), 0)
            print(end="." if val == 0 else str(val))
        print()
    print()

def part1(inp):
    lines = parse_inp(inp)
    points = defaultdict(lambda: 0)
    for s, e in lines:
        lpoints, straight = get_line_points(s, e)
        if not straight:
            continue
        for x, y in lpoints:
            points[(x, y)] += 1
    #dbg(points)
    return sum(1 for v in points.values() if v >= 2)

def part2(inp):
    lines = parse_inp(inp)
    points = {}
    for s, e in lines:
        lpoints, straight = get_line_points(s, e)
        for x, y in lpoints:
            points.setdefault((x, y), 0)
            points[(x, y)] += 1
    #dbg(points)
    return sum(1 for v in points.values() if v >= 2)
