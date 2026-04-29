class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        # Weighted median minimizes sum of weighted absolute deviations
        pairs = sorted(zip(nums, cost))
        total = sum(cost)
        acc = 0
        for val, c in pairs:
            acc += c
            if acc * 2 >= total:
                target = val
                break
        return sum(abs(v - target) * c for v, c in zip(nums, cost))
