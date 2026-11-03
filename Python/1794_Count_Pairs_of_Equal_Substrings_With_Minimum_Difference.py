# Author: Kaustav Ghosh
# Problem: Count Pairs of Equal Substrings With Minimum Difference
# Approach: Lengthening the two matched substrings pushes j to the right and a to the left, so j - a can only grow; the minimum is therefore always attained by single characters, and the whole problem reduces to picking one position in each string holding the same letter. For a chosen position in the first string the best partner is that letter's last occurrence in the second string, since any earlier occurrence makes the difference strictly larger, which also means no other partner can ever tie the minimum. One pass with a table of last occurrences finds the minimum and counts how many positions reach it.

class Solution(object):
    def countQuadruples(self, firstString, secondString):
        """
        :type firstString: str
        :type secondString: str
        :rtype: int
        """
        last = {}
        for index, letter in enumerate(secondString):
            last[letter] = index

        smallest = None
        count = 0
        for index, letter in enumerate(firstString):
            if letter not in last:
                continue
            difference = index - last[letter]
            if smallest is None or difference < smallest:
                smallest, count = difference, 1
            elif difference == smallest:
                count += 1
        return count
