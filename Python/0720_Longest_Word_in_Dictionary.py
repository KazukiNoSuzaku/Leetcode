# Find the longest word in a dictionary that can be built one letter at a time.

# Author: Kaustav Ghosh

class Solution(object):
    def longestWord(self, words):
        word_set = set(words)
        res = ''
        for word in words:
            if all(word[:i] in word_set for i in range(1, len(word))):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res
