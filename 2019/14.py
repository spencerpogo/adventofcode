import math
from collections import defaultdict


class Element:
    def __init__(self, amnt, item):
        self.amnt = amnt
        self.item = item

    def __eq__(self, obj):
        return (
            isinstance(obj, Element) and obj.item == self.item and obj.amnt == self.amnt
        )

    def __repr__(self):
        return f"{self.amnt} {self.item}"


class Reaction:
    def __init__(self, inputs, output):
        self.inputs = inputs
        self.output = output

    def __eq__(self, obj):
        return (
            isinstance(obj, Reaction)
            and obj.inputs == self.inputs
            and obj.output == self.output
        )

    def __repr__(self):
        return ", ".join(str(i) for i in self.inputs) + f" => {self.output}"


class Factory:
    def __init__(self, reactions):
        self.reactions = reactions
        self.have = {}
        # self.PRODUCED = defaultdict(lambda: 0)
        # self.DEBUG = defaultdict(lambda: 0)

    def reaction_for(self, outputitem):
        # reactions = [i for i in self.reactions if i.output.item == outputitem]
        # assert len(reactions) == 1
        # return reactions[0]
        return self.reactions[outputitem]

    def raw_needed(self, rawitem, amnt, outitem, indent=0):
        if outitem == rawitem:
            # print(" "*indent + f"Consume {amnt} {rawitem}")
            return amnt
        # print(" "*indent + f"Need {amnt} {outitem}", end='')

        # old = amnt
        if outitem in self.have:
            amnt -= self.have[outitem]
            if amnt < 0:
                self.have[outitem] = -amnt
                amnt = 0
            else:
                self.have[outitem] = 0
            # print("\n"+" "*indent + f"Took {old - amnt} {outitem} from inventory", end='')

        if amnt < 0:
            raise ValueError(f"amnt is negative: {amnt}")
        elif amnt == 0:
            return 0

        # get the reactions
        r = self.reaction_for(outitem)
        # how many times to run
        times = math.ceil(amnt / r.output.amnt)
        # print(f", reacting {times} times: " + ", ".join(f"{n.amnt * times} {n.item}" for n in r.inputs))
        # oldprods = dict(self.PRODUCED)
        # actually do the reaction
        raw = 0
        for _ in range(times):
            for i in r.inputs:
                # if i.item == rawitem:
                #    print(" "*(indent+4)+f"For {outitem}:")
                #    self.DEBUG[outitem] += i.amnt
                raw += self.raw_needed(rawitem, i.amnt, i.item, indent=indent + 4)

        # print(" "*indent + f"Produced {r.output.amnt * times} {r.output.item} with {raw} {rawitem}, produced new items: " + ", ".join(f"{self.PRODUCED[k] - oldprods.get(k, 0)} {k}" for k in self.PRODUCED.keys() if k not in oldprods or oldprods[k] != self.PRODUCED[k]))
        # self.PRODUCED[r.output.item] += r.output.amnt * times

        # add any leftovers to inventory
        if r.output.item not in self.have:
            self.have[r.output.item] = 0
        self.have[r.output.item] += (r.output.amnt * times) - amnt

        # if self.have[r.output.item] > 0:
        #    print(" "*indent + f"{self.have[r.output.item]} leftover {r.output.item}")

        if self.have[r.output.item] < 0:
            raise ValueError(
                f"Made less than needed of {outitem}: have[{r.output.item}] is {self.have[r.output.item]}"
            )
        return raw

    @staticmethod
    def make_reations(data):
        # elements = []
        elements = {}
        for l in data.split("\n"):
            if not l:
                continue
            inptext, out = l.strip().split(" => ")
            oamnt, oitem = out.split(" ")
            oamnt = int(oamnt)
            out = Element(oamnt, oitem)
            inps = []
            for inp in inptext.split(", "):
                amnt, item = inp.split(" ")
                amnt = int(amnt)
                inps.append(Element(amnt, item))
            # elements.append(Reaction(inps, out))
            elements[oitem] = Reaction(inps, out)
        return Factory(elements)


def part1(data):
    reactions = Factory.make_reations(data)
    ore = reactions.raw_needed("ORE", 1, "FUEL")
    # print()
    # print(dict(reactions.DEBUG))
    # print("Produced the following:")
    # for item, amnt in dict(reactions.PRODUCED).items():
    #    print(f"{amnt} {item}")
    return ore


def part2(data):
    # return
    have = 1000000000000
    reactions = Factory.make_reations(data)
    # Binary search (idrk how this works)
    low = 1
    high = 1 << 24
    i = 0
    while True:
        # i += 1
        # print(i)
        # r = reactions.raw_needed("ORE", i, "FUEL")
        # print(r)
        # if r > have:
        #    return i

        # continue
        if high <= low:
            break
        mid = low + math.floor((high - low) / 2)
        print(mid)
        cur = reactions.raw_needed("ORE", mid, "FUEL")
        if cur == have:
            return cur
        elif cur > have:
            high = mid - 1
        else:
            low = mid + 1
    return low - 1
