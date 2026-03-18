# Author: Kaustav Ghosh
# Problem: 1566 - Detect Pattern of Length M Repeated K or More Times
# Approach: Check m*k window if each element equals element m positions back

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        n = len(arr)
        count = 0
        for i in range(n - m):
            if arr[i] == arr[i + m]:
                count += 1
            else:
                count = 0
            if count == m * (k - 1):
                return True
        return False
