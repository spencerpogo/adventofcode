
# Part 1 Benchmarks on puzzle input:
# Using is_valid: 3ms 83µs
# Using is_valid_naive: 15ms 865µs

def is_valid(preamble, n):
    #print(preamble, n)
    targets = set()
    for a in preamble:
        #print(a, targets)
        if a in targets:
            #print(f"{a} + {n - a} = {n}")
            return True
        if a >= n:
            continue
        targets.add(n - a)

    return False

def is_valid_naive(preamble, n):
    for i, a in enumerate(preamble):
        for j, b in enumerate(preamble):
            if i != j and a + b == n:
                #print(f"{a} + {b} = {n}")
                return True
    return False


def part1(data):
    nums = [int(i) for i in data.split("\n")]

    PREAMBLE_LEN = 25
    preamble = nums[:PREAMBLE_LEN]

    for n in nums[PREAMBLE_LEN:]:
        if not is_valid(preamble, n):
            return n
        preamble = preamble[1:]
        preamble.append(n)

# Benchmark part 2:
# With hardcoded invalid_num:   2ms 837µs
# With part1(data) invalid_num: 4ms 667µs

def part2(data):
    invalid_num = part1(data)
    #invalid_num = 1398413738

    nums = [int(i) for i in data.split("\n")]
    seq = []
    seq_sum = 0

    for n in nums:
        if seq_sum == invalid_num:
            return min(seq) + max(seq)
        new_sum = seq_sum + n
        #print(new_sum, seq, n)
        if new_sum == invalid_num:
            seq.append(n)
            return min(seq) + max(seq)
        elif new_sum > invalid_num:
            while len(seq) and new_sum > invalid_num:
                new_sum -= seq[0]
                seq = seq[1:]
        seq.append(n)
        seq_sum = new_sum
