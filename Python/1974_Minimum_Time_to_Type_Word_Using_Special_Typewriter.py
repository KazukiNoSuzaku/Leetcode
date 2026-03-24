# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        time = 0
        curr = 0  # 'a' = 0
        for c in word:
            target = ord(c) - ord('a')
            diff = abs(target - curr)
            # Can go clockwise or counterclockwise
            time += min(diff, 26 - diff) + 1  # +1 for typing
            curr = target
        return time
