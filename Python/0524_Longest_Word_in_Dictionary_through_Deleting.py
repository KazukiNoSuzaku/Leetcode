# Given a string s and a string array dictionary, return the longest string in the dictionary
# that can be formed by deleting some characters of s without reordering the remaining characters.

# Author: Kaustav Ghosh

class Solution(object):
    def findLongestWord(self, s, dictionary):
        def is_subseq(w):
            it = iter(s)
            return all(c in it for c in w)
        dictionary.sort(key=lambda x: (-len(x), x))
        for w in dictionary:
            if is_subseq(w):
                return w
        return ''
