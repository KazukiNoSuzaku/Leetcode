# Author: Kaustav Ghosh
# Problem: 2283. Check if Number Has Equal Digit Count and Digit Value
# URL: https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
# Difficulty: Easy
#
# Approach:
# For each index i, check if the count of digit i in num equals num[i].

class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            if num.count(str(i)) != int(num[i]):
                return False
        return True
