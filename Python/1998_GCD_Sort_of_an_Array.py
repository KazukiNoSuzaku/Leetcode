# Author: Kaustav Ghosh
# Problem: GCD Sort of an Array
# Approach: Two values can be swapped directly when they share a prime, and swaps compose, so the values split into groups where everything inside a group can be permuted freely. Those groups are found by union-find over the values themselves: a sieve of smallest prime factors factors each entry, and each entry is joined to every prime dividing it, which links two entries that share a prime without ever comparing pairs. The array can then be sorted exactly when every position's current value and the value the sorted array wants there belong to the same group.

class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        limit = max(nums)
        smallest = list(range(limit + 1))
        factor = 2
        while factor * factor <= limit:
            if smallest[factor] == factor:
                for multiple in range(factor * factor, limit + 1, factor):
                    if smallest[multiple] == multiple:
                        smallest[multiple] = factor
            factor += 1

        parent = list(range(limit + 1))

        def find(value):
            root = value
            while parent[root] != root:
                root = parent[root]
            while parent[value] != root:
                parent[value], value = root, parent[value]
            return root

        def union(left, right):
            left_root = find(left)
            right_root = find(right)
            if left_root != right_root:
                parent[left_root] = right_root

        for value in nums:
            remaining = value
            while remaining > 1:
                prime = smallest[remaining]
                union(value, prime)
                while remaining % prime == 0:
                    remaining //= prime

        for current, wanted in zip(nums, sorted(nums)):
            if current != wanted and find(current) != find(wanted):
                return False
        return True
