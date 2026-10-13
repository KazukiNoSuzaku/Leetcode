# Author: Kaustav Ghosh
# Problem: Maximum Sum Obtained of Any Permutation
# Approach: Each position contributes its value once per request that covers it, so the total is the dot product of the values with the per-position request counts, and it is maximised by pairing the largest value with the most-requested position. Counting coverage by walking every request range would be quadratic, so I mark each range's start and one past its end in a difference array and take a running total to recover all the counts in one pass, then sort both lists descending and pair them off.

class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        delta = [0] * (n + 1)
        for start, end in requests:
            delta[start] += 1
            delta[end + 1] -= 1

        counts = []
        running = 0
        for i in range(n):
            running += delta[i]
            counts.append(running)

        counts.sort(reverse=True)
        nums.sort(reverse=True)
        return sum(value * times for value, times in zip(nums, counts)) % MOD
