import os

def part_1(data):
    known_segment_lengths = [2, 3, 4, 7]

    sum = 0
    for line in data:
        for output in line[1]:
            if len(output) in known_segment_lengths:
                sum += 1

    return sum

def part_2(data):
    sum = 0
    for line in data:
        adg = abfg = all = set('abcdefg')
        for signal in line[0]:
            if len(signal) == 2:
                cf = set(signal)
            elif len(signal) == 3:
                acf = set(signal)
            elif len(signal) == 4:
                bcdf = set(signal)
            elif len(signal) == 5:
                adg = adg.intersection(set(signal))
            elif len(signal) == 6:
                abfg = abfg.intersection(set(signal))
        
        bd = bcdf.difference(cf)
        ag = adg.intersection(abfg)
        bf = abfg.difference(ag)

        a = acf.difference(cf)
        b = bf.intersection(bd)
        f = bf.difference(b)
        g = ag.difference(a)
        c = cf.difference(f)
        d = bd.difference(b)
        e = all.difference(a, b, c, d, f, g)

        segments = {"0" : a.union(b, c, e, f, g),
                    "1" : c.union(f),
                    "2" : a.union(c, d, e, g),
                    "3" : a.union(c, d, f, g),
                    "4" : b.union(c, d, f), 
                    "5" : a.union(b, d, f, g), 
                    "6" : a.union(b, d, e, f, g), 
                    "7" : a.union(c, f),
                    "8" : a.union(b, c, d, e, f, g), 
                    "9" : a.union(b, c, d, f, g)}

        values = ""
        for output in line[1]:
            for value in segments:
                if set(output) == segments[value]:
                    values += value
                    break

        sum += int(values)
    return sum

path = os.path.dirname(os.path.realpath(__file__))
with open(path+"/input.txt") as file:
  input = [[x.split() for x in x.split('|')] for x in file.readlines()]

print(f"Part 1: {part_1(input)}")
print(f"Part 2: {part_2(input)}")
