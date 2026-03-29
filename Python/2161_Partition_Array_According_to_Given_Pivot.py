# Author: Kaustav Ghosh
# Problem: 2161. Partition Array According to Given Pivot
# URL: https://leetcode.com/problems/partition-array-according-to-given-pivot/
# Difficulty: Medium

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        return less + equal + greater
