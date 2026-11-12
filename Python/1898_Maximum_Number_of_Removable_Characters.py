# Author: Kaustav Ghosh
# Problem: Maximum Number of Removable Characters
# Approach: Removals are applied as a prefix of the given order, and removing more characters can only make the pattern harder to find, never easier, so whether a given count still works is monotone and the largest workable count comes from a binary search. Each probe marks the first so many removable positions and then walks the string once, advancing through the pattern at every surviving character that matches, which decides containment as a subsequence. Marking into a reused flag array keeps each probe linear, so the whole search is one pass per candidate rather than per removal.

class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        def survives(count):
            gone = [False] * len(s)
            for index in range(count):
                gone[removable[index]] = True
            matched = 0
            for position, character in enumerate(s):
                if gone[position]:
                    continue
                if character == p[matched]:
                    matched += 1
                    if matched == len(p):
                        return True
            return False

        low, high = 0, len(removable)
        while low < high:
            middle = (low + high + 1) // 2
            if survives(middle):
                low = middle
            else:
                high = middle - 1
        return low
