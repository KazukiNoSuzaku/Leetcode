# Author: Kaustav Ghosh
# Problem: Concatenation of Array
# Approach: The answer is the array followed by itself, which list concatenation produces directly; building a new list rather than extending the original leaves the caller's array untouched.

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums
