# Advent of code 2021

def read_draw(file):
    line = file.readline()
    return line.split(",")


def read_boards(file):
    board = []
    boards = []
    for line in file:
        if line.isspace():
            if len(board) > 1:
                boards.append((board, [x for x in zip(*board)]))
                board = []
            continue
        board.append(line.split())

    if len(board) > 1:
        boards.append((board, [x for x in zip(*board)]))
    return boards


def get_winning_board(boards, draws):
    for board, board_t in boards:
        for row in board:
            if all(x in draws for x in row):
                return board
        for col in board_t:
            if all(x in draws for x in col):
                return board
    return None


def calculate_score(winning_board, draws):
    flat_board = [item for row in winning_board for item in row]
    return sum(int(item) for item in flat_board if item not in draws) * int(draws[-1])


# Day 4 - Part 1
with open("Day4/input.txt") as file:
    draw = read_draw(file)
    boards = read_boards(file)
past_drawn = []
for num in draw:
    past_drawn.append(num)
    win = get_winning_board(boards, past_drawn)
    if win:
        print(calculate_score(win, past_drawn))
        break


# Day 4 - Part 2
past_drawn = []
for num in draw:
    past_drawn.append(num)
    win = get_winning_board(boards, past_drawn)
    while win:
        score = calculate_score(win, past_drawn)
        boards.remove((win, [x for x in zip(*win)]))
        win = get_winning_board(boards, past_drawn)
    if len(boards) == 0:
        break
print(score)