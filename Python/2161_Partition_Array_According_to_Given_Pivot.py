# Author: Kaustav Ghosh
# Problem: Partition Array According to Given Pivot
# Approach: Make one pass collecting elements less than, equal to, and greater than the pivot into three lists preserving order, then concatenate

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less, equal, greater = [], [], []
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return less + equal + greater
