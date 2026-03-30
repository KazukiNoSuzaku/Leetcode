# Author: Kaustav Ghosh
# Problem: 2180. Count Integers With Even Digit Sum
# URL: https://leetcode.com/problems/count-integers-with-even-digit-sum/
# Approach: Iterate from 1 to num inclusive. For each integer, sum its digits
#           and count it if the sum is even.

class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for n in range(1, num + 1):
            if sum(int(d) for d in str(n)) % 2 == 0:
                count += 1
        return count
