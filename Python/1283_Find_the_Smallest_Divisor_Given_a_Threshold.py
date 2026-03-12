# Author: Kaustav Ghosh
# Binary search on divisor value

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        import math
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            total = sum(int(math.ceil(n / float(mid))) for n in nums)
            if total <= threshold:
                hi = mid
            else:
                lo = mid + 1
        return lo
