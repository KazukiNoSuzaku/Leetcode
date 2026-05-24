class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        ans = 0
        # Process pairs bottom-up (1-indexed nodes n//2 down to 1)
        for i in range(n // 2, 0, -1):
            left, right = 2 * i - 1, 2 * i  # 0-indexed children in cost[]
            ans += abs(cost[left] - cost[right])
            cost[i - 1] += max(cost[left], cost[right])
        return ans
