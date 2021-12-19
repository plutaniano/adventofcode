from typing import *

l = open('input.txt').read().split('\n')


class Game:
    def __init__(self, numbers: List[int]):
        self.spoken_pos = {}
        self.numbers = numbers
        self.n_len = len(numbers) - 1
        for i, n in enumerate(numbers):
            try:
                self.spoken_pos[n].append(i)
            except KeyError:
                self.spoken_pos[n] = [i]
    
    def speak(self) -> None:
        last = self.numbers[-1]
        if len(self.spoken_pos[last]) <= 1:
            number = 0
        else:
            number = self.spoken_pos[last][-1] - self.spoken_pos[last][-2]
        self.numbers.append(number)
        try:
            self.spoken_pos[number].append(len(self.numbers) - 1)
        except:
                self.spoken_pos[number] = [len(self.numbers) -1]

g = Game([0,6,1,7,2,19,20])

for i in range(30000000):
    g.speak()


print(f'Part 1: {g.numbers[2020-1]}')
print(f'Part 2: {g.numbers[30000000-1]}')
        


