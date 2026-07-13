# Author: Kaustav Ghosh
# Problem: Ways to Split Array Into Three Subarrays
# Approach: Values are non-negative so prefix sums are sorted; for each first cut, binary search the range of second cuts satisfying left <= mid and mid <= right

from bisect import bisect_left, bisect_right

class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        total = prefix[n]

        ways = 0
        for i in range(1, n - 1):
            left = prefix[i]
            if left * 3 > total:  # left can never stay the smallest past here
                break
            # mid >= left  =>  prefix[j] >= 2*prefix[i]
            lo = bisect_left(prefix, 2 * left, i + 1, n)
            # mid <= right =>  prefix[j] <= (total + prefix[i]) // 2
            hi = bisect_right(prefix, (total + left) // 2, i + 1, n)
            ways += max(0, hi - lo)

        return ways % MOD
