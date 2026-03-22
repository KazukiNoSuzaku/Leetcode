# Author: Kaustav Ghosh
# https://leetcode.com/problems/cat-and-mouse-ii/

class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        mouse_start = cat_start = food = None

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'M':
                    mouse_start = (r, c)
                elif grid[r][c] == 'C':
                    cat_start = (r, c)
                elif grid[r][c] == 'F':
                    food = (r, c)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        MAX_TURNS = rows * cols * 2

        memo = {}

        def dp(mouse, cat, turn):
            if turn >= MAX_TURNS:
                return False
            if mouse == cat:
                return False
            if cat == food:
                return False
            if mouse == food:
                return True

            state = (mouse, cat, turn)
            if state in memo:
                return memo[state]

            mouse_turn = (turn % 2 == 0)

            if mouse_turn:
                # Mouse tries to win
                # Mouse can stay in place is not an option, must move
                for dr, dc in directions:
                    for jump in range(1, mouseJump + 1):
                        nr, nc = mouse[0] + dr * jump, mouse[1] + dc * jump
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            break
                        if grid[nr][nc] == '#':
                            break
                        if dp((nr, nc), cat, turn + 1):
                            memo[state] = True
                            return True
                memo[state] = False
                return False
            else:
                # Cat tries to prevent mouse from winning
                for dr, dc in directions:
                    for jump in range(1, catJump + 1):
                        nr, nc = cat[0] + dr * jump, cat[1] + dc * jump
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            break
                        if grid[nr][nc] == '#':
                            break
                        if not dp(mouse, (nr, nc), turn + 1):
                            memo[state] = False
                            return False
                memo[state] = True
                return True

        return dp(mouse_start, cat_start, 0)
