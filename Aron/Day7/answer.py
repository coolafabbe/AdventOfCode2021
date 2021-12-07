import sys, math

with open(sys.argv[1], "r") as file:
    data = [int(i) for i in file.read().split(',')]

positions = [0 for i in range(min(data), max(data))]

for p in range(len(positions)):
    fuel_spent = 0
    for crab in data:
        fuel_spent += abs(crab - p)
    positions[p] = fuel_spent

print('Answer 1:', min(positions))

for p in range(len(positions)):
    fuel_spent = 0
    for crab in data:
        fuel_spent += (abs(crab - p) * (abs(crab - p)+1)) / 2
    positions[p] = int(fuel_spent)

print('Answer 2:', min(positions))

