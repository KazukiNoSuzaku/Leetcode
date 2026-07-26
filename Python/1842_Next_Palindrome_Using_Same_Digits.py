# Author: Kaustav Ghosh
# Problem: Next Palindrome Using Same Digits (Premium)
# Approach: A palindrome is fixed by its left half, so find the next-permutation of that half; mirror it back. If the half is already the largest permutation, no greater palindrome exists

class Solution(object):
    def nextPalindrome(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)
        half = list(num[:n // 2])

        # next_permutation on the half, in place
        i = len(half) - 2
        while i >= 0 and half[i] >= half[i + 1]:
            i -= 1
        if i < 0:
            return ""  # half already the largest permutation
        j = len(half) - 1
        while half[j] <= half[i]:
            j -= 1
        half[i], half[j] = half[j], half[i]
        half[i + 1:] = reversed(half[i + 1:])

        left = ''.join(half)
        middle = num[n // 2] if n % 2 else ''
        return left + middle + left[::-1]
