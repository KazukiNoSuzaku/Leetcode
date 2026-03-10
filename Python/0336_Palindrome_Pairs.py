# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the
# given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]

# Constraints:
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300

# Author: Kaustav Ghosh

class Solution(object):
    def palindromePairs(self, words):
        word_map = {w: i for i, w in enumerate(words)}
        res = []

        def is_palindrome(s):
            return s == s[::-1]

        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                prefix, suffix = w[:j], w[j:]
                if is_palindrome(prefix):
                    rev = suffix[::-1]
                    if rev != w and rev in word_map:
                        res.append([word_map[rev], i])
                if j != len(w) and is_palindrome(suffix):
                    rev = prefix[::-1]
                    if rev != w and rev in word_map:
                        res.append([i, word_map[rev]])
        return res
