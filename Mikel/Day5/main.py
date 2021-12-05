import os
import numpy as np
path = os.path.dirname(os.path.realpath(__file__))

def hydrothermal_venture(size:int=10, lines:list=[], diagonals:bool=False):

    def mark(diagram, x, y):
        diagram[x,y] = diagram[x,y] + 1
        

    diagram = np.zeros((size,size), dtype='int32')

    for ([x1,y1],[x2,y2]) in lines:
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                mark(diagram, x1, y)
        elif y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                mark(diagram, x, y1)
        elif diagonals:
            if x1 < x2 and y1 < y2:
                for i, x in enumerate(range(x1,x2+1)):
                    mark(diagram, x, y1+i)
            elif x1 > x2 and y1 > y2:
                for i, x in enumerate(range(x2,x1+1)):
                    mark(diagram, x, y2+i)
            elif x1 < x2 and y1 > y2:
                for i, x in enumerate(range(x1,x2+1)):
                    mark(diagram, x, y1-i)
            elif x1 > x2 and y1 < y2:
                for i, x in enumerate(range(x2,x1+1)):
                    mark(diagram, x, y2-i)
           
    return np.count_nonzero(diagram > 1)

test_size = 10
test_lines = [
    ([0,9],[5,9]),
    ([8,0],[0,8]),
    ([9,4],[3,4]),
    ([2,2],[2,1]),
    ([7,0],[7,4]),
    ([6,4],[2,0]),
    ([0,9],[2,9]),
    ([3,4],[1,4]),
    ([0,0],[8,8]),
    ([5,5],[8,2]),
]

lines = []
with open(path+"/input.txt") as file:
    s_lines = file.readlines()
    s_lines = [s_lines.strip() for s_lines in s_lines]
    lines = []
    size = 1000
    while s_lines:
        [p1, p2] = s_lines.pop().split(" -> ")
        [x1,y1] = p1.split(',')
        [x2,y2] = p2.split(',')
        lines.append(([int(x1),int(y1)],[int(x2),int(y2)]))

assert hydrothermal_venture(test_size, test_lines) == 5, "Function is wrong"

print("Part A:", hydrothermal_venture(size, lines))

assert hydrothermal_venture(test_size, test_lines, True) == 12, "Function is wrong"

print("Part B:", hydrothermal_venture(size, lines, True))

