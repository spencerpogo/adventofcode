

def binsearch(p, high, lchar):
    low = 0
    high = high
    
    for c in p:
        change = ((high - low) // 2)
        if c == lchar:
            high = low + change
        else:
            low = low + change + 1

    assert low == high
    return low


def find_seat(data):
    return binsearch(data[:7], 127, "F"), binsearch(data[7:], 7, "L")


def seatid(data):
    row, seat = find_seat(data)
    return 8 * row + seat


def part1(data):
    return max([seatid(i) for i in data.split("\n")])


def part2(data):
    taken = sorted([seatid(i) for i in data.split("\n")])
    last = taken[0] - 1
    for i in taken:
        if i != last + 1:
            return i - 1
        last = i
