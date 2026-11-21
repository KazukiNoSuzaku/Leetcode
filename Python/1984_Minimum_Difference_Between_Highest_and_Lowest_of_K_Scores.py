# Author: Kaustav Ghosh
# Problem: Minimum Difference Between Highest and Lowest of K Scores
# Approach: Only the largest and smallest of the chosen scores matter, so for any choice of k scores the spread can only shrink by replacing an extreme with something between the two; that means an optimal choice is k scores that are consecutive in sorted order. Sorting and sliding a window of width k therefore covers every candidate, and the spread of a window is just its last element minus its first. Picking a single score, or k equal to the whole array, falls out of the same sweep with no special case. Sorting dominates at O(n log n).

class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ordered = sorted(nums)
        best = None
        for start in range(len(ordered) - k + 1):
            spread = ordered[start + k - 1] - ordered[start]
            if best is None or spread < best:
                best = spread
        return best
