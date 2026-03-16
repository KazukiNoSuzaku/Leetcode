# Author: Kaustav Ghosh
# Problem: Find the Distance Value Between Two Arrays
# Approach: For each element in arr1, check if no element in arr2 is within distance d

import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        count = 0
        for a in arr1:
            idx = bisect.bisect_left(arr2, a - d)
            if idx == len(arr2) or arr2[idx] > a + d:
                count += 1
        return count
