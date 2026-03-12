# Author: Kaustav Ghosh
# Backtracking with bitmask to track used characters

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # Filter strings with duplicate chars and convert to bitmasks
        masks = []
        for s in arr:
            mask = 0
            valid = True
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if mask & bit:
                    valid = False
                    break
                mask |= bit
            if valid:
                masks.append((mask, len(s)))

        self.result = 0

        def backtrack(idx, used, length):
            self.result = max(self.result, length)
            for i in range(idx, len(masks)):
                mask, l = masks[i]
                if used & mask == 0:
                    backtrack(i + 1, used | mask, length + l)

        backtrack(0, 0, 0)
        return self.result
