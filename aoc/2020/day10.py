from collections import defaultdict

inp = open("input.txt").read().split()
inp = list(map(int, inp))
inp.append(0)
inp.sort()
inp.append(inp[-1] + 3)

diffs = [inp[i + 1] - inp[i] for i in range(len(inp[:-1]))]
solution1 = diffs.count(1) * diffs.count(3)

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
