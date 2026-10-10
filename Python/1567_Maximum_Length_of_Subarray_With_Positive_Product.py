# Author: Kaustav Ghosh
# Problem: Maximum Length of Subarray With Positive Product
# Approach: Only the sign matters, and a zero wipes the slate clean, so scanning left to right I keep two numbers: the length of the longest subarray ending here whose product is positive and the longest whose product is negative. A positive element extends both; a negative element swaps their roles, since a negative-product run becomes positive and vice versa, with the caveat that a zero-length negative run cannot be extended into a real one.

class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive = negative = 0
        best = 0
        for value in nums:
            if value == 0:
                positive = negative = 0
            elif value > 0:
                positive += 1
                negative = negative + 1 if negative else 0
            else:
                positive, negative = (negative + 1 if negative else 0), positive + 1
            if positive > best:
                best = positive
        return best
