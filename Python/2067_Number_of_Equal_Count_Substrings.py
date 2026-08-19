# Author: Kaustav Ghosh
# Problem: Number of Equal Count Substrings
# Approach: A valid substring with k distinct characters has length k*count. For each k from 1..26, slide a fixed-length window of k*count, tracking how many characters currently hit exactly count occurrences; the window is valid when all k distinct characters do

class Solution(object):
    def equalCountSubstrings(self, s, count):
        """
        :type s: str
        :type count: int
        :rtype: int
        """
        n = len(s)
        total = 0
        for k in range(1, 27):
            length = k * count
            if length > n:
                break
            freq = [0] * 26
            exact = 0        # chars with freq == count
            for i in range(n):
                c = ord(s[i]) - 97
                freq[c] += 1
                if freq[c] == count:
                    exact += 1
                elif freq[c] == count + 1:
                    exact -= 1
                if i >= length:
                    d = ord(s[i - length]) - 97
                    freq[d] -= 1
                    if freq[d] == count:
                        exact += 1
                    elif freq[d] == count - 1:
                        exact -= 1
                if i >= length - 1 and exact == k:
                    total += 1
        return total
