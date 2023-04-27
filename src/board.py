from copy import deepcopy
import random
from sudoku import Sudoku
import pygame
from typing import List

from src.config import WIDTH, HEIGHT, BLUE, BLACK, RED, OFF_WHITE, font
from src.solver import Solver

class Board:
    def __init__(self, window: pygame.surface.Surface, difficulty='hard'):
        self.window = window
        self.difficulty = difficulty
        self.empty_board = self.generate_board(self.difficulty)
        self.play_board = deepcopy(self.empty_board)

    def solve(self):
        solver = Solver(deepcopy(self.empty_board), self.window)
        solver.solve(0, 0)
        self.play_board = solver.state

    def clear(self):
        self.play_board = deepcopy(self.empty_board)

    def generate(self):
        self.empty_board = self.generate_board()
        self.play_board = deepcopy(self.empty_board)

    def _generate_board(self, difficulty: str) -> List[List[int]]:
        difficulty_mapping = {
            "easy": (0.3, 0.4),
            "medium": (0.5, 0.6),
            "hard": (0.7, 0.8),
            "expert": (0.9, 1.0)
        }
        
        if difficulty not in difficulty_mapping:
            raise ValueError(f"Invalid difficulty: {difficulty}. Use 'easy', 'medium', 'hard', or 'expert'.")

        min_diff, max_diff = difficulty_mapping[difficulty]
        random_difficulty = random.uniform(min_diff, max_diff)
        seed = random.randint(0, 1000)
    
        puzzle = Sudoku(3, seed=seed).difficulty(random_difficulty)
        puzzle.show()

        return [[0 if value is None else value for value in row] for row in puzzle.board]

    def draw_lines(self):
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.window, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 4)  # vertical lines
                pygame.draw.line(self.window, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 4)  # horizontal lines
            else:
                pygame.draw.line(self.window, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 2)  # vertical lines
                pygame.draw.line(self.window, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 2)  # horizontal lines

    def draw_numbers(self):
        for i in range(0, len(self.play_board)):
            for j in range(0, len(self.play_board[0])):
                if self.play_board[i][j]:
                    value = font.render(str(self.play_board[i][j]), True, RED)
                    self.window.blit(value, ((j + 1) * 50 + 18, (i + 1) * 50))

        for i in range(0, len(self.empty_board)):
            for j in range(0, len(self.empty_board[0])):
                if self.empty_board[i][j]:
                    value = font.render(str(self.empty_board[i][j]), True, BLUE)
                    self.window.blit(value, ((j + 1) * 50 + 18, (i + 1) * 50))

    def generate_board(self, difficulty=None):
        if difficulty is not None:
            self.difficulty = difficulty
        return self._generate_board(self.difficulty)
