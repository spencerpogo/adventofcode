def process_input(data):
    return [int(i) for i in data.split("\n") if i.strip()]


def find_2020_num(inp):
    possible = set()
    for i in inp:
        if i in possible:
            return i
        if i < 2020:
            possible.add(2020 - i)
    raise ValueError("Not found")


def part1(data):
    inp = process_input(data)
    factor = find_2020_num(inp)
    return factor * (2020 - factor)


def find_2020_triplet(inp):
    possibleA = set()
    possibleBMap = {}
    possibleB = set()

    for i in inp:
        if i in possibleB:
            a = 2020 - possibleBMap[i]
            b = i
            c = 2020 - (a + b)
            return (a, b, c)

        if i < 2020:
            possibleA.add(2020 - i)
            for a in possibleA:
                if i < a:
                    to_add = a - i
                    possibleB.add(to_add)
                    possibleBMap[to_add] = a

    raise ValueError("Not Found")


def part2(data):
    inp = process_input(data)
    a, b, c = find_2020_triplet(inp)
    return a * b * c
