from collections import Counter

with open('input.txt') as f:
    txt = [i for i in f.read().splitlines()]

def solution_1(txt):
    bits = [[int(n[i]) for n in txt] for i in range(len(txt[0]))]
    most_common_bit = [int(sum(l) > len(txt)/2) for l in bits]
    n = int(''.join(map(str, most_common_bit)))
    return n * ((2 ** len(txt[0]) -1) - n)


print(f'Part 1: {solution_1(txt)}')
#print(f'Part 2: {solution_2(txt)}')
