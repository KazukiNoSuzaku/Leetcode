# Author: Kaustav Ghosh
# Problem: Minimum Time to Type Word Using Special Typewriter
# Approach: Typing each character costs one second regardless, so the whole word contributes its length, and the only choice is which way to turn the dial between consecutive characters. The letters sit on a circle of 26, so moving from one to another costs either the clockwise gap or the counter-clockwise gap, whichever is smaller, and those choices are completely independent of one another because the pointer always ends up on the character being typed. Starting the pointer at 'a', I add the smaller of the two gaps for each step plus one per character, which is a single pass with constant work.

class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        seconds = len(word)
        pointer = 0
        for letter in word:
            target = ord(letter) - ord('a')
            gap = abs(target - pointer)
            seconds += min(gap, 26 - gap)
            pointer = target
        return seconds
