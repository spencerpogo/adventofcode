from itertools import combinations


class Moon:
    def __init__(self, x, y, z):
        #print(x, y, z)
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]
    
    def update_velocity(self, other):
        for i in range(3):
            selfv = self.pos[i]
            otherv = other.pos[i]
            if selfv > otherv:
                self.vel[i] -= 1
            elif otherv > selfv:
                self.vel[i] += 1
    
    def step(self):
        for i in range(3):
            self.pos[i] += self.vel[i]
    
    def potential(self):
        val = sum(abs(i) for i in self.pos)
        #print(" + ".join(str(i) for i in self.pos), "=", val)
        return val
    
    def kinetic(self):
        val = sum(abs(i) for i in self.vel)
        #print(" + ".join(str(i) for i in self.vel), "=", val)
        return val
    
    def total_energy(self):
        return self.potential() * self.kinetic()
    
    def get_state(self):
        return (self.pos, self.vel)

    def __repr__(self):
        return f"Moon() pos=<{', '.join(str(i) for i in self.pos)}>, vel=<{', '.join(str(i) for i in self.vel)}>"


class Universe:
    def __init__(self, moons):
        self.moons = moons
    
    def get_state(self):
        return (i.get_state() for i in self.moons)
    
    def step(self):
        for m1, m2 in combinations(self.moons, 2):
            m1.update_velocity(m2)
            m2.update_velocity(m1)
        for m in self.moons:
            m.step()
    
    def total_energy(self):
        return sum(m.total_energy() for m in self.moons)

def part1(data):
    uni = Universe([Moon(x, y, z) for x, y, z in [[int(a.split("=")[1]) for a in l.split(", ")] for l in [i.replace("<", "").replace(">", "") for i in data.split("\n") if i]]])
    for _ in range(1000):
        uni.step()
    return uni.total_energy()

def part2(data):
    uni = Universe([Moon(x, y, z) for x, y, z in [[int(a.split("=")[1]) for a in l.split(", ")] for l in [i.replace("<", "").replace(">", "") for i in data.split("\n") if i]]])
    previous = set()
    steps = 0
    while True:
        uni.step()
        steps += 1
        state = uni.get_state()
        if state in previous:
            break
        previous.add(state)
    return steps
