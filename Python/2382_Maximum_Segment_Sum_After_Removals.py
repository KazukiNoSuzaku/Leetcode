class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        n = len(nums)
        parent = list(range(n + 1))
        seg_sum = [0] * (n + 1)
        present = [False] * n
        max_sum = 0

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            parent[b] = a
            seg_sum[a] += seg_sum[b]

        ans = []
        for q in reversed(removeQueries):
            ans.append(max_sum)
            present[q] = True
            seg_sum[q] = nums[q]
            if q > 0 and present[q - 1]:
                union(q, q - 1)
            if q < n - 1 and present[q + 1]:
                union(q, q + 1)
            max_sum = max(max_sum, seg_sum[find(q)])

        return ans[::-1]
