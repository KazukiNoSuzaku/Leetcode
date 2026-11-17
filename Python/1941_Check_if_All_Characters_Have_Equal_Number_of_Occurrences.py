# Author: Kaustav Ghosh
# Problem: Check if All Characters Have Equal Number of Occurrences
# Approach: The question is only about the multiset of occurrence counts, so I tally how often each letter appears and then ask whether those tallies are all the same value. Collecting the counts of the letters that actually occur into a set reduces that question to a single size check: one distinct count means every present letter occurs equally often, and the string is never empty so the set is never empty either. One pass over the string plus a constant-size set gives O(n) time and O(1) space.

from collections import Counter

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(set(Counter(s).values())) == 1
