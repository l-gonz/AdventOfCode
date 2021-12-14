# Advent of code 2021
# Day 12

START = 'start'
END = 'end'

def read_map(input):
    connections = {}
    with open(input) as file:
        for line in file:
            caves = line.strip().split('-')
            for i, cave in enumerate(caves):
                if cave in connections:
                    connections[cave].add(caves[-i-1])
                else:
                    connections[cave] = set([caves[-i-1]])
    return connections

def is_possible_visit_1(path, c):
    return c.isupper() or c not in path

def is_possible_visit_2(path, c):
    if c.isupper() or c not in path:
        return True
    small_caves = [c for c in path if c.islower()]
    return c != START and c != END and len(small_caves) == len(set(small_caves))

def puzzle(input, possible_visit_func):
    connections = read_map(input)
    paths = [[START]]

    while any(map(lambda p: p[-1] != END, paths)):
        new_paths = []
        for path in paths:
            if path[-1] == END: 
                new_paths.append(path)
                continue
            for c in connections[path[-1]]:
                if possible_visit_func(path, c):
                    new_paths.append(path + [c])
        paths = new_paths

    return len(paths)

print(puzzle("Day12/test1.txt", is_possible_visit_1))
print(puzzle("Day12/test2.txt", is_possible_visit_1))
print(puzzle("Day12/test3.txt", is_possible_visit_1))
print(puzzle("Day12/input.txt", is_possible_visit_1))

print(puzzle("Day12/test1.txt", is_possible_visit_2))
print(puzzle("Day12/test2.txt", is_possible_visit_2))
print(puzzle("Day12/test3.txt", is_possible_visit_2))
print(puzzle("Day12/input.txt", is_possible_visit_2))