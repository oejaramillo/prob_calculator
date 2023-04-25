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
        indices = range(0, len(initial)+1)
        item = random.choice(indices)
        draw += [initial[item]]
        new = copy.copy(initial)
        new.pop(item)
        initial = new

        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  total = 0
  for x in range(num_experiments):
    draw = hat.draw(num_balls_drawn)
    if num_balls_drawn < sum(list(expected_balls.values())):
      total += 0
    else:
      draw_names = list(set(draw))
      draw_counts = []

      for x in range(len(draw_names)):
        counts = draw.count(draw_names[x])
        draw_counts.append(counts)

        draw_dic = {item: draw_counts[i] for i, item in enumerate(draw_names)}

      if all(
          draw_dic.get(item, 0) >= count
          for item, count in expected_balls.items()):
        total += 1
      else:
        total += 0

  prob = total / num_experiments
  return prob
