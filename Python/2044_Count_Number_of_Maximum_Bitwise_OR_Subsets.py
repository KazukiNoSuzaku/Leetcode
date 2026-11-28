# Author: Kaustav Ghosh
# Problem: Count Number of Maximum Bitwise-OR Subsets
# Approach: With at most sixteen numbers there are only sixty-odd thousand subsets, so every one can be examined, and the largest achievable combined value is simply the largest seen along the way. Recomputing a subset's combined value from scratch would repeat work, so each subset reuses the value of the same subset with its lowest member removed and folds that one member back in, which makes every subset cost a single operation. The running maximum and its tally are updated together, resetting the tally whenever a strictly larger value appears.

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        combined = [0] * (1 << total)
        best = 0
        found = 0
        for mask in range(1, 1 << total):
            lowest = mask & -mask
            index = lowest.bit_length() - 1
            value = combined[mask ^ lowest] | nums[index]
            combined[mask] = value
            if value > best:
                best = value
                found = 1
            elif value == best:
                found += 1
        return found
