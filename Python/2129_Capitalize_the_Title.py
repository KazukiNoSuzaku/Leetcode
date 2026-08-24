# Author: Kaustav Ghosh
# Problem: Capitalize the Title
# Approach: Lowercase words of length one or two; for longer words, uppercase the first letter and lowercase the rest. Rejoin with spaces

class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = []
        for w in title.split():
            if len(w) <= 2:
                words.append(w.lower())
            else:
                words.append(w[0].upper() + w[1:].lower())
        return ' '.join(words)
