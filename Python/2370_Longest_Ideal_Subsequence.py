# Author: Kaustav Ghosh
# Problem: Longest Ideal Subsequence
# Approach: Keep, for each of the 26 letters, the longest ideal subsequence seen so far that ends with it. A new character can extend only those ending within k places of it in the alphabet, so take the best over that window and add one

class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        best = [0] * 26
        for ch in s:
            c = ord(ch) - ord('a')
            lo = max(0, c - k)
            hi = min(25, c + k)
            best[c] = max(best[lo:hi + 1]) + 1
        return max(best)
