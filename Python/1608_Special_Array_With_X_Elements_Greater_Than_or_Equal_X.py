# Author: Kaustav Ghosh
# Problem: 1608 - Special Array With X Elements Greater Than or Equal X
# Approach: Sort, binary search for valid x

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for x in range(n + 1):
            # count elements >= x
            import bisect
            count = n - bisect.bisect_left(nums, x)
            if count == x:
                return x
        return -1
