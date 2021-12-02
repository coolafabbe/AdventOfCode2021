import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

start_time = time.perf_counter()
print(f'Analyzing {len(entries)} entries')

entries = [entries[i].split() for i in range(0, len(entries))]

depth = horizontal = aim = 0

for i in range(0, len(entries)):
    if entries[i][0]=="forward":
        horizontal += int(entries[i][1])
        depth += aim * int(entries[i][1])
    elif entries[i][0]=="up":
        aim -= int(entries[i][1])
    elif entries[i][0]=="down":
        aim += int(entries[i][1])

print(f'Depth: {GREEN}{depth}{END_COLOR}| Horizontal: {GREEN}{horizontal}{END_COLOR}')
print(f'Answer: {GREEN}{depth*horizontal}{END_COLOR}')
print(f'Completed in {time.perf_counter()-start_time} s')

