# Author: Kaustav Ghosh
# Problem: Maximum Product of the Length of Two Palindromic Substrings
# Approach: Manacher gives the longest odd palindrome centered at each index. Derive the longest odd palindrome ending at / starting at each index (a length-l palindrome implies length l-2 shifted inward), then prefix/suffix maxima give the best palindrome fully left/right of each split. Maximize the product over all splits

class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        p = [0] * n
        c = r = 0
        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and s[i - p[i] - 1] == s[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]

        end_here = [1] * n     # longest odd palindrome ending at i (every single char)
        start_here = [1] * n   # longest odd palindrome starting at i
        for i in range(n):
            length = 2 * p[i] + 1
            end_here[i + p[i]] = max(end_here[i + p[i]], length)
            start_here[i - p[i]] = max(start_here[i - p[i]], length)

        for i in range(n - 2, -1, -1):
            end_here[i] = max(end_here[i], end_here[i + 1] - 2)
        for i in range(1, n):
            start_here[i] = max(start_here[i], start_here[i - 1] - 2)

        prefix_max = [0] * n
        prefix_max[0] = end_here[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], end_here[i])

        suffix_max = [0] * n
        suffix_max[n - 1] = start_here[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], start_here[i])

        best = 0
        for i in range(n - 1):
            best = max(best, prefix_max[i] * suffix_max[i + 1])
        return best
