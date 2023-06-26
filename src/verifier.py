from typing import List

class Verifier:

    @staticmethod
    def verify(board: List[List[int]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for j in range(3)] for i in range(3)]

        for i in range(9):
            for j in range(9):
                cell_value = board[i][j]
                if cell_value in rows[i] or cell_value in cols[j] or cell_value in boxes[i // 3][j // 3]:
                    raise Exception('board is not valid!')
                rows[i].add(cell_value)
                cols[j].add(cell_value)
                boxes[i // 3][j // 3].add(cell_value)