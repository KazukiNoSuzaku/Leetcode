# Author: Kaustav Ghosh
# Problem: Two Out of Three
# Approach: Deduplicate each array to sets, count in how many sets each value appears, and return values seen in at least two

from collections import Counter

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        counts = Counter()
        for arr in (set(nums1), set(nums2), set(nums3)):
            for v in arr:
                counts[v] += 1
        return [v for v, c in counts.items() if c >= 2]
