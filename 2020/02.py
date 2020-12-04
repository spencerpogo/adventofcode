from dataclasses import dataclass


@dataclass
class PasswordRule:
    numa: int
    numb: int
    char: str


def valid_sled(rule, pwd):
    count = pwd.count(rule.char)
    return count >= rule.numa and count <= rule.numb


def valid_toboggan(rule, pwd):
    pos_a_valid = 0 <= rule.numa - 1 < len(pwd) and pwd[rule.numa - 1] == rule.char
    pos_b_valid = 0 <= rule.numb - 1 < len(pwd) and pwd[rule.numb - 1] == rule.char
    return pos_a_valid ^ pos_b_valid


def parse_password_rule(rule):
    amts, char = rule.split(" ")
    numa, numb = amts.split("-")
    return PasswordRule(int(numa), int(numb), char)


def count_valid(data, parser):
    lines = [l.strip().split(": ") for l in data.split("\n")]
    valid = 0

    for rule_text, pwd in lines:
        rule = parse_password_rule(rule_text)
        if parser(rule, pwd):
            valid += 1

    return valid


def part1(data):
    return count_valid(data, valid_sled)


def part2(data):
    return count_valid(data, valid_toboggan)
