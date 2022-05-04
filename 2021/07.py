
def solve(inp, f):
    positions = list(map(int, inp.split(",")))

    high = max(positions)
    low = min(positions)
    while low < high:
        mid = low + ((high - low) // 2)
        a = f(positions, mid)
        b = f(positions, mid + 1)
        if a < b:
            high = mid
        elif a > b:
            low = mid + 1
    return f(positions, min(low, high))

def needed_fuel_constant(positions, pos):
    return sum(abs(i - pos) for i in positions)

def part1(inp):
    return solve(inp, needed_fuel_constant)

def fast_range_sum(n):
    return n * (n + 1) // 2

def needed_fuel_linear(positions, pos):
    return sum(fast_range_sum(abs(i - pos)) for i in positions)

def part2(inp):
    return solve(inp, needed_fuel_linear)
