# Author: Kaustav Ghosh

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        # s1 < s2, we need to increase s1 or decrease s2
        # Max gain from nums1[i]: 6 - nums1[i] (increase to 6)
        # Max gain from nums2[i]: nums2[i] - 1 (decrease to 1)
        gains = []
        for x in nums1:
            gains.append(6 - x)
        for x in nums2:
            gains.append(x - 1)
        gains.sort(reverse=True)
        diff = s2 - s1
        ops = 0
        for g in gains:
            if diff <= 0:
                break
            diff -= g
            ops += 1
        return ops if diff <= 0 else -1
