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
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print(hat)

hat1 = Hat(yellow=3, blue=2, green=6)


print(hat1)
