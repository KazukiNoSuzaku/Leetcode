# Author: Kaustav Ghosh
# Problem: Minimum Number of Increments on Subarrays to Form a Target Array
# Approach: An operation raises a whole stretch by one, so a position only needs its own operations when it sits higher than its left neighbour; otherwise the operations covering that neighbour can be stretched to cover it. Summing those rises, starting from the first element, counts the minimum

class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        operations = target[0]
        for previous, current in zip(target, target[1:]):
            if current > previous:
                operations += current - previous
        return operations
