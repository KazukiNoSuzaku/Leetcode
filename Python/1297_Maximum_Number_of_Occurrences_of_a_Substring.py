# Author: Kaustav Ghosh
# Only need to check substrings of length minSize (smaller = more occurrences)

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        from collections import Counter
        count = Counter()
        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                count[sub] += 1
        return max(count.values()) if count else 0
