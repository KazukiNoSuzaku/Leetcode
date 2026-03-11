# Find the longest distance between two consecutive 1s in binary representation of n.

# Author: Kaustav Ghosh

class Solution(object):
    def binaryGap(self, n):
        bits = bin(n)[2:]
        positions = [i for i, b in enumerate(bits) if b == '1']
        return max(positions[i+1] - positions[i] for i in range(len(positions)-1)) if len(positions) > 1 else 0
