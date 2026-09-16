# Author: Kaustav Ghosh
# Problem: Minimum Replacements to Sort the Array
# Approach: Work right to left keeping the largest value the next element may end with. Splitting nums[i] into p parts costs p - 1 operations and needs ceil(nums[i] / p) <= limit, so take the smallest such p; spreading the value evenly then leaves nums[i] // p as the biggest possible new limit for the element to the left

class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        limit = nums[-1]
        ops = 0
        for x in reversed(nums[:-1]):
            parts = (x + limit - 1) // limit
            ops += parts - 1
            limit = x // parts
        return ops
