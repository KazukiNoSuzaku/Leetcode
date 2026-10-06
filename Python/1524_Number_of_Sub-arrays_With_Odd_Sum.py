# Author: Kaustav Ghosh
# Problem: Number of Sub-arrays With Odd Sum
# Approach: A subarray's sum is odd exactly when the two prefix sums bounding it have different parities, so sweep the prefixes tracking how many even and how many odd ones have appeared, and add the opposite count at each step. The empty prefix counts as even

class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        even, odd = 1, 0
        parity = 0
        total = 0
        for x in arr:
            parity ^= x & 1
            if parity:
                total += even
                odd += 1
            else:
                total += odd
                even += 1
        return total % (10 ** 9 + 7)
