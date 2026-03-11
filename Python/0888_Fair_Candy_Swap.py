# Find one candy from each person to swap so both have equal total.

# Author: Kaustav Ghosh

class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob_set = set(bobSizes)
        for a in aliceSizes:
            if a - diff in bob_set:
                return [a, a - diff]
