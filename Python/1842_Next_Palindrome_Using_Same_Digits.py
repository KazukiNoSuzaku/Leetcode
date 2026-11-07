# Author: Kaustav Ghosh
# Problem: Next Palindrome Using Same Digits
# Approach: A palindrome is fully determined by its first half together with the middle digit of an odd-length number, and comparing two palindromes of the same length comes down to comparing those halves. So the smallest larger palindrome is built from the next lexicographic arrangement of the first half alone, mirrored back onto the second half, which also guarantees the digit multiset is preserved. The next arrangement is found in place by the standard pivot-and-reverse step, and its failing is exactly the case where the half is already the largest arrangement and no larger palindrome exists.

class Solution(object):
    def nextPalindrome(self, num):
        """
        :type num: str
        :rtype: str
        """
        digits = list(num)
        half = len(digits) // 2

        # Standard next-permutation over digits[:half].
        pivot = half - 2
        while pivot >= 0 and digits[pivot] >= digits[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return ""
        swap = half - 1
        while digits[swap] <= digits[pivot]:
            swap -= 1
        digits[pivot], digits[swap] = digits[swap], digits[pivot]
        digits[pivot + 1:half] = reversed(digits[pivot + 1:half])

        digits[len(digits) - half:] = reversed(digits[:half])
        return "".join(digits)
