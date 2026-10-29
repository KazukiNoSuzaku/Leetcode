# Author: Kaustav Ghosh
# Problem: Minimum Length of String After Deleting Similar Ends
# Approach: An operation needs the two ends to carry the same character, and when they do it is always worth stripping every copy of that character from both ends at once: leaving some behind could only block a later operation, never enable one. So two pointers walk inward, and whenever they meet on the same character each runs past the whole run of it. The process halts the moment the ends differ, and the pointers crossing is what produces a length of zero.

class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s) - 1
        while left < right and s[left] == s[right]:
            ch = s[left]
            while left <= right and s[left] == ch:
                left += 1
            while right >= left and s[right] == ch:
                right -= 1
        return right - left + 1
