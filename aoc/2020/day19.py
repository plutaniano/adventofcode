import re

l = open("sample.txt").read().split("\n\n")
rules = l[0].split("\n")
del rules[0]

msgs = l[1].split("\n")
del msgs[-1]


def get_rule(rule):
    print(rule)
    input()
    for i in rules:
        if i.split(": ")[0] == rule:
            rule = i.split(": ")[1]
            break
    if '"' in rule:
        return rule.split('"')[1]
    else:
        halfs = []
        for i in rule.split(" | "):
            print(i)
            total = ""
            for n in i:
                total += get_rule(n)
            halfs.append(total)
        return total
