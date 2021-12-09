# Advent of code 2021
RATE = 7

# Day 6 - Part 1
# Can be brute-forced for low values
def pass_day(fish):
    new_fish_amount = 0
    for i, f in enumerate(fish):
        fish[i] = f - 1 if f > 0 else RATE - 1
        new_fish_amount += f == 0
    fish += [RATE + 1] * new_fish_amount


def calculate_fish(input, days):
    with open(input) as file:
        fish = [int(x) for x in file.readline().split(",")]

    for i in range(days):
        if i % 5 == 0:
            print("Day", i)
        pass_day(fish)
    return len(fish)

# print(calculate_fish("Day6/test.txt", 18)) # 26
# print(calculate_fish("Day6/test.txt", 80)) # 5934
# print(calculate_fish("Day6/input.txt", 80)) # 387413

# Day 6 - Part 2
# Using population growth model

def pass_day_2(fish):
    new_fish = fish[0]
    for days_left in range(1, RATE+2):
        fish[days_left-1] = fish[days_left]
    fish[RATE+1] = new_fish
    fish[RATE-1] += new_fish

def calculate_fish_2(input, days):
    fish = {i: 0 for i in range(RATE + 2)}
    with open(input) as file:
        initial_fish = [int(x) for x in file.readline().split(",")]
        for f in initial_fish:
            fish[f] += 1

    for i in range(days):
        # if i % 5 == 0:
            # print("Day", i)
        pass_day_2(fish)
    return sum(fish.values())

print(calculate_fish_2("Day6/test.txt", 18)) # 26
print(calculate_fish_2("Day6/test.txt", 80)) # 5934
print(calculate_fish_2("Day6/input.txt", 80)) # 387413
print(calculate_fish_2("Day6/input.txt", 256)) # 1738377086345
