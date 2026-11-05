# Author: Kaustav Ghosh
# Problem: Sign of the Product of an Array
# Approach: The product's magnitude is irrelevant, so nothing has to be multiplied: a single zero anywhere makes the product zero, and otherwise the sign is decided purely by whether the count of negative values is even or odd. One pass therefore answers it, which also sidesteps the thousand-term product that a literal reading would build.

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negatives = 0
        for value in nums:
            if value == 0:
                return 0
            if value < 0:
                negatives += 1
        return -1 if negatives % 2 else 1
