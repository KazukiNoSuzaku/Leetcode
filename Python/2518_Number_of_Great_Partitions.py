# Author: Kaustav Ghosh
# Problem: Number of Great Partitions
# Approach: Count the bad partitions instead. Each element goes to one of two groups, giving 2^n ordered partitions, and a partition fails only when one group sums below k. With a total of at least 2k both groups cannot fail at once, so each subset summing under k spoils exactly two partitions. A knapsack capped at k counts those subsets

class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        if sum(nums) < 2 * k:
            return 0
        under = [0] * k
        under[0] = 1
        for x in nums:
            for total in range(k - 1, x - 1, -1):
                under[total] = (under[total] + under[total - x]) % MOD
        bad = sum(under) % MOD
        return (pow(2, len(nums), MOD) - 2 * bad) % MOD
