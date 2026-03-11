# The Fibonacci numbers form a sequence: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2).
# Given n, return F(n).

# Author: Kaustav Ghosh

class Solution(object):
    def fib(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
