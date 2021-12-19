l = open('input.txt').read().split('\n')
del l[-1]

solution1 = 0
solution2 = 0

for i in l:
    i = i.split()
    letter = i[1][0]
    a, b = list(map(int, i[0].split('-')))
    string = i[2]
    if a <= string.count(letter) <= b:
        solution1 += 1

    if ((string[a-1] == letter) + (string[b-1] == letter)) == 1:
        solution2 += 1 

print(f'Part 1: {solution1}')
print(f'Part 2: {solution2}')

