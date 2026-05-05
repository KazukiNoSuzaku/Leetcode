class Solution:
    def cycleLengthQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        # Find LCA by repeatedly halving the larger node until both are equal.
        # Cycle length = steps taken + 1 (for the added edge).
        ans = []
        for a, b in queries:
            steps = 1
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                steps += 1
            ans.append(steps)
        return ans
