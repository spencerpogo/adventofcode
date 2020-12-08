

def parse_asm(data):
    r = []
    for l in data.split("\n"):
        op, arg_str = l.split(" ")
        r.append((op, int(arg_str)))
    return r


def exec_asm(asm):
    executed = set()

    acc = 0
    pos = 0
    while pos not in executed:
        if pos >= len(asm):
            return 0, acc

        executed.add(pos)
        op, arg = asm[pos]

        if op == "acc":
            acc += arg
            pos += 1
        elif op == "jmp":
            pos += arg
        else:
            pos += 1

    return 1, acc


def part1(data):
    asm = parse_asm(data)
    _, acc = exec_asm(asm)
    return acc


def part2(data):
    # Everyone else is doing brute force, so I will too
    original_asm = parse_asm(data)
    for i in range(len(original_asm)):
        asm = original_asm.copy()
        op, arg = asm[i]
        if op == "jmp":
            asm[i] = ("nop", arg)
        elif op == "nop":
            asm[i] = ("jmp", arg)
        else:
            continue
        status, acc = exec_asm(asm)
        if status == 0:
            return acc
    raise ValueError("No solution found")
