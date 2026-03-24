# Author: Kaustav Ghosh
# Problem 2009: Minimum Number of Operations to Make Array Continuous

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        n = len(nums)
        unique = sorted(set(nums))
        result = n
        for i, start in enumerate(unique):
            end = start + n - 1
            # Count unique elements in [start, end]
            j = bisect.bisect_right(unique, end)
            count = j - i  # number of unique elements already in range
            result = min(result, n - count)
        return result
