# Author: Kaustav Ghosh
# Track rows, cols, diags for each player, check for winner

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        rows = [[0, 0] for _ in range(3)]
        cols = [[0, 0] for _ in range(3)]
        diag = [0, 0]
        anti_diag = [0, 0]

        for i, (r, c) in enumerate(moves):
            player = i % 2
            rows[r][player] += 1
            cols[c][player] += 1
            if r == c:
                diag[player] += 1
            if r + c == 2:
                anti_diag[player] += 1

            if rows[r][player] == 3 or cols[c][player] == 3 or \
               diag[player] == 3 or anti_diag[player] == 3:
                return "A" if player == 0 else "B"

        return "Draw" if len(moves) == 9 else "Pending"
