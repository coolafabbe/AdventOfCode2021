import os.path

OPEN =  ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']
SCORE_SYNTAX = {")": 3,
                "]": 57,
                "}": 1197,
                ">": 25137}
SCORE_AUTO_COMPLETE = {"(" : 1,
                       "[" : 2,
                       "{" : 3, 
                       "<" : 4}

def syntax_score(data):
    illegal_chars = []
    incomplete_scores = []
    for line in data:
        opening_chars = []
        for char in line:
            if char in OPEN: 
                opening_chars.append(char)
            elif char in CLOSE:
                if char == CLOSE[OPEN.index(opening_chars[-1])]:
                    opening_chars.pop(-1)
                else:
                    illegal_chars.append(char)
                    break
        else: # No break called.
            if len(opening_chars) > 0:
                sum = 0
                for char in reversed(opening_chars):
                    sum = sum * 5 + SCORE_AUTO_COMPLETE[char]
                incomplete_scores.append(sum)
    
    syntax_error_score = 0
    for char in illegal_chars:
        syntax_error_score += SCORE_SYNTAX[char]

    acp_score = sorted(incomplete_scores)[len(incomplete_scores)//2]
    
    return (syntax_error_score, acp_score)


path = os.path.dirname(os.path.realpath(__file__))
with open(path+"/input.txt") as file:
  input = [x.strip() for x in file.readlines()]
with open(path+"/input_example.txt") as file:
  input_example = [x.strip() for x in file.readlines()]

assert syntax_score(input_example) == (26397, 288957), "Function is wrong"
answer = syntax_score(input)
print(f"Part 1: {answer[0]}")
print(f"Part 2: {answer[1]}")