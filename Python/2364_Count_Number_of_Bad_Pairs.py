# Author: Kaustav Ghosh
# Problem: Count Number of Bad Pairs
# Approach: A pair is good when j - i equals nums[j] - nums[i], which rearranges to nums[i] - i == nums[j] - j. Count how many earlier indices share the current value of nums[i] - i to total the good pairs, then subtract them from all n * (n - 1) / 2 pairs

from collections import Counter


class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = Counter()
        good = 0
        for i, x in enumerate(nums):
            good += seen[x - i]
            seen[x - i] += 1
        n = len(nums)
        return n * (n - 1) // 2 - good
