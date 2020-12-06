l = open('input.txt').read().split()

def seat_id(s):
    d = {
            'B': '1',
            'F': '0',
            'R': '1',
            'L': '0'
        }

    for i in d.keys():
        s = s.replace(i, d[i])

    row = int(s[:-3], 2)
    col = int(s[-3:], 2)

    return row * 8 + col

ids = sorted([seat_id(i) for i in l])
solution1 = max(ids)

for i, n in enumerate(ids):
    if ids[i] != ids[i+1] - 1:
        solution2 = ids[i] + 1
        break

print(f'Part 1: {solution1}')
print(f'Part 2: {solution2}')
