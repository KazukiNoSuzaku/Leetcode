# Author: Kaustav Ghosh
# Problem: Widest Pair of Indices With Equal Range Sum
# Approach: Two ranges summing equally is the same as the range of the elementwise difference summing to zero, so I work with the running total of nums1[i] - nums2[i]. A window from i to j has difference sum zero exactly when the running total before i equals the running total at j, which turns the question into finding, for each total, the earliest position it occurred at and the latest, and keeping the biggest span. Only the first occurrence of each total ever matters, so a dictionary storing each total the first time it is seen suffices, seeded with zero at position minus one so that windows starting at the array's beginning are covered. One pass gives O(n) time.

class Solution(object):
    def widestPairOfIndices(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        earliest = {0: -1}
        running = 0
        widest = 0
        for index in range(len(nums1)):
            running += nums1[index] - nums2[index]
            if running in earliest:
                span = index - earliest[running]
                if span > widest:
                    widest = span
            else:
                earliest[running] = index
        return widest
