import os

l = open('./input.txt').read().split('\n\n')
l[-1] = l[-1][:-1]
solution1 = 0
solution2 = 0

for group in l:
    people = group.count('\n') + 1 
    s = set(list(group))
    try:
        s.remove('\n')
    except:
        pass
    solution1 += len(s) 
    for letter in s:
        if group.count(letter) == people:
            solution2 += 1

print(f'Part 1: {solution1}')
print(f'Part 2: {solution2}')
