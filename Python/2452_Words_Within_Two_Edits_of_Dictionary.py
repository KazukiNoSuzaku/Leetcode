# Author: Kaustav Ghosh
# Problem: Words Within Two Edits of Dictionary
# Approach: Every word has the same length, so an edit is only ever a substitution and the distance between two words is the count of positions where they differ. Keep a query when some dictionary word differs in at most two positions

class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        return [query for query in queries
                if any(sum(a != b for a, b in zip(query, word)) <= 2 for word in dictionary)]
