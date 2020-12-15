from typing import *

l = open('input.txt').read().split('\n')


class Game:
    def __init__(self, numbers: List[int]):
        self.spoken_pos = {}
        self.numbers = numbers
        for i, n in enumerate(numbers, start=1):
            try:
                self.spoken_pos[n].append(i)
            except KeyError:
                self.spoken_pos[n] = [i]
    
    def speak(self) -> None:
        last = self.numbers[-1]
        if last not in self.numbers:
            self.numbers.append(0)
            self.spoken_pos[0].append(len(numbers))
        else:
            number = self.spoken_pos[last][0] - self.spoken_pos[last][1]
            self.numbers.append(number)
            self.spoken_pos[number].append(len(numbers))



        


