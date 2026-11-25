# Author: Kaustav Ghosh
# Problem: Maximum Alternating Subarray Sum
# Approach: The sign a given element carries depends only on its distance from the subarray's start, so at each position it is enough to know the best alternating sum of a subarray ending there with that element added and the best with it subtracted. An element enters with a plus either by extending a subarray whose last element was subtracted or by starting a fresh subarray, whichever is better, while an element enters with a minus only by extending a subarray whose last element was added, since the first element of any subarray always carries a plus. Both quantities roll forward in constant space and the answer is the largest either ever reaches.

class Solution(object):
    def maximumAlternatingSubarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NONE = -(10 ** 18)
        added = NONE
        subtracted = NONE
        best = NONE
        for value in nums:
            extended = subtracted if subtracted > 0 else 0
            added, subtracted = extended + value, added - value
            if added > best:
                best = added
            if subtracted > best:
                best = subtracted
        return best
