# Author: Kaustav Ghosh
# Problem: Number of Different Subsequences GCDs
# Approach: Rather than building subsequences, each candidate divisor is tested directly: a value g is the greatest common divisor of some subsequence exactly when the numbers in the array that are multiples of g have g as their own greatest common divisor, because taking all of them is the most favourable subsequence for g and any subset can only raise the result. So the array is turned into a membership table and, for every g up to the largest value, the multiples of g are folded together and compared with g. The work is the harmonic sum over the value range, far cheaper than examining subsequences, and the fold stops early once it has already reached g.

class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from math import gcd

        largest = max(nums)
        present = [False] * (largest + 1)
        for value in nums:
            present[value] = True

        found = 0
        for candidate in range(1, largest + 1):
            running = 0
            for multiple in range(candidate, largest + 1, candidate):
                if present[multiple]:
                    running = gcd(running, multiple)
                    if running == candidate:
                        break
            if running == candidate:
                found += 1
        return found
