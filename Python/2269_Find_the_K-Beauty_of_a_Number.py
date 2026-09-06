# Author: Kaustav Ghosh
# Problem: Find the K-Beauty of a Number
# Approach: Slide a window of length k over the decimal digits of num; each window is a substring whose integer value counts toward the k-beauty when it is non-zero and divides num

class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s = str(num)
        count = 0
        for i in range(len(s) - k + 1):
            val = int(s[i:i + k])
            if val != 0 and num % val == 0:
                count += 1
        return count
