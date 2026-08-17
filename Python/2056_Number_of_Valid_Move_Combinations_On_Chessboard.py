# Author: Kaustav Ghosh
# Problem: Number of Valid Move Combinations On Chessboard
# Approach: For each piece enumerate every move as a timed path (position at each second, holding at the destination). A combination is valid if no two pieces share a square at the same second. DFS assigns one move per piece, checking pairwise collisions incrementally

class Solution(object):
    def countCombinations(self, pieces, positions):
        """
        :type pieces: List[str]
        :type positions: List[List[int]]
        :rtype: int
        """
        DIRS = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)],
        }
        T = 8  # max seconds needed (board side)

        def moves_for(piece, r, c):
            paths = []
            # stay in place
            paths.append(tuple((r, c) for _ in range(T)))
            for dr, dc in DIRS[piece]:
                dist = 1
                while 1 <= r + dr * dist <= 8 and 1 <= c + dc * dist <= 8:
                    path = []
                    for t in range(T):
                        step = min(t, dist)
                        path.append((r + dr * step, c + dc * step))
                    paths.append(tuple(path))
                    dist += 1
            return paths

        all_moves = [moves_for(pieces[i], positions[i][0], positions[i][1])
                     for i in range(len(pieces))]

        def collide(p1, p2):
            return any(p1[t] == p2[t] for t in range(T))

        n = len(pieces)
        self_count = [0]

        def dfs(i, chosen):
            if i == n:
                self_count[0] += 1
                return
            for path in all_moves[i]:
                if all(not collide(path, prev) for prev in chosen):
                    chosen.append(path)
                    dfs(i + 1, chosen)
                    chosen.pop()

        dfs(0, [])
        return self_count[0]
