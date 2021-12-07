# Advent of code
# Day 3 - Part 1

length = 0
counter = None
with open("Day3/input.txt") as file:
    for line in file:
        length += 1
        if not counter:
            counter = [int(c) for c in line.strip()]
        else:
            counter = [x + int(y) for x, y in zip(counter, line)]

gamma_rate = sum(int(c > length // 2) << (len(counter) - 1 - i) for i, c in enumerate(counter))
epsilon_rate = (1 << len(counter)) - 1 - gamma_rate

print(counter)
print(bin(gamma_rate))
print(bin(epsilon_rate))
print(gamma_rate * epsilon_rate)
