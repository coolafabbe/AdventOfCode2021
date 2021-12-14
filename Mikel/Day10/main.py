import os
from collections import deque
path = os.path.dirname(os.path.realpath(__file__))

CHARS_PAIRS = {'(':')', '[':']', '{':'}', '<':'>'}
POINTS_CORRUPTED = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
POINTS_CORRECT = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def navigation_subsystem(lines:list, detect_corrupted:bool=True):
    points = 0
    line_points = []
    for line in lines:
        line_chars = deque(line)
        open_chars = []
        ilegal = ''
        while line_chars:
            c = line_chars.popleft()
            if c in CHARS_PAIRS:
                open_chars.append(c)
            else:
                o = open_chars.pop()
                if CHARS_PAIRS[o] != c:
                    ilegal = c
                    break        

        if detect_corrupted:
            if ilegal in POINTS_CORRUPTED:
                points += POINTS_CORRUPTED[ilegal]
        elif ilegal == '':
            p = 0
            while open_chars:
                o = open_chars.pop()
                p = p*5 + POINTS_CORRECT[CHARS_PAIRS[o]]
            line_points.append(p)
    if line_points:
        line_points = sorted(line_points)
        points = line_points[int((len(line_points)-1)/2)]

    return points
    

test_lines = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]

lines = []
with open(path+"/input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

assert navigation_subsystem(test_lines) == 26397, "Function is wrong"
print("Part A:", navigation_subsystem(lines))
assert navigation_subsystem(test_lines, False) == 288957, "Function is wrong"
print("Part B:", navigation_subsystem(lines, False))

