# Author: Kaustav Ghosh
# Problem: Find Lucky Integer in an Array
# Approach: Count frequencies, find max x where count(x) == x

from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr)
        result = -1
        for num, freq in count.items():
            if num == freq:
                result = max(result, num)
        return result
