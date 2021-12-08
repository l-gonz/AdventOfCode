# Advent of code 2021
# Part 1

class Point:
    def from_string(self, point: str):
        self.tuple = tuple([int(x) for x in point.split(",")])
        self.x = int(self.tuple[0])
        self.y = int(self.tuple[1])
        return self

    def from_coords(self, x, y):
        self.x = x
        self.y = y
        self.tuple = (x, y)
        return self

    def __str__(self):
        return str(self.tuple)
    def __eq__(self, obj):
        return isinstance(obj, Point) and self.x == obj.x and self.y == obj.y
    def __ne__(self, obj):
        return not self == obj


def sign(num):
    if num == 0: return 0
    return 1 if num > 0 else -1

def add_to_grid(grid, point):
    if point in grid:
        grid[point] += grid[point]
    else:
        grid[point] = 1


grid = {}
with open("Day5/input.txt") as file:
    for line in file:
        points = [point.strip() for point in line.split("->")]
        start = Point().from_string(points[0])
        end = Point().from_string(points[1])
        # if start.x != end.x and start.y != end.y:
        #     continue # Diagonal, ignore

        add_to_grid(grid, start.tuple)
        next_point = start
        diff_x = sign(end.x - start.x)
        diff_y = sign(end.y - start.y)
        while next_point != end:
            next_point = Point().from_coords(next_point.x + diff_x, next_point.y + diff_y)
            add_to_grid(grid, next_point.tuple)

print(sum(map(lambda key: grid[key] > 1, grid.keys())))

        