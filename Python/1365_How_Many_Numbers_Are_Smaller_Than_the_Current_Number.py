# Author: Kaustav Ghosh
# Problem: How Many Numbers Are Smaller Than the Current Number
# Approach: Sort with index mapping or counting sort

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * 101
        for n in nums:
            count[n] += 1
        prefix = [0] * 101
        for i in range(1, 101):
            prefix[i] = prefix[i - 1] + count[i - 1]
        return [prefix[n] for n in nums]
