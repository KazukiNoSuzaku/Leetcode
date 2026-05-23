from math import gcd

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones

        min_ops = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_ops = min(min_ops, j - i)
                    break

        return -1 if min_ops == float('inf') else min_ops + n - 1
