from aoc import Solution


class Day05(Solution):
    date = 2020, 5
    table = {"B": "1", "F": "0", "R": "1", "L": "0"}

    def parse(self, raw_data):
        return raw_data.splitlines()

    def seat_id(self, seat):
        for letter in seat:
            seat.replace(letter, self.table[letter])
        row = int(seat[:-3], 2)
        col = int(seat[-3:], 2)
        return row * 8 + col

    def part_one(self, seats):
        return max([self.seat_id(seat) for seat in seats])

    def part_two(self, seats):
        ids = sorted([self.seat_id(seat) for seat in seats])
        for i, seat in enumerate(ids):
            if ids[i + 1] != seat + 1:
                return seat + 1
