# Author: Kaustav Ghosh
# Problem 2056: Number of Valid Move Combinations On Chessboard

class Solution(object):
    def countCombinations(self, pieces, positions):
        """
        :type pieces: List[str]
        :type positions: List[List[int]]
        :rtype: int
        """
        directions = {
            'rook': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'queen': [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        }
        n = len(pieces)

        def get_moves(piece, pos):
            """Get all possible (direction, steps) including staying."""
            r, c = pos
            moves = [(0, 0, 0)]  # stay: dr=0, dc=0, steps=0
            for dr, dc in directions[piece]:
                for steps in range(1, 8):
                    nr, nc = r + steps * dr, c + steps * dc
                    if 1 <= nr <= 8 and 1 <= nc <= 8:
                        moves.append((dr, dc, steps))
                    else:
                        break
            return moves

        all_moves = []
        for i in range(n):
            all_moves.append(get_moves(pieces[i], positions[i]))

        count = [0]

        def backtrack(idx, chosen):
            if idx == n:
                # Check if all moves are valid (no collisions at any time)
                if valid(chosen):
                    count[0] += 1
                return
            for move in all_moves[idx]:
                chosen.append(move)
                backtrack(idx + 1, chosen)
                chosen.pop()

        def valid(chosen):
            max_steps = max(c[2] for c in chosen) if chosen else 0
            for t in range(max_steps + 1):
                occupied = set()
                for i in range(n):
                    dr, dc, steps = chosen[i]
                    r, c = positions[i]
                    s = min(t, steps)
                    pos = (r + s * dr, c + s * dc)
                    if pos in occupied:
                        return False
                    occupied.add(pos)
            return True

        backtrack(0, [])
        return count[0]
