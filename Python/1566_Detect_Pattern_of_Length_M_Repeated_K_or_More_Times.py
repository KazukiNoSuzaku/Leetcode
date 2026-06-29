# Author: Kaustav Ghosh
# Problem: Detect Pattern of Length M Repeated K or More Times
# Approach: Count a running streak where arr[i] == arr[i+m]; a run reaching (k-1)*m means a length-m block repeats k times

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        count = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                count += 1
                if count == (k - 1) * m:
                    return True
            else:
                count = 0
        return False
