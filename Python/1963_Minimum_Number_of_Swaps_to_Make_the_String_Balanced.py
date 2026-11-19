# Author: Kaustav Ghosh
# Problem: Minimum Number of Swaps to Make the String Balanced
# Approach: Scanning left to right and cancelling every closing bracket against a pending opening one leaves behind some number of unmatched closing brackets; since the counts of the two bracket types are equal, exactly that many opening brackets are left unmatched at the end, and the string is balanced precisely when that number is zero. One swap can take a leading unmatched closer and a trailing unmatched opener and fix two of each at once, so the answer is half the leftover count rounded up, the rounding covering the case of a single leftover pair in the middle. Tracking the leftover count needs just a running counter over one pass, so the million-character limit is handled in O(n) time and constant space.

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        pending = 0
        unmatched = 0
        for bracket in s:
            if bracket == '[':
                pending += 1
            elif pending:
                pending -= 1
            else:
                unmatched += 1
        return (unmatched + 1) // 2
