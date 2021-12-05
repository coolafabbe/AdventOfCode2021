import time, sys

GREEN = '\033[92m'
GRAY = '\033[90m'
END_COLOR = '\033[0m'
CLR = '\x1B[0K'

def print_graph(graph, graph_dim):
    danger_points = 0
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if graph[x][y] == 0:
                if graph_dim[0] < 50:
                    print(f'{GRAY}{graph[x][y]}{END_COLOR}', end=' ')
                pass
            elif graph[x][y] == 1:
                if graph_dim[0] < 50:
                   print(f'{graph[x][y]}', end=' ')
                pass
            else:
                danger_points += 1
                if graph_dim[0] < 50:
                    print(f'{GREEN}{graph[x][y]}{END_COLOR}', end=' ')
        if graph_dim[0] < 50:
            print(CLR)
    return danger_points

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Please provide an input file as second argument: python {__file__} input')
        exit()

    with open(sys.argv[1], "r") as file:
        entries = file.read().splitlines()

    print(f'Analyzing {len(entries)} entries')

    lines = [[[int(c) for c in l.split(',')] for l in e.split(' -> ')] for e in entries]

    graph_dim = [0, 0]
    for line in lines:
        for x, y in line:
            if x+1 > graph_dim[0]:
                graph_dim[0] = x+1
            if y+1 > graph_dim[1]:
                graph_dim[1] = y+1

    print(f'Graph max coords: {graph_dim}\n')
    if graph_dim[0] > 50:
        print(f'Graph larger than 50 columns, not visualizing output.')

    graph = [[0 for x in range(graph_dim[0])] for y in range(graph_dim[1])]

    if graph_dim[0] < 50:
        print_graph(graph, graph_dim)
        print(f'Danger points: {GREEN}0{END_COLOR}')

    for id, line in enumerate(lines):
        if graph_dim[0] < 50:
            time.sleep(1)
        x1, y1 = line[0]
        x2, y2 = line[1]
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        if graph_dim[0] < 50:
            print(f'\x1B[{graph_dim[1]+3}A')
        if x_min == x_max:
            print(f'Adding vertical line: ({x1}, {y1}) -> ({x2}, {y2}){CLR}')
            for y in range(y_min, y_max+1):
                graph[x_min][y] += 1
        elif y_min == y_max:
            print(f'Adding horizontal line: ({x1}, {y1}) -> ({x2}, {y2}){CLR}')
            for x in range(x_min, x_max+1):
                graph[x][y_min] += 1
        else:
            if not 'no-diagonals' in sys.argv:
                print(f'Adding diagonal line: ({x1}, {y1}) -> ({x2}, {y2}){CLR}')
                for d in range(x_max + 1 - x_min):
                    x = x1 + d if x1 < x2 else x1 - d
                    y = y1 + d if y1 < y2 else y1 - d
                    graph[x][y] += 1
            else:
                print(f'Omitting diagonal line: ({x1}, {y1}) -> ({x2}, {y2}){CLR}')
        danger_points = print_graph(graph, graph_dim)
        print(f'Danger points: {GREEN}{danger_points}{END_COLOR}{CLR}')
        if graph_dim[0] > 50 and id+1 < len(lines):
            print('\x1B[3A')

