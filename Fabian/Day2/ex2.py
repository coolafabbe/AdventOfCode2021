with open("input.txt", mode="r") as file:
    input = file.readlines()

commands = [x.split() for x in input]
commands = [[x[0], int(x[1])] for x in commands]


horizontal = depth = aim = 0

for (cmd, x) in commands:
    if cmd == "forward":
        horizontal += x
        depth += aim * x
    elif cmd == "down":
        aim += x
    elif cmd == "up":
        aim -= x

print(horizontal * depth)

