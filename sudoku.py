import random as r

def generate_board(b, d):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r.shuffle(nums)
    c = 0
    seed = []

    for i in nums:
        b[c][c]=i
        c+=1

    solve(b)

    if d == 'e':
        randomizer = 15
    elif d == 'm':
        randomizer = 30
    elif d == 'h':
        randomizer = 70

    while len(seed) < randomizer:
        seed.append((r.randint(0, 8), r.randint(0, 8)))
    seed = set(seed)
    for s in seed:
        b[s[0]][s[1]] = 0

def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True

            b[row][col] = 0

    return False

def valid_row(b, n, p):
    for i in range(len(b[0])):
        if b[p[0]][i] == n and p[1] != i:
            return False
    return True

def valid_column(b, n, p):
    for i in range(len(b)):
        if b[i][p[1]] == n and p[0] != i:
            return False
    return True

def valid_cell(b, n, p):
    cell_x = p[1] // 3
    cell_y = p[0] // 3

    for i in range(cell_y*3, cell_y*3 + 3):
        for j in range(cell_x * 3, cell_x*3 + 3):
            if b[i][j] == n and (i, j) != p:
                return False
    return True

def is_valid(b, n, p):
    if valid_cell(b, n, p) and valid_column(b, n, p) and valid_row(b, n, p):
        return True
    else:
        return False

def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("--------------------------")

        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")
    print("______________________________")


def find_empty(b):
    for r in range(len(b)):
        for c in range(len(b[0])):
            if b[r][c] == 0:
                return (r, c)

    return None

def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    difficulties = ['e', 'm', 'h']
    difficulty = 'x'

    print("Sodoku\n_____________________________\n")

    while difficulty not in difficulties:
        difficulty = input("Choose difficulty - Easy(e), Medium(m), or Hard(h): ")
    print("______________________________\n")
    generate_board(board, difficulty)
    print_board(board)
    s = input("Type 'solve' to print solved puzzle: ")
    while s != 'solve':
        s = input("Type 'solve' to print solved puzzle: ")
    print("______________________________\n")
    solve(board)
    print_board(board)

main()
