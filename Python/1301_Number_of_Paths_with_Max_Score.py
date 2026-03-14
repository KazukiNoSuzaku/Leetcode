# Given a board, find the maximum score path from bottom-right to top-left
# and the number of such paths (mod 1e9+7).

# Author: Kaustav Ghosh

class Solution(object):
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] in ('S', 'E') and (i, j) != (n-1, n-1):
                    continue
                if dp[i][j][1] == 0:
                    continue
                val = int(board[i][j]) if board[i][j].isdigit() else 0
                for di, dj in [(-1,0),(0,-1),(-1,-1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != 'X':
                        new_score = dp[i][j][0] + (int(board[ni][nj]) if board[ni][nj].isdigit() else 0)
                        cur_score, cur_cnt = dp[ni][nj]
                        if new_score > cur_score:
                            dp[ni][nj] = (new_score, dp[i][j][1] % MOD)
                        elif new_score == cur_score:
                            dp[ni][nj] = (cur_score, (cur_cnt + dp[i][j][1]) % MOD)
        score, cnt = dp[0][0]
        return [score, cnt] if cnt > 0 else [0, 0]
