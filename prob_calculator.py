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

    total = 0
    for x in range(num_experiments):
        draw = hat.draw(num_balls_drawn)
        # Comprobamos si num_balls_draw está contenido en expected
        if num_balls_drawn < sum(list(expected_balls.values())):
            total += 0
        else:
            draw_names = list(set(draw)) 
            draw_counts = []
            for x in range(len(draw_names)):
                counts = draw.count(draw_names[x])
                draw_counts.append(counts)

            draw_dic = {item: draw_counts[i] for i, item in enumerate(draw_names)}
            
            # Comprobamos si expected_balls está en draw_dic
            if all(draw_dic.get(item, 0) >= count for item, count in expected_balls.items()):
                total += 1
            else:
                total += 0

    prob = total/num_experiments     
    return prob


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red":2, "black": 1},
                  num_balls_drawn=4,
                  num_experiments=2000)

print(probability)
