# Author: Kaustav Ghosh
# Problem: Smallest String With A Given Numeric Value
# Approach: Lexicographically smallest means the earliest positions must be as small as possible, so the cheapest arrangement is to start from the all-'a' string, which is the minimum possible value, and then spend the surplus as late in the string as it will go. Filling from the back with the largest letters each position can absorb pushes every increase as far right as possible, which keeps the prefix minimal; at most one position ends up partially raised, between the trailing block of z's and the leading block of a's.

class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        letters = [1] * n           # every position starts as 'a'
        surplus = k - n
        index = n - 1
        while surplus > 0:
            extra = 25 if surplus > 25 else surplus
            letters[index] += extra
            surplus -= extra
            index -= 1
        return ''.join(chr(96 + value) for value in letters)
