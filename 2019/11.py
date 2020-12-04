intcodev4 = __import__('09').intcodev4

"""
def rotate_left(xdir, ydir):
    print("turn left")
    if xdir == 0 and ydir==1: # up
        return -1, 0 # left
    elif xdir == -1 and ydir==0: #left
        return 0, -1 # down
    elif xdir == 0 and ydir==-1: # down
        return 1, 0 # right
    elif xdir == 1 and ydir==0: # right
        return 0, 1 # up
    else:
        raise ValueError(f"Invalid xdir and ydir: {xdir} {ydir}")

def rotate_right(xdir, ydir):
    print("Turn right")
    if xdir == 0 and ydir == 1: # up
        return 1, 0 # right
    elif xdir == -1 and ydir == 0: #left
        return 0, 1 # up
    elif xdir == 0 and ydir == -1: # down
        return -1, 0 # left
    elif xdir == 1 and ydir == 0: # right
        return 0, -1 # down
    else:
        raise ValueError(f"Invalid xdir and ydir: {xdir} {ydir}")
"""
DIRS = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}
def rotate(pdir, dirs):
    i = dirs.index(pdir)
    return dirs[i+1] if i+1 < 4 else dirs[0]

def rotate_left(pdir):
    #print("*turns left*")
    return rotate(pdir, "ULDR")

def rotate_right(pdir):
    #print("*turns right*")
    return rotate(pdir, "URDL")

def get_outputs(iterator, amnt):
    while True:
        outs = []
        try:
            for _ in range(amnt):
                outs.append(next(iterator))
            yield outs
        except StopIteration:
            return


def paint_execute(code, initial_color):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x = y = direction = 0
    panel = { (x, y): initial_color }
    def camera():
        val = panel[(x, y)] if (x, y) in panel else 0
        #print(f"{x}, {y}: {val}")
        return val

    for output1, output2 in get_outputs(intcodev4(code, camera), 2):
        print(output1, output2)
        panel[(x, y)] = output1
        direction = ((direction + 1) if output2 == 1 else (direction - 1 + len(directions))) % len(directions)
        x, y = x + directions[direction][0], y + directions[direction][1]
    return panel


def part1(data):
    print("THIS DOESNT WORK")
    icode = [int(i) for i in data.split(',') if i]

    #return len(paint_execute(icode, 0))
    pdir = "U"
    x = y = 0
    panels = {(x, y): 0}
    def camera():
        val = panels[(x, y)] if (x, y) in panels else 0
        #print(f'{x}, {y}: {val} heading {pdir}')
        return val
    needscolor = True
    for val in intcodev4(icode, camera):
        if needscolor:
            if val == 0:
                #print(f"paint {x},{y} black")
                panels[(x, y)] = 0
            elif val == 1:
                #print(f"paint {x},{y} white")
                panels[(x, y)] = 1
            else:
                raise ValueError(f"Invalid val {val}")
        else:
            if val == 0: # turn left
                pdir = rotate_left(pdir)
            elif val == 1:
                pdir = rotate_right(pdir)
            else:
                raise ValueError(f"Invalid val {val}")
            xdir, ydir = DIRS[pdir]
            x += xdir
            y += ydir
        needscolor = not needscolor
    return len(panels)


def build_registration(panel_points):
    registration = [[' ']*40 for _ in range(6)]
    for row in range(6):
        for col in range(40):
            if panel_points.get((col, row), 0) == 1:
                registration[row][col] = '*'
    return '\n'.join(''.join(row) for row in registration)


def part2(data):
    icode = [int(i) for i in data.split(',') if i]

    #return len(paint_execute(icode, 0))
    pdir = "U"
    x = y = 0
    panels = {(x, y): 1}
    def camera():
        val = panels[(x, y)] if (x, y) in panels else 0
        #print(f'{x}, {y}: {val} heading {pdir}')
        return val
    needscolor = True
    for val in intcodev4(icode, camera):
        if needscolor:
            if val == 0:
                #print(f"paint {x},{y} black")
                panels[(x, y)] = 0
            elif val == 1:
                #print(f"paint {x},{y} white")
                panels[(x, y)] = 1
            else:
                raise ValueError(f"Invalid val {val}")
        else:
            if val == 0: # turn left
                pdir = rotate_left(pdir)
            elif val == 1:
                pdir = rotate_right(pdir)
            else:
                raise ValueError(f"Invalid val {val}")
            xdir, ydir = DIRS[pdir]
            x += xdir
            y += ydir
        needscolor = not needscolor
    return 'god I\'m stupid why won\'t this work\n' + build_registration(panels)
