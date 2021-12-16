import time
import sys

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

template = [entries[0][i]+entries[0][i+1] for i in range(len(entries[0])-1)]
rules = {p: i for p, i in [e.split(' -> ') for e in entries if '->' in e]}
pairs = {p:template.count(p) for p in rules}

def count_elements(pairs, rules, n):

    elements = {v:entries[0].count(v) for v in rules.values()}

    for step in range(n):
        new_pairs = {p:0 for p in rules}
        for p, n in pairs.items():
            new_pairs[p[0]+rules[p]] += n
            new_pairs[rules[p]+p[1]] += n
            elements[rules[p]] += n
        pairs = new_pairs

    return elements

elements = count_elements(pairs, rules, 10)
print(f'Answer 1 (10 steps): \033[92m{max(elements.values())-min(elements.values())}\033[0m')
elements = count_elements(pairs, rules, 40)
print(f'Answer 2 (40 steps): \033[92m{max(elements.values())-min(elements.values())}\033[0m')

