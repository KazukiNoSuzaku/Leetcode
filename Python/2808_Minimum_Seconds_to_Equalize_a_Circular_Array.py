from collections import defaultdict

class Solution:
    def minimumSeconds(self, nums: list[int]) -> int:
        n = len(nums)
        positions = defaultdict(list)
        for i, x in enumerate(nums):
            positions[x].append(i)
        ans = n
        for pos in positions.values():
            max_gap = pos[0] + n - pos[-1]
            for i in range(1, len(pos)):
                max_gap = max(max_gap, pos[i] - pos[i - 1])
            ans = min(ans, max_gap // 2)
        return ans
