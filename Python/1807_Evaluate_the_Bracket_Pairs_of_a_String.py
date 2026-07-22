# Author: Kaustav Ghosh
# Problem: Evaluate the Bracket Pairs of a String
# Approach: Build a key->value map, then scan the string replacing each bracketed key with its value, or "?" if the key is unknown

class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        values = {k: v for k, v in knowledge}
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]
                res.append(values.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
