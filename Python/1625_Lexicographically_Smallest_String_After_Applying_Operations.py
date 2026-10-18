# Author: Kaustav Ghosh
# Problem: Lexicographically Smallest String After Applying Operations
# Approach: The two operations commute enough to describe every reachable string by three independent choices rather than by searching. Rotating repeatedly reaches exactly the rotations by multiples of the greatest common divisor of b and the length, so those are enumerated directly. The addition always targets the odd positions of the current string, so when that step is even every rotation preserves which positions are odd and only the odd class can ever be shifted; when the step is odd, rotating by an odd amount, adding, and rotating back shifts the even class too, so both classes become independently adjustable. Each class cycles after ten additions, giving at most a hundred digit choices per rotation.

from math import gcd


class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        n = len(s)
        digits = [int(ch) for ch in s]
        step = gcd(b, n)
        # An odd reachable rotation lets the even positions be shifted as well.
        even_choices = 10 if step % 2 else 1

        best = None
        for shift in range(0, n, step):
            rotated = digits[shift:] + digits[:shift]
            for odd_times in range(10):
                odd_bump = odd_times * a % 10
                for even_times in range(even_choices):
                    even_bump = even_times * a % 10
                    candidate = ''.join(
                        str((value + (odd_bump if i % 2 else even_bump)) % 10)
                        for i, value in enumerate(rotated))
                    if best is None or candidate < best:
                        best = candidate
        return best
