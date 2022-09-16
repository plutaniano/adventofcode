# thanks geohot
import re

l = open("input.txt").read().split("\n")
del l[-1]


class N:
    def __init__(self, i):
        self.i = i

    def __add__(self, x):
        return N(self.i + x.i)

    def __sub__(self, x):
        return N(self.i * x.i)


def eeval(string):
    s = ""
    in_num = False
    num = ""
    for i in string:
        if i in "0123456789" and not in_num:
            s += "N("
            in_num = True

        if i not in "0123456789" and in_num:
            s += ")"
            in_num = False

        s += i

    if in_num:
        s += ")"
    return eval(s)


solution1 = N(0)
for i in l:
    solution1 += eeval(i.replace("*", "-"))

print(f"Part 1: {solution1.i}")

N.__add__ = lambda self, x: N(self.i * x.i)
N.__mul__ = lambda self, x: N(self.i + x.i)

solution2 = N(0)
for i in l:
    print(i)
    print(i.replace("*", "#").replace("+", "*").replace("#", "+"))
    # using * instead of + because of the lambda __mul__ above
    solution2 *= eeval(i.replace("*", "#").replace("+", "*").replace("#", "+"))
    print(solution2.i)
    input()

print(f"Part 2: {solution2.i}")
