# Advent of code 2021


def len_digit(digit):
    return DIGITS[digit].count('1')

def get_digits_by_length_dict():
    lengths = {}
    for i in range(10):
        l = len_digit(i)
        if l in lengths:
            lengths[l].append(i)
        else:
            lengths[l] = [i]
    return lengths

DIGITS = {
    0: '1110111',
    1: '0010010',
    2: '1011101',
    3: '1011011',
    4: '0111010',
    5: '1101011',
    6: '1101111',
    7: '1010010',
    8: '1111111',
    9: '1111011'
}

DIGITS_BY_LENGTH = get_digits_by_length_dict()
# {
#     2: [1],
#     3: [7],
#     4: [4],
#     5: [2, 3, 5],
#     6: [0, 6, 9],
#     7: [8]
# }

SINGLE_DIGITS = [x for x in DIGITS_BY_LENGTH.keys() if len(DIGITS_BY_LENGTH[x]) == 1]
POSITIONS = range(len_digit(8))

def get_input(input):
    with open(input) as file:
        patterns, outputs = [], []
        for line in file:
            p, o = tuple(line.split('|'))
            patterns.append(p.split())
            outputs.append(o.split())  
    return patterns, outputs

def inspect_pattern(pattern, position_map):
    """Removes possibilities from position_map that don't match the pattern."""
    digit_positions = [DIGITS[d] for d in DIGITS_BY_LENGTH[len(pattern)]]
    and_digits = [int(all(map(int, t))) for t in zip(*digit_positions)]
    or_digits = [int(any(map(int, t))) for t in zip(*digit_positions)]

    for pos in POSITIONS:
        # Keep only wires present in pattern if wire is used for all possible digits
        if and_digits[pos]:
            position_map[pos] = [c for c in position_map[pos] if c in pattern]
        # Remove wires not present in pattern if wire is not used in all possible digits
        if not or_digits[pos]:
            position_map[pos] = [c for c in position_map[pos] if c not in pattern]

def map_to_digits(pos_map, enc_digits):
    decoded = []
    for enc in enc_digits:
        bits = "".join([str(int(c[0] in enc)) for c in pos_map])
        digit = list(DIGITS.keys())[list(DIGITS.values()).index(bits)]
        decoded.append(digit)
    return decoded

def puzzle_1(input):
    patterns, outputs = get_input(input)
    flat_outputs = [cell for row in outputs for cell in row]
    return sum(map(lambda out: len(out) in SINGLE_DIGITS, flat_outputs))

def puzzle_2(input):
    patterns, outputs = get_input(input)
    all_input = [p + o for p, o in zip(patterns, outputs)]
    result = 0
    for index, config in enumerate(all_input):
        # Keep list with wire possibilities for each position
        position_map = [[chr(c) for c in range(ord('a'), ord('h'))] for i in POSITIONS]
        config.sort(key=lambda p: len(p))
        config.sort(key=lambda p: len(DIGITS_BY_LENGTH[len(p)]))

        # Each new pattern removes possibilities from the map
        for pattern in config:
            inspect_pattern(pattern, position_map)

        # Remove wires that have been discovered as mapped to a different position
        for i, m in enumerate(position_map):
            if len(m) > 1:
                position_map[i] = [c for c in m if not any(map(lambda x: len(x) == 1 and x[0] == c, position_map))]

        # Find solution from mapping
        assert(all(map(lambda x: len(x) == 1, position_map)))
        decrypted = map_to_digits(position_map, outputs[index])
        result += int("".join([str(x) for x in decrypted]))

    return result


# print(puzzle_1("Day8/test.txt"))
# print(puzzle_1("Day8/input.txt"))
print(puzzle_2("Day8/test.txt"))
print(puzzle_2("Day8/input.txt"))
