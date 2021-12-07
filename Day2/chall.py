# Advent of code
# Day 2 - Part 1

FORWARD = "forward"
UP = "up"
DOWN = "down"

horizontal_pos = 0
depth = 0
with open("Day2/input.txt", 'r') as file:
    for line in file:
        command, amount = line.split()
        if command == FORWARD:
            horizontal_pos += int(amount)
        elif command == UP:
            depth -= int(amount)
        elif command == DOWN:
            depth += int(amount)
    
print("Solution", horizontal_pos * depth)

# Day 2 - Part 2

aim = 0
horizontal_pos = 0
depth = 0
with open("Day2/input.txt", 'r') as file:
    for line in file:
        command, amount = line.split()
        if command == FORWARD:
            horizontal_pos += int(amount)
            depth += aim * int(amount)
        elif command == UP:
            aim -= int(amount)
        elif command == DOWN:
            aim += int(amount)
    
print("Solution", horizontal_pos * depth)