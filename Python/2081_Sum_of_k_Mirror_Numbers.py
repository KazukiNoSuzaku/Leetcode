# Author: Kaustav Ghosh
# Problem: Sum of k-Mirror Numbers
# Approach: Generate base-10 palindromes in increasing order (build from the first half and mirror it), keep the ones that are also palindromes in base k, and sum the first n of them

class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def base10_palindromes():
            for d in range(1, 10):
                yield d
            length = 2
            while True:
                half = (length + 1) // 2
                for prefix in range(10 ** (half - 1), 10 ** half):
                    s = str(prefix)
                    if length % 2 == 0:
                        pal = s + s[::-1]
                    else:
                        pal = s + s[-2::-1]
                    yield int(pal)
                length += 1

        def is_base_k_palindrome(num):
            digits = []
            while num:
                digits.append(num % k)
                num //= k
            return digits == digits[::-1]

        total = 0
        found = 0
        for p in base10_palindromes():
            if is_base_k_palindrome(p):
                total += p
                found += 1
                if found == n:
                    break
        return total
