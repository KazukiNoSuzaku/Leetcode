# Author: Kaustav Ghosh
# 2342. Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
# Difficulty: Medium
#
# Group numbers by digit sum, track top-2 per group, answer is max(top1 + top2)

from collections import defaultdict

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        groups = defaultdict(list)
        for num in nums:
            groups[digit_sum(num)].append(num)

        ans = -1
        for vals in groups.values():
            if len(vals) >= 2:
                vals.sort(reverse=True)
                ans = max(ans, vals[0] + vals[1])
        return ans
