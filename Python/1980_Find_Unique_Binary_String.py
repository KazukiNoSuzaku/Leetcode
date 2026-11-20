# Author: Kaustav Ghosh
# Problem: Find Unique Binary String
# Approach: There are n strings of length n but 2^n possible strings, so a missing one always exists, and Cantor's diagonal argument finds one without any searching: take the i-th character of the i-th given string and flip it. The string built that way differs from the i-th input at position i for every i, so it cannot equal any of them, and no comparison between candidates and inputs is ever needed. That reads exactly one character per input, giving O(n) time and an answer that is correct by construction rather than by verification.

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        return "".join('1' if word[index] == '0' else '0'
                       for index, word in enumerate(nums))
