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


        
    







    return f'esperado {expected_balls} in {draw_dic} resultados {total} experados {expected_balls_values} realizaciones, prueba {realizaciones} valor de verdad {experimento}'


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red":2, "black": 1},
                  num_balls_drawn=1,
                  num_experiments=5)

print(probability)
