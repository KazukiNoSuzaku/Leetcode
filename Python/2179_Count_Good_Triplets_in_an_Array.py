# Author: Kaustav Ghosh
# Problem: Count Good Triplets in an Array
# Approach: Map each value to its position in nums2, then rewrite nums1 as those positions. A good triplet becomes an increasing triple in that array. For each element as the middle, multiply the count of smaller elements to its left by the count of larger elements to its right, using a Fenwick tree for the left counts

class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i
        a = [pos2[v] for v in nums1]

        tree = [0] * (n + 1)

        def update(i):
            i += 1
            while i <= n:
                tree[i] += 1
                i += i & (-i)

        def query(i):  # count of inserted values with index <= i (0-based)
            i += 1
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s

        total = 0
        for j in range(n):
            v = a[j]
            smaller_left = query(v - 1) if v > 0 else 0
            larger_left = j - smaller_left
            larger_right = (n - 1 - v) - larger_left
            total += smaller_left * larger_right
            update(v)
        return total
