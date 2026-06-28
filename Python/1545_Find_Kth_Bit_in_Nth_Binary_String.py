# Author: Kaustav Ghosh
# Problem: Find Kth Bit in Nth Binary String
# Approach: Recurse on the self-similar structure; the middle bit is '1', the left half mirrors Sn-1, the right half is the reversed-inverted left half

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
        mid = (length + 1) // 2
        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)
        # right half: take the mirrored position in Sn-1 and invert it
        bit = self.findKthBit(n - 1, length - k + 1)
        return "1" if bit == "0" else "0"
