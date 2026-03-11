# Count words that can be stretched to match s by extending groups of 3+ chars.

# Author: Kaustav Ghosh

class Solution(object):
    def expressiveWords(self, s, words):
        def check(s, w):
            i = j = 0
            while i < len(s) and j < len(w):
                if s[i] != w[j]: return False
                i2 = i; j2 = j
                while i < len(s) and s[i] == s[i2]: i += 1
                while j < len(w) and w[j] == w[j2]: j += 1
                cnt_s, cnt_w = i - i2, j - j2
                if cnt_s < cnt_w or (cnt_s < 3 and cnt_s != cnt_w): return False
            return i == len(s) and j == len(w)
        return sum(check(s, w) for w in words)
