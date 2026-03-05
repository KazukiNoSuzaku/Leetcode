# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences
# (substrings) that occur more than once in a DNA molecule.
# You may return the answer in any order.

# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

# Constraints:
# 1 <= s.length <= 10^5
# s[i] is either 'A', 'C', 'G', or 'T'.

# Author: Kaustav Ghosh

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                repeated.add(sub)
            seen.add(sub)
        return list(repeated)
