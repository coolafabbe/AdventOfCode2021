import time
import sys

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

template = list(entries[0])
pairs = {p: i for p, i in [e.split(' -> ') for e in entries if '->' in e]}

for step in range(10):
    for i in range(1, len(template)*2-1, 2):
        template.insert(i, pairs[''.join([template[i-1],template[i]])])

occurances = sorted([template.count(c) for c in set(template)])

print(f'Answer 1: {occurances[-1] - occurances[0]}')

