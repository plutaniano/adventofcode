from collections import Counter

with open('input.txt') as f:
    txt = [i for i in f.read().splitlines()]

def solution_1(txt):
    gamma = []
    for bit in range(len(txt[0])):
        bits = [line[bit] for line in txt]
        counter = Counter(bits)
        gamma.append(counter.most_common()[0][0])

    gamma = ''.join(gamma)
    epsilon = gamma.replace('1', '-').replace('0', '1').replace('-', '0')
    epsilon = ''.join(epsilon)

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon

print(f'Part 1: {solution_1(txt)}')
#print(f'Part 2: {solution_2(txt)}')
