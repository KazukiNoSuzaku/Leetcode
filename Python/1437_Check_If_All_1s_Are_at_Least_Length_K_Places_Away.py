# Author: Kaustav Ghosh
# Problem: Check If All 1's Are at Least Length K Places Away
# Approach: Scan for 1s and check gaps between consecutive 1s

class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last = -k - 1
        for i, n in enumerate(nums):
            if n == 1:
                if i - last - 1 < k:
                    return False
                last = i
        return True
