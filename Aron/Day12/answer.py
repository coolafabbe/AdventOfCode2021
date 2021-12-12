import sys, time

def find_paths(twice_allowed=False):
    def continue_paths(paths):
        new_paths = []
        for p in paths:
            if p[-1] == 'end':
                new_paths.append(p)
            else:
                for c in caves[p[-1]]:
                    if c.lower() not in p or twice_allowed and c != 'start':
                        visited_twice = False
                        if twice_allowed and c.islower() and c != 'end':
                            for c1 in set(p):
                                if p.count(c1.lower()) == 2 and c in p:
                                    visited_twice = True
                        if not visited_twice:
                            new_paths.append(p + [c])
        return new_paths

    paths = [['start']]
    paths_found = False
    while not paths_found:
        paths_found = True
        paths = continue_paths(paths)
        for p in paths:
            if p[-1] != 'end':
                paths_found = False

    return paths



with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

caves = {}
for e in entries:
    a, b = e.split('-')
    if a not in caves:
        caves[a] = []
    if b not in caves:
        caves[b] = []

    caves[a].append(b)
    caves[b].append(a)

print('Visit small caves once:', len(find_paths()))
print('Allow visiting small caves twice:', len(find_paths(True)))

