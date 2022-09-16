l = open("input.txt").read().split("\n")
inp = set()
for x, line in enumerate(l):
    for y, status in enumerate(line):
        if status == "#":
            inp.add((x, y, 0))
now = inp


def neighbors(tup: tuple):
    neighbors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if z == y == x == 0:
                    continue
                else:
                    neighbors.append((tup[0] + x, tup[1] + y, tup[2] + z))
    return neighbors


for _ in range(6):
    new = set()
    to_check = set()
    for active in now:
        to_check.add(active)
        for neighbor in neighbors(active):
            to_check.add(neighbor)

    for cube in to_check:
        qnty = len(set(neighbors(cube)).intersection(now))
        if cube in now:
            if qnty in (2, 3):
                new.add(cube)
        else:
            if qnty == 3:
                new.add(cube)
    now = new

solution1 = len(new)


def neighbors4d(tup: tuple):
    neighbors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    if x == y == z == w == 0:
                        continue
                    else:
                        neighbors.append(
                            (tup[0] + x, tup[1] + y, tup[2] + z, tup[3] + w)
                        )
    return neighbors


now = set([(x, y, z, 0) for x, y, z in inp])

for _ in range(6):
    new = set()
    to_check = set()
    for active in now:
        to_check.add(active)
        for neighbor in neighbors4d(active):
            to_check.add(neighbor)

    for cube in to_check:
        qnty = len(set(neighbors4d(cube)).intersection(now))
        if cube in now:
            if qnty in (2, 3):
                new.add(cube)
        else:
            if qnty == 3:
                new.add(cube)
    now = new

solution2 = len(new)

print(f"Part 1: {solution1}")
print(f"Part 2: {solution2}")
