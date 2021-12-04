import time
import sys

GREEN = '\033[92m'
END_COLOR = '\033[0m'

def find_reading(entries, i, most_common=True):
    filtered_entries = []
    bit_counter = 0

    for entry in entries:
        if entry[i] == "1":
            bit_counter += 1

    most_common_bit = "1" if bit_counter >= len(entries)/2 else "0"

    for entry in entries:
        if most_common and entry[i] == most_common_bit:
            filtered_entries.append(entry)
        elif not most_common and entry[i] != most_common_bit:
            filtered_entries.append(entry)

    if len(filtered_entries) > 1:
        return find_reading(filtered_entries, i+1, most_common)
    else:
        return int(filtered_entries[0], base=2)

start_time = time.perf_counter()

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()
    # entries_numeric = [int(i, base=2) for i in entries]

print(f'Analyzing {len(entries)} entries')

oxygen_rating = find_reading(entries, 0)
co2_rating = find_reading(entries, 0, False)

print(f'Oxygen generator rating: {oxygen_rating}')
print(f'CO2 scrubber rating: {co2_rating}')
print(f'Answer (Oxygen [{oxygen_rating}] * CO2 [{co2_rating}]): {GREEN}{oxygen_rating * co2_rating}{END_COLOR}')

print(f'Completed in {time.perf_counter()-start_time} s')

