# Author: Kaustav Ghosh
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return 'ba' not in s
