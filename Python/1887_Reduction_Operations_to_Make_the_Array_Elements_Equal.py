# Author: Kaustav Ghosh
# Problem: Reduction Operations to Make the Array Elements Equal
# Approach: Sort descending; each element above the minimum needs as many operations as the number of distinct larger values, which is its rank among the distinct values

class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        operations = 0
        rank = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                rank += 1
            operations += rank
        return operations
