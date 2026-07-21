# Author: Kaustav Ghosh
# Problem: Count Pairs of Equal Substrings With Minimum Difference (Premium)
# Approach: A single matching character always beats any longer match on j-a, so per letter use its first index in firstString and last index in secondString; count the letters hitting the minimum difference

class Solution(object):
    def countQuadruples(self, firstString, secondString):
        """
        :type firstString: str
        :type secondString: str
        :rtype: int
        """
        first_min = {}
        for i, c in enumerate(firstString):
            first_min.setdefault(c, i)

        last_second = {}
        for i, c in enumerate(secondString):
            last_second[c] = i  # keep updating -> last occurrence

        best = float('inf')
        count = 0
        for c, i in first_min.items():
            if c in last_second:
                diff = i - last_second[c]
                if diff < best:
                    best, count = diff, 1
                elif diff == best:
                    count += 1
        return count
