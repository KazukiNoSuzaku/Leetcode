# Author: Kaustav Ghosh
# Problem: Partition Array Such That Maximum Difference Is K
# Approach: Order does not matter for subsequences, so sort. Greedily open a group anchored at the smallest unassigned value and absorb everything within k of it; start a new group at the first value that exceeds anchor+k. Count the groups

class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        groups = 0
        anchor = None
        for x in nums:
            if anchor is None or x - anchor > k:
                groups += 1
                anchor = x
        return groups
