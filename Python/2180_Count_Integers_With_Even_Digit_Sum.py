# Author: Kaustav Ghosh
# Problem: Count Integers With Even Digit Sum
# Approach: Count the integers from 1 to num whose digit sum is even by checking each

class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        return sum(1 for x in range(1, num + 1)
                   if sum(int(d) for d in str(x)) % 2 == 0)
