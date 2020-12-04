from dataclasses import dataclass


@dataclass
class Passport:
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None
    pid: str = None
    cid: str = None


ATTRS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]


def is_valid_part1(pport):
    for i in ATTRS:
        if i != "cid" and getattr(pport, i, None) is None:
            return False
    return True


def parse_passport(data):
    parts = data.replace("\n", " ").split(" ")
    attrs = {}
    for a in parts:
        k, v = a.split(":")
        if k in ATTRS:
            attrs[k] = v
    return Passport(**attrs)


def parse_batch(data):
    return [parse_passport(i) for i in data.split("\n\n")]


def part1(data):
    pports = parse_batch(data)
    r = 0
    for i in pports:
        if is_valid_part1(i):
            r += 1
    return r


def try_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1


def valid_height(s):
    n = try_int(s[:-2])
    if n == -1:
        return False
    m = s[-2:]
    if m == "cm":
        return 150 <= n <= 193
    elif m == "in":
        return 59 <= n <= 76
    else:
        return False


def is_valid_part2(pport):
    return (
        1920 <= try_int(pport.byr) <= 2002
        and 2010 <= try_int(pport.iyr) <= 2020
        and 2020 <= try_int(pport.eyr) <= 2030
        and pport.hgt
        and valid_height(pport.hgt)
        and pport.ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        and try_int(pport.pid) >= 100000000  # 9 digits
    )


def part2(data):
    pports = parse_batch(data)
    r = 0
    for i in pports:
        if is_valid_part2(i):
            r += 1
    return r
