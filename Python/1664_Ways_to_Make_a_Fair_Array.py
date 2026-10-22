# Author: Kaustav Ghosh
# Problem: Ways to Make a Fair Array
# Approach: Removing an index leaves everything before it where it was and shifts everything after it one place left, which flips the parity of every later position, so the two sums after a removal are the even-indexed prefix plus the odd-indexed suffix, and the odd-indexed prefix plus the even-indexed suffix. Both pairs of running totals can be maintained as the removal point sweeps right, with each element moving from the suffix side to the prefix side exactly once, so every candidate index is tested in a single pass rather than by rebuilding the array.

class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_after = sum(nums[0::2])
        odd_after = sum(nums[1::2])
        even_before = 0
        odd_before = 0
        fair = 0
        for i, value in enumerate(nums):
            # Take this element out of the suffix totals before testing it.
            if i % 2 == 0:
                even_after -= value
            else:
                odd_after -= value
            # Positions after i change parity, so the sides cross over.
            if even_before + odd_after == odd_before + even_after:
                fair += 1
            if i % 2 == 0:
                even_before += value
            else:
                odd_before += value
        return fair
