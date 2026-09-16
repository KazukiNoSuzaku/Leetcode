# Author: Kaustav Ghosh
# Problem: Number of Arithmetic Triplets
# Approach: The array is strictly increasing, so a triplet is fixed by its middle value: count the values x for which both x + diff and x + 2 * diff are present, using a set for lookups

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        present = set(nums)
        return sum(1 for x in nums if x + diff in present and x + 2 * diff in present)
