from aoc import Solution


class Day01(Solution):
    date = 2021, 1

    def parse(self, data):
        return [int(i) for i in data.splitlines()]

    def part_one(self, data):
        return sum([data[i] < data[i + 1] for i in range(len(data) - 1)])

    def part_two(self, data):
        windows = [sum(data[i : i + 3]) for i in range(len(data) - 2)]
        return self.part_one(windows)
