# Author: Kaustav Ghosh
# Problem: Minimum Limit of Balls in a Bag
# Approach: Feasibility is monotonic in the penalty, so binary search it; splitting a bag of x balls down to size p costs ceil(x/p) - 1 == (x-1)//p operations

class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            operations = sum((x - 1) // mid for x in nums)
            if operations <= maxOperations:
                hi = mid
            else:
                lo = mid + 1
        return lo
