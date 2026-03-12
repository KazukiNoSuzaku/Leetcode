# Author: Kaustav Ghosh
# Binary search on the mutation value to minimize |sum - target|

class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        def compute_sum(value):
            import bisect
            idx = bisect.bisect_right(arr, value)
            return prefix[idx] + value * (n - idx)

        lo, hi = 0, max(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if compute_sum(mid) < target:
                lo = mid + 1
            else:
                hi = mid

        # Check lo-1 and lo to find closest
        if lo > 0 and abs(compute_sum(lo - 1) - target) <= abs(compute_sum(lo) - target):
            return lo - 1
        return lo
