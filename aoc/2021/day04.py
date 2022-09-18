from aoc import Solution
from dataclasses import dataclass
from colorama import Back, Style


@dataclass
class Number:
    value: int
    played: bool = False

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        else:
            return self.value == other

    def __bool__(self):
        return self.played

    def __repr__(self):
        color = Back.GREEN if self.played else Back.BLACK
        return f"{color}{self.value:02}{Style.RESET_ALL}"


class Board:
    def __init__(self, board):
        self.won = False
        self.rows = []
        for line in board.splitlines():
            self.rows.append([Number(int(n)) for n in line.split()])

    def __iter__(self):
        for r, row in enumerate(self.rows):
            for c, number in enumerate(row):
                yield r, c, number

    def __getitem__(self, key):
        return self.rows[key]

    def find(self, n):
        for row, col, number in self:
            if n == number:
                return row, col

    def column(self, i):
        return [row[i] for row in self.rows]

    def row(self, i):
        return self.rows[i]

    def unmarked_sum(self):
        total = 0
        for _, _, number in self:
            total += number.value * (not number.played)
        return total

    def play(self, n):
        if found := self.find(n):
            r, c = found
            self[r][c].played = True
            self.won = self.won or all(self.row(r)) or all(self.column(c))
        return self.won

    def __repr__(self):
        rows = "\n\t".join([str(row) for row in self.rows])
        return f"Board,{self.won}([\n\t{rows}\n])"


class Day04:
    date = 2021, 4

    def parse(self, raw_data):
        numbers, boards = raw_data.split("\n\n", maxsplit=1)
        numbers = [int(i) for i in numbers.split(",")]
        boards = [Board(i) for i in boards.split("\n\n")]
        return numbers, boards

    def part_one(self, parsed_data):
        numbers, boards = parsed_data
        for number in numbers:
            for b in boards:
                has_won = b.play(number)
                if has_won:
                    return number * b.unmarked_sum()

    def part_two(self, parsed_data):
        numbers, boards = parsed_data
        numbers = iter(numbers)
        for number in numbers:
            for board in boards:
                board.play(number)
            if [b.won for b in boards].count(False) == 1:
                break
        last = next(b for b in boards if not b.won)
        for number in numbers:
            last.play(number)
            if last.won:
                break
        return last.unmarked_sum() * number
