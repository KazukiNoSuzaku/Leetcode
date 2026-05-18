from bisect import bisect_left, bisect_right
from itertools import accumulate

class Solution:
    def minOperations(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        prefix = [0] + list(accumulate(nums))
        result = []
        for q in queries:
            lo = bisect_left(nums, q)
            hi = bisect_right(nums, q)
            below = q * lo - prefix[lo]
            above = (prefix[n] - prefix[hi]) - q * (n - hi)
            result.append(below + above)
        return result
