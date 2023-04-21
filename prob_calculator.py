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

    expected_colors = list(expected_balls.keys())
    expected = []
    for key, value in expected_balls.items():
        for x in range(0, value):
           expected.append(key)

    total = []
    realizaciones = 0
    for y in range(0, num_experiments):
        result = hat.draw(num_balls_drawn)
        
        for x in expected_colors:
            total.append(result.count(expected_colors))

            if sum(total) >= len(expected):
                realizacion = 1
                realizaciones += realizacion
            else:
                realizacion = 0
                realizaciones += realizacion
                

    

    return f'resultado {result} esperado {expected}, realizaciones {realizaciones}, matriz {total}'


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red":2},
                  num_balls_drawn=5,
                  num_experiments=5)

print(probability)

resultado = ['black', 'black', 'green', 'red', 'red'] 
esperado = ['red', 'red', 'green']

print(esperado in resultado)
