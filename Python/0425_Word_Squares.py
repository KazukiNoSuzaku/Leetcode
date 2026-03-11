# Given an array of unique strings words, return all the word squares you can build from words.
# A word square is a k x k grid of words where the words form a valid word square.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def wordSquares(self, words):
        n = len(words[0])
        prefix = defaultdict(list)
        for w in words:
            for i in range(n):
                prefix[w[:i]].append(w)

        res = []
        def backtrack(square):
            if len(square) == n:
                res.append(square[:])
                return
            idx = len(square)
            prefix_needed = ''.join(w[idx] for w in square)
            for candidate in prefix[prefix_needed]:
                square.append(candidate)
                backtrack(square)
                square.pop()

        for w in words:
            backtrack([w])
        return res
