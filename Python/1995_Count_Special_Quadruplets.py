# Author: Kaustav Ghosh
# Problem: Count Special Quadruplets
# Approach: Rearranging the condition so that the two outer indices sit on one side turns the search into a pair-matching problem: the requirement that the first three values sum to the fourth is the same as the first two summing to the fourth minus the third. Sweeping the second index from right to left lets every pair whose third index is just past it be folded into a tally keyed by that difference, after which each candidate first index only has to look its own pair sum up in the tally. That gives a quadratic scan instead of the four nested loops the statement suggests.

class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        total = len(nums)
        differences = defaultdict(int)
        found = 0
        for second in range(total - 3, 0, -1):
            third = second + 1
            for fourth in range(third + 1, total):
                differences[nums[fourth] - nums[third]] += 1
            for first in range(second):
                found += differences[nums[first] + nums[second]]
        return found
