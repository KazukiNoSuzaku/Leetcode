# Author: Kaustav Ghosh
# Problem: Sum of Beauty of All Substrings
# Approach: Every substring has to be scored, but the substrings sharing a start can be grown one character at a time, so a single frequency table per start is extended rather than rebuilt and each extension costs one increment. The beauty itself only depends on the frequency table, and since there are at most 26 letters the largest and smallest non-zero counts are found by one sweep over the table; letters that never appear are skipped because the least frequent character must be one that is actually present.

class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        codes = [ord(c) - 97 for c in s]
        n = len(codes)
        total = 0
        for start in range(n):
            counts = [0] * 26
            for end in range(start, n):
                counts[codes[end]] += 1
                most = 0
                least = n
                for count in counts:
                    if count:
                        if count > most:
                            most = count
                        if count < least:
                            least = count
                total += most - least
        return total
