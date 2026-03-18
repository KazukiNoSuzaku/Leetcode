# Author: Kaustav Ghosh
# Problem: 1520 - Maximum Number of Non-Overlapping Substrings
# Approach: Greedy interval scheduling with expanded ranges

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = {}
        right = {}
        for i, c in enumerate(s):
            if c not in left:
                left[c] = i
            right[c] = i

        def get_range(c):
            l, r = left[c], right[c]
            i = l
            while i <= r:
                ch = s[i]
                if left[ch] < l:
                    return None
                if right[ch] > r:
                    r = right[ch]
                i += 1
            return l, r

        intervals = []
        for c in set(s):
            res = get_range(c)
            if res:
                intervals.append(res)

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r+1])
                prev_end = r

        return result
