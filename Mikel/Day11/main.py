import os
import numpy as np


def octopuses(lines:list, step_count:int=100):

    def step(arr):
        res = []
        for i in range(len(arr)):
            for k in range(len(arr[0])):
                if arr[i,k]<9:
                    arr[i,k] = arr[i,k] + 1
                else:
                    arr[i,k] = 0
                    res.append((i,k))
        return res
    
    def bright(arr, i, k):
        if 0 != arr[i,k]:
            arr[i,k] = arr[i,k] + 1
            if arr[i,k]>9:
                arr[i,k] = 0
                return True
        return False
            

    def process(arr, i, k):
        res = []
        if i-1>=0:
            if bright(arr, i-1, k): res.append((i-1,k))
            if k-1>=0:
                if bright(arr, i-1, k-1): res.append((i-1,k-1))
            if k+1<len(arr[0]):
                if bright(arr, i-1, k+1): res.append((i-1,k+1))
        if i+1<len(arr):
            if bright(arr, i+1, k): res.append((i+1,k))
            if k+1<len(arr[0]):
                if bright(arr, i+1, k+1): res.append((i+1,k+1))
            if k-1>=0:
                if bright(arr, i+1, k-1): res.append((i+1,k-1))
        if k-1>=0:
            if bright(arr, i, k-1): res.append((i,k-1))
        if k+1<len(arr[0]):
            if bright(arr, i, k+1): res.append((i,k+1))

        return res

    data = [[int(i) for i in list(line.strip())] for line in lines]
    arr = np.array(data, dtype='int32')
    
    flashes = 0
    s = 0
    while s<step_count or step_count==-1:
        s += 1
        res = step(arr)
        flashes += len(res)
        while res:
            (i,k) = res.pop()
            news = process(arr, i, k)
            flashes += len(news)
            res += news
        
        if step_count == -1:
            if np.max(arr) == 0:
                return s

    return flashes
    



test_lines = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]

lines = [
    '6636827465',
    '6774248431',
    '4227386366',
    '7447452613',
    '6223122545',
    '2814388766',
    '6615551144',
    '4836235836',
    '5334783256',
    '4128344843',
]


assert octopuses(test_lines, 100) == 1656, "Function is wrong"
print("Part A:", octopuses(lines, 100))
assert octopuses(test_lines, -1) == 195, "Function is wrong"
print("Part B:", octopuses(lines, -1))

