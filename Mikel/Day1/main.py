import os
path = os.path.dirname(os.path.realpath(__file__))

Data = []
with open(path+"/input.txt") as file:
    lines = file.readlines()
    Data = [int(line.rstrip()) for line in lines]


prev = Data[0]
counter = 0
for i in Data[1:]:
    if i > prev:
        counter += 1
    prev = i
print("Part A:", counter)

counter = 0
for i in range(len(Data)-3):
    prev = Data[i]+Data[i+1]+Data[i+2]
    next = Data[i+1]+Data[i+2]+Data[i+3]
    if next > prev:
        counter += 1
print("Part B:", counter)