# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-unique-binary-string/

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        # Cantor's diagonal argument
        result = []
        for i in range(len(nums)):
            result.append('0' if nums[i][i] == '1' else '1')
        return ''.join(result)
