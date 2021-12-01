import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()
    entries = [int(i) for i in entries]

print(f'Analyzing {len(entries)} entries from file: {sys.argv[1]}')

num_increased = 0

for id, entry in enumerate(entries):
    if id == 0:
        pass
    if entry > entries[id-1]:
        num_increased += 1
print(f'Number of increased measurements (out of {len(entries)}): {GREEN}{num_increased}{END_COLOR}')

print(f'Completed in {time.perf_counter()-start_time} s')

