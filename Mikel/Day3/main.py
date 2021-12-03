import os
import numpy as np
path = os.path.dirname(os.path.realpath(__file__))

def consumption(lines:list):
    data = [[int(i) for i in list(line.strip())] for line in lines]
    arr = np.array(data, dtype='int32')
    l = len(arr)
    w = len(arr[0])

    gamma_rate = []
    epsilon_rate = []
    for i in range(w):
        t = 1 if sum(arr[:,i]) >=l/2 else 0
        gamma_rate.append(t)
        epsilon_rate.append(1-t)

    gamma_val = int(''.join(map(lambda x: str(int(x)), gamma_rate)), 2)
    epsilon_val = int(''.join(map(lambda x: str(int(x)), epsilon_rate)), 2)

    return gamma_val * epsilon_val

def life_support_ratig(lines:list):

    def count(l,i,c):
        res = 0
        for k in range(len(l)): 
            if l[k][i] == c:
                res += 1 
        return res

    def clean(l,i,c):
        k = 0
        while k < len(l): 
            if l[k][i] != c:
                l.pop(k)
                continue
            k += 1 
        return l

    oxygen = lines.copy()
    co2 = lines.copy()

    i = 0
    while len(oxygen)>1 or len(co2)>1:
        if len(oxygen)>1:
            c = count(oxygen,i,'1') 
            t = '1' if c >= len(oxygen)/2 else '0'
            oxygen = clean(oxygen,i,t)

        if len(co2)>1:
            c = count(co2,i,'1')
            t = '0' if c >= len(co2)/2 else '1'
            co2 = clean(co2,i,t) 

        i += 1

    return int(oxygen[0], 2) * int(co2[0], 2)


test_lines = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

lines = []
with open(path+"/input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

assert consumption(test_lines) == 198, "Function is wrong"

print("Part A:", consumption(lines))

assert life_support_ratig(test_lines) == 230, "Function is wrong"

print("Part B:", life_support_ratig(lines))


"""

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
"""

"""
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
"""