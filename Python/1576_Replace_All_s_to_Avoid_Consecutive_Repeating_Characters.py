# Author: Kaustav Ghosh
# Problem: Replace All ?'s to Avoid Consecutive Repeating Characters
# Approach: Each question mark only has to differ from its immediate left and right neighbours, so it never needs more than three candidate letters: with two neighbours to avoid, one of 'a', 'b', 'c' is always free. Filling left to right and reading the already-decided character on the left means every choice is final the moment it is made, with no backtracking.

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        n = len(chars)
        for i in range(n):
            if chars[i] != '?':
                continue
            before = chars[i - 1] if i > 0 else ''
            after = chars[i + 1] if i + 1 < n else ''
            for candidate in 'abc':
                if candidate != before and candidate != after:
                    chars[i] = candidate
                    break
        return ''.join(chars)
