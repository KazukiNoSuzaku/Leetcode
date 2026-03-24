# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Bitmask of parity of each character a-j (10 bits)
        count = {0: 1}
        mask = 0
        result = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            # All even frequencies
            result += count.get(mask, 0)
            # Exactly one odd frequency
            for i in range(10):
                result += count.get(mask ^ (1 << i), 0)
            count[mask] = count.get(mask, 0) + 1
        return result
