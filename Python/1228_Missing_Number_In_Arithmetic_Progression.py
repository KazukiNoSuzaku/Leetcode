# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Calculate expected common difference, find missing element

class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        for i in range(1, n):
            if arr[i] - arr[i - 1] != diff:
                return arr[i - 1] + diff
        return arr[0]
