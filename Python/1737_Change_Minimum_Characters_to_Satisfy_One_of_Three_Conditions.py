# Author: Kaustav Ghosh
# Problem: Change Minimum Characters to Satisfy One of Three Conditions
# Approach: Each condition reduces to counting characters rather than searching over edits. Making both strings a single shared letter costs every character that is not already that letter, minimised over the twenty-six choices. Making one string strictly below the other needs a cut letter: everything at or above the cut in the lower string must change, and everything strictly below it in the upper string must change, which prefix counts of the two letter tallies answer in constant time per cut. The cut letter runs from the second through the last, since a cut at the first letter leaves nothing strictly below it, and the two directions are handled by running the same computation with the strings swapped.

from collections import Counter


class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        count_a = [0] * 26
        count_b = [0] * 26
        for ch in a:
            count_a[ord(ch) - 97] += 1
        for ch in b:
            count_b[ord(ch) - 97] += 1

        # Condition three: both strings collapse to one shared letter.
        best = len(a) + len(b) - max(count_a[i] + count_b[i] for i in range(26))

        below_a = 0          # characters of a strictly below the cut
        below_b = 0
        for cut in range(1, 26):
            below_a += count_a[cut - 1]
            below_b += count_b[cut - 1]
            # every letter in a under the cut, every letter in b at or above it
            best = min(best, (len(a) - below_a) + below_b)
            best = min(best, (len(b) - below_b) + below_a)
        return best
