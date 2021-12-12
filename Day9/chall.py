# Advent of code 2021
# Day 9 - Part 1

def is_low(grid, i, j):
    point = grid[i][j]
    return (
        i == 0 or point < grid[i - 1][j]) and (
        j == 0 or point < grid[i][j - 1]) and (
        i == len(grid) - 1 or point < grid[i + 1][j]) and (
        j == len(grid[i]) - 1 or point < grid[i][j + 1])

def get_neighbor_cells(i, j):
    return [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]

def get_basin_size(grid, i, j):
    size = 0
    cells_to_check = set([(i, j)])
    while len(cells_to_check) > 0:
        current_cell = cells_to_check.pop()
        size += 1
        grid[current_cell[0]][current_cell[1]] = 0
        for x, y in get_neighbor_cells(*current_cell):
            if x < 0 or y < 0: continue
            if x >= len(grid) or y >= len(grid[x]): continue
            if grid[x][y] != 0 and grid[x][y] != 9:
                cells_to_check.add((x, y))
    return size

def extract_max(basins):
    size = max(basins)
    basins.remove(size)
    return size

def puzzle_1(input):
    with open(input) as file:
        grid = [[int(c) for c in line.strip()] for line in file]
    
    result = 0
    for i, row in enumerate(grid):
        for j, point in enumerate(row):
            if is_low(grid, i, j):
                result += point + 1
    return result

def puzzle_2(input):
    with open(input) as file:
        grid = [[int(c) for c in line.strip()] for line in file]
    
    basins = []
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if is_low(grid, i, j):
                basins.append(get_basin_size(grid, i, j))

    return extract_max(basins) * extract_max(basins) * extract_max(basins)

# print(puzzle_1("Day9/test.txt"))
# print(puzzle_1("Day9/input.txt"))
# print(puzzle_2("Day9/test.txt"))
print(puzzle_2("Day9/input.txt"))