l = open("input.txt").read().split("\n")
del l[-1]

data = []
for i in l:
    if "mask" in i:
        data.append(("mask", i.split()[-1]))
    else:
        addr = int(i[4:].split("]")[0])
        value = int(i.split(" ")[-1])
        data.append((addr, value))


class Mask:
    def __init__(self, s):
        self.s = s

    def apply(self, target):
        result = []
        target = bin(target)[2:].zfill(36)
        for m, t in zip(self.s, target):
            if m == "X":
                result.append(t)
            else:
                result.append(m)
        return "".join(result)

    def apply2(self, addr):
        addr = list(bin(addr)[2:].zfill(36))
        for i, char in enumerate(self.s):
            if char == "X":
                addr[i] = char
            elif char == "1":
                addr[i] = "1"
        x = addr.count("X")
        results = []
        if x > 0:
            for i in range(2**x):
                bin_sub = list(bin(i)[2:].zfill(x))[::-1]
                new_addr = []
                for i in addr:
                    if i == "X":
                        new_addr.append(bin_sub.pop())
                    else:
                        new_addr.append(i)
                results.append("".join(new_addr))
        else:
            results.append("".join(addr))

        return list(map(lambda x: int(x, 2), results))


mem = {}
for i in data:
    if i[0] == "mask":
        m = Mask(i[1])
    else:
        mem[int(addr)] = m.apply(int(value))

solution1 = sum([int(i, 2) for i in mem.values()])
