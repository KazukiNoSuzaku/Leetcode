# Author: Kaustav Ghosh
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result
