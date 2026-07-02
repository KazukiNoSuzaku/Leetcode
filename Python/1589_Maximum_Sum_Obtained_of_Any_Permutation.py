# Author: Kaustav Ghosh
# Problem: Maximum Sum Obtained of Any Permutation
# Approach: A difference array gives how many requests touch each index; assign the largest values to the most-requested indices

class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        diff = [0] * (n + 1)
        for start, end in requests:
            diff[start] += 1
            diff[end + 1] -= 1

        freq = [0] * n
        running = 0
        for i in range(n):
            running += diff[i]
            freq[i] = running

        freq.sort(reverse=True)
        nums.sort(reverse=True)
        return sum(f * v for f, v in zip(freq, nums)) % MOD
