class Solution:
    def colorRed(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1, 1]]
        # Minimum connected set covering all rows:
        # (1,1) -> (2,2) -> (2,1) -> (3,2) -> (3,1) -> (4,2) -> ...
        # Each pair (i,2),(i,1) for i in 2..n-1, plus (n,2) as endpoint
        ans = [[1, 1], [2, 2]]
        for i in range(2, n):
            ans.append([i, 1])
        for i in range(3, n + 1):
            ans.append([i, 2])
        return sorted(ans)
