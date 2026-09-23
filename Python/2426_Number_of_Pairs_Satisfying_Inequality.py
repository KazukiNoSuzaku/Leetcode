# Author: Kaustav Ghosh
# Problem: Number of Pairs Satisfying Inequality
# Approach: Rearranging nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff gives a[i] <= a[j] + diff for a = nums1 - nums2, so the condition only involves one value per index. Sweep j from left to right counting earlier values at most a[j] + diff with a Fenwick tree over the compressed values

from bisect import bisect_left, bisect_right


class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        a = [x - y for x, y in zip(nums1, nums2)]
        points = sorted(set(a))
        size = len(points)
        tree = [0] * (size + 1)

        def add(i):
            i += 1
            while i <= size:
                tree[i] += 1
                i += i & -i

        def count_upto(i):
            i += 1
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            return total

        pairs = 0
        for value in a:
            limit = bisect_right(points, value + diff) - 1
            if limit >= 0:
                pairs += count_upto(limit)
            add(bisect_left(points, value))
        return pairs
