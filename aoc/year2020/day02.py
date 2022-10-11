import re
from aoc import Solution


class Day02(Solution):
    date = 2020, 2

    def parse(self, raw_data):
        parsed_data = []
        pat = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
        for line in raw_data.splitlines():
            x, y, l, s = pat.match(line).groups()
            parsed_data.append((int(x), int(y), l, s))
        return parsed_data

    def part_one(self, parsed_data):
        pass

    def part_two(self, parsed_data):
        return super().part_two(parsed_data)
