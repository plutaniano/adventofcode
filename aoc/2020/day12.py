from math import *

l = open("input.txt").readlines()
l = [(i[0], int(i[1:])) for i in l]


class Ship:
    def __init__(self, waypoint=False):
        self.dir = complex(1, 0)
        self.position = complex(0, 0)

    def N(self, steps):
        self.position += steps * complex(0, 1)

    def S(self, steps):
        self.position += steps * complex(0, -1)

    def E(self, steps):
        self.position += steps * complex(1, 0)

    def W(self, steps):
        self.position += steps * complex(-1, 0)

    def F(self, steps):
        self.position += steps * self.dir

    def R(self, angle):
        angle = angle // 90
        angle = angle % 4
        for i in range(angle):
            self.dir *= complex(0, -1)

    def L(self, angle):
        angle = angle // 90
        angle = angle % 4
        for i in range(angle):
            self.dir *= complex(0, 1)


s = Ship()
for i in l:
    method = getattr(s, i[0])
    method(i[1])

solution1 = int(abs(s.position.imag) + abs(s.position.real))


class WaypointShip:
    def __init__(self, waypoint: complex):
        self.dir = complex(1, 0)
        self.position = complex(0, 0)
        self.waypoint = waypoint

    def N(self, steps):
        self.waypoint += steps * complex(0, 1)

    def S(self, steps):
        self.waypoint += steps * complex(0, -1)

    def E(self, steps):
        self.waypoint += steps * complex(1, 0)

    def W(self, steps):
        self.waypoint += steps * complex(-1, 0)

    def F(self, steps):
        self.position += steps * self.waypoint

    def R(self, angle):
        angle = angle // 90
        angle = angle % 4
        for i in range(angle):
            self.waypoint *= complex(0, -1)

    def L(self, angle):
        angle = angle // 90
        angle = angle % 4
        for i in range(angle):
            self.waypoint *= complex(0, 1)


ws = WaypointShip(complex(10, 1))
for i in l:
    method = getattr(ws, i[0])
    method(i[1])

solution2 = int(abs(ws.position.imag) + abs(ws.position.real))

print(f"Part 1: {solution1}")
print(f"Part 2: {solution2}")
