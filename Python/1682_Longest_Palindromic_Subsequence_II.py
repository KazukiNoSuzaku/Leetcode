# Author: Kaustav Ghosh
# Problem: Longest Palindromic Subsequence II
# Approach: The ordinary longest-palindromic-subsequence recurrence is not enough here, because whether a matching pair of ends may be taken depends on which character was paired immediately outside it; so the state carries that character alongside the interval. Matching ends are taken only when they differ from the enclosing pair, which is exactly the no-equal-neighbours rule, and otherwise the interval shrinks from one side or the other. A sentinel character stands for "nothing paired yet" so the outermost call needs no special case. The table is filled by increasing interval length so every value it reads is already final, which avoids recursion entirely; lengths never exceed the string length, so a byte per entry is enough to hold the whole table compactly.

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0
        letters = [ord(ch) - 97 for ch in s]
        NONE = 26
        width = 27
        # table[(i * n + j) * width + x]: best over s[i..j] enclosed by character x
        table = bytearray(n * n * width)

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                base = (i * n + j) * width
                inner = ((i + 1) * n + (j - 1)) * width if j - 1 >= i + 1 else None
                drop_left = ((i + 1) * n + j) * width
                drop_right = (i * n + (j - 1)) * width
                same = letters[i] == letters[j]
                for x in range(width):
                    if same and letters[i] != x:
                        value = 2 if inner is None else 2 + table[inner + letters[i]]
                    else:
                        left = table[drop_left + x]
                        right = table[drop_right + x]
                        value = left if left > right else right
                    table[base + x] = value

        return table[(0 * n + (n - 1)) * width + NONE]
