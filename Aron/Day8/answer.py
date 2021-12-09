import sys

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

signals, outputs = zip(*(e.split('|') for e in entries))

signal_entries = [s.split() for s in signals]
output_entries = [o.split() for o in outputs]

o_len = [len(d) for o in output_entries for d in o]
expected_occ = [8, 6, 8, 7, 4, 9, 7]

print('Answer 1:',  o_len.count(2) + o_len.count(4) + o_len.count(3) + o_len.count(7))

num_2_s = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

unique_n = [0, 2, 0, 0, 4, 0, 0, 3, 7, 0]

out_n = 0
for s_list, o_list in zip(signal_entries, output_entries):
    remapped_n = ['' for i in range(10)]
    for s in s_list:
        if len(s) in unique_n:
            remapped_n[unique_n.index(len(s))] = s
    for c in remapped_n[7]:
        if not c in remapped_n[1]:
            for n in [0, 2, 3, 5, 6, 9]:
                remapped_n[n] += c
    for c in remapped_n[4]:
        if not c in remapped_n[1]:
            for n in [5, 6, 9]:
                remapped_n[n] += c
    remapped_n[0] += remapped_n[1]
    remapped_n[3] += remapped_n[1]
    remapped_n[9] += remapped_n[1]
    occ = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
    for s in s_list:
        for c in s:
            occ[c]+=1
    for c, o in occ.items():
        if o == 6:
            for n in [0]:
                remapped_n[n] += c
        if o == 8 and c in remapped_n[1]:
            remapped_n[2] += c
        if o == 4:
            for n in [0, 2, 6]:
                remapped_n[n] += c
        if o == 7 and c in remapped_n[4]:
            for n in [2, 3]:
                remapped_n[n] += c
        if o == 7 and c not in remapped_n[4]:
            for n in [0, 2, 3, 5, 6, 9]:
                remapped_n[n] += c
        if o == 9:
            for n in [5, 6]:
                remapped_n[n] += c


    four_d_n = ''
    for o in o_list:
        for n in range(10):
            print(sorted(o), sorted(remapped_n[n]))
            if sorted(o) == sorted(remapped_n[n]):
                four_d_n += str(n)
    out_n += int(four_d_n)
    print(four_d_n)

print('Answer 2:', out_n)

