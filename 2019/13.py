runintcode = __import__('09').intcodev4

def get_outputs(iterator, amnt):
    while True:
        outs = []
        try:
            for _ in range(amnt):
                outs.append(next(iterator))
            yield outs
        except StopIteration:
            return


def part1(data):
    icode = [int(i) for i in data.split(",") if i]
    def inpf():
        raise ValueError("shouldn't input")
    screen = {}
    for x, y, tile in get_outputs(runintcode(icode, inpf), 3):
        screen[(x, y)] = tile
    return len([i for i in screen.values() if i == 2])


def part2(data):
    icode = [int(i) for i in data.split(",") if i]
    icode[0] = 2
    screen = {}
    score = None
    scores = []
    ballpos = None
    paddlepos = None
    def inpf():
        if ballpos is None or paddlepos is None:
            return 0
        if paddlepos[0] < ballpos[0]:
            return 1
        elif paddlepos[0] == ballpos[0]:
            return 0
        elif paddlepos[0] > ballpos[0]:
            return -1
        else:
            raise ValueError("lol")
    for x, y, tile in get_outputs(runintcode(icode, inpf), 3):
        if x == -1 and y == 0:
            score = tile
        else:
            screen[(x, y)] = tile
            if tile == 4:
                ballpos = (x, y)
            elif tile == 3:
                paddlepos = (x, y)
        if score and len([i for i in screen.values() if i == 2]) == 0: # number of blocks
            scores.append(score)
    return scores[-1]
    #return len([i for i in screen.values() if i == 2])
