

def digits_increasing(s):
    last = int(s[0])
    for i in s:
        d = int(i)
        if d < last:
            return False
        last = d
    return True

def has_pair(s):
    for i in range(0, len(s)):
        try:
            if s[i] == s[i + 1]:
                return True
        except IndexError:
            pass
    return False


def part1(data):
    lowest, highest = [int(i) for i in data.split('-')]
    total = 0
    for n in range(lowest, highest):
        s = str(n)
        if (len(s) == 6) and digits_increasing(s) and has_pair(s):
            total += 1
    return total


def has_small_group(s):
    last = None
    group_len = 1
    for c in s:
        if last is not None:
            if c == last:
                group_len += 1
            else:
                if group_len == 2:
                    return True
                group_len = 1
        last = c
    if group_len == 2:
        return True
    return False

def part2(data):
    lowest, highest = [int(i) for i in data.split('-')]
    total = 0
    for n in range(lowest, highest):
        s = str(n)
        if (len(s) == 6) and digits_increasing(s) and has_small_group(s):
            total += 1
    return total
