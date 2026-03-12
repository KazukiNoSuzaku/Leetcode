# Author: Kaustav Ghosh
# Mathematical: probability is 1/n for n>1, 1.0 for n==1

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 1.0 if n == 1 else 0.5
