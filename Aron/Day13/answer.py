import sys
with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()
marked = [[int(x), int(y)] for x, y in [e.split(',') for e in entries if ',' in e]]
folds = [[d, int(n)] for d, n in [e.split()[2].split('=') for e in entries if 'fold' in e]]
for d, n in folds:
    for c in marked:
        c[0], c[1] = 2*int(n) - c[0] if c[0] > n and d == 'x' else c[0], 2*n - c[1] if c[1] > n and d == 'y' else c[1]
    marked = [list(x) for x in set(tuple(x) for x in marked)]
    print(len(marked))
max_x, max_y = max([c[0] for c in marked]), max([c[1] for c in marked])
paper = [['.' if not [x, y] in marked else '#' for x in range(max_x+1)] for y in range(max_y+1)]
print('\n'.join([''.join(paper[y])for y in range(max_y+1)]))
