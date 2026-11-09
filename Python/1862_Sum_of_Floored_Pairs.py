# Author: Kaustav Ghosh
# Problem: Sum of Floored Pairs
# Approach: For a fixed denominator the quotient is constant across a whole band of numerators: every value from q times d up to q times d plus d minus one floors to q. So instead of pairing numbers, each distinct denominator sweeps its multiples and counts how many values fall in each band, which a prefix-count array answers in one subtraction. Multiplying by how often that denominator itself occurs covers all its copies at once, and the total work is the harmonic sum over the value range rather than the square of the array length. The modulus is applied once at the end.

class Solution(object):
    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        largest = max(nums)

        occurrences = [0] * (largest + 1)
        for value in nums:
            occurrences[value] += 1
        upto = [0] * (largest + 2)
        for value in range(largest + 1):
            upto[value + 1] = upto[value] + occurrences[value]

        total = 0
        for divisor in range(1, largest + 1):
            if not occurrences[divisor]:
                continue
            contribution = 0
            quotient = 1
            low = divisor
            while low <= largest:
                high = min(largest, low + divisor - 1)
                contribution += quotient * (upto[high + 1] - upto[low])
                quotient += 1
                low += divisor
            total += occurrences[divisor] * contribution
        return total % MOD
