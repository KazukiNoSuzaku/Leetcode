# Author: Kaustav Ghosh
# Problem: Maximum Subarray Min-Product
# Approach: For each element treated as the subarray minimum, a monotonic stack finds the widest span where it stays the minimum; prefix sums give that span's total, and min * total is a candidate answer

class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        best = 0
        stack = []  # indices with increasing values
        for i in range(n + 1):
            val = nums[i] if i < n else -1  # sentinel below all values (>= 1)
            while stack and nums[stack[-1]] >= val:
                j = stack.pop()
                left = stack[-1] if stack else -1
                total = prefix[i] - prefix[left + 1]
                best = max(best, nums[j] * total)
            stack.append(i)

        return best % MOD
