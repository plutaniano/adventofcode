from aoc import Solution
from collections import Counter, defaultdict


class Bag:
    all = defaultdict(dict)

    def __new__(cls, kind, color):
        if cls.all[kind].get(color):
            return cls.all[kind][color]
        new = super().__new__(cls)
        cls.all[kind][color] = new
        return new

    def __init__(self, kind, color):
        self.kind = kind
        self.color = color
        self.inside = Counter()

    def __iter__(self):
        return self.inside.items()

    def __contains__(self, other_bag):
        if self.is_empty():
            return False
        return any([other_bag in bag for bag in self])

    def is_empty(self):
        return bool(self.inside)

    def put_inside(self, n, kind, color):
        bag = Bag(kind, color)
        self.inside[bag] += n

    def bags_inside(self):
        total = 0
        for bag, n in self:
            total += n + bag.bags_inside() * n
        return total

    def __repr__(self) -> str:
        return f"Bag('{self.kind}', '{self.color}')"


class Day07(Solution):
    date = 2020, 7

    def parse(self, raw_data):
        for line in raw_data.splitlines():
            outside, inside = line.split(" contain ")
            kind, color, _ = outside.split()
            outside = Bag(kind, color)
            if inside == "no other bags.":
                continue
            else:
                for bag in inside.split(","):
                    n, kind, color, _ = bag.split()
                    outside.put_inside(int(n), kind, color)
        return Bag.all

    def part_one(self, bags):
        shiny_gold = Bag("shiny", "gold")
        return sum([shiny_gold in bag for bag in bags])

    def part_two(self, _):
        return Bag("shiny", "gold").bags_inside()
