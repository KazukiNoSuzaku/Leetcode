# Author: Kaustav Ghosh
# Problem: Smallest K-Length Subsequence With Occurrences of a Letter
# Approach: The smallest subsequence of a fixed length is built greedily with a stack that keeps its characters as small as possible: a character already chosen is discarded when a smaller one arrives, since replacing it lowers the result at the earliest differing position. Two guards restrict those discards here. A character may only be dropped if enough of the string remains to still reach the required length, and a copy of the required letter may only be dropped if the copies kept plus those still to come can still meet the quota. Symmetrically, an ordinary character is only taken when the remaining slots can still accommodate the outstanding quota of required letters, which is what forces the stack to leave room for them.

class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        total = len(s)
        still_to_come = [0] * (total + 1)
        for index in range(total - 1, -1, -1):
            still_to_come[index] = still_to_come[index + 1] + (1 if s[index] == letter else 0)

        chosen = []
        held = 0
        for index in range(total):
            char = s[index]
            while chosen:
                top = chosen[-1]
                if top <= char:
                    break
                if len(chosen) - 1 + total - index < k:
                    break
                if top == letter and held - 1 + still_to_come[index] < repetition:
                    break
                chosen.pop()
                if top == letter:
                    held -= 1
            if len(chosen) < k:
                if char == letter:
                    chosen.append(char)
                    held += 1
                elif k - len(chosen) - 1 >= repetition - held:
                    chosen.append(char)
        return ''.join(chosen)
