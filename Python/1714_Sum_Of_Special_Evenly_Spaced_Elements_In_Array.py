# Author: Kaustav Ghosh
# Problem: Sum Of Special Evenly-Spaced Elements In Array
# Approach: A query with a large stride is cheap to answer directly, because it touches only the array length divided by the stride, while a query with a small stride is expensive but there are few distinct small strides to precompute. Splitting at the square root of the length balances the two: for every stride up to that threshold a suffix table is built once, giving constant-time answers, and any larger stride is summed on the spot in at most the square root of the length steps. Either way a query costs about the square root of the length, and the precomputation is the same order overall.

class Solution(object):
    def solve(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        threshold = int(n ** 0.5)

        # suffix[stride][start] totals nums[start], nums[start+stride], ...
        suffix = [None] * (threshold + 1)
        for stride in range(1, threshold + 1):
            table = [0] * (n + stride)
            for start in range(n - 1, -1, -1):
                table[start] = table[start + stride] + nums[start]
            suffix[stride] = table

        answers = []
        for start, stride in queries:
            if stride <= threshold:
                answers.append(suffix[stride][start] % MOD)
            else:
                answers.append(sum(nums[start::stride]) % MOD)
        return answers
