# Author: Kaustav Ghosh
# Problem: Cat and Mouse II
# Approach: Memoized minimax over (mouse, cat, turn). Each side slides 0..jump cells in a direction, stopping at walls. A turn cap stands in for "forever": if the mouse cannot win within it, repetition means it never will

from functools import lru_cache

class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        mouse = cat = food = None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'M':
                    mouse = (r, c)
                elif grid[r][c] == 'C':
                    cat = (r, c)
                elif grid[r][c] == 'F':
                    food = (r, c)

        limit = rows * cols * 2
        DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        @lru_cache(maxsize=None)
        def play(mp, cp, turn):
            if mp == cp:
                return False       # cat caught the mouse
            if mp == food:
                return True        # mouse reached the food
            if cp == food:
                return False       # cat is sitting on the food
            if turn >= limit:
                return False       # mouse is just stalling

            mouse_turn = turn % 2 == 0
            r, c = mp if mouse_turn else cp
            jump = mouseJump if mouse_turn else catJump

            for dr, dc in DIRS:
                for step in range(jump + 1):
                    nr, nc = r + dr * step, c + dc * step
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == '#':
                        break
                    if mouse_turn:
                        if play((nr, nc), cp, turn + 1):
                            return True
                    else:
                        if not play(mp, (nr, nc), turn + 1):
                            return False
            return not mouse_turn  # mouse exhausted its moves / cat couldn't force a win

        return play(mouse, cat, 0)
