# Author: Kaustav Ghosh
# Problem: Append K Integers With Minimal Sum
# Approach: The minimal set is the k smallest positive integers not already present. Sort the unique values and walk the gaps between consecutive present values; in each gap take as many of the smallest missing integers as still needed, summing consecutive ranges in closed form. If integers remain after the last value, take them from just above it

class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def range_sum(lo, cnt):
            # sum of cnt consecutive integers starting at lo
            return cnt * lo + cnt * (cnt - 1) // 2

        total = 0
        prev = 0
        for num in sorted(set(nums)):
            if k == 0:
                break
            gap = num - prev - 1
            if gap > 0:
                take = min(gap, k)
                total += range_sum(prev + 1, take)
                k -= take
            prev = num
        if k > 0:
            total += range_sum(prev + 1, k)
        return total
