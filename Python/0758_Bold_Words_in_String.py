# Add bold tags around substrings of s matching any word in dict.

# Author: Kaustav Ghosh

class Solution(object):
    def boldWords(self, words, s):
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
                    res.append(s[i]); i += 1
                res.append('</b>')
            else:
                res.append(s[i]); i += 1
        return ''.join(res)
