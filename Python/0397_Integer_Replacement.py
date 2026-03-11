# Given a positive integer n, you can apply one of the following operations:
# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.
# Return the minimum number of operations needed for n to become 1.

# Author: Kaustav Ghosh

class Solution(object):
    def integerReplacement(self, n):
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or (n >> 1) & 1 == 0:
                n -= 1
            else:
                n += 1
            steps += 1
        return steps
