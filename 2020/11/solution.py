import copy

grid = open('input.txt').read().split('\n')
grid = [list(i) for i in grid]
del grid[-1]

originalgrid = copy.deepcopy(grid)

def count_adj(g, i, j):
    n = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            try:
                if i+a < 0 or j+b < 0:
                    continue
                if g[i+a][j+b] == '#' and (a != 0 or b != 0):
                    n += 1
            except:
                pass
    return n

def round(g):
    new_grid = copy.deepcopy(g) 

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if g[i][j] == 'L' and count_adj(g, i, j) == 0:
                new_grid[i][j] = '#'
            elif g[i][j] == '#' and count_adj(g, i, j) >= 4:
                new_grid[i][j] = 'L'
            else:
                pass
    return new_grid 

ok = True
n = 0
while ok:
    x = round(grid)
    n += 1

    print(n)
    if x == grid:
        ok = False
    grid = x

solution1 = sum([line.count('#') for line in grid])

def count_adj(g, i, j):
    n = 0
    print('new counter')
    for a in range(-1, 2):
        for b in range(-1, 2):
            try:
                mult = 1
                found = False
                while not found:
                    if a == 0 and b == 0:
                        break                        

                    if (seat := g[i + mult*a][j + mult * b]) != '.':
                        if seat == 'L':
                            found = True
                        elif seat == '#':
                            n += 1
                            found = True
                            
            except KeyboardInterrupt:
                break
    return n

grid = copy.deepcopy(originalgrid)
ok = True
n = 0
while ok:
    x = round(grid)
    n += 1

    print(n)
    if x == grid:
        ok = False
    grid = x

solution2 = sum([line.count('#') for line in grid])
