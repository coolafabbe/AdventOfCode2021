import os
path = os.path.dirname(os.path.realpath(__file__))
os.system('cls')

def calculate_score(board:list, score_board:list, number:int):
  sum = 0
  print(board)
  print(score_board)
  for r in range(5):
    for c in range(5):
      if not score_board[r][c]:
        sum += board[r][c]

  return sum * number

excercise1 = False
with open(path+"/input.txt") as file:
  input = file.readlines()

  drawn_numbers = [int(x)for x in input.pop(0).strip().split(',')]

  boards = []
  while len(input) >= 5:
    
    input.pop(0)
    board = []
    for i in range(5):
      board.append([int(x) for x in input.pop(0).strip().split()])

    boards.append(board)

score_board = [[[False for x in range(5)] for x in range(5)] for x in range(len(boards))]
completed_boards = []
for number in drawn_numbers:
  for b, board in enumerate(boards):
    if not completed_boards.__contains__(b):
      for r, row in enumerate(board):
        for c, col in enumerate(row):
          if number == col:
            score_board[b][r][c] = True

  for b, board in enumerate(score_board):
    if not completed_boards.__contains__(b):
      # Check rows for complete
      for r, row in enumerate(board):
        if not row.__contains__(False):
          if excercise1:
            print(f"whole row found, number = {number}, board number {b}")
            print(calculate_score(boards[b], board, number))
            quit()
          else:
            completed_boards.append(b)
            if len(completed_boards) == len(boards):
              print(f"last winner is board {b}")
              print(calculate_score(boards[b], board, number))
              quit()

    if not completed_boards.__contains__(b):
      # check column for complete
      for c in range(5):
        column = [x[c] for x in board]
        if not column.__contains__(False):
          if excercise1: 
            print(f"whole column found, number = {number}, board number {b}")
            print(calculate_score(boards[b], board, number))
            quit()
          else:
            completed_boards.append(b)
            if len(completed_boards) == len(boards):
              print(f"last winner is board {b}")
              print(calculate_score(boards[b], board, number))
              quit()

