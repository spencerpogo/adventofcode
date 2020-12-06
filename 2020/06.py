
def part1(data):
    groups = data.split("\n\n")
    r = 0

    for g in groups:
        answers = set()
        for p in g.split("\n"):
            for c in p:
                answers.add(c)
        r += len(answers)
    
    return r


def part2(data):
    groups = data.split("\n\n")
    r = 0

    for g in groups:
        lines = g.split("\n")
        all_yes = list(lines[0])
        for p in lines[1:]:
            all_yes = [i for i in all_yes if i in p]
        r += len(all_yes)
    return r
