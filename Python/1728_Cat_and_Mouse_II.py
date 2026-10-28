# Author: Kaustav Ghosh
# Problem: Cat and Mouse II
# Approach: The outcome depends on both animals' positions and on whose turn it is, and since the mouse loses if it cannot win promptly, the turn count has to be part of the state with a cap beyond which the cat is declared the winner. The table is filled backwards from that cap, so each state only ever reads states one turn later and no recursion or memo dictionary is needed: on the mouse's turn the mouse wins if any jump leads to a winning state, and on the cat's turn the mouse wins only if every jump still leads to one. The immediate outcomes, mouse on the food, cat on the food, or the two sharing a cell, short-circuit before any move is considered. Jumps may pass over floor but not through walls, so the reachable cells are precomputed per position by walking outward and stopping at the first wall.

class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        cells = rows * cols
        walls = set()
        mouse_start = cat_start = food = -1
        for r in range(rows):
            for c in range(cols):
                ch = grid[r][c]
                index = r * cols + c
                if ch == '#':
                    walls.add(index)
                elif ch == 'M':
                    mouse_start = index
                elif ch == 'C':
                    cat_start = index
                elif ch == 'F':
                    food = index
        open_cells = [i for i in range(cells) if i not in walls]

        def reach(jump):
            table = [[] for _ in range(cells)]
            for index in open_cells:
                r, c = divmod(index, cols)
                spots = [index]
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    for step in range(1, jump + 1):
                        nr, nc = r + dr * step, c + dc * step
                        if not (0 <= nr < rows and 0 <= nc < cols):
                            break
                        target = nr * cols + nc
                        if target in walls:
                            break
                        spots.append(target)
                table[index] = spots
            return table

        mouse_moves = reach(mouseJump)
        cat_moves = reach(catJump)

        limit = cells * 2
        later = [False] * (cells * cells)      # past the cap the cat wins
        for turn in range(limit - 1, -1, -1):
            now = [False] * (cells * cells)
            mouse_to_move = turn % 2 == 0
            for mouse in open_cells:
                base = mouse * cells
                for cat in open_cells:
                    if mouse == food:
                        now[base + cat] = True
                        continue
                    if cat == food or cat == mouse:
                        continue
                    if mouse_to_move:
                        for nextMouse in mouse_moves[mouse]:
                            if later[nextMouse * cells + cat]:
                                now[base + cat] = True
                                break
                    else:
                        survives = True
                        for nextCat in cat_moves[cat]:
                            if not later[base + nextCat]:
                                survives = False
                                break
                        now[base + cat] = survives
            later = now
        return later[mouse_start * cells + cat_start]
