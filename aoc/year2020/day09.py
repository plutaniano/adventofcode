from aoc import Solution

class Day09(Solution):
    date = 2020, 9

    def parse(self, raw_data):
        return [int(i) for i in raw_data.splitlines()]

class Day9:
    def __init__(self, first25):
        self.list = first25

    def add(self, item):
        self.list = self.list[1:] + [item]


d = Day9(l[:25])
for index, number in enumerate(l[25:]):
    ok = False
    for i, n in enumerate(d.list):
        if number - n in d.list[i:]:
            ok = True

    if not ok:
        solution1 = number
        break
    d.add(number)

solution2 = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        soma = sum(l[i:j])
        if soma > solution1:
            break
        if soma == solution1:
            solution2 = max(l[i:j]) + min(l[i:j])
            break
    if solution2:
        break

print(f"Part 1: {solution1}")
print(f"Part 2: {solution2}")
