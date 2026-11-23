# Author: Kaustav Ghosh
# Problem: Count Number of Pairs With Absolute Difference K
# Approach: Taking the absolute difference means each qualifying pair has a smaller and a larger member differing by exactly the given gap, so counting pairs reduces to counting, for every value present, how many copies of that value and how many copies of the value a gap above it exist. Tallying the values once and then multiplying those two counts for each distinct value visits every pair exactly once, because each pair is attributed only to its smaller member and never counted again from the larger side.

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        counts = Counter(nums)
        return sum(count * counts[value + k] for value, count in counts.items())
