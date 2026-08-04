# Author: Kaustav Ghosh
# Problem: Concatenation of Array
# Approach: The answer is nums followed by nums again

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums
