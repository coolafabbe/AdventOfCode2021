import matplotlib.pyplot as plt
import numpy as np
import os
import re

path = os.path.dirname(os.path.realpath(__file__))

dim_max = 0
with open(path+"/input.txt") as file:
  input = file.readlines()
  
lines = []
for line in input:
  line = re.split("-> |,", line)

  x = [int(line[0]), int(line[2])]
  y = [int(line[1]), int(line[3])]

  lines.append([x, y])

  # find largest number, to set map dimension.
  line_max = max(x) if max(x) > max(y) else max(y)
  if line_max > dim_max -1:
    dim_max = line_max +1

map = np.zeros((dim_max, dim_max), dtype=np.int64)

# Plot the lines on map
for [x, y] in lines:
  dx, dy = x[1]-x[0], y[1] - y[0]
  dir_x = dir_y = 0
  if dx != 0:
    dir_x = dx / abs(dx)
  if dy != 0:
    dir_y = dy/ abs(dy)
  
  for i in range(0, max(abs(dx), abs(dy)) + 1):
    map[y[0] + int(i*dir_y)][x[0] + int(i*dir_x)] += 1

count_arr = np.count_nonzero(map >= 2)
print(f"Part 1: Amount of crossing of at least two lines {count_arr}")

plt.imshow(map >= 1)
plt.show()