from aoc import Solution


class Line:
    def __init__(self, raw_data):
        p1, p2 = raw_data.split(" -> ")
        x1, y1, x2, y2 = map(int, f"{p1},{p2}".split(","))
        self.start = x1, y1
        self.end = x2, y2

    def is_straight(self):
        return self.start[0] == self.end[0] or self.start[1] == self.end[1]


class Day05(Solution):
    date = 2021, 5

    def parse(self, raw_data):
        return [Line(i) for i in raw_data.splitlines()]
