import matplotlib.pyplot as plt
import numpy as np
import os
import re

path = os.path.dirname(os.path.realpath(__file__))

def lantern_fish(max_days, data):
  for day in range(max_days):
    #print(f"Day {day}: {data}")
    new_fishes = []
    for i in range(len(data)):
      data[i] -= 1
      if data[i] < 0:
        data[i] = 6
        new_fishes.append(8)
    
    data.extend(new_fishes)

  return(len(data))
        

with open(path+"/input.txt") as file:
  input = [int(x) for x in file.read().split(',')]

test_input = [3,4,3,1,2]

assert lantern_fish(80, test_input) == 5934, "Function is wrong"
print("Part A:", lantern_fish(80, input))
assert lantern_fish(265, test_input) == 26984457539, "Function is wrong"
print("Part A:", lantern_fish(265, input))
# assert hydrothermal_venture(test_size, test_lines, True) == 12, "Function is wrong"
# print("Part B:", hydrothermal_venture(size, lines, True))


# plt.imshow(map >= 1)
# plt.show()