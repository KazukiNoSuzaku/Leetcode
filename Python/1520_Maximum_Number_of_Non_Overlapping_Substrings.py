# Author: Kaustav Ghosh
# Problem: Maximum Number of Non-Overlapping Substrings
# Approach: For each char find [first, last]; expand right boundary to include all occurrences of every char inside; greedily pick by earliest end

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        def get_right(l, init_r):
            r = init_r
            i = l
            while i <= r:
                c = s[i]
                if first[c] < l:
                    return -1
                r = max(r, last[c])
                i += 1
            return r

        candidates = []
        for c in set(s):
            l = first[c]
            r = get_right(l, last[c])
            if r != -1:
                candidates.append((r, l))

        candidates.sort()

        result = []
        prev_end = -1
        for r, l in candidates:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result
