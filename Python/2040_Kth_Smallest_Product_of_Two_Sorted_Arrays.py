# Author: Kaustav Ghosh
# Problem: Kth Smallest Product of Two Sorted Arrays
# Approach: There are far too many products to list, but the number of products at or below a given bound is easy to compute and rises with the bound, so the answer is found by binary searching the bound for the smallest one whose count reaches the required rank. Counting fixes one factor at a time: a positive factor needs its partner no larger than the bound divided by it, which is a floor division, while a negative factor flips the inequality and needs its partner at least the bound divided by it rounded up. Since the second array is sorted, each of those is one binary search, and a factor of zero contributes every partner when the bound is not negative and none otherwise. The outer loop runs over the shorter array so the counting cost follows the smaller length.

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        import bisect
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        width = len(nums2)
        bisect_right = bisect.bisect_right
        bisect_left = bisect.bisect_left

        def at_most(limit):
            total = 0
            for value in nums1:
                if value > 0:
                    total += bisect_right(nums2, limit // value)
                elif value < 0:
                    total += width - bisect_left(nums2, -((-limit) // value))
                elif limit >= 0:
                    total += width
            return total

        low = -(10 ** 10)
        high = 10 ** 10
        while low < high:
            middle = (low + high) // 2
            if at_most(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low
