# Author: Kaustav Ghosh
# Problem: Shifting Letters II
# Approach: Record each shift range in a difference array (+1 at start and -1 after end for a forward shift, the reverse for a backward one), so a running prefix sum gives every position's net shift in one pass; apply it modulo 26

class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        diff = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            step = 1 if direction else -1
            diff[start] += step
            diff[end + 1] -= step
        result = []
        net = 0
        for i, ch in enumerate(s):
            net += diff[i]
            result.append(chr((ord(ch) - ord('a') + net) % 26 + ord('a')))
        return "".join(result)
