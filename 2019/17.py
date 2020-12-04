intcode = __import__('09').intcodev4


def part1(data):
    icode = [int(i) for i in data.split(',') if i]
    def inp():
        raise ValueError()
    for val in intcode(icode, inp):
        pass
