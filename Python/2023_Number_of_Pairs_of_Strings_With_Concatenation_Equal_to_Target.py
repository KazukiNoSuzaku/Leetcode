# Author: Kaustav Ghosh
# Problem: Number of Pairs of Strings With Concatenation Equal to Target
# Approach: For each split of target into prefix + suffix, an ordered pair (i, j) works when nums[i] equals the prefix and nums[j] the suffix. Count prefix and suffix matches per split, subtracting pairs that reuse one index

from collections import Counter

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        count = Counter(nums)
        total = 0
        for split in range(1, len(target)):
            prefix = target[:split]
            suffix = target[split:]
            pairs = count[prefix] * count[suffix]
            if prefix == suffix:
                pairs -= count[prefix]   # cannot pair an index with itself
            total += pairs
        return total
