import sys, time

GREEN = '\033[92m'
END_COLOR = '\033[0m'
UP = "\x1B[7A"
CLR = "\x1B[0K"

class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.marked = [[False for n in r] for r in numbers]

    def mark(self, drawn_number):
        for r in range(len(self.numbers)):
            for c in range(len(self.numbers[r])):
                if not self.marked[r][c]:
                    self.marked[r][c] = self.numbers[r][c] == drawn_number

    def print_marked(self):
        for r in range(len(self.numbers)):
            for c in range(len(self.numbers[r])):
                if self.marked[r][c]:
                    print(f'{GREEN}{self.numbers[r][c].rjust(2)}{END_COLOR}', end=" ")
                else:
                    print(f'{self.numbers[r][c].rjust(2)}', end=" ")
            print(CLR)

    def check_progress(self):
        # Check rows
        best_line = 0
        for row in self.marked:
            best_line = max(best_line, sum(row))

        # Check columns
        for col in range(len(self.marked[0])):
            best_line = max(best_line, sum([row[col] for row in self.marked]))

        return best_line

    def sum_unmarked(self):
        sum = 0
        for r in range(len(self.numbers)):
            for c in range(len(self.numbers[r])):
                if not self.marked[r][c]:
                    sum += int(self.numbers[r][c])
        return sum


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        entries = file.read().splitlines()

    with open(sys.argv[1], "r") as file:
        entries = file.read().splitlines()

    drawn = entries[0].split(',')
    lines = [l.split() for l in entries[2:]]

    boards = []
    numbers = []
    # Create Board objects

    while lines or numbers:
        if (len(lines) > 0) and lines[0]:
            numbers.append(lines.pop(0))
        else:
            boards.append(Board(numbers))
            numbers = []
            if len(lines) > 0:
                lines.pop(0)

    completed_boards = []
    best_progress = 0
    best_boards = []

    print(f'Analyzing {len(boards)} boards.\n\n\n\n\n\n\n')

    for drawn_id, drawn_number in enumerate(drawn):
        for id, board in enumerate(boards):
            board.mark(drawn_number)
            board_progress = board.check_progress()
            if board_progress > best_progress:
                best_boards = [id]
                best_progress = board_progress
            elif not id in best_boards and board_progress == best_progress:
                best_boards.append(id)
            if not id in completed_boards and board_progress == 5:
                if len(completed_boards) == 0:
                    print(f'{UP}BINGO! On board {id+1}{CLR}')
                    board.print_marked()
                    board_sum = board.sum_unmarked()
                    print(f'Answer 1: sum_unmarked [{board_sum}] * drawn_number [{drawn_number}] = {GREEN}{board_sum * int(drawn_number)}{END_COLOR}')

                completed_boards.append(id)

                if len(completed_boards) == len(boards):
                    print(f'Answer 2: The last board to reach BINGO! was nr {id+1} with a score of {GREEN}{board_sum * int(drawn_number)}{END_COLOR}')
                    exit()
        if not completed_boards:
            print(f'{UP}Drawn numbers: {GREEN}{" ".join(drawn[:drawn_id+1])}{END_COLOR}{CLR}')
            print(f'Best progress: Board {best_boards[0]} ({best_progress} in a line), along with {len(best_boards)} other boards.{CLR}')
            boards[best_boards[0]].print_marked()
            time.sleep(1)
