# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Count consecutive runs, each run of length n contributes n*(n+1)/2

class Solution(object):
    def countLetters(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            n = j - i
            result += n * (n + 1) // 2
            i = j
        return result
