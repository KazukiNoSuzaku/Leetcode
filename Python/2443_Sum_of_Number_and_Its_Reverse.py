# Author: Kaustav Ghosh
# Problem: Sum of Number and Its Reverse
# Approach: A candidate can never exceed num itself since reverses are non-negative, so test every value from 0 to num and check whether it plus its digit reverse hits the target

class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return any(x + int(str(x)[::-1]) == num for x in range(num + 1))
