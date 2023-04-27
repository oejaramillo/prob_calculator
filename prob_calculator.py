import copy
import random

# Consider using the modules imported above.
class Hat:
  contents = []

  def __init__(self, **kwargs):
    self.contents = []
    self.arguments = kwargs

    for key, value in self.arguments.items():
      for x in range(0, value):
        self.contents += [key]

  def __str__(self):
    return str(self.contents)

  def draw(self, balls):
    initial = copy.copy(self.contents)
    if balls > len(initial):
      draw = initial
      return draw
    
    else:
      draw = []
      for x in range(balls):
        indices = range(len(initial))
        item = random.choice(indices)
        draw += [initial[item]]
        new = copy.copy(initial)
        new.pop(item)
        initial = new
        
      return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  total = 0
  for x in range(num_experiments):
    dr = hat.draw(num_balls_drawn)
    dr_names = list(set(dr))
    dr_counts = []

    for y in range(len(dr_names)):
      counts = dr.count(dr_names[y])
      dr_counts += [counts]

      dr_dic = {key: value for key, value in zip(dr_names, dr_counts)}

    if all(dr_dic.get(key, 0) >= value for key, value in expected_balls.items()):
      total += 1
    else:
      total += 0
  
  prob = total/num_experiments
  return prob 

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
actual = probability
expected = 0.272


hat2 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability2 = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
actual2 = probability2
expected2 = 1.0

print(probability2)

