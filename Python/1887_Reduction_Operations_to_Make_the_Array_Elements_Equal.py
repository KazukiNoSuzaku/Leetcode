# Author: Kaustav Ghosh
# Problem: Reduction Operations to Make the Array Elements Equal
# Approach: Each operation takes every copy of the current largest value down to the next largest, so an element ends up being lowered once for every distinct value below it; its own value never matters, only its rank among the distinct values. Sorting and walking upwards keeps that rank as a running count of the distinct values passed so far, and adding it for every element totals the operations without simulating any of them.

class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered = sorted(nums)
        operations = 0
        rank = 0
        for index in range(1, len(ordered)):
            if ordered[index] != ordered[index - 1]:
                rank += 1
            operations += rank
        return operations
