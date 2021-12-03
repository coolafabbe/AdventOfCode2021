with open("input example.txt", mode="r") as file:
    input = file.readlines()

input = [list(x.strip()) for x in input]

def count(data, least):
    list = []
    for j in range(len(data[0])):
        sum_zeros = sum_ones = 0
        for i in range(len(data)):
            if input[i][j] == '1':
                sum_ones += 1 
            elif input[i][j] == '0':
                sum_zeros += 1 
        
        if sum_ones >= sum_zeros and not least or sum_zeros >= sum_ones and least:
            list.append('1')
        else:
            list.append('0')
    return list


gamma_list = count(input, False)
gamma_rate = int("".join(str(x) for x in gamma_list), 2)
print(gamma_rate)

epsilon_list = count(input, True)
epsilon_rate = int("".join(str(x) for x in epsilon_list), 2)
print(epsilon_rate)

print(gamma_rate * epsilon_rate)

############### Ex2


print(gamma_list)
oxygen_list = []
for count, value in enumerate(gamma_list):

    for index in input:
        print(index[count])
        print(value)
        print("\n")
        if index[count] != value:
            input.pop(index)

print(oxygen_list)

