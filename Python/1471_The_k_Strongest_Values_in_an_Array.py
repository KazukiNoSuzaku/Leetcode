# Author: Kaustav Ghosh
# Problem: The k Strongest Values in an Array (Premium)
# Approach: Sort, find median, sort by |a - median| descending, take k

class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda x: (-abs(x - median), -x))
        return arr[:k]
