# Advent of Code
# Day 1 - Part 1

prev_num = None
increase = 0
with open("Day1/input.txt", 'r') as file:
    for line in file:
        num = int(line)
        if prev_num:
            if num > prev_num:
                increase += 1
        prev_num = num

print("Increase:", increase)

# Day 1 - Part 2
window = []
prev_result = None
increase = 0
with open("Day1/input.txt", 'r') as file:
    for line in file:
        num = int(line)
        window.append(num)
        if len(window) > 3:
            window.pop(0)
        
        if len(window) == 3:
            result = sum(window)
            if prev_result and result > prev_result:
                increase += 1
            prev_result = result
            
print("Increase:", increase)