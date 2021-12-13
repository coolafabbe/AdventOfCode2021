import sys

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

entries = [[int(n) for n in e] for e in entries]

def is_low(x, y, entries):
    low = True
    n = entries[y][x]
    if x > 0 and entries[y][x-1] <= n:
        low = False
    elif x < len(entries[y])-1 and entries[y][x+1] <= n:
        low = False
    elif y > 0 and entries[y-1][x] <= n:
        low = False
    elif y < len(entries)-1 and entries[y+1][x] <= n:
        low = False
    return low

def get_basin(x, y, entries, basin_size=0, already_counted=[]):
    n = entries[y][x]
    global basins
    basins.append(1)
    tmp_basin = 0
    if x > 0 and entries[y][x-1] < 9 and [x-1, y] not in already_counted:
        already_counted.append([x-1, y])
        tmp_basin += get_basin(x-1, y, entries, basin_size+1, already_counted)
    if x < len(entries[y])-1 and entries[y][x+1] < 9 and [x+1, y] not in already_counted:
        already_counted.append([x+1, y])
        tmp_basin += get_basin(x+1, y, entries, basin_size+1, already_counted)
    if y > 0 and entries[y-1][x] < 9 and [x, y-1] not in already_counted:
        already_counted.append([x, y-1])
        tmp_basin += get_basin(x, y-1, entries, basin_size+1, already_counted)
    if y < len(entries)-1 and entries[y+1][x] < 9 and [x, y+1] not in already_counted:
        already_counted.append([x, y+1])
        tmp_basin += get_basin(x, y+1, entries, basin_size+1, already_counted)
    return len(already_counted)
risk_points = []
for y in range(len(entries)):
    for x in range(len(entries[0])):
        if is_low(x, y, entries):
            risk_points.append([x, y])

risk_level = 0
basins = []
basin_sizes = []
for x, y in risk_points:
    risk_level += entries[y][x] + 1
    get_basin(x, y, entries, 0, [])
    basin_sizes.append(len(basins)-1)
    basins = []

print(sorted(basin_sizes))

basin_3_product = 1
for t in sorted(basin_sizes)[-3:]:
    print(t)
    basin_3_product = basin_3_product * t

print('Answer 1:', risk_level)
print('Answer 2:', basin_3_product)

