f = open('input.txt').read().replace('\n', ' ').split('  ')

fields = {
        'byr': lambda yr: 1920 <= int(yr) <= 2002,
        'iyr': lambda yr: 2010 <= int(yr) <= 2020,
        'eyr': lambda yr: 2020 <= int(yr) <= 2030,
        'hgt': lambda s: 150 <= int(s[:-2]) <= 193 if s[-2:] == 'cm' else 59 <= int(s[:-2]) <= 76 if s[-2:] == 'in' else False,
        'hcl': lambda hcl: all([i in '0123456789abcdefABCDEF' for i in hcl[1:]]) if hcl[0] == '#' else False, 
        'ecl': lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda n: n.isnumeric() and len(n) == 9
        }

solution1 = 0
solution2 = 0

for pp in f:
    fail = False
    for field in fields.keys():
        if field + ':' not in pp:
            fail = True
            break
    if not fail:
        solution1 += 1
        pp = pp.split()
        for item in pp:
            if item[:3] == 'cid':
                continue
            func = fields[item[:3]]
            if not func(item[4:]):
                fail = True
                break
        if not fail:
            solution2 += 1

print(f'Part 1: {solution1}')
print(f'Part 2: {solution2}')
