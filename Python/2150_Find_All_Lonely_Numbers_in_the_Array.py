# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

from collections import Counter

class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        result = []
        for num in nums:
            if count[num] == 1 and (num - 1) not in count and (num + 1) not in count:
                result.append(num)
        return result
