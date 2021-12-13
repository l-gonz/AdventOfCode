# Advent of code 2021

def increase_surround(grid, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i < 0) or (x + i >= len(grid)) or (y + j < 0) or (y + j >= len(grid[x])):
                continue
            grid[x + i][y + j] += 1

def step(grid):
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            grid[i][j] += 1
    
    i, j = (0, 0)
    glowed = []
    while i < len(grid):
        if j == len(grid[i]):
            j = 0
            i += 1
            continue

        if grid[i][j] > 9 and (i, j) not in glowed:
            glowed.append((i, j))
            increase_surround(grid, i, j)
            i, j = 0, 0
        else:
            j += 1

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] > 9:
                grid[i][j] = 0

    return len(glowed)
    

def puzzle_1(input, steps):
    grid = []
    with open(input) as file:
        for line in file:
            grid.append([int(c) for c in line.strip()])

    glows = 0
    for i in range(steps):
        glows += step(grid)

    return glows

def puzzle_2(input, max_tries=10000):
    grid = []
    with open(input) as file:
        for line in file:
            grid.append([int(c) for c in line.strip()])

    for i in range(max_tries):
        step(grid)
        if all(map(lambda row: not any(map(bool, row)), grid)):
            return(i + 1)


# print(puzzle_1("Day11/test.txt", 10))
# print(puzzle_1("Day11/test.txt", 100))
# print(puzzle_1("Day11/input.txt", 100))

print(puzzle_2("Day11/test.txt"))
print(puzzle_2("Day11/input.txt"))