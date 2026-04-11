# Author: Kaustav Ghosh
# Problem: 2281. Sum of Total Strength of Wizards
# URL: https://leetcode.com/problems/sum-of-total-strength-of-wizards/
# Difficulty: Hard
#
# Approach:
# For each element as the minimum, find the range [left, right) where it is min
# using monotonic stack. Use prefix sum of prefix sums to compute the sum of all
# subarray sums in that range efficiently.

class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(strength)

        # Find previous less or equal and next less using monotonic stack
        left = [-1] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD

        # Prefix sum of prefix sum
        pp = [0] * (n + 2)
        for i in range(n + 1):
            pp[i + 1] = (pp[i] + prefix[i]) % MOD

        result = 0
        for i in range(n):
            l = left[i]
            r = right[i]
            # Sum of subarrays where strength[i] is minimum
            # left_count = i - l, right_count = r - i
            left_sum = (pp[i + 1] - pp[l + 1]) * (r - i) % MOD
            right_sum = (pp[r + 1] - pp[i + 1]) * (i - l) % MOD
            result = (result + strength[i] * (right_sum - left_sum)) % MOD

        return result % MOD
