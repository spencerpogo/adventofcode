orbit = None


class Obj:
    def __init__(self, name, sub=None):
        self.name = name
        self.sub = sub
        self.parent = None

    def sub_orbits(self):
        if self.sub:
            return [self.sub] + self.sub.sub_orbits()
        else:
            return []

    def __repr__(self):
        return f"<Orbit {self.name}>"


def init_orbits(items):
    orbits = {}
    for it in items:
        obj, sat = it.split(")")
        if obj in orbits:
            obj_o = orbits[obj]
        else:
            obj_o = Obj(obj)
            orbits[obj] = obj_o
        if sat in orbits:
            sat_o = orbits[sat]
        else:
            sat_o = Obj(sat)
            orbits[sat] = sat_o
        sat_o.sub = obj_o
        obj_o.parent = sat_o
    return orbits


def find_connection(o1, o2, count=0):
    if o1.sub in o2.sub_orbits():
        return o1.sub, count
    return find_connection(o1.sub, o2, count + 1)


def shortest_path(o1, o2):
    dest, steps = find_connection(o1, o2)
    while dest != o2.sub:
        o2 = o2.sub
        steps += 1
    return steps


def part1(data):
    items = [i for i in data.split("\n") if i]
    orbits = init_orbits(items)
    total = 0
    for n in orbits:
        total += len(orbits[n].sub_orbits())
    # print(orbits)
    return total


def part2(data):
    global orbits
    items = [i for i in data.split("\n") if i]
    orbits = init_orbits(items)
    return shortest_path(orbits["YOU"], orbits["SAN"])
