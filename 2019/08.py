

def iter_layer(l):
    count = 0
    for r in l:
        for pixel in r:
            yield pixel
    return count


def amt_in_layer(l, target):
    t = str(target)
    count = 0
    for pixel in iter_layer(l):
        #if t in str(pixel):
        if str(pixel) == t:
            count += 1
    return count


def make_layers(data, w, h):
    layers = []
    pos = 0
    while pos < len(data) - 1:
        l = []
        for _ in range(h):
            l.append([])
            r = l[-1]
            for _ in range(w):
                r.append(data[pos])
                pos += 1
        layers.append(l)
    return layers


def part1(data):
    data = [int(i) for i in data]
    layers = make_layers(data, 25, 6)
    zero_counts = []
    for l in layers:
        zero_counts.append((l, amt_in_layer(l, 0)))
    best = min(zero_counts, key=(lambda val: val[1]))[0]
    return amt_in_layer(best, 1) * amt_in_layer(best, 2)


def collapse2(img, width=25, height=6):
    layers = []
    for l in img:
        layers.append(list(iter_layer(l)))
    return make_layers([next(filter(lambda v: v != 2, lay)) for lay in zip(*layers)], w=width, h=height)


def part2(data):
    data = [int(i) for i in data]
    layers = make_layers(data, 25, 6)
    final = collapse2(layers)
    assert len(final) == 1
    final = final[0]
    for row in final:
        for pix in row:
            if pix == 1:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()
