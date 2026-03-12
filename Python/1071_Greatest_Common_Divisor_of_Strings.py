# Author: Kaustav Ghosh
# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:math.gcd(len(str1), len(str2))]
