with open("input.txt") as f:
    numbers, boards = f.read().split("\n\n", maxsplit=1)
    boards = boards.split("\n\n")
    for i, b in enumerate(boards):
        b = [[int(n) for n in row.split(" ")] for row in b.splitlines()]
        boards[i] = b

print(boards)
