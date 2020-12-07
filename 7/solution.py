l = open('input.txt').read().split('\n')
del l[-1]

class Bag:
    all = []

    def __init__(self, type, color):
        Bag.all.append(self)
        self.type = type
        self.color = color
        self.contain = []

    def add_contain(self, bag, qnty):
        self.contain.append((bag, qnty))

    @classmethod
    def get_bag(cls, type, color):
        for bag in Bag.all:
            if bag.type == type and bag.color == color:
                return bag
        return Bag(type, color)

    def bags_inside(self):
        if not self.contain:
            return 0
        else:
            #print(f'{self} contains {",".join([i[0].__repr__() for i in self.contain])}.')
            return sum([i[1] + i[0].bags_inside()*i[1] for i in self.contain])

    def is_inside(self, type, color):
        for i in self.contain:
            if i[0].type == type and i[0].color == color:
                return True

        return any([i[0].is_inside(type, color) for i in self.contain])
    
    def __repr__(self):
        return f'[bag] <{self.type} {self.color}>'

def parse_line(line):
    line = line.split(' contain ')
    main = line[0].split()
    
    if 'no other' not in line[1]:
        contain = line[1].replace('.','').split(', ') 
        contain = [i.split() for i in contain]
    else:
        contain = []

    d = {
            'main_color': main[1],
            'main_type': main[0],
            'contain_qnty': [int(i[0]) for i in contain], 
            'contain_type': [i[1] for i in contain],
            'contain_color': [i[2] for i in contain],
        }
    return d

for line in l:
    d = parse_line(line)
    bag = Bag.get_bag(d['main_type'], d['main_color'])

    for i, qnty in enumerate(d['contain_qnty']):
        bag.add_contain(Bag.get_bag(d['contain_type'][i], d['contain_color'][i]), qnty)


print(f"Part 1: {sum([i.is_inside('shiny', 'gold') for i in Bag.all])}")
print(f"Part 2: {Bag.get_bag('shiny', 'gold').bags_inside()}")
