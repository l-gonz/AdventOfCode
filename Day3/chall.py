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
print("---------------")

# Day 3 - Part 2

with open("Day3/input.txt") as file:
    oxygen = [line.strip() for line in file]
    co2 = oxygen.copy()
    for i in range(len(oxygen[0])):
        if len(oxygen) > 1:
            ones = sum(int(num[i]) for num in oxygen)
            most_common = int(ones > len(oxygen) // 2 or ones == len(oxygen) / 2)
            oxygen = [num for num in oxygen if int(num[i]) == most_common]

        if len(co2) > 1:
            ones = sum(int(num[i]) for num in co2)
            least_common = int(not (ones > len(co2) // 2 or ones == len(co2) / 2))
            co2 = [num for num in co2 if int(num[i]) == least_common]

print(len(oxygen), oxygen[0])
print(len(co2), co2[0])
print(int(oxygen[0], 2) * int(co2[0], 2))
