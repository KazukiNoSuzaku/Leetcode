# Author: Kaustav Ghosh
# Problem 2081: Sum of k-Mirror Numbers

class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_palindrome(s):
            return s == s[::-1]

        def generate_base10_palindromes():
            """Generate base-10 palindromes in increasing order."""
            length = 1
            while True:
                half = (length + 1) // 2
                start = 10 ** (half - 1) if half > 1 else 1
                end = 10 ** half
                for first_half in range(start, end):
                    s = str(first_half)
                    if length % 2 == 0:
                        pal = s + s[::-1]
                    else:
                        pal = s + s[-2::-1]
                    yield int(pal)
                length += 1

        def to_base_k(num, base):
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))

        total = 0
        count = 0
        for pal in generate_base10_palindromes():
            base_k = to_base_k(pal, k)
            if is_palindrome(base_k):
                total += pal
                count += 1
                if count == n:
                    return total
