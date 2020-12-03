TREE = 1
OPEN = 0

def parse_map(data):
    r = []
    for l in data.split("\n"):
        r.append([TREE if i == "#" else OPEN for i in l])
    
    # for row in r:
    #     if len(row) != len(r[0]):
    #         raise AssertionError("oof")
    return r


def count_trees(m, right, down):
    width = len(m[0])
    x = y = trees = 0

    while y < len(m):
        if m[y][x % width] == TREE:
            trees += 1
        x += right
        y += down
    return trees


def part1(data):
    m = parse_map(data)
    return count_trees(m, 3, 1)


def part2(data):
    m = parse_map(data)
    return count_trees(m, 1, 1) * count_trees(m, 3, 1) * count_trees(m, 5, 1) * count_trees(m,7, 1) * count_trees(m, 1, 2)
