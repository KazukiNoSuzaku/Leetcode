# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-absolute-difference-queries/

class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        # Prefix count for each value 1..100
        prefix = [[0] * 101 for _ in range(n + 1)]
        for i in range(n):
            for v in range(101):
                prefix[i + 1][v] = prefix[i][v]
            prefix[i + 1][nums[i]] += 1

        ans = []
        for l, r in queries:
            min_diff = float('inf')
            prev = -1
            for v in range(1, 101):
                if prefix[r + 1][v] - prefix[l][v] > 0:
                    if prev != -1:
                        min_diff = min(min_diff, v - prev)
                    prev = v
            ans.append(min_diff if min_diff != float('inf') else -1)
        return ans
