from aoc import Solution


class Submarine:
    def __init__(self, aim=False):
        self.position = complex(0, 0)
        self.aim = 0
        self.use_aim = aim

    def _move_depth(self, command, units):
        match command:
            case "forward":
                self.position += complex(units, 0)
            case "up":
                self.position += complex(0, -units)
            case "down":
                self.position += complex(0, units)

    def _move_aim(self, command, units):
        match command:
            case "forward":
                self.position += complex(units, self.aim * units)
            case "up":
                self.aim -= units
            case "down":
                self.aim += units

    def move(self, command, units):
        if self.use_aim:
            self._move_aim(command, units)
        else:
            self._move_depth(command, units)

    def answer(self):
        return self.position.real * self.position.imag


class Day02(Solution):
    date = 2021, 2

    def parse(self, raw_data):
        lines = [line.split() for line in raw_data.splitlines()]
        return [(instr, int(n)) for instr, n in lines]

    def part_one(self, parsed_data):
        sub = Submarine()
        for instr, n in parsed_data:
            sub.move(instr, n)
        return sub.answer()

    def part_two(self, parsed_data):
        sub = Submarine(aim=True)
        for instr, n in parsed_data:
            sub.move(instr, n)
        return sub.answer()
