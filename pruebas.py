from prob_calculator import Hat
import random
import copy

coo1 = [1,2,3,4,5,6,7,8,9,10]
coo2= copy.deepcopy(coo1)
coo2 += [2]

print(coo1, coo2)