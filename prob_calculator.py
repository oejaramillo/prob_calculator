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
        draw = []
        initial = copy.copy(self.contents)
        for x in range(0, balls):
            dropped = random.choice(self.contents)
            new = [y for y in initial if y != dropped]
            initial = new

            draw.append(dropped)
            
        
            
            

        return f'{initial} and {draw}'

    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print(hat)

hat1 = Hat(yellow=3, blue=2, green=6)



print(hat1.draw(2))
