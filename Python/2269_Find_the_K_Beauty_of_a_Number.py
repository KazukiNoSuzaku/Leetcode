# Author: Kaustav Ghosh
# Problem: 2269. Find the K-Beauty of a Number
# URL: https://leetcode.com/problems/find-the-k-beauty-of-a-number/
# Difficulty: Easy
#
# Approach:
# Slide a window of size k over the string representation of num.
# Count substrings that form a nonzero number dividing num evenly.

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
            sub = int(s[i:i + k])
            if sub != 0 and num % sub == 0:
                count += 1
        return count
