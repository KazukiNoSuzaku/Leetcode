# Author: Kaustav Ghosh
# Problem: Closest Subsequence Sum
# Approach: Meet in the middle - enumerate all subset sums of each half (2^20 each), sort one side, then binary search it for the best complement of every sum in the other

from bisect import bisect_left

class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def subset_sums(arr):
            sums = [0]
            for x in arr:
                sums += [s + x for s in sums]
            return sums

        half = len(nums) // 2
        left = subset_sums(nums[:half])
        right = sorted(subset_sums(nums[half:]))

        best = abs(goal)  # the empty subsequence
        for s in left:
            target = goal - s
            i = bisect_left(right, target)
            for idx in (i - 1, i):
                if 0 <= idx < len(right):
                    best = min(best, abs(s + right[idx] - goal))
                    if best == 0:
                        return 0
        return best
