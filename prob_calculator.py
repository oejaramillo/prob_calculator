import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if not kwargs or sum(kwargs.values()) < 1:
            contents = ["color"]
        else:
            self.contents = kwargs
            

    def __str__(self):
        return f'{self.contents}'
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print(hat)

hat1 = Hat(blue=1, red=50)
hat2 = Hat(blue=0)
print(hat2)
