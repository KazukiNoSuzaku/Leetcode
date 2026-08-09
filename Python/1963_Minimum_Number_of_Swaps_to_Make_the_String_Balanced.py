# Author: Kaustav Ghosh
# Problem: Minimum Number of Swaps to Make the String Balanced
# Approach: Cancel matched bracket pairs; the leftover unmatched closing brackets determine the answer. Each swap fixes two of them, so the result is ceil(unmatched / 2)

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_count = 0
        unmatched = 0
        for ch in s:
            if ch == '[':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    unmatched += 1
        return (unmatched + 1) // 2
