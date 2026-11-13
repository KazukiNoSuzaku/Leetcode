# Author: Kaustav Ghosh
# Problem: Remove All Occurrences of a Substring
# Approach: Removing an occurrence can bring together characters that were previously apart and create a new occurrence, but only one ending exactly where the removal happened, so a single left-to-right pass with a stack of kept characters is enough: after appending each character, if the stack now ends with the pattern then that occurrence is the leftmost one available and is dropped immediately. Nothing ever needs to be rescanned from the beginning, and comparing the stack's tail costs the pattern's length rather than the string's.

class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        width = len(part)
        kept = []
        for character in s:
            kept.append(character)
            if len(kept) >= width and "".join(kept[-width:]) == part:
                del kept[-width:]
        return "".join(kept)
