# Author: Kaustav Ghosh
# Problem: Maximum Segment Sum After Removals
# Approach: Removals only ever split segments, which is awkward to track, so run them backwards as insertions that only ever merge. Union-find joins each re-added index with its present neighbours while keeping per-segment sums, and the best sum seen so far after re-adding query i is the answer for the state after removal i - 1

class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        """
        :type nums: List[int]
        :type removeQueries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        parent = list(range(n))
        total = [0] * n
        present = [False] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        answer = [0] * n
        best = 0
        for i in range(n - 1, 0, -1):
            idx = removeQueries[i]
            present[idx] = True
            total[idx] = nums[idx]
            for nb in (idx - 1, idx + 1):
                if 0 <= nb < n and present[nb]:
                    root = find(nb)
                    parent[root] = idx
                    total[idx] += total[root]
            best = max(best, total[idx])
            answer[i - 1] = best
        return answer
