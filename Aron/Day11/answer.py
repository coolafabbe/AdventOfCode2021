import sys, time
import numpy as np

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

octo = [[int(l[c]) for l in entries] for c in range(len(entries[0]))]

def flash_check(x, y):
    global octo
    global flashes
    if octo[x][y] == 10:
        flashes += 1
        print_octo(octo)
        for x1, y1 in np.ndindex((3, 3)):
            x2, y2 = x-1+x1, y-1+y1
            if x2 < 0 or y2 < 0 or x2 > 9 or y2 > 9:
                continue
            octo[x2][y2] += 1
            flash_check(x2, y2)

def print_octo(octo):
    global step
    print(f'\x1B[11AStep: {step}')
    time.sleep(0.002)
    for y in range(10):
        line = ''
        for x in range(10):
            if octo[x][y] == 0:
                line += f'\033[107m\033[97m{octo[x][y]}\033[0m '
            elif octo[x][y] < 10:
                line += f'\033[90m{octo[x][y]}\033[0m '
            else:
                line += str(octo[x][y])
        print(line)

flashes = 0
step = 0
print('\n'*10)
while True:
    step += 1
    last_flashes = flashes
    for x, y in np.ndindex((10,10)):
        octo[x][y] += 1
        flash_check(x, y)
    for x, y in np.ndindex((10, 10)):
        if octo[x][y] > 9:
            octo[x][y] = 0
    print_octo(octo)
    if step == 100:
        step_100 = flashes
    if flashes - last_flashes == 100:
        print('Answer 1:', step_100)
        print('Answer 2:', step)
        break

