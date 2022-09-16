from aoc import Solution


class Day01(Solution):
    date = 2020, 1

    def parse(self, raw_data):
        return [int(i) for i in raw_data.split()]

    def part_one(self, parsed_data):
        for i, a in enumerate(parsed_data):
            for j, b in enumerate(parsed_data[i + 1 :]):
                if a + b == 2020:
                    return a * b

    def part_two(self, parsed_data):
        for i, a in enumerate(parsed_data):
            for j, b in enumerate(parsed_data[i + 1 :]):
                for k, c in enumerate(parsed_data[i + j + 1 :]):
                    if a + b + c == 2020:
                        return a * b * c
