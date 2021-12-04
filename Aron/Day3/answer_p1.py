import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()
    # entries_numeric = [int(i, base=2) for i in entries]

print(f'Analyzing {len(entries)} entries')

bit_counter = [0 for i in range(0, len(entries[0]))]
entry_length = len(bit_counter)

for entry in entries:
    for bit in range(0, len(bit_counter)):
        if entry[bit] == "1":
            bit_counter[bit] += 1

most_common_bit = [(num_bits>len(entries)/2) for num_bits in bit_counter]
gamma_rate = 0
epsilon_rate = 0
for i in range(0, entry_length):
    gamma_rate += 2**(entry_length-i-1) if most_common_bit[i] else 0
    epsilon_rate += 2**(entry_length-i-1) if not most_common_bit[i] else 0

print(f'Answer (gamma_rate[{gamma_rate}] * epsilon_rate[{epsilon_rate}]): {GREEN}: {gamma_rate * epsilon_rate}{END_COLOR}')

print(f'Completed in {time.perf_counter()-start_time} s')

