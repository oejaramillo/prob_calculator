from prob_calculator import Hat
import random

random.seed(95)
hat = Hat(red=5,blue=2)
actual = hat.draw(2)
print(actual)