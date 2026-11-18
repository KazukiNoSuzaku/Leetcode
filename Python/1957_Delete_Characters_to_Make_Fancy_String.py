# Author: Kaustav Ghosh
# Problem: Delete Characters to Make Fancy String
# Approach: Deleting as few characters as possible means never deleting one unless it would create a third consecutive equal character, and that decision only depends on what has already been kept. So I build the result left to right and append each character unless the last two kept characters are already equal to it, which is exactly the condition that keeping it would make a run of three. Greedy is safe here because keeping a character can never force a later deletion that skipping it would have avoided: the kept suffix only ever gets shorter by skipping. One pass with a list of kept characters gives O(n) time.

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        kept = []
        for letter in s:
            if len(kept) >= 2 and kept[-1] == letter and kept[-2] == letter:
                continue
            kept.append(letter)
        return "".join(kept)
