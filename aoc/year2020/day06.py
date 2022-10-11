from functools import reduce
from aoc import Solution


class Day06(Solution):
    date = 2020, 6

    def parse(self, raw_data):
        return [group.splitlines() for group in raw_data.split("\n\n")]

    def part_one(self, groups):
        unique_letters = [set("".join(group)) for group in groups]
        return sum([len(letters) for letters in unique_letters])

    def part_two(self, groups):
        common_letters = [reduce(lambda a, b: {*a} & {*b}, group) for group in groups]
        return sum([len(letters) for letters in common_letters])


Day06().submit()
