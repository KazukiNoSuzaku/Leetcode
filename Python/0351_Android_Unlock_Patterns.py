# Android devices have a special lock screen with a 3 x 3 grid of dots. A valid unlock pattern
# moves over at least m keys and at most n keys. Count the number of unique and valid unlock patterns.
# A line drawn between two dots must not pass over a third dot unless that dot has already been visited.

# Example 1:
# Input: m = 1, n = 1
# Output: 9

# Example 2:
# Input: m = 1, n = 2
# Output: 65

# Constraints:
# 1 <= m, n <= 9

# Author: Kaustav Ghosh

class Solution(object):
    def numberOfPatterns(self, m, n):
        # skip[i][j] = key that must be visited before going from i to j (0 if none)
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5

        visited = [False] * 10

        def dfs(cur, remaining):
            if remaining == 0:
                return 1
            visited[cur] = True
            count = 0
            for nxt in range(1, 10):
                s = skip[cur][nxt]
                if not visited[nxt] and (s == 0 or visited[s]):
                    count += dfs(nxt, remaining - 1)
            visited[cur] = False
            return count

        res = 0
        for length in range(m, n + 1):
            # 1,3,7,9 are symmetric; 2,4,6,8 are symmetric; 5 is unique
            res += dfs(1, length - 1) * 4
            res += dfs(2, length - 1) * 4
            res += dfs(5, length - 1)
        return res
