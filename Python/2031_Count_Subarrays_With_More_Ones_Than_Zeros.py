# Author: Kaustav Ghosh
# Problem: Count Subarrays With More Ones Than Zeros
# Approach: Map 0 -> -1 and 1 -> +1. A subarray has more ones than zeros exactly when prefix[b] > prefix[a] for its endpoints a < b. Sweep prefixes, using a Fenwick tree over the value range to count how many earlier prefixes are strictly smaller

class Solution(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        size = 2 * n + 2          # values shifted by n: range [0, 2n]
        tree = [0] * (size + 1)

        def update(i):
            i += 1
            while i <= size:
                tree[i] += 1
                i += i & (-i)

        def query(i):             # count of inserted values with index <= i (0-based)
            i += 1
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        total = 0
        prefix = 0
        update(prefix + n)        # insert prefix[0] = 0
        for v in nums:
            prefix += 1 if v == 1 else -1
            # count earlier prefixes strictly less than current
            total += query(prefix + n - 1)
            update(prefix + n)
        return total % MOD
