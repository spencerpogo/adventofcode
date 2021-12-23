def nums(l):
    return list(map(int, l.split()))

def parse_board(b):
    return [nums(l) for l in b.split("\n")]

def parse(inp):
    numbers, *boards = inp.split("\n\n")
    return list(map(int, numbers.split(","))), list(map(parse_board, boards))

def all_poss(board):
    # cols
    for i in range(len(board[0])):
        yield [row[i] for row in board]
    # rows
    yield from board

def solve(inp, f):
    numbers, boards = parse(inp)
    inds = {n: i for i, n in enumerate(numbers)}

    board_inds = []
    for board in boards:
        row_lasts = [max(inds[i] for i in group) for group in all_poss(board)]
        board_inds.append(min(row_lasts))

    winning_board, winning_ind = f(enumerate(board_inds), key=lambda i: i[1])
    called = set(numbers[:winning_ind + 1])
    unmarked = [i for row in boards[winning_board] for i in row if i not in called]
    return sum(unmarked) * numbers[winning_ind]

def part1(inp):
    return solve(inp, min)

def part2(inp):
    return solve(inp, max)
