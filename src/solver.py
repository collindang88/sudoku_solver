from typing import List
import pygame
import time

from src.config import OFF_WHITE, RED, font, DELAY

class Solver:
    def __init__(self, state: List[List[int]], window: pygame.surface.Surface):
        self.state = state
        self.window = window

    def solve(self, row_num=0, col_num=0) -> bool:
        if row_num == 8 and col_num == 9:
            return True
        if col_num > 8:
            col_num = 0
            row_num += 1

        solved = False
        if self.state[row_num][col_num] == 0:
            for k in range(1, 10):
                self.state[row_num][col_num] = k
                self.update_board(row_num, col_num, k)
                if self.check_square(row_num, col_num):
                    solved = self.solve(row_num, col_num + 1)
                    if solved:
                        return True
                self.state[row_num][col_num] = 0
                self.update_board(row_num, col_num, 0)
        else:
            solved = self.solve(row_num, col_num + 1)

        return solved

    def update_board(self, row: int, column: int, number: int) -> None:
        if number == 0:
            pygame.draw.rect(self.window, OFF_WHITE, [55 + 50 * column, 55 + 50 * row, 40, 40])
        else:
            value = font.render(str(number), True, RED)
            self.window.blit(value, ((column + 1) * 50 + 18, (row + 1) * 50))
        pygame.display.update()
        time.sleep(DELAY)

    def check_square(self, row_num: int, col_num: int) -> bool:
        my_set = set()

        # check that the row is valid
        for i in self.state[row_num]:
            if i in my_set and i != 0:
                return False
            my_set.add(i)
        my_set.clear()

        # check that the column is valid
        for row in self.state:
            if row[col_num] in my_set and row[col_num] != 0:
                return False
            my_set.add(row[col_num])
        my_set.clear()

        return True