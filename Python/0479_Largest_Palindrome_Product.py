# Given an integer n, return the largest palindromic integer that can be represented as
# the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

# Author: Kaustav Ghosh

class Solution(object):
    def largestPalindrome(self, n):
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        for a in range(upper, lower - 1, -1):
            # Construct palindrome by mirroring a
            s = str(a)
            palindrome = int(s + s[::-1])
            # Check if palindrome = x * y for n-digit x, y
            b = upper
            while b * b >= palindrome:
                if palindrome % b == 0:
                    return palindrome % 1337
                b -= 1
        return -1
