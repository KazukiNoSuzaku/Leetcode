# Author: Kaustav Ghosh
# Problem: Split Two Strings to Make Palindrome
# Approach: Trying every split point and testing each joined string would be quadratic, but the outer characters settle themselves: for a prefix of one string joined to a suffix of the other, the first character must match the last, the second the second-last, and so on, and those pairs come from the two different strings, so they can be matched without knowing where the split is. Walking inward while they agree leaves a middle stretch that lies wholly inside one string or the other depending on where the cut falls, so it suffices to test whether that stretch is a palindrome in either string. The whole thing is then run twice, once for each way round of the two strings.

class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def works(front, back):
            left, right = 0, len(back) - 1
            while left < right and front[left] == back[right]:
                left += 1
                right -= 1
            return is_palindrome(front, left, right) or is_palindrome(back, left, right)

        return works(a, b) or works(b, a)
