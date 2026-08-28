# Author: Kaustav Ghosh
# Problem: Unique Substrings With Equal Digit Frequency
# Approach: For each start, extend the substring tracking digit counts. All present digits share a frequency exactly when the length equals max-count times the number of distinct digits. Deduplicate qualifying substrings with a rolling polynomial hash

class Solution(object):
    def equalDigitFrequency(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = (1 << 61) - 1
        base = 131
        n = len(s)
        seen = set()
        for i in range(n):
            counts = [0] * 10
            distinct = 0
            max_count = 0
            h = 0
            for j in range(i, n):
                d = ord(s[j]) - 48
                if counts[d] == 0:
                    distinct += 1
                counts[d] += 1
                if counts[d] > max_count:
                    max_count = counts[d]
                h = (h * base + d + 1) % MOD
                if (j - i + 1) == max_count * distinct:
                    seen.add(h)
        return len(seen)
