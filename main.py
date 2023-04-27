import pygame
from src.config import WIDTH, HEIGHT, OFF_WHITE, DIFFICULTY, font
from src.board import Board
from src.button import Button

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku Solver')
    window.fill(OFF_WHITE)

    board = Board(window, difficulty=DIFFICULTY)
    board.draw_lines()
    board.draw_numbers()

    solve_img = pygame.image.load('img/solve_btn.png').convert_alpha()
    solve_button = Button(60, 525, solve_img, .35)

    clear_img = pygame.image.load('img/clear_btn.png').convert_alpha()
    clear_button = Button(300, 525, clear_img, .6)

    generate_img = pygame.image.load('img/generate_btn.png').convert_alpha()
    generate_button = Button(175, 600, generate_img, .75)

    pygame.display.update()

    while True:
        solve_click = solve_button.draw(window)
        clear_click = clear_button.draw(window)
        generate_click = generate_button.draw(window)

        if solve_click:
            board.solve()
            window.fill(OFF_WHITE)
            board.draw_lines()
            board.draw_numbers()

        if clear_click:
            board.clear()
            window.fill(OFF_WHITE)
            board.draw_lines()
            board.draw_numbers()

        if generate_click:
            board.generate()
            window.fill(OFF_WHITE)
            board.draw_lines()
            board.draw_numbers()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

if __name__ == '__main__':
    main()
