import copy
import random

class Hat:
    contents = []
    def __init__(self, **kwargs):
        self.arguments = kwargs

        for key, value in self.arguments.items():
            for x in range(0,value):
                self.contents.append(key)
            
    def __str__(self):
        return f'{self.contents}'
    
    def draw(self, balls):
        initial = copy.copy(self.contents)
        if balls > len(initial):
            draw = initial

            return draw
        
        else:
            draw = []

            for x in range(0, balls):
                indices = range(0, len(initial))
                item = random.choice(indices)
                draw.append(initial[item])
                new = copy.copy(initial)
                new.pop(item)
                initial = new

            return draw

    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print(hat)

hat1 = Hat(yellow=3, blue=2, green=6)



print(hat1.draw(2))
