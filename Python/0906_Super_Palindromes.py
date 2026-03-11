# Count palindromic integers whose square roots are also palindromes in [left, right].

# Author: Kaustav Ghosh

class Solution(object):
    def superpalindromesInRange(self, left, right):
        lo, hi = int(left), int(right)
        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]
        count = 0
        for k in range(100000):
            s = str(k)
            # Odd length palindrome
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > hi: break
            if v >= lo and is_palindrome(v): count += 1
            # Even length palindrome
            t = s + s[::-1]
            v = int(t) ** 2
            if v <= hi and v >= lo and is_palindrome(v): count += 1
        return count
