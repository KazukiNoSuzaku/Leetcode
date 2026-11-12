# Author: Kaustav Ghosh
# Problem: Redistribute Characters to Make All Strings Equal
# Approach: Characters may be moved anywhere, so their positions are irrelevant and only the pooled tally matters. Making all the strings identical means each of them holds the same multiset, so every character's total count has to split evenly across them, which is exactly divisibility of each count by the number of strings. That also implies the lengths work out, so no separate length check is needed.

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        from collections import Counter

        pooled = Counter()
        for word in words:
            pooled.update(word)
        return all(count % len(words) == 0 for count in pooled.values())
