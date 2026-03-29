# Author: Kaustav Ghosh
# Problem: 2170. Minimum Operations to Make Array Alternating
# URL: https://leetcode.com/problems/minimum-operations-to-make-array-alternating/
# Difficulty: Medium

from collections import Counter

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        def top2(counter):
            # Returns (val1, cnt1, val2, cnt2) for top 2 frequencies
            items = counter.most_common(2)
            if len(items) == 1:
                return items[0][0], items[0][1], -1, 0
            return items[0][0], items[0][1], items[1][0], items[1][1]

        even_cnt = Counter(nums[0::2])
        odd_cnt = Counter(nums[1::2])

        ev1, ec1, ev2, ec2 = top2(even_cnt)
        ov1, oc1, ov2, oc2 = top2(odd_cnt)

        even_total = len(nums[0::2])
        odd_total = len(nums[1::2])

        # If top even and top odd values differ, use both top frequencies
        if ev1 != ov1:
            return n - ec1 - oc1
        else:
            # Must use second best for one of them
            opt1 = n - ec1 - oc2  # keep top even, use 2nd odd
            opt2 = n - ec2 - oc1  # use 2nd even, keep top odd
            return min(opt1, opt2)
