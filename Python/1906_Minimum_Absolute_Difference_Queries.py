# Author: Kaustav Ghosh
# Problem: Minimum Absolute Difference Queries
# Approach: Values are at most 100, so keep prefix counts per value. For a query, the values present in the range are those whose count grew; scan 1..100 in order and take the smallest gap between consecutive present values

class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MAX = 100
        n = len(nums)
        prefix = [[0] * (MAX + 1)]
        for x in nums:
            row = prefix[-1][:]
            row[x] += 1
            prefix.append(row)

        ans = []
        for l, r in queries:
            lo = prefix[l]
            hi = prefix[r + 1]
            prev = -1
            best = float('inf')
            for v in range(1, MAX + 1):
                if hi[v] - lo[v] > 0:
                    if prev != -1:
                        best = min(best, v - prev)
                    prev = v
            ans.append(-1 if best == float('inf') else best)
        return ans
