# Decode a string where 1-9 map to a-i and 10#-26# map to j-z.

# Author: Kaustav Ghosh

class Solution(object):
    def freqAlphabets(self, s):
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                res.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                res.append(chr(ord('a') + int(s[i]) - 1))
                i -= 1
        return ''.join(reversed(res))
