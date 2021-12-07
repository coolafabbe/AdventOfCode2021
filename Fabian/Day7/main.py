import os

def align_crabs(data, constant_rate:bool = True):
    max_value = max(data)
    values = []
    for i in range(max_value +1):
        sum = 0
        for crab_position in data:
            if constant_rate:
                sum += abs(i-crab_position)
            else:
                sum += (abs(crab_position - i) * (abs(crab_position - i)+1)) / 2
        values.append(sum)
    return int(min(values))

path = os.path.dirname(os.path.realpath(__file__))
with open(path+"/input.txt") as file:
  input = [int(x) for x in file.read().split(',')]

test_input = [16,1,2,0,4,2,7,1,2,14]

assert align_crabs(test_input, True) == 37, "Function is wrong"
print("Part A:", align_crabs(input))
assert align_crabs(test_input, False) == 168, "Function is wrong"
print("Part B:", align_crabs(input, False))