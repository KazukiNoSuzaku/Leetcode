# Author: Kaustav Ghosh
# Problem: Minimum Deletions to Make Character Frequencies Unique
# Approach: Only the multiset of frequencies matters, never which letters they belong to, so the task is to make a list of numbers pairwise distinct at the least total cost, where cost is how much each number is reduced. Taking the frequencies in descending order and pushing each one down to just below the smallest value already kept is optimal, because a larger frequency can always afford to sit at a higher slot than a smaller one, so no cheaper assignment exists; a frequency forced to zero means that letter is deleted entirely, which is allowed since zero need not be distinct.

from collections import Counter


class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        taken = set()
        for count in sorted(Counter(s).values(), reverse=True):
            while count in taken:
                count -= 1
                deletions += 1
            if count:
                taken.add(count)
        return deletions
