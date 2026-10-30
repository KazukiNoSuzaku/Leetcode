# Author: Kaustav Ghosh
# Problem: Closest Subsequence Sum
# Approach: Forty elements is far too many to enumerate every subset, but splitting the array in half brings each side down to around a million subsets, which is affordable. Any subsequence of the whole array is a subset of the first half together with a subset of the second, so after listing both sides' sums the task becomes pairing one from each to land nearest the goal. Sorting the second side lets each first-side sum binary search for its best partner, and the candidates worth checking are only the two straddling the shortfall, since the sorted order means anything further away is worse. The subset sums themselves are built by repeated doubling rather than by recursion.

from bisect import bisect_left


class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        middle = len(nums) // 2

        def subset_sums(part):
            totals = [0]
            for value in part:
                totals += [total + value for total in totals]
            return totals

        left = subset_sums(nums[:middle])
        right = sorted(subset_sums(nums[middle:]))
        limit = len(right)

        best = abs(goal)
        for total in left:
            shortfall = goal - total
            at = bisect_left(right, shortfall)
            if at < limit:
                gap = abs(total + right[at] - goal)
                if gap < best:
                    best = gap
                    if best == 0:
                        return 0
            if at:
                gap = abs(total + right[at - 1] - goal)
                if gap < best:
                    best = gap
                    if best == 0:
                        return 0
        return best
