def get_num_ones(t):
    big = 2 ** 64
    r = 0
    while t > 0:
        # grab 1 byte at a time
        n = t & (2 ** 8 - 1)

        # https://graphics.stanford.edu/~seander/bithacks.html#CountBitsFromMSBToPos
        n -= (n >> 1) & big // 3
        n = (n & big // 5) + ((n >> 2) & big // 5)
        n = (n + (n >> 4)) & big // 17

        # increment total and shift off processed byte
        r += n
        t = t >> 8
    return r


def get_bits(vals, bit_ind):
    digits = 0
    mask = 1 << bit_ind
    for v in vals:
        digits = (digits << 1) | ((v & mask) >> bit_ind)
    return digits


def part1(inp):
    lines = inp.split("\n")
    vals = [int(l, 2) for l in lines]

    gamma = 0
    llen = len(lines[0])
    vlen = len(vals)
    for i in range(1, llen + 1):
        numones = get_num_ones(get_bits(vals, llen - i))
        numzeroes = vlen - numones
        gamma = (gamma << 1) + (numones > numzeroes)
    # binary NOT of gamma
    epsilon = (1 << llen) - 1 - gamma
    return gamma * epsilon


def find_rating(vals, llen, m):
    while len(vals) > 1:
        for i in range(1, llen + 1):
            bit_ind = llen - i
            numones = get_num_ones(get_bits(vals, bit_ind))
            numzeroes = len(vals) - numones
            mask = 1 << bit_ind
            if (numones >= numzeroes) == m:
                vals = {v for v in vals if v & mask}
            else:
                vals = {v for v in vals if not v & mask}
            if len(vals) <= 1:
                break
    return next(iter(vals))


def part2(inp):
    lines = inp.split("\n")
    vals = {int(l, 2) for l in lines}
    llen = len(lines[0])
    oxy = find_rating(vals, llen, True)
    co2 = find_rating(vals, llen, False)
    return oxy * co2
