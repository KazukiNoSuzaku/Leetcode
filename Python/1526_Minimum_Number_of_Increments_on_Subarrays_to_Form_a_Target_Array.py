# Author: Kaustav Ghosh
# Problem: 1526 - Minimum Number of Increments on Subarrays to Form a Target Array
# Approach: Sum of positive differences between consecutive elements

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        result = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                result += target[i] - target[i - 1]
        return result
