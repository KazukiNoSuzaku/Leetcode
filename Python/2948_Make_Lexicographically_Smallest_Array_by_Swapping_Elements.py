from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[order[j]] - nums[order[j - 1]] <= limit:
                j += 1
            # values within a group are mutually reachable; put them in
            # ascending order at the group's indices in ascending order
            for idx, pos in zip(range(i, j), sorted(order[i:j])):
                ans[pos] = nums[order[idx]]
            i = j
        return ans
