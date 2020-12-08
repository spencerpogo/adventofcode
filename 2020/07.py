from dataclasses import dataclass


@dataclass
class Bag:
    name: str
    count: int


def parse_rules(data, need_count):
    bags = {}
    for l in data.split(".\n"):
        bag_name, contains = l.split(" contain ")
        if not contains.startswith("no other bags"):
            children = []
            for n in contains.split(", "):
                parts = n.split(" ")
                name = " ".join(parts[1:-1])
                if need_count:
                    count = int(parts[0])
                    children.append(Bag(name=name, count=count))
                else:
                    children.append(name)
            bags[bag_name[:-5]] = children
    return bags


def expand_rule(rules, key):
    if key not in rules:
        return []
    r = []
    for child in rules[key]:
        r.append(child)
        r += expand_rule(rules, child)
    return r


def part1(data):
    rules = parse_rules(data, False)

    expanded_rules = {}
    for r in rules.keys():
        expanded_rules[r] = expand_rule(rules, r)
    
    r = 0
    for k, bags in expanded_rules.items():
        if 'shiny gold' in bags:
            r += 1

    return r


def count_needed(rules, key, counts):
    if key in counts:
        return counts[key], counts

    r = 1
    for dep in rules.get(key, [ ]):
        c, counts = count_needed(rules, dep.name, counts)
        r += c * dep.count

    counts[key] = r
    return r, counts


def part2(data):
    rules = parse_rules(data, True)
    total, _ = count_needed(rules, 'shiny gold', {})
    return total - 1
