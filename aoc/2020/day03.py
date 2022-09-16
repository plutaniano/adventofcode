from aoc import Solution


class Day03(Solution):
    date = 2020, 3

    def parse(self, raw_data):
        trees = raw_data.split()
        height = len(trees)
        width = len(trees[0])
        return trees, height, width

    def slope(self, x_step, y_step):
        trees, height, width = self.parsed_data
        for i in range(0, height, y_step):
            if trees[i][x] == "#":
                trees += 1
            x += x_step
            x %= width
        return trees

    def part_one(self, parsed_data):
        return self.slope(3, 1)

    def part_two(self, parsed_data):
        return (
            self.slope(1, 1)
            * self.slope(3, 1)
            * self.slope(5, 1)
            * self.slope(7, 1)
            * self.slope(1, 2)
        )
