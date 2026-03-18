# Author: Kaustav Ghosh
# Problem: 1542 - Find Longest Awesome Substring
# Approach: Bitmask prefix XOR for even/odd digit counts

class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {0: -1}
        prefix = 0
        result = 0

        for i, c in enumerate(s):
            prefix ^= 1 << int(c)
            if prefix in seen:
                result = max(result, i - seen[prefix])
            else:
                seen[prefix] = i
            # try flipping each bit (at most one odd count digit)
            for bit in range(10):
                mask = prefix ^ (1 << bit)
                if mask in seen:
                    result = max(result, i - seen[mask])

        return result
