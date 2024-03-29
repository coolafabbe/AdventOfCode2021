with open("input.txt", mode="r") as file:
  input = file.read().strip().split("\n")
#print(input)

def find_gamma_epsilon(data, ones=True):
  count_one = count_zero = 0
  for value in data:
    if value == "1":
      count_one += 1
    else:
      count_zero += 1
  

  if (count_one >= count_zero and ones) or (count_zero <= count_one and not ones): 
    return ("1", "0")
  else:
    return ("0", "1")

#Part 1
gamma = epsilon = ""

for i in range(len(input[0])):
  column = [x[i] for x in input]
  values = find_gamma_epsilon(column)
  gamma += values[0]
  epsilon += values[1]

#print(int(gamma,2))
#print(int(epsilon,2))
power_consumption = int(gamma,2) * int(epsilon,2)
print(f"Part 1: {power_consumption}")



# Part 2
# print(input)
oxygen_co2 = []
for i in range(2):
  data = input.copy()
  for bit_index in range(len(data[0])):
    column = [x[bit_index] for x in data]
    if i == 0:
      value_to_keep = find_gamma_epsilon(column)[0]
    else:
      value_to_keep = find_gamma_epsilon(column, ones = False)[1]

    values_to_remove = []
    for value in data:

      if value[bit_index] != value_to_keep:
        values_to_remove.append(value)
    
    for value in values_to_remove:
      data.remove(value)

    if len(data) == 1:
      break

  oxygen_co2.append(data[0])

#print("Part 2 oxygen: " + oxygen_co2[0] + ", " + str(int(oxygen_co2[0],2)))
#print("Part 2 co2: " + oxygen_co2[1] + ", " + str(int(oxygen_co2[1],2)))
oxygen_generator_rating = int(oxygen_co2[0], 2) * int(oxygen_co2[1], 2)
print(f"Part 2: {oxygen_generator_rating}")


















quit()
# with open("input example.txt", mode="r") as file:
#     input = file.readlines()
# input = [list(x.strip()) for x in input]


# def count_bit(j, data, least):
#   sum_zeros = sum_ones = 0
#   for i in range(len(data)):
#       if input[i][j] == '1':
#           sum_ones += 1
#       elif input[i][j] == '0':
#           sum_zeros += 1

#   if sum_ones >= sum_zeros and not least or sum_zeros >= sum_ones and least:
#       return('1')
#   else:
#       return('0')

# def count_list(data, least):
#     list = []
#     for j in range(len(data[0])):
#         list.append(count_bit(j, data, least))
#     return list


# gamma_list = count_list(input, False)
# gamma_rate = int("".join(str(x) for x in gamma_list), 2)
# print(gamma_rate)

# epsilon_list = count_list(input, True)
# epsilon_rate = int("".join(str(x) for x in epsilon_list), 2)
# print(epsilon_rate)

# print(gamma_rate * epsilon_rate)

# quit()
# # Ex2


# print(gamma_list)
# print(input)

# updated_list = input
# token = gamma_list
# for j in range(len(gamma_list)):
#     new_list = []

#     for i in range(len(updated_list)):
#         print(f"i = {i}, j = {j}")
#         print(token)
#         if updated_list[i][j] == token[j]:
#             new_list.append(input[i])

#     updated_list = new_list
#     token[j+1] = count_bit(j + 1, updated_list, False)

#     print("\n")
#     print(updated_list)
#     print("\n")
#     print(token)

# quit()

# oxygen_list = []

# gamma_list[0]


# for count_list, value in enumerate(gamma_list):

#     for index in input:
#         print(index[count_list])
#         print(value)
#         print("\n")
#         if index[count_list] != value:
#             input.pop(index)

# print(oxygen_list)
