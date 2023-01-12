from aoc import Solution

class Day10(Solution):
    date = 2020, 10

    def parse(self, raw_data):
        return sorted([int(i) for i in raw_data.split()])
    
    def part_one(self, parsed_data):
        data = [0] + parsed_data
        diffs = [data[i + 1] - data[i] for i in range(len(data[:-1]))]
        return diffs.count(1) * diffs.count(3)

options = []
for i in range(len(inp)):
    n = inp[i]
    options.append(inp.count(n + 1) + inp.count(n + 2) + inp.count(n + 3))

dd = defaultdict(int)
dd[0] = 1

for i in inp:
    for j in range(1, 4):
        next = i + j
        if next in inp:
            dd[next] += dd[i]
