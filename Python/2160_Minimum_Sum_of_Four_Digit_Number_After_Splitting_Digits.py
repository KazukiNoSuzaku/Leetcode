# Author: Kaustav Ghosh
# Problem: Minimum Sum of Four Digit Number After Splitting Digits
# Approach: To minimize the sum of two two-digit numbers, place the two smallest digits in the tens positions and the two largest in the units. Sort the digits and combine accordingly

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        d = sorted(int(c) for c in str(num).zfill(4))
        return (d[0] + d[1]) * 10 + (d[2] + d[3])
