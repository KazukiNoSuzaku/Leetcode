# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: For each pair of phrases, check if last word of one equals first word of another

class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        words = [p.split() for p in phrases]
        result = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i][-1] == words[j][0]:
                    merged = ' '.join(words[i] + words[j][1:])
                    result.add(merged)
        return sorted(result)
