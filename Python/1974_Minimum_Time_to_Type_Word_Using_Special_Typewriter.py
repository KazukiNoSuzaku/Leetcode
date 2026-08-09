# Author: Kaustav Ghosh
# Problem: Minimum Time to Type Word Using Special Typewriter
# Approach: The pointer starts at 'a'. For each character add the shorter circular rotation (clockwise or counterclockwise) from the current letter, plus one second to type it

class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        total = 0
        cur = 0
        for ch in word:
            target = ord(ch) - ord('a')
            diff = abs(target - cur)
            total += min(diff, 26 - diff) + 1
            cur = target
        return total
