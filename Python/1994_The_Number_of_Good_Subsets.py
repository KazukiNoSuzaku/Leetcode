# Author: Kaustav Ghosh
# Problem: The Number of Good Subsets
# Approach: A good subset has a squarefree product, so only squarefree values 2..30 can participate and their prime sets must be pairwise disjoint. DP over a bitmask of the ten primes <=30, adding each distinct value (weighted by its multiplicity). The 1s multiply nothing, so every good subset can freely include any subset of them: multiply by 2^(count of 1s)

from collections import Counter

class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def mask_of(v):
            m = 0
            for i, p in enumerate(primes):
                if v % p == 0:
                    if v % (p * p) == 0:      # square factor -> not usable
                        return -1
                    m |= 1 << i
            return m

        count = Counter(nums)
        dp = [0] * (1 << len(primes))
        dp[0] = 1
        for v in range(2, 31):
            if v not in count:
                continue
            vmask = mask_of(v)
            if vmask == -1:
                continue
            c = count[v]
            new_dp = dp[:]
            for mask in range(len(dp)):
                if dp[mask] and (mask & vmask) == 0:
                    new_dp[mask | vmask] = (new_dp[mask | vmask] + dp[mask] * c) % MOD
            dp = new_dp

        good = sum(dp[1:]) % MOD
        good = good * pow(2, count[1], MOD) % MOD
        return good
