from aoc import Solution


class Ship:
    def __init__(self):
        self.direction = complex(1, 0)
        self.position = complex(0, 0)

    def manhattan_distance(self):
        return abs(self.position.imag) + abs(self.position.real)

    def move(self, direction, units):
        return getattr(self, f"move_{direction}")(units)

    def move_N(self, units):
        self.position += units * complex(0, 1)

    def move_S(self, units):
        self.position += units * complex(0, -1)

    def move_E(self, units):
        self.position += units * complex(1, 0)

    def move_W(self, units):
        self.position += units * complex(-1, 0)

    def move_F(self, units):
        self.position += units * self.direction

    def move_R(self, units):
        angle = (units // 90) % 4
        for _ in range(angle):
            self.direction *= complex(0, -1)

    def move_L(self, units):
        angle = (units // 90) % 4
        for _ in range(angle):
            self.direction *= complex(0, 1)


class WaypointShip(Ship):
    def __init__(self, waypoint):
        super().__init__()
        self.waypoint = waypoint

    def move_N(self, units):
        self.waypoint += units * complex(0, 1)

    def move_S(self, units):
        self.waypoint += units * complex(0, -1)

    def move_W(self, units):
        self.waypoint += units * complex(1, 0)

    def move_E(self, units):
        self.waypoint += units * complex(-1, 0)

    def move_F(self, units):
        self.position += units * self.waypoint

    def move_R(self, angle):
        angle = (angle // 90) % 4
        for _ in range(angle):
            self.waypoint *= complex(0, -1)

    def move_L(self, angle):
        angle = (angle // 90) % 4
        for _ in range(angle):
            self.waypoint *= complex(0, 1)


class Day12(Solution):
    date = 2020, 12

    def parse(self, raw_data):
        data = []
        for line in raw_data.splitlines():
            direction, units = line[:1], line[1:]
            data.append((direction, int(units)))
        return data

    def part_one(self, moves):
        s = Ship()
        for dir, units in moves:
            s.move(dir, units)
        return s.manhattan_distance()

    def part_two(self, moves):
        s = WaypointShip(waypoint=complex(10, 1))
        for dir, units in moves:
            s.move(dir, units)
        return s.manhattan_distance()
