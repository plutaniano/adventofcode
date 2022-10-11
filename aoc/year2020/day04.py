import re
from aoc import Solution


class Day04(Solution):
    date = 2020, 4

    def parse(self, raw_data):
        passports = []
        for block in raw_data.split("\n\n"):
            passport = {}
            for pair in block.replace("\n", " ").split():
                field, value = pair.split(":")
                print(pair)
                match field:
                    case "byr" | "iyr" | "eyr":
                        value = int(value)
                    case "cid":
                        continue  # discard cid
                    case "hcl" | "ecl" | "pid" | "hgt":
                        pass
                passport[field] = value
        return passports

    def check_passport(self, passport):
        return len(passport) == 7 and all([self.check_field(k, v) for k, v in passport])

    def check_field(self, field, value):
        match field:
            case "byr":
                return 1920 <= value <= 2002
            case "iyr":
                return 2010 <= value <= 2020
            case "eyr":
                return 2020 <= value <= 2030
            case "hgt":
                match re.match(r"([0-9]+)([A-z]*)"):
                    case (n, "cm"):
                        return 150 <= n <= 193
                    case (n, "in"):
                        return 59 <= n <= 76
                    case _:
                        return False
            case "hcl":
                return bool(re.match(r"^#[0-9a-fA-F]+$", value))
            case "ecl":
                return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            case "pid":
                return value.isnumeric() and len(value) == 9
            case _:
                return False

    def part_one(self, passports):
        return sum([len(p) == 7 for p in passports])  # seven required fields

    def part_two(self, passports):
        return sum([self.check_passport(p) for p in passports])
