# Author: Kaustav Ghosh
# Problem: Find Unique Binary String
# Approach: Cantor diagonalization - build a string whose i-th bit is the flip of the i-th bit of the i-th input string. It differs from every input in at least one position, so it cannot be in the list

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))
