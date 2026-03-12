# Author: Kaustav Ghosh
# Check every n/4-th element as candidate

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        quarter = n // 4
        for i in range(0, n, quarter):
            if i + quarter < n and arr[i] == arr[i + quarter]:
                return arr[i]
        return arr[-1]
