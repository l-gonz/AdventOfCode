# Advent of code 2021
# Day 13

from typing import NamedTuple

class Fold(NamedTuple):
    axis: str
    amount: int

def read_input(input):
    points = set()
    folds = []
    with open(input) as file:
        for line in file:
            if line.isspace(): break
            points.add(tuple([int(coord) for coord in line.strip().split(',')]))
        for line in file:
            fold = line.strip().split()[-1].split('=')
            folds.append(Fold(fold[0], int(fold[1])))

    return points, folds

def draw_points(points, size):
    grid = [['.' for i in range(size[0])] for j in range(size[1])]
    for point in points:
        grid[point[1]][point[0]] = "#"
    for row in grid:
        print("".join(row))
    print()

def get_size(folds):
    size = [0, 0]
    for fold in folds:
        if all(map(bool, size)): break
        coord = int(fold.axis == 'y')
        if size[coord] == 0:
            size[coord] = fold.amount * 2 + 1
    return size

def puzzle(input, n_folds=-1):
    points, folds = read_input(input)
    size = get_size(folds)

    for i, fold in enumerate(folds):
        if n_folds > 0 and i >= n_folds: break
        new_points = list(points)
        fold_coord = int(fold.axis == 'y')
        for j, point in enumerate(new_points):
            if point[fold_coord] > fold.amount:
                point = list(point)
                point[fold_coord] = fold.amount * 2 - point[fold_coord]
                new_points[j] = tuple(point)
        points = set(new_points)
        size[fold_coord] //= 2

    draw_points(points, size)
    return len(points)


print(puzzle("Day13/test.txt", 1))
puzzle("Day13/input.txt")
