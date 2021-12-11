import sys

with open(sys.argv[1], "r") as file:
    entries = file.read().splitlines()

open_chars  = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']

char_map = {o:c for o, c in zip(open_chars, close_chars)}
points = {')': 3, ']':57, '}':1197, '>': 25137}

syntax_score = 0
acp_scores = []

for line in entries:
    levels = []
    for c in line:
        if c in open_chars:
            levels.append(c)
        elif c == char_map[levels[-1]]:
            levels.pop()
        else:
            syntax_score += points[c]
            break
    else:
        score = 0
        for l in reversed(levels):
            score = score * 5 + 1 + open_chars.index(l)

        acp_scores.append(score)

acp_score = sorted(acp_scores)[len(acp_scores)//2]

print('Answer 1:', syntax_score)
print('Answer 2:', acp_score)


