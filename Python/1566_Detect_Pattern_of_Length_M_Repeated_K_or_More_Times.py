# Author: Kaustav Ghosh
# Problem: Detect Pattern of Length M Repeated K or More Times
# Approach: A block of length m repeated k times back to back is exactly a stretch where every element equals the one m positions earlier, so instead of extracting candidate patterns I walk the array once comparing arr[i] with arr[i - m] and count how long the current agreeing stretch is; k consecutive copies need m * (k - 1) such agreements in a row, and any break resets the counter.

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        need = m * (k - 1)
        if need == 0:
            return m <= len(arr)
        run = 0
        for i in range(m, len(arr)):
            if arr[i] == arr[i - m]:
                run += 1
                if run == need:
                    return True
            else:
                run = 0
        return False
