# Author: Kaustav Ghosh
# Problem: Sort the Jumbled Numbers
# Approach: For each number, map its decimal digits through the mapping array to get its "jumbled" value, then stable-sort the original numbers by that value using Python's stable sort (preserving original order on ties)

class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def mapped(x):
            return int("".join(str(mapping[int(d)]) for d in str(x)))

        return sorted(nums, key=mapped)
