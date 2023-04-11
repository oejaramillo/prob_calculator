import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if kwargs == None:
            self = 1
        else:
            self.contents = kwargs
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print(hat)

hat1 = Hat()
print(hat1)
