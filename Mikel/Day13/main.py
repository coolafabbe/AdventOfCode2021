import os
import numpy as np
path = os.path.dirname(os.path.realpath(__file__))


def proccess_manual(lines:list, folds:list):

    def get_size(lines):
        max_x = 0
        max_y = 0
        for [x,y] in lines:
            max_x = max(max_x,x)
            max_y = max(max_y,y)
        return [max_y+1, max_x+1]
    
    def process_lines(lines, arr):
        for [x,y] in lines:
            arr[y,x] = 1
    
    def fold(arr, x=None, y=None):
        l = len(arr)
        w = len(arr[0])
        if x is not None:
            for i_x in range(w-x-1):
                for i_y in range(l):
                    arr[i_y, x-i_x-1] |= arr[i_y, x+i_x+1]
                    arr[i_y, x+i_x+1] = 0
            return arr[:,:x]
        if y is not None:
            for i_y in range(l-y-1):
                for i_x in range(w):
                    arr[y-i_y-1, i_x] |= arr[y+i_y+1, i_x]
                    arr[y+i_y+1, i_x] = 0
            return arr[:y,:]

    size = get_size(lines)
    arr = np.zeros(size, dtype='int32')

    process_lines(lines, arr)
    for [c, n] in folds:
        if c=='x':
            arr = fold(arr, x=n)
        else:
            arr = fold(arr, y=n)
    
    l = len(arr)
    w = len(arr[0])
    print(l,w)
    code = np.zeros([l,w],str)
    for x in range(l):
        for y in range(w):
            code[x,y] = '#' if arr[x,y]==1 else '.'
    print(np.transpose(code))
    count = sum(sum(arr))
    return count
            

test_lines = [
    [6,10],
    [0,14],
    [9,10],
    [0,3],
    [10,4],
    [4,11],
    [6,0],
    [6,12],
    [4,1],
    [0,13],
    [10,12],
    [3,4],
    [3,0],
    [8,4],
    [1,10],
    [2,14],
    [8,10],
    [9,0],
]

lines = []
with open(path+"/input.txt") as file:
    data = file.readlines()
    for line in data:
        [x,y] = line.strip().split(',')
        lines.append([int(x),int(y)]) 


folds = [
    ['x',655],
    ['y',447],
    ['x',327],
    ['y',223],
    ['x',163],
    ['y',111],
    ['x',81],
    ['y',55],
    ['x',40],
    ['y',27],
    ['y',13],
    ['y',6],
]

assert proccess_manual(test_lines, folds=[['y',7]]) == 17, "Function is wrong"
print("Part A:", proccess_manual(lines, folds=[['x',655]]))
assert proccess_manual(test_lines, folds=[['y',7], ['x',5]]), "Function is wrong"
print("Part B:", proccess_manual(lines, folds=folds))
