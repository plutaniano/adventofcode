from __future__ import annotations
from collections import defaultdict

from aocd import get_data, submit


ALL_SOLUTIONS = defaultdict(dict)


class SolutionMeta(type):
    def __new__(cls, name, bases, body):
        new = super().__new__(cls, name, bases, body)
        if body.get("date"):
            cls.year, cls.day = body["date"]
            ALL_SOLUTIONS[cls.year][cls.day] = new()
        return new


class SolutionBase(metaclass=SolutionMeta):
    def __init__(self):
        self.year, self.day = self.date
        self.raw_data = get_data(year=self.year, day=self.day)
        self.parsed_data = self.parse(self.raw_data)

    def parse(self, raw_data):
        pass

    def part_one(self, parsed_data):
        raise NotImplemented

    def part_two(self, parsed_data):
        raise NotImplemented

    def solve(self):
        one = self.part_one(self.parsed_data)
        two = self.part_two(self.parsed_data)
        return one, two

    def submit(self):
        one, two = self.solve()
        # implement actual check
        print(one, two)
        return False, False

    def __repr__(self):
        return f"<Solution: year={self.year}, day={self.day}>"


class Solution(SolutionBase, metaclass=SolutionMeta):
    pass
