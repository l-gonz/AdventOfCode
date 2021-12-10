# Advent of code 2021

def get_cost(iter, pos):
    sum = 0
    for p in iter:
        diff = pos - p
        sum += diff if diff >= 0 else -diff
    return sum


def get_cost_2(iter, pos):
    sum = 0
    for p in iter:
        diff = pos - p if pos - p >= 0 else p - pos
        sum += (diff + 1) * diff / 2 # Gauss
    return int(sum)


def get_optimal_position(input, cost_function):
    with open(input) as file:
        positions = [int(x) for x in file.readline().split(",")]

    costs = []
    start, end = min(positions), max(positions)
    for i in range(start, end):
        costs.append(cost_function(positions, i))

    target = min(costs)
    for i, c in enumerate(costs):
        if c == target:
            break

    return i + start, target


# Day 7 - Part 1
print(get_optimal_position("Day7/test.txt", get_cost))
print(get_optimal_position("Day7/input.txt", get_cost))

# Day 7 - Part 2
print(get_optimal_position("Day7/test.txt", get_cost_2))
print(get_optimal_position("Day7/input.txt", get_cost_2))
