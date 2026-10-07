# Author: Kaustav Ghosh
# Problem: Get the Maximum Score
# Approach: Both arrays are strictly increasing, so values shared by them are the only places a path can switch sides. Walk the two arrays together accumulating each side's sum between consecutive shared values, and at every shared value commit the better of the two stretches plus the shared value itself; the tails after the last shared value are settled the same way

class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = j = 0
        first = second = 0
        total = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                first += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                second += nums2[j]
                j += 1
            else:
                total += max(first, second) + nums1[i]
                first = second = 0
                i += 1
                j += 1
        first += sum(nums1[i:])
        second += sum(nums2[j:])
        return (total + max(first, second)) % (10 ** 9 + 7)
