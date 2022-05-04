def unique_digit(d):
    s = len(d)    
    return (
        s == len("cf") or # 1
        s == len("bcdf") or # 4
        s == len("acf") or # 7
        s == len("abcdefg") # 8
    )

def part1(inp):
    t = 0
    for l in inp.split("\n"):
        _, _, out = l.partition("|")
        t += sum(1 for d in out.split(" ") if unique_digit(d))
    return t

WIRES = set("abcdefg")
NUMBER_SETS = [
    set("abcefg"),
    set("cf"),
    set("acdeg"),
    set("acdfg"),
    set("bcdf"),
    set("abdfg"),
    set("abdefg"),
    set("acf"),
    set("abcdefg"),
    set("abcdfg"),
]
NUMBERS_BY_LENGTH = {}
for n in NUMBER_SETS:
    l = len(n)
    NUMBERS_BY_LENGTH.setdefault(l, [])
    NUMBERS_BY_LENGTH[l].append(n)
NUMBERS = {"".join(sorted(s)): i for i, s in enumerate(NUMBER_SETS)}

def overlap_count(a, b):
    return sum(1 for c in a if c in b)

def solve_config(signals):
    signals = sorted(signals, key=len)
    translations = {}
    one = None
    four = None
    for s in signals:
        l = len(s)
        if l == 2:
            translations[s] = 1
            one = set(s)
        elif l == 3:
            translations[s] = 7
        elif l == 4:
            translations[s] = 4
            four = set(s)
        elif l == 7:
            translations[s] = 8
        elif l == 5:
            if overlap_count(s, one) == 2:
                translations[s] = 3
            elif overlap_count(s, four) == 3:
                translations[s] = 5
            else:
                translations[s] = 2
        elif l == 6:
            if overlap_count(s, four) == 4:
                translations[s] = 9
            elif overlap_count(s, one) == 2:
                translations[s] = 0
            else:
                translations[s] = 6
        else:
            raise ValueError("wtf")
    #l = list(translations.values())
    #s = set(translations.values())
    #print(l, s)
    #if len(l) != len(s):
    #    raise ValueError("oops")
    return translations

def part2(inp):
    total = 0
    for l in inp.split("\n"):
        signals, _, outputs = l.partition(" | ")
        signals = ["".join(sorted(s)) for s in signals.split(" ")]
        outputs = ["".join(sorted(s)) for s in outputs.split(" ")]
        translations = solve_config(signals)
        digits = [str(translations[i]) for i in outputs]
        total += int("".join(digits))
    return total
