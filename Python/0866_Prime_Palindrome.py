# Find the smallest prime palindrome >= n.

# Author: Kaustav Ghosh

class Solution(object):
    def primePalindrome(self, n):
        def is_prime(x):
            if x < 2: return False
            if x == 2: return True
            if x % 2 == 0: return False
            for i in range(3, int(x**0.5)+1, 2):
                if x % i == 0: return False
            return True
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        # All even-length palindromes > 1 are divisible by 11
        x = n
        while True:
            if is_palindrome(x) and is_prime(x): return x
            if 10**7 < x < 10**8: x = 10**8
            x += 1
