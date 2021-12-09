import os
import numpy as np
path = os.path.dirname(os.path.realpath(__file__))


def risk_level(lines:list):
    data = [[int(i) for i in list(line.strip())] for line in lines]
    arr = np.array(data, dtype='int32')
    l = len(arr)
    w = len(arr[0])
    risk = 0
    for i in range(l):
        for k in range(w):
            is_low = True
            if i-1>=0:
                if arr[i,k]>=arr[i-1,k]:
                    is_low = False   
            if k-1>=0:
                if arr[i,k]>=arr[i,k-1]:
                    is_low = False   
            if i+1<l:
                if arr[i,k]>=arr[i+1,k]:
                    is_low = False   
            if k+1<w:
                if arr[i,k]>=arr[i,k+1]:
                    is_low = False  
            if is_low:
                risk += arr[i,k]+1

    return risk
    

def basins(lines:list):

    def check_point_passed(i, k, points):
        for (a,b) in points:
            if a==i and b==k:
                return True
        return False

    def calc_basin(arr, i, k, val, points):
        if not check_point_passed(i, k, points):
            if i>=0 and i<len(arr) and k>=0 and k<len(arr[0]):
                if 9 > arr[i,k] > val:
                    points.append((i,k))
                    res = 1
                    res += calc_basin(arr, i+1, k, arr[i,k], points)
                    res += calc_basin(arr, i-1, k, arr[i,k], points)
                    res += calc_basin(arr, i, k+1, arr[i,k], points)
                    res += calc_basin(arr, i, k-1, arr[i,k], points)
                    return res
        return 0

    data = [[int(i) for i in list(line.strip())] for line in lines]
    arr = np.array(data, dtype='int32')
    l = len(arr)
    w = len(arr[0])

    top = [0,0,0]
    for i in range(l):
        for k in range(w):
            points = []
            c = calc_basin(arr, i, k, -1, points)
            #print(c, points)
            if c > min(top):
                top.pop(top.index(min(top)))
                top.append(c)

    return top[0]*top[1]*top[2]

test_lines = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]

lines = []
with open(path+"/input.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

assert risk_level(test_lines) == 15, "Function is wrong"
print("Part A:", risk_level(lines))
assert basins(test_lines) == 1134, "Function is wrong"
print("Part B:", basins(lines))

