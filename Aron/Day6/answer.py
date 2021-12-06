import sys

with open(sys.argv[1], "r") as file:
    data = [int(i) for i in file.read().split(',')]

def simulate(d):
    fish = [data.count(i) for i in range(9)]
    for d in range(d):
        fish[7] += fish[0]
        fish.append(fish.pop(0))
    return sum(fish)

print('Answer 1:', simulate(80))
print('Answer 2:', simulate(256))
