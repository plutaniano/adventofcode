from aoc import Solution


class Day08(Solution):
    date = 2020, 8

    def parse(self, raw_data):
        data = []
        for line in raw_data.splitlines():
            opcode, operand = line.split()
            data.append([opcode, operand])
        return data

    def execute(self, program):
        pc = 0  # program counter
        accumulator = 0
        executed = set()
        while pc not in executed or pc >= len(program):
            executed.add(pc)
            match program[pc]:
                case "acc", v:
                    accumulator += int(v)
                    pc += 1
                case "jmp", v:
                    pc += int(v)
                case "nop":
                    pc += 1
        return accumulator, pc not in executed

    def part_one(self, program):
        accumulator, _ = self.execute(program)
        return accumulator

    def part_two(self, program):
        for nop_jmp in range(len(program)):
            nop_jmp_counter = 0
            modified_program = program.copy()
            for i, (opcode, _) in enumerate(program):
                if opcode in "nop", "jmp":
                    nop_jmp_counter += 1
                if nop_jmp == nop_jmp_counter:
                    modified_program[i][0] = "jmp" if opcode == "nop" else "nop"
                acc, terminated = self.execute(modified_program)
                if terminated:
                    return acc
