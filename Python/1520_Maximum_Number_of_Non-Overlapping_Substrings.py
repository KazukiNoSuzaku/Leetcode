# Author: Kaustav Ghosh
# Problem: Maximum Number of Non-Overlapping Substrings
# Approach: A valid piece must hold every occurrence of each letter it contains, so grow the span of each letter's first-to-last range until it closes over all letters inside, discarding it if the growth reaches back before the start. Those candidate spans never partially overlap, so sorting them by end and greedily taking each one that clears the last gives the most pieces, and the shortest ones among nested candidates survive

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first, last = {}, {}
        for i, ch in enumerate(s):
            first.setdefault(ch, i)
            last[ch] = i

        def close(ch):
            left, right = first[ch], last[ch]
            i = left
            while i <= right:
                if first[s[i]] < left:
                    return None
                right = max(right, last[s[i]])
                i += 1
            return left, right

        spans = []
        for ch in first:
            span = close(ch)
            if span is not None:
                spans.append(span)
        spans.sort(key=lambda pair: pair[1])

        chosen = []
        reached = -1
        for left, right in spans:
            if left > reached:
                chosen.append(s[left:right + 1])
                reached = right
        return chosen
