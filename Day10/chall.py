# Advent of code 2021
# Day 10

OPEN = ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']
ERROR_POINTS = {
    CLOSE[0]: 3,
    CLOSE[1]: 57,
    CLOSE[2]: 1197,
    CLOSE[3]: 25137
}

COMPLETE_POINTS = {k: i + 1 for i, k in enumerate(CLOSE)}

def puzzle_1(input):
    points = 0
    with open(input) as file:
        for line in file:
            chunks = []
            for c in line:
                if c in OPEN:
                    chunks.append(c)
                elif c in CLOSE:
                    # Correct closing
                    if c == CLOSE[OPEN.index(chunks[-1])]:
                        chunks.pop()
                    # Corrupt
                    else:
                        points += ERROR_POINTS[c]
                        break
    return points

def puzzle_2(input):
    incomplete = []
    chunks = []
    with open(input) as file:
        for line in file:
            for c in line:
                if c in OPEN:
                    chunks.append(c)
                elif c in CLOSE:
                    # Correct closing
                    if c == CLOSE[OPEN.index(chunks[-1])]:
                        chunks.pop()
                    else: # Corrupt
                        chunks = []
                        break
            if len(chunks) > 0: # Incomplete
                incomplete.append(chunks)
            chunks = []
    all_points = []
    for line in incomplete:
        points = 0
        for opening in reversed(line):
            closing = CLOSE[OPEN.index(opening)]
            points = points * 5 + COMPLETE_POINTS[closing]
        all_points.append(points)

    all_points.sort()
    return all_points[len(all_points) // 2]


# print(puzzle_1("Day10/test.txt"))
# print(puzzle_1("Day10/input.txt"))
# print(puzzle_2("Day10/test.txt"))
print(puzzle_2("Day10/input.txt"))


    
