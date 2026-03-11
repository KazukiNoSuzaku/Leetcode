# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be
# represented as a string s of length n where s[i] == 'I' if perm[i] < perm[i + 1], else 'D'.
# Given a string s, reconstruct the permutation perm and return it.
# If there are multiple valid permutations perm, return the lexicographically smallest one.

# Author: Kaustav Ghosh

class Solution(object):
    def findPermutation(self, s):
        n = len(s)
        res = list(range(1, n + 2))
        i = 0
        while i < n:
            if s[i] == 'D':
                j = i
                while j < n and s[j] == 'D':
                    j += 1
                res[i:j+1] = res[i:j+1][::-1]
                i = j
            else:
                i += 1
        return res
