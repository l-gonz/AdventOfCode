# Advent of code
# Day 14

def read_input(input):
    pairs = {}
    with open(input) as file:
        template = file.readlines(2)[0].strip()
        for line in file:
            if line.isspace(): continue
            pair = line.split()
            pairs[pair[0]] = pair[2]
    return template, pairs

def insert_pairs(template, pairs):
    result = ""
    for i, c in enumerate(template):
        result += c
        if i == len(template) - 1: break
        pair = c + template[i + 1]
        if pair in pairs:
            result += pairs[pair]
    return result

def get_score_1(template):
    keys = set(list(template))
    occurrences = {k: sum(map(lambda c: c == k, template)) for k in keys}
    print(occurrences)
    return max(occurrences.values()) - min(occurrences.values())

def get_score_2(pairs, start, end):
    keys = set([c for key in pairs.keys() for c in key])
    occurrences = {k: 0 for k in keys}
    for pair, amount in pairs.items():
        occurrences[pair[0]] += amount
        occurrences[pair[1]] += amount
    for key, value in occurrences.items():
        occurrences[key] = value // 2
    occurrences[start] += 1
    if start != end:
        occurrences[end] += 1
    print(occurrences)
    return max(occurrences.values()) - min(occurrences.values())

def puzzle_1(input, steps):
    template, pairs = read_input(input)

    for _ in range(steps):
        result = insert_pairs(template, pairs)
        template = result
        
    return get_score_1(result)

def puzzle_2(input, steps):
    template, pair_rules = read_input(input)
    start, end = template[0], template[-1]
    current_pairs = {k: 0 for k in pair_rules.keys()}
    for i in range(len(template) - 1):
        current_pairs[template[i] + template[i+1]] += 1
    
    for _ in range(steps):
        new_pairs = {k: 0 for k in pair_rules.keys()}
        for key, value in current_pairs.items():
            insert = pair_rules[key]
            new_pairs[key[0] + insert] += value
            new_pairs[insert + key[1]] += value
        current_pairs = new_pairs

    return get_score_2(current_pairs, start, end)

print(puzzle_1("Day14/test.txt", 10))
print(puzzle_1("Day14/input.txt", 10))
print(puzzle_2("Day14/test.txt", 10))
print(puzzle_2("Day14/input.txt", 10))

print(puzzle_2("Day14/test.txt", 40))
print(puzzle_2("Day14/input.txt", 40))