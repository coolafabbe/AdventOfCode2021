with open("input example.txt", mode="r") as file:
    input = file.readlines()

commands = [x.split() for x in input]

commands_horizontal = [int(x[1]) for x in commands if x[0] == "forward"]
commands_down = [int(x[1]) for x in commands if x[0] == "down"]
commands_down += [-int(x[1]) for x in commands if x[0] == "up"]

print(sum(commands_horizontal) * sum(commands_down))