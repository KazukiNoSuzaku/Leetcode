# Author: Kaustav Ghosh
# Problem 2006: Count Number of Pairs With Absolute Difference K

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        result = 0
        for num in count:
            if num + k in count:
                result += count[num] * count[num + k]
        return result
