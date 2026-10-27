# Author: Kaustav Ghosh
# Problem: Ways to Split Array Into Three Subarrays
# Approach: Fixing where the first part ends turns both conditions into bounds on the second cut rather than a search: the middle part must total at least the first, which forces the running sum at the second cut to be at least twice the first part's, and the middle must not exceed the last, which caps that running sum at the midpoint of the first part's total and the whole array's. Because the values are non-negative the running sums never decrease, so those two bounds are found by binary search and every second cut between them is valid, contributing a whole block of answers at once. The cut must also leave a non-empty third part, which is what limits the search range.

from bisect import bisect_left, bisect_right
from itertools import accumulate


class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        running = list(accumulate(nums))
        total = running[-1]
        answer = 0
        for i in range(n - 2):
            first = running[i]
            # Middle at least as big as the first part.
            low = bisect_left(running, first * 2, i + 1, n - 1)
            # Middle no bigger than the last part.
            high = bisect_right(running, (total + first) // 2, low, n - 1)
            answer += high - low
        return answer % MOD
