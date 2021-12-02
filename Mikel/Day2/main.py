import os
path = os.path.dirname(os.path.realpath(__file__))

Data = []
with open(path+"/input.txt") as file:
    lines = file.readlines()
    Data = [line.rstrip() for line in lines]


horizontal = 0
depth = 0
for i in Data:
    move, count = i.split(" ")
    count = int(count)
    if move == "forward":
        horizontal += count
    elif move == "down":
        depth += count
    else:
        depth -= count
position = horizontal * depth
print("Part A:", position)


horizontal = 0
depth = 0
aim = 0
for i in Data:
    move, count = i.split(" ")
    count = int(count)
    if move == "forward":
        horizontal += count
        depth += aim * count
    elif move == "down":
        aim += count
    else:
        aim -= count
position = horizontal * depth
print("Part B:", position)