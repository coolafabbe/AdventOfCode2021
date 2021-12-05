import matplotlib.pyplot as plt
import numpy as np
import os
import re

path = os.path.dirname(os.path.realpath(__file__))
#os.system('cls')

STRAIGHLINES = True

dim_max = 0
with open(path+"/input.txt") as file:
  input = file.readlines()
  
  lines = []
  for line in input:
    line = re.split("-> |,", line)

    x = [int(line[0]), int(line[2])]
    y = [int(line[1]), int(line[3])]

    line_max = max(x) if max(x) > max(y) else max(y)
    if line_max > dim_max -1:
      dim_max = line_max +1

    if (not STRAIGHLINES or x[0] == x[1] or y[0] == y[1]):
      lines.append([x, y])

map = np.zeros((dim_max, dim_max), dtype=np.int64)

for [x, y] in lines:
  x.sort()
  y.sort()

  for i in range(x[0], x[1]+1):
    for j in range(y[0], y[1]+1):
      map[j][i] += 1

count_arr = np.count_nonzero(map >= 2)
print(f"Part 1: Amount of crossing of at least two lines {count_arr}")


for x1, y1 in lines:
  if (not STRAIGHLINES or x1[0] == x1[1] or y1[0] == y1[1]):
    plt.plot(x1,y1)

plt.show()

