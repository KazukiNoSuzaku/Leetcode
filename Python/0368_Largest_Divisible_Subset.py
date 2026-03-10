# Given a set of distinct positive integers nums, return the largest subset answer such
# that every pair (answer[i], answer[j]) of elements in this subset satisfies:
# answer[i] % answer[j] == 0, or answer[j] % answer[i] == 0.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,2]

# Example 2:
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.

# Author: Kaustav Ghosh

class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        best = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > dp[best]:
                best = i

        res = []
        idx = best
        while idx >= 0:
            res.append(nums[idx])
            idx = parent[idx]
        return res[::-1]
