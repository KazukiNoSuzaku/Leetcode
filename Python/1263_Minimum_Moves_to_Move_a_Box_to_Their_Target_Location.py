# Author: Kaustav Ghosh
# BFS with state (box_row, box_col, player_row, player_col), 0-1 BFS

class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        # State: (box_r, box_c, player_r, player_c)
        start = (box[0], box[1], player[0], player[1])
        visited = {start}
        queue = deque([(start, 0)])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def can_reach(pr, pc, tr, tc, br, bc):
            """Check if player at (pr,pc) can reach (tr,tc) without going through box at (br,bc)"""
            if tr < 0 or tr >= m or tc < 0 or tc >= n or grid[tr][tc] == '#':
                return False
            seen = {(pr, pc)}
            q = deque([(pr, pc)])
            while q:
                r, c = q.popleft()
                if r == tr and c == tc:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] != '#' and (nr, nc) != (br, bc):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return False

        while queue:
            (br, bc, pr, pc), pushes = queue.popleft()
            if (br, bc) == target:
                return pushes
            for dr, dc in dirs:
                # Player needs to be on opposite side of box
                player_needed = (br - dr, bc - dc)
                new_box = (br + dr, bc + dc)
                if new_box[0] < 0 or new_box[0] >= m or new_box[1] < 0 or new_box[1] >= n:
                    continue
                if grid[new_box[0]][new_box[1]] == '#':
                    continue
                if not can_reach(pr, pc, player_needed[0], player_needed[1], br, bc):
                    continue
                state = (new_box[0], new_box[1], br, bc)
                if state not in visited:
                    visited.add(state)
                    queue.append((state, pushes + 1))
        return -1
