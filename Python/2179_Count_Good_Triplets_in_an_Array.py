# Author: Kaustav Ghosh
# Problem: 2179. Count Good Triplets in an Array
# URL: https://leetcode.com/problems/count-good-triplets-in-an-array/
# Approach: For each value as the middle element (by position in nums2),
#           count how many values to its left in nums2 also appear to the left
#           of it in nums1, and similarly for the right. Use a Fenwick tree
#           (BIT) indexed by position-in-nums1 to do this in O(n log n).

class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        # pos1[v] = index of value v in nums1
        pos1 = [0] * n
        for i, v in enumerate(nums1):
            pos1[v] = i

        # Fenwick tree for prefix sum queries
        tree = [0] * (n + 1)

        def update(i):
            i += 1  # 1-indexed
            while i <= n:
                tree[i] += 1
                i += i & (-i)

        def query(i):
            i += 1  # 1-indexed
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        ans = 0
        for v in nums2:
            p = pos1[v]
            # left_both: count of elements seen so far (left in nums2) with pos1 < p
            left_both = query(p - 1) if p > 0 else 0
            # right_both: total elements not yet processed with pos1 > p
            # total remaining in nums2 to the right = (n - 1 - current_index_in_nums2)
            # but easier: elements with pos1 > p not yet inserted
            already_inserted = query(n - 1)  # all inserted so far
            left_total = already_inserted  # total seen so far
            # elements already inserted with pos1 > p
            right_inserted = left_total - left_both - (1 if False else 0)
            # elements not yet inserted = n - 1 - already_inserted (excluding current)
            # elements not yet inserted with pos1 > p
            right_remaining = (n - 1 - already_inserted) - (n - 1 - p - right_inserted)
            # Simpler formulation:
            # left_both already computed
            # right_both = (n - 1 - p) - (already_inserted - left_both)
            right_both = (n - 1 - p) - (left_total - left_both)
            ans += left_both * right_both
            update(p)
        return ans
