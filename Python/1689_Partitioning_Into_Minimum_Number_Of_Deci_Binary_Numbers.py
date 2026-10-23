# Author: Kaustav Ghosh
# Problem: Partitioning Into Minimum Number Of Deci-Binary Numbers
# Approach: Each deci-binary number contributes at most one to any single digit position and the additions never carry, since every column only ever sums digits that are zero or one up to the original digit there. So the count needed is dictated by the most demanding column alone, and that many numbers also suffice, because the ones can be distributed independently per column. The answer is therefore the largest digit.

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return int(max(n))
