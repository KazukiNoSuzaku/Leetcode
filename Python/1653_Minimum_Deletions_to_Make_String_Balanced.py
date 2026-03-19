# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        b_count = 0
        deletions = 0
        for c in s:
            if c == 'b':
                b_count += 1
            else:  # c == 'a'
                deletions = min(deletions + 1, b_count)
        return deletions
