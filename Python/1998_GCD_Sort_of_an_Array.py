# Author: Kaustav Ghosh
# Problem 1998: GCD Sort of an Array

class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Union-Find: numbers sharing a common factor > 1 can be swapped
        max_val = max(nums)
        parent = list(range(max_val + 1))
        rank = [0] * (max_val + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        # Sieve-like factorization
        for num in set(nums):
            d = 2
            while d * d <= num:
                if num % d == 0:
                    union(num, d)
                    union(num, num // d)
                d += 1

        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if find(a) != find(b):
                return False
        return True
