# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def partition(self, s):
        res = []
        def is_palindrome(sub):
            return sub == sub[::-1]
        def backtrack(start, path):
            if start == len(s):
                res.append(list(path))
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return res
