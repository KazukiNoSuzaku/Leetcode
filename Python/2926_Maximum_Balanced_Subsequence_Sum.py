from typing import List

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        # Transform: condition nums[j]-j >= nums[i]-i becomes non-decreasing in b[i]=nums[i]-i
        b = [nums[i] - i for i in range(n)]
        sorted_b = sorted(set(b))
        rank = {v: i + 1 for i, v in enumerate(sorted_b)}
        m = len(sorted_b)
        bit = [float('-inf')] * (m + 2)

        def update(pos, val):
            while pos <= m:
                if val > bit[pos]:
                    bit[pos] = val
                pos += pos & -pos

        def query(pos):
            res = float('-inf')
            while pos > 0:
                if bit[pos] > res:
                    res = bit[pos]
                pos -= pos & -pos
            return res

        ans = float('-inf')
        for i in range(n):
            r = rank[b[i]]
            best = query(r)
            dp_i = nums[i] + max(0, best)
            ans = max(ans, dp_i)
            update(r, dp_i)
        return ans
