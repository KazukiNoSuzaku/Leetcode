# Author: Kaustav Ghosh
# Problem: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
# Approach: Sweep the prefix sums keeping the set of those seen since the last cut. The moment the current prefix minus target is in that set, a qualifying subarray ends here, so take it and clear the set: closing a subarray as early as possible leaves the most room for later ones

class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seen = {0}
        running = 0
        count = 0
        for x in nums:
            running += x
            if running - target in seen:
                count += 1
                seen = {0}
                running = 0
            else:
                seen.add(running)
        return count
