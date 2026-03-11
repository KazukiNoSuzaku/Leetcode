# Given an array of distinct strings words, return the shortest unique abbreviation for each word.
# An abbreviation of a word w is a prefix of w of length k followed by the count of removed chars.

# Author: Kaustav Ghosh

class Solution(object):
    def wordsAbbreviation(self, words):
        def abbrev(word, k):
            if k >= len(word) - 2:
                return word
            return word[:k+1] + str(len(word) - k - 2) + word[-1]

        n = len(words)
        prefix = [0] * n
        res = [abbrev(w, 1) for w in words]
        for i in range(n):
            while True:
                dups = [j for j in range(n) if j != i and res[i] == res[j]]
                if not dups:
                    break
                for j in dups + [i]:
                    prefix[j] += 1
                    res[j] = abbrev(words[j], prefix[j])
        return res
