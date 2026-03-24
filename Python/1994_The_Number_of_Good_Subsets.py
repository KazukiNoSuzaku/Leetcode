# Author: Kaustav Ghosh
# Problem 1994: The Number of Good Subsets

class Solution(object):
    def numberOfGoodSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_idx = {p: i for i, p in enumerate(primes)}

        # Count frequency of each number
        from collections import Counter
        cnt = Counter(nums)

        # Numbers with repeated prime factors are invalid (4,8,9,12,16,18,20,24,25,27,28)
        # Map valid numbers (2-30) to their prime bitmask
        num_mask = {}
        for num in range(2, 31):
            mask = 0
            temp = num
            valid = True
            for p in primes:
                if temp % p == 0:
                    temp //= p
                    if temp % p == 0:
                        valid = False
                        break
                    mask |= (1 << prime_idx[p])
            if valid and temp == 1:
                num_mask[num] = mask

        # DP over bitmask of used primes
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num, mask in num_mask.items():
            if cnt[num] == 0:
                continue
            c = cnt[num]
            for state in range((1 << 10) - 1, -1, -1):
                if dp[state] == 0:
                    continue
                if state & mask == 0:
                    dp[state | mask] = (dp[state | mask] + dp[state] * c) % MOD

        # Sum all non-zero states, multiply by 2^count(1) since 1s can be included freely
        total = sum(dp[1:]) % MOD
        total = total * pow(2, cnt[1], MOD) % MOD
        return total
