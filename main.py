from copy import deepcopy
import pygame
import button
import requests
import time


def print_board(arr):
    print('     sudoku solver')
    print('-------------------------')
    for row in arr:
        for element in row:
            if element != 0:
                print(str(element) + "  ", end="")
            else:
                print("-  ", end="")
        print()


def fill_static_board(arr):
    # row 1
    arr[0][0] = 1
    arr[0][2] = 8
    arr[0][3] = 5
    arr[0][6] = 6

    # row 2
    arr[1][1] = 2
    arr[1][5] = 1

    # row 3
    arr[2][1] = 4
    arr[2][8] = 8

    # row 4
    arr[3][0] = 8
    arr[3][2] = 5
    arr[3][5] = 3
    arr[3][8] = 9

    # row 5
    arr[4][2] = 4

    # row 6
    arr[5][4] = 9
    arr[5][6] = 2

    # row 7
    arr[6][0] = 3
    arr[6][2] = 9
    arr[6][5] = 5
    arr[6][8] = 2

    # row 8
    arr[7][3] = 6
    arr[7][7] = 7

    # row 9
    arr[8][1] = 1


def check_square(arr, row_num, col_num) -> bool:
    my_set = set()

    # check that the row is valid
    for i in arr[row_num]:
        if i in my_set and i != 0:
            return False
        my_set.add(i)
    my_set.clear()

    # check that the column is valid
    for row in arr:
        if row[col_num] in my_set and row[col_num] != 0:
            return False
        my_set.add(row[col_num])
    my_set.clear()

    # check that the 3x3 square is valid
    row_num_rounded = row_num // 3
    col_num_rounded = col_num // 3
    for i in range(3 * row_num_rounded, 3 * row_num_rounded + 3):
        for j in range(3 * col_num_rounded, 3 * col_num_rounded + 3):
            if arr[i][j] in my_set and arr[i][j] != 0:
                return False
            my_set.add(arr[i][j])
    my_set.clear()

    return True


def solve_board(play_board, row_num, col_num) -> bool:
    if row_num == 8 and col_num == 9:
        return True
    if col_num > 8:
        col_num = 0
        row_num += 1

    solved = False
    if play_board[row_num][col_num] == 0:
        for k in range(1, 10):
            play_board[row_num][col_num] = k
            update_board(row_num, col_num, k)
            if check_square(play_board, row_num, col_num):
                solved = solve_board(play_board, row_num, col_num + 1)
                if solved:
                    return True
            play_board[row_num][col_num] = 0
            update_board(row_num, col_num, 0)
    else:
        solved = solve_board(play_board, row_num, col_num + 1)

    return solved


def update_board(row, column, number):
    if number == 0:
        pygame.draw.rect(window, OFF_WHITE, [55 + 50 * column, 55 + 50 * row, 40, 40])
    else:
        value = font.render(str(number), True, RED)
        window.blit(value, ((column + 1) * 50 + 18, (row + 1) * 50))
    pygame.display.update()
    # time.sleep(.0000000000000000001)


def fill_unsolved_squares():
    for i in range(0, len(play_board)):
        for j in range(0, len(play_board[0])):
            if 1 <= play_board[i][j] <= 9 and arr[i][j] == 0:
                value = font.render(str(play_board[i][j]), True, RED)
                window.blit(value, ((j + 1) * 50 + 18, (i + 1) * 50))


def clear_board():
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            pygame.draw.rect(window, OFF_WHITE, [55 + 50 * j, 55 + 50 * i, 40, 40])


def generate_board(difficulty):
    url = 'https://sugoku.herokuapp.com/board?difficulty=' + difficulty
    x = requests.get(url)
    board = eval(x.text)
    return board['board']


def draw_numbers():
    # draw numbers
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if 1 <= arr[i][j] <= 9:
                value = font.render(str(arr[i][j]), True, BLUE)
                window.blit(value, ((j + 1) * 50 + 18, (i + 1) * 50))


# main function
if __name__ == '__main__':
    rows = 9
    cols = 9
    arr = [[0 for i in range(cols)] for j in range(rows)]
    WIDTH = 550
    HEIGHT = 650
    BLUE = (52, 31, 151)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    OFF_WHITE = (255, 247, 245)
    DIFFICULTY = 'easy'

    arr = generate_board(DIFFICULTY)
    # print_board(arr)

    play_board = deepcopy(arr)
    # print_board(play_board)

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku Solver')
    window.fill(OFF_WHITE)
    font = pygame.font.SysFont('Comic Sans MS', 35)

    # draw lines
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(window, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 4)  # vertical lines
            pygame.draw.line(window, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 4)  # horizontal lines
        else:
            pygame.draw.line(window, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 2)  # vertical lines
            pygame.draw.line(window, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 2)  # horizontal lines

    draw_numbers()

    # add buttons
    solve_img = pygame.image.load('img/solve_btn.png').convert_alpha()
    solve_button = button.Button(60, 525, solve_img, .35)
    clear_img = pygame.image.load('img/clear_btn.png').convert_alpha()
    clear_button = button.Button(300, 525, clear_img, .6)
    generate_img = pygame.image.load('img/generate_btn.png').convert_alpha()
    generate_button = button.Button(175, 600, generate_img, .75)

    pygame.display.update()

    while True:
        # my logic
        if solve_button.draw(window):
            # fills in the squares if the button is pressed
            play_board = deepcopy(arr)
            solve_board(play_board, 0, 0)
            # fill_unsolved_squares()

        if clear_button.draw(window):
            clear_board()
            draw_numbers()

        if generate_button.draw(window):
            arr = generate_board(DIFFICULTY)
            clear_board()
            draw_numbers()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # updates the computer graphics
        pygame.display.update()
