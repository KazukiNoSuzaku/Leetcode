# Author: Kaustav Ghosh

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        return sum(k for k, v in count.items() if v == 1)
