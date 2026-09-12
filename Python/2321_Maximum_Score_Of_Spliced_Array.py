# Author: Kaustav Ghosh
# Problem: Maximum Score Of Spliced Array
# Approach: Swapping a subarray [l,r] between the two arrays changes one array's sum by the sum of (other[i]-this[i]) over that range. To maximize sum(nums1) we want the maximum subarray sum of (nums2-nums1); to maximize sum(nums2), the maximum subarray sum of (nums1-nums2). Add the best positive gain (Kadane, floored at 0) to each base sum and take the larger

class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def max_subarray(diff):
            best = 0
            cur = 0
            for d in diff:
                cur = max(0, cur + d)
                best = max(best, cur)
            return best

        s1, s2 = sum(nums1), sum(nums2)
        gain1 = max_subarray([b - a for a, b in zip(nums1, nums2)])
        gain2 = max_subarray([a - b for a, b in zip(nums1, nums2)])
        return max(s1 + gain1, s2 + gain2)
