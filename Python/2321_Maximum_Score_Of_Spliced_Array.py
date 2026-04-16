# Author: Kaustav Ghosh
# Problem: 2321. Maximum Score Of Spliced Array
# URL: https://leetcode.com/problems/maximum-score-of-spliced-array/
# Difficulty: Hard
#
# Approach:
# For each array, try replacing a subarray with the corresponding subarray from the other.
# The gain from replacing nums1[l..r] with nums2[l..r] is sum(nums2[l..r] - nums1[l..r]).
# Use Kadane's algorithm on the difference array to find the maximum gain.
# Answer is max(sum(nums1) + max_gain_from_nums2, sum(nums2) + max_gain_from_nums1).

class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def kadane_max_gain(a, b):
            # type: (List[int], List[int]) -> int
            # Max subarray sum of (b[i] - a[i]) using Kadane's
            max_gain = 0
            cur_gain = 0
            for x, y in zip(a, b):
                cur_gain = max(0, cur_gain + (y - x))
                max_gain = max(max_gain, cur_gain)
            return max_gain

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        # Replace subarray in nums1 with nums2: sum1 + max_gain
        # Replace subarray in nums2 with nums1: sum2 + max_gain
        return max(sum1 + kadane_max_gain(nums1, nums2),
                   sum2 + kadane_max_gain(nums2, nums1))
