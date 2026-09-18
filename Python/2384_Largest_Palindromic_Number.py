# Author: Kaustav Ghosh
# Problem: Largest Palindromic Number
# Approach: Build the left half greedily from the largest digits, using every available pair, and put the largest digit with an odd count left over in the middle. If the half consists only of zeros it would create leading zeros, so drop it; an empty result means the best is the single digit 0

from collections import Counter


class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        count = Counter(num)
        half = "".join(d * (count[d] // 2) for d in "9876543210").lstrip("0")
        middle = next((d for d in "9876543210" if count[d] % 2), "")
        return (half + middle + half[::-1]) or "0"
