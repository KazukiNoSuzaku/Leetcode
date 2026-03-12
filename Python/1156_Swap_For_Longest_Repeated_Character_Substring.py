# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Group consecutive chars, try merging adjacent groups with one swap

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import Counter
        count = Counter(text)
        # Build groups of consecutive chars
        groups = []
        i = 0
        while i < len(text):
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1
            groups.append((text[i], j - i))
            i = j

        result = 0
        for i, (ch, length) in enumerate(groups):
            # Single group, maybe extend by 1 if more of same char exists
            result = max(result, min(length + 1, count[ch]))
            # Two groups separated by single different char
            if i + 2 < len(groups) and groups[i + 2][0] == ch and groups[i + 1][1] == 1:
                merged = length + groups[i + 2][1]
                result = max(result, min(merged + 1, count[ch]))
        return result
