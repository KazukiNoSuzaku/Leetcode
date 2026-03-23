# Author: Kaustav Ghosh
# Problem 1842: Next Palindrome Using Same Digits (Premium)

class Solution(object):
    def nextPalindrome(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)
        half = list(num[:n // 2])
        # Find next permutation of the first half
        i = len(half) - 2
        while i >= 0 and half[i] >= half[i + 1]:
            i -= 1
        if i < 0:
            return ""
        j = len(half) - 1
        while half[j] <= half[i]:
            j -= 1
        half[i], half[j] = half[j], half[i]
        half[i + 1:] = half[i + 1:][::-1]
        if n % 2 == 1:
            return "".join(half) + num[n // 2] + "".join(half[::-1])
        return "".join(half) + "".join(half[::-1])
