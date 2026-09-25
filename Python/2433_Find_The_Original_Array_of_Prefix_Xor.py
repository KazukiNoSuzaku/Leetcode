# Author: Kaustav Ghosh
# Problem: Find The Original Array of Prefix Xor
# Approach: pref[i] is the running XOR, so XOR-ing consecutive prefixes cancels everything before position i and leaves arr[i] = pref[i] ^ pref[i - 1], with arr[0] = pref[0]

class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        return [pref[0]] + [a ^ b for a, b in zip(pref, pref[1:])]
