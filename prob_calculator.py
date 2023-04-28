import copy
import random

# Consider using the modules imported above.
class Hat:

  def __init__(self, **kwargs):
    self.icontents = []
    self.contents =[]
    self.arguments = kwargs

    for key, value in self.arguments.items():
      for x in range(0, value):
        self.icontents += [key]

    self.contents = self.icontents

  def __str__(self):
    return str(self.icontents)

  def draw(self, balls):
    initial = copy.copy(self.icontents)
    if balls > len(initial):
      draw = initial
      self.contents = self.icontents
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

      self.contents = new
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


