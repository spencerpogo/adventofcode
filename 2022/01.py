def counts(data):
    return (sum(map(int, group.split("\n"))) for group in data.strip().split("\n\n"))


def part1(data):
    return max(counts(data))


def part2(data):
    return sum(sorted(counts(data))[-3:])
