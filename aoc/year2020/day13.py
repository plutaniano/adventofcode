from aoc import Solution
from functools import reduce

#  Chinese Remainder Theorem for part 2
#  using buses 7,13,x,x,59,x,31,19
#
# "x =  b mod  n"
# ---------------
#  t =  0 mod  7
#  t = 12 mod 13
#  t = 55 mod 59      bi | Ni      | Xi | bi*Ni*Xi    |
#  t = 25 mod 31       0 | 451_763 |  2 |           0 |
#  t = 12 mod 19      12 | 243_257 |  1 |   2_919_084 |
#                     55 | 53_599  | 35 | 103_178_075 |   sum mod N = 1_068_781
#  N = 3_162_341      25 | 102_011 |  3 |   7_650_825 |
#                     12 | 166_439 | 18 |  35_950_824 |
#                                    sum: 149_698_808


class Day13:
    date = 2020, 13

    def parse(self, raw_data):
        arrival, ids = raw_data.splitlines()
        arrival = int(arrival)
        ids = [int(id) if id.isnumeric() else "x" for id in ids.split(",")]
        return arrival, ids

    def calculate_Xi(self, Ni, n):
        # a * Xi = 1 mod n
        a = Ni % n
        for Xi in range(1, n + 1):
            if ((a * Xi) % n) == 1:
                return Xi

    def chinese_remainder(self, ids):
        equations = []
        for i, n in enumerate(ids):
            if n == "x":
                continue
            b = (n - i) % n
            equations.append((b, n))

        N = reduce(lambda i, j: i * j, [n for _, n in equations])
        total = 0
        for b, n in equations:
            Ni = N / n
            total += b * Ni * self.calculate_Xi(Ni, n)
        return total % N

    def part_one(self, parsed_data):
        arrival, ids = parsed_data
        best = float("inf"), None
        for id in ids:
            if id != "x":
                delay = id - (arrival % id)
                if delay < best[0]:
                    best = delay, id
        return best[0] * best[1]
