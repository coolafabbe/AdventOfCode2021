import os.path

def smoke_basin(data, search_for_basin_size:bool=False):
    def find_adjecent_values(line, col, max_lines, max_cols):
        adj = []
        if line > 0:
            adj.append(data[line -1][col])
        if line < max_lines - 1:
            adj.append(data[line + 1][col])
        if col > 0:
            adj.append(data[line][col-1])
        if col < max_cols -1:
            adj.append(data[line][col+1])
        return adj
    def find_adjecent_coords(basin, line, col, max_lines, max_cols):
        def check_coord(line, col):
            if not (line, col) in basin and data[line][col] != 9:
                return True
            else:
                return False
                
        if line > 0:
            if check_coord(line - 1, col):
                basin.append((line - 1, col))
                basin = find_adjecent_coords(basin, line - 1, col, no_of_lines, no_of_cols)
        if line < max_lines - 1:
            if check_coord(line + 1, col):
                basin.append((line + 1, col))
                basin = find_adjecent_coords(basin, line + 1, col, no_of_lines, no_of_cols)
        if col > 0:
            if check_coord(line, col - 1):
                basin.append((line, col - 1))
                basin = find_adjecent_coords(basin, line, col - 1, no_of_lines, no_of_cols)
        if col < max_cols -1:
            if check_coord(line, col + 1):
                basin.append((line, col + 1))
                basin = find_adjecent_coords(basin, line, col + 1, no_of_lines, no_of_cols)
        return basin
    
    def calc_risk_level(points:list):
        sum = 0
        for (line, col) in points:
            sum += 1 + data[line][col]
        return sum

    no_of_lines = len(data)
    no_of_cols = len(data[0])
    lowest_points = []
    for line in range(no_of_lines):
        for col in range(no_of_cols):
            if data[line][col] < min(find_adjecent_values(line, col, no_of_lines, no_of_cols)):
                lowest_points.append((line,col))

    if not search_for_basin_size:
        return calc_risk_level(lowest_points)

    basin_sizes = []
    for line, col in lowest_points:
        basin = [(line, col)]
        basin = find_adjecent_coords(basin, line, col, no_of_lines, no_of_cols)
        basin_sizes.append(len(basin))
    
    product = 1
    for i in range(3):
        top = max(basin_sizes)
        basin_sizes.remove(top)
        product *= top

    return product

path = os.path.dirname(os.path.realpath(__file__))

#Read input
with open(path+"/input.txt") as file:
  input = [[int(dig) for dig in x.strip()] for x in file.readlines()]

#read example_input
with open(path+"/input_example.txt") as file:
  input_example =  [[int(dig) for dig in x.strip()] for x in file.readlines()]
  #print(input_example)

assert smoke_basin(input_example) == 15, "Function is wrong"
print(f"Part 1: {smoke_basin(input)}")
assert smoke_basin(input_example, True) == 1134, "Function is wrong"
print(f"Part 2: {smoke_basin(input, True)}")
