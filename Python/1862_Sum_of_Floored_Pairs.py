# Author: Kaustav Ghosh
# Problem: Sum of Floored Pairs
# Approach: For each divisor d present, every quotient value q contributes q to all numerator elements in [q*d, q*d + d). A prefix-count array lets us tally, per d, how many numerators land in each band in near O(max log max)

class Solution(object):
    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        top = max(nums)

        count = [0] * (top + 1)
        for x in nums:
            count[x] += 1
        # prefix[v] = how many numbers are <= v
        prefix = [0] * (top + 2)
        for v in range(1, top + 1):
            prefix[v] = prefix[v - 1] + count[v]
        prefix[top + 1] = prefix[top]

        total = 0
        for d in range(1, top + 1):
            if count[d] == 0:
                continue
            q = 1
            while q * d <= top:
                lo = q * d
                hi = min((q + 1) * d - 1, top)
                # numbers in [lo, hi] floor-divide by d to q
                band = prefix[hi] - prefix[lo - 1]
                total += count[d] * q * band
                q += 1
            total %= MOD

        return total % MOD
