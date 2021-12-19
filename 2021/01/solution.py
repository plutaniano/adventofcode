with open('input.txt') as f:
    txt = f.read()

txt = [int(i) for i in txt.splitlines()]

def solution_1(txt):
    return sum([txt[i] < txt[i+1] for i in range(len(txt[1:]))])

def solution_2(txt):
    windows = [sum(txt[i:i+3]) for i in range(len(txt[2:]))]
    return solution_1(windows)

print(f'Part 1: {solution_1(txt)}')
print(f'Part 2: {solution_2(txt)}')
