# Author: Kaustav Ghosh
# Problem: Partitioning Into Minimum Number Of Deci-Binary Numbers
# Approach: Each deci-binary number contributes 0 or 1 to every digit place, so the count needed equals the largest digit in n

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return int(max(n))
