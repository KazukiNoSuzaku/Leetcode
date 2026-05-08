import bisect

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        # Binary search for the boundaries of the zero block; return max(negatives, positives).
        neg = bisect.bisect_left(nums, 0)
        pos = len(nums) - bisect.bisect_right(nums, 0)
        return max(neg, pos)
