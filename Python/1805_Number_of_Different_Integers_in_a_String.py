# Author: Kaustav Ghosh
# Problem: Number of Different Integers in a String
# Approach: The letters serve only as separators, so swapping each of them for a space and splitting leaves exactly the digit groups. Leading zeros make different strings stand for the same number, which stripping them away normalises, and the empty string left behind by a group of all zeros stands for zero itself. Collecting the normalised groups in a set then counts the distinct values, and because the groups stay as strings no number ever has to be parsed.

class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        spaced = "".join(c if c.isdigit() else " " for c in word)
        return len({group.lstrip("0") for group in spaced.split()})
