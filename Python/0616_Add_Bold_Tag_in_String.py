# Given a string s and an array of strings words, add bold tags around substrings
# of s that match any word in words. Merge overlapping/adjacent bold tags.

# Author: Kaustav Ghosh

class Solution(object):
    def addBoldTag(self, s, words):
        n = len(s)
        bold = [False] * n
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)
        res = []
        i = 0
        while i < n:
            if bold[i]:
                res.append('<b>')
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append('</b>')
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
