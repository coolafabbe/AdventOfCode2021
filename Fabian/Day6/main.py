import matplotlib.pyplot as plt
import numpy as np
import os
import re

path = os.path.dirname(os.path.realpath(__file__))

def lantern_fish(max_days, input):
  data = [0] * 9
  for fish in input:
    data[fish] += 1


  for day in range(max_days +1):
    if day > 0:
      data = next_day
    next_day = [0] * 9

    for i in range(len(data)):
      if i > 0:
        next_day[i-1] += data[i]
      else:
        next_day[8] += data[i]
        next_day[6] += data[i]

  sum = 0
  for d in data:
    sum += d
  return(sum)
        

with open(path+"/input.txt") as file:
  input = [int(x) for x in file.read().split(',')]

test_input = [3,4,3,1,2]

assert lantern_fish(80, test_input) == 5934, "Function is wrong"
print("Part A:", lantern_fish(80, input))
assert lantern_fish(256, test_input) == 26984457539, "Function is wrong"
print("Part B:", lantern_fish(256, input))