# Author: Kaustav Ghosh
# Problem: Largest Positive Integer That Exists With Its Negative
# Approach: Put every value in a set, then take the largest positive value whose negation is also present, falling back to -1 when no such pair exists

class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set(nums)
        return max((x for x in seen if x > 0 and -x in seen), default=-1)
