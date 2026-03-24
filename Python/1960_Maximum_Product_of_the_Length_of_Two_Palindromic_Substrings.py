# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Manacher's algorithm for odd-length palindromes only (all chars are lowercase)
        p = [0] * n
        c = r = 0
        for i in range(n):
            mirror = 2 * c - i
            if i < r:
                p[i] = min(r - i, p[mirror])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and s[i - p[i] - 1] == s[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]

        # max_left[i] = length of longest odd palindrome ending at or before i
        max_left = [0] * n
        # max_right[i] = length of longest odd palindrome starting at or after i
        max_right = [0] * n

        # For max_left: for each palindrome centered at c with radius p[c],
        # it ends at c + p[c], its length is 2*p[c]+1
        # We want max_left[i] = max length of palindrome ending at index <= i
        # Use the observation: if palindrome of radius r centered at c ends at c+r,
        # then palindrome of radius r-1 centered at c ends at c+r-1
        # So we can propagate: for each center, the max palindrome ending at c+p[c] has length 2*p[c]+1

        for i in range(n):
            max_left[i + p[i]] = max(max_left[i + p[i]] if i + p[i] < n else 0, 2 * p[i] + 1)

        # Fill max_left: if max_left[i] is set, then max_left[i-1] can be at least max_left[i]-2
        # Also max_left[i] >= max_left[i-1]
        # We need to propagate both ways
        # First propagate backwards: max_left[i-1] >= max_left[i] - 2
        for i in range(n):
            end = i + p[i]
            if end < n:
                max_left[end] = max(max_left[end], 2 * p[i] + 1)

        for i in range(n - 2, -1, -1):
            max_left[i] = max(max_left[i], max_left[i + 1] - 2)
        for i in range(1, n):
            max_left[i] = max(max_left[i], max_left[i - 1])

        # Ensure all values are at least 1
        for i in range(n):
            max_left[i] = max(max_left[i], 1)

        # For max_right
        for i in range(n):
            start = i - p[i]
            if start >= 0:
                max_right[start] = max(max_right[start], 2 * p[i] + 1)

        for i in range(1, n):
            max_right[i] = max(max_right[i], max_right[i - 1] - 2)
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i], max_right[i + 1])

        for i in range(n):
            max_right[i] = max(max_right[i], 1)

        result = 0
        for i in range(n - 1):
            result = max(result, max_left[i] * max_right[i + 1])
        return result
