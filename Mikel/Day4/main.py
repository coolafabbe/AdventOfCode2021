import os
import numpy as np
path = os.path.dirname(os.path.realpath(__file__))

def bingo(numbers:list, boards:list, play2loose:bool=False):

    def play(boards, number):
        for b in range(len(boards)):
            for r in range(5):
                for c in range(5):
                    if boards[b][r][c] == number:
                        boards[b][r][c] = -1
    
    def check(boards):
        results = []
        for b in range(len(boards)):
            tot = 0
            rows = [0 for i in range(5)]
            cols = [0 for i in range(5)]

            for r in range(len(boards[b])):
                for c in range(len(boards[b][r])):
                    v = boards[b][r][c]
                    rows[r] = rows[r] + v
                    cols[c] = cols[c] + v
                    if v >= 0:
                        tot += v

            if (-5 in rows) or (-5 in cols):
                results.append([b, tot])
            else:
                results.append([b, None])
        
        return results

    leaderboard = []
    for number in numbers:
        play(boards, number)
        results = check(boards)
        for (board, total) in results:
            if total != None:
                if not play2loose:
                    return (board,total*number)
                else:
                    if len(leaderboard)<len(boards)-1:
                        if (board not in leaderboard):
                            leaderboard.append(board)
                    else:
                        if (board not in leaderboard):
                            return (board,total*number)

    return (None, None)
    
    
test_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
test_boards = [
    [
        [22,13,17,11,0],
        [8,2,23,4,24],
        [21,9,14,16,7],
        [6,10,3,18,5],
        [1,12,20,15,19],
    ],
    [
        [3,15,0,2,22],
        [9,18,13,17,5],
        [19,8,7,25,23],
        [20,11,10,24,4],
        [14,21,16,12,6],
    ],
    [
        [14,21,17,24,4],
        [10,16,15,9,19],
        [18,8,23,26,20],
        [22,11,13,6,5],
        [2,0,12,3,7],
    ]
]

numbers = []
boards = []
with open(path+"/input.txt") as file:
    lines = file.readlines()
    numbers = [int(i) for i in lines.pop(0).strip().split(",")]

    while len(lines)>=5:
        lines.pop(0)
        board = []
        for i in range(5):
            row = [int(i) for i in lines.pop(0).strip().split()]
            board.append(row)   
        boards.append(board)

assert bingo(test_numbers, test_boards) == (2, 4512), "Function is wrong"
print("Part A:", bingo(numbers, boards))

assert bingo(test_numbers, test_boards, play2loose=True) == (1, 1924), "Function is wrong"
print("Part B:", bingo(numbers, boards, play2loose=True))

