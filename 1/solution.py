l = list(map(int, open('input.txt').read().split()))

for i, n in enumerate(l):
    for j, m in enumerate(l[i+1:]):
        if n + m == 2020:
            solution1 = n*m

print(f'Part 1: {solution1}')

for i, n in enumerate(l):
    for j, m in enumerate(l[i+1:]):
        for k, o in enumerate(l[i+j+1:]):
            if n + m + o == 2020:
                solution2 = n*m*o

print(f'Part 2: {solution2}')

