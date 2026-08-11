# Author: Kaustav Ghosh
# Problem: GCD Sort of an Array
# Approach: Two values can be swapped (directly or transitively) when they share a prime factor, so union each value with its prime factors via a smallest-prime-factor sieve. The array is sortable iff every element lies in the same component as the value that belongs in its sorted position

class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = max(nums)
        spf = list(range(m + 1))
        i = 2
        while i * i <= m:
            if spf[i] == i:
                for j in range(i * i, m + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        parent = list(range(m + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for v in nums:
            x = v
            while x > 1:
                p = spf[x]
                union(v, p)
                while x % p == 0:
                    x //= p

        sorted_nums = sorted(nums)
        return all(find(a) == find(b) for a, b in zip(nums, sorted_nums))
