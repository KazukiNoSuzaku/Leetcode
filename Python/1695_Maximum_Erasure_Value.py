# Author: Kaustav Ghosh
# Problem: Maximum Erasure Value
# Approach: The subarray must be contiguous and free of repeats, and both properties behave well under a sliding window: extending the right end can only introduce a duplicate of the element just added, and advancing the left end past the earlier copy of it restores uniqueness. Keeping the window's membership in a set and its total as a running sum means each element is added and removed at most once, so the whole scan is linear and the best total is read off as the window moves.

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inside = set()
        running = 0
        best = 0
        left = 0
        for value in nums:
            while value in inside:
                inside.discard(nums[left])
                running -= nums[left]
                left += 1
            inside.add(value)
            running += value
            if running > best:
                best = running
        return best
