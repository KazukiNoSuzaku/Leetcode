# Author: Kaustav Ghosh
# Problem: Special Array With X Elements Greater Than or Equal X
# Approach: Sorting descending makes the count of elements that are at least some threshold readable straight off the prefix: after x elements, x is the right answer when those first x are all at least x while the next one is not, which is the only way the count can equal x exactly. Scanning x upward over the sorted array therefore settles it in one pass, and since the count of qualifying elements falls as x rises while x itself climbs, at most one x can ever work.

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered = sorted(nums, reverse=True)
        n = len(ordered)
        for x in range(1, n + 1):
            if ordered[x - 1] >= x and (x == n or ordered[x] < x):
                return x
        return -1
