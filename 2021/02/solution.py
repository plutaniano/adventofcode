with open('input.txt') as f:
    txt = [i.split() for i in f.read().splitlines()]
    txt = [(c, int(v)) for c, v in txt]


def solution_1(txt):
    x, y = 0, 0
    for command, value in txt:
        if command == 'forward': x += value
        if command == 'up': y -= value
        if command == 'down': y += value

    return x * y

def solution_2(txt):
    x, y, aim = 0, 0, 0
    for command, value in txt:
        if command == 'up': aim -= value
        if command == 'down': aim += value
        if command == 'forward':
            x += value
            y += aim * value
    return x * y


print(f'Part 1: {solution_1(txt)}')
print(f'Part 2: {solution_2(txt)}')
