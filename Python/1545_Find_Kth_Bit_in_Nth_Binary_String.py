# Author: Kaustav Ghosh
# Problem: Find Kth Bit in Nth Binary String
# Approach: Each string is the previous one, then a '1', then the previous one reversed and inverted, so never build it. If k is the middle it is that '1'; before the middle the answer comes straight from the previous string; past it, mirror k to the matching position in the previous string and flip the bit

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "0"
        length = (1 << n) - 1
        middle = length // 2 + 1
        if k == middle:
            return "1"
        if k < middle:
            return self.findKthBit(n - 1, k)
        mirrored = self.findKthBit(n - 1, length - k + 1)
        return "1" if mirrored == "0" else "0"
