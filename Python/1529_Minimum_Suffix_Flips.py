# Author: Kaustav Ghosh
# Problem: Minimum Suffix Flips
# Approach: Each operation flips a suffix, so scanning left to right the current character is settled only when it already matches what the flips so far produced. Every mismatch forces exactly one flip from that point onward, so the answer counts the changes along the string starting from all zeros

class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        flips = 0
        current = '0'
        for ch in target:
            if ch != current:
                flips += 1
                current = ch
        return flips
