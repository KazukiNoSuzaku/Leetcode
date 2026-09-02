# Author: Kaustav Ghosh
# Problem: Find Palindrome With Fixed Length
# Approach: A length-L palindrome is fully determined by its first ceil(L/2) digits, which run from 10^(half-1) upward. The q-th smallest palindrome uses first-half = 10^(half-1) + (q-1); mirror it (dropping the middle digit for odd L) to build the palindrome. If q exceeds the count of valid first halves, the answer is -1

class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)
        count = 9 * start  # number of palindromes of this length

        res = []
        for q in queries:
            if q > count:
                res.append(-1)
                continue
            first = start + q - 1
            s = str(first)
            if intLength % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]
            res.append(int(pal))
        return res
