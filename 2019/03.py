from pprint import pprint


def distance_to(x, y, start=(0, 0)):
    sx, sy = start
    return abs(x - sx) + abs(y - sy)


def find_points(dirs, start=(0, 0)):
    points = set()
    x, y = start
    for part in dirs:
        d = part[0].upper()
        amt = int(part[1:])
        oldx = x
        oldy = y
        if d == "U":
            y += amt
        elif d == "D":
            y -= amt
        elif d == "L":
            x -= amt
        elif d == "R":
            x += amt
        xchange = x - oldx
        ychange = y - oldy
        for c in range(*sorted([1, xchange + 1])):
            assert oldy == y
            cx = oldx + c
            points.add((cx, y))
        for c in range(*sorted([1, ychange + 1])):
            assert oldx == x
            cy = oldy + c
            points.add((x, cy))
    return points


def _DEBUG_draw_points(w1points, w2points):
    for y in reversed(range(11)):
        s = []
        for x in reversed(range(11)):
            p = (x, y)
            if p in w1points:
                if p in w2points:
                    print("X", end="")
                else:
                    print("1", end="")
            elif p in w2points:
                print("2", end="")
            else:
                print(" ", end="")
        print()


def part1(data):
    wire1, wire2 = [i for i in data.split("\n") if i]
    wire1 = [i for i in wire1.split(",") if i]
    wire2 = [i for i in wire2.split(",") if i]
    w1points = find_points(wire1)
    w2points = find_points(wire2)

    # print("Processing...")
    # find the duplicates in each set and make a set with no duplicates
    crosses = set.intersection(w1points, w2points)
    # print(f'{len(crosses)} crosses')
    # dict of distance for each
    cdist = {i: distance_to(*i) for i in crosses}
    # lowest
    best = sorted(cdist, key=(lambda k: cdist[k]))[0]
    return distance_to(*best)


def steps_to(pntx, pnty, paths, start=(0, 0)):
    x, y = start
    steps = 0
    for part in paths:
        d = part[0].upper()
        amt = int(part[1:])
        oldx = x
        oldy = y
        if d == "U":
            y += amt
        elif d == "D":
            y -= amt
        elif d == "L":
            x -= amt
        elif d == "R":
            x += amt
        xchange = x - oldx
        ychange = y - oldy
        for c in range(*sorted([1, xchange + 1])):
            steps += 1
            cx = oldx + c
            if cx == pntx and y == pnty:
                return steps

        for c in range(*sorted([1, ychange + 1])):
            steps += 1
            cy = oldy + c
            if x == pntx and cy == pnty:
                return steps
    return None


def part2(data):
    wire1, wire2 = [i for i in data.split("\n") if i]
    wire1 = [i for i in wire1.split(",") if i]
    wire2 = [i for i in wire2.split(",") if i]
    # print("Finding points 1...")
    w1points = find_points(wire1)
    # print("Finding points 2...")
    w2points = find_points(wire2)

    # print("Processing...")
    # find the duplicates in each set and make a set with no duplicates
    crosses = set.intersection(w1points, w2points)
    # print(f'{len(crosses)} crosses')
    bestd = float("inf")
    for c in crosses:
        dist = steps_to(*c, wire1) + steps_to(*c, wire2)
        if dist < bestd:
            bestd = dist
    return bestd
