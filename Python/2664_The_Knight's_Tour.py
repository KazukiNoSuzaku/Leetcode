class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> list[list[int]]:
        MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]
        board = [[-1] * n for _ in range(m)]

        def degree(x, y):
            return sum(
                1 for dx, dy in MOVES
                if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == -1
            )

        board[r][c] = 0
        x, y = r, c
        for step in range(1, m * n):
            candidates = sorted(
                ((degree(x + dx, y + dy), x + dx, y + dy)
                 for dx, dy in MOVES
                 if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == -1)
            )
            _, x, y = candidates[0]
            board[x][y] = step

        return board
