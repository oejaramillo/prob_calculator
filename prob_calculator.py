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
    contents = hat.contents

    expected = []
    for key, value in expected_balls.items():
        for x in range(0, value):
           expected.append(key)

    result = hat.draw(num_balls_drawn)
    if result == expected:
        proof = 1
    else:
        proof = 0


    return f'resultados {result} esperado {expected} prueba {proof}'

hat1 = Hat(yellow=3, blue=2, green=6)



print(experiment(hat1, {"yellow":2}, 2, 2000))
