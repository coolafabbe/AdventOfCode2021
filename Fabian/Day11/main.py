input = [[1,3,2,6,2,5,3,3,1,5],
         [3,4,2,7,7,2,8,1,1,3],
         [5,7,5,1,6,1,2,5,4,2],
         [6,5,4,3,8,6,8,3,2,2],
         [4,4,2,2,5,2,6,2,2,1],
         [2,2,3,4,3,2,5,6,4,7],
         [1,7,7,3,1,7,4,8,8,7],
         [7,2,8,1,3,2,1,6,7,4],
         [6,5,6,2,5,1,3,1,1,8],
         [4,8,2,4,5,4,1,5,2,2]]

input_example = [[5,4,8,3,1,4,3,2,2,3],
                 [2,7,4,5,8,5,4,7,1,1],
                 [5,2,6,4,5,5,6,1,7,3],
                 [6,1,4,1,3,3,6,1,4,6],
                 [6,3,5,7,3,8,5,4,7,8],
                 [4,1,6,7,5,2,4,6,4,5],
                 [2,1,7,6,8,4,1,7,2,1],
                 [6,8,8,2,8,8,1,1,3,4],
                 [4,8,4,6,8,4,8,5,5,4],
                 [5,2,8,3,7,5,1,5,2,6]]

def flash_count(data, no_of_days):
    def inc_adjecent(row, col):
        for r in range(-1, 2):
            for c in range(-1, 2):
                if row + r >= 0 and row + r < len(data) and col + c >= 0 and col + c < len(data):
                    data[row + r][col + c] += 1
                    if data[row + r][col + c] == 10:
                        inc_adjecent(row + r, col + c)

    sum_flashes = 0
    for day in range(no_of_days):
        #print(f"day {day}")
        #increase charge
        for row in range(len(data)):
            for col in range(len(data[0])):
                data[row][col] += 1

                if data[row][col] == 10:
                    inc_adjecent(row,col)

        #check for flash
        for row in range(len(data)):
            for col in range(len(data[0])):
                if data[row][col] > 9:
                    data[row][col] = 0
                    sum_flashes += 1
            
            #print(data[row])

    return sum_flashes


print(f"Part 1: {flash_count(input, 100)}")
