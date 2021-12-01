# input = [199, 200, 208,210, 200, 207, 240, 269, 260, 263]

with open("day1\ex1\input.txt", mode="r") as file:
    input = [int(x) for x in file.readlines()]

def count_increases(array):
    num_inc = 0
    for i in range(len(array)):
        try:
           if array[i] > array[i-1]:
                num_inc += 1
        except IndexError:
            pass
    return num_inc


three_meas = []
for i in range(len(input) - 2):
    sum = 0
    for j in range(3):
        sum += int(input[i + j])
    three_meas.append(sum)

print(count_increases(three_meas))

