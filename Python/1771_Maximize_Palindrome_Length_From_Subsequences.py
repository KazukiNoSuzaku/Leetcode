# Author: Kaustav Ghosh
# Problem: Maximize Palindrome Length From Subsequences
# Approach: Concatenating the two words turns the task into the ordinary longest palindromic subsequence of one string, with the single extra rule that the outermost matched pair has to straddle the join so that both halves contribute. For a fixed letter the widest such pair is its first occurrence in word1 and its last occurrence in word2, and widening the pair can only enlarge the interval left inside, so only 26 candidate pairs ever need checking. The interval table is filled bottom-up over start indices, and since each candidate reads one entry of one particular row, the rows are consumed as they are produced and only two are ever held, keeping memory linear instead of the four million cells a full table would need.

class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        s = word1 + word2
        n = len(s)
        split = len(word1)

        # For each shared letter the pair of outer positions is fixed, and the
        # palindrome inside it is s[outer_start .. inner_end].
        wanted = {}
        for letter in set(word1) & set(word2):
            outer_start = word1.index(letter) + 1
            inner_end = split + word2.rindex(letter) - 1
            wanted.setdefault(outer_start, []).append(inner_end)

        best = 0
        # row[j] is the longest palindromic subsequence of s[start .. j].
        row = [0] * n
        for start in range(n - 1, -1, -1):
            below = row
            row = [0] * n
            row[start] = 1
            here = s[start]
            for j in range(start + 1, n):
                if here == s[j]:
                    row[j] = below[j - 1] + 2
                else:
                    row[j] = below[j] if below[j] > row[j - 1] else row[j - 1]
            for inner_end in wanted.get(start, ()):
                if row[inner_end] + 2 > best:
                    best = row[inner_end] + 2
        return best
