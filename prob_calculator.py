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
    contents = hat.arguments

    draw = hat.draw(5)
    draw_names = list(set(draw)) 
    draw_counts = []
    for x in range(0, len(draw_names)):
        counts = draw.count(draw_names[x])
        draw_counts.append(counts)

    draw_dic = {item: draw_counts[i] for i, item in enumerate(draw_names)}

    # Comprobamos si expected_balls está en draw_dic
    total = []
    expected_balls_names = list(expected_balls.keys())

    # lista con el conteo de las bolas de expected en draw
    for x in range(0, len(expected_balls_names)):
        total.append(draw_dic.get(expected_balls_names[x]))

    expected_balls_values = list(expected_balls.values())

    # Comparamos ambas listas valor a valor
    







    return f'esperado {expected_balls} in {draw_dic} resultados {total} experados {expected_balls_values} realizaciones'


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red":2, "black": 1},
                  num_balls_drawn=5,
                  num_experiments=5)

print(probability)
